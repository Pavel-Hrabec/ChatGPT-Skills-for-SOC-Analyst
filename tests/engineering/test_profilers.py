"""Offline regression checks for the two bundled profilers.

Run from the repository root:
python -m unittest discover -s tests/engineering -v
Synthetic inputs are generated in temporary directories and never uploaded.
"""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LOG_PATH = 'skills/telemetry-engineering/log-quality/scripts/profile_logs.py'
FEED_PATH = 'skills/threat-intelligence-engineering/feed-quality/scripts/profile_feed.py'
LOG = load('log_profiler', LOG_PATH)
FEED = load('feed_profiler', FEED_PATH)
AS_OF = datetime(2026,10,20,tzinfo=timezone.utc)


class Profilers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.file = Path(self.temp.name) / 'input.ndjson'

    def records(self, records):
        self.file.write_text(''.join(json.dumps(r)+'\n' for r in records), encoding='utf-8')
        return self.file

    def observation(self, **changes):
        obj = dict(type='domain',indicator='example.org',provider='source-a',
                   reference='https://example.org/report',confidence=75,
                   first_seen='2026-10-18T00:00:00Z',last_seen='2026-10-19T00:00:00Z',
                   tlp='TLP:CLEAR',revoked=False)
        obj.update(changes)
        return obj

    def test_zero_and_false_are_present(self):
        self.records([{'t':'2026-10-20T00:00:00Z','a':0,'b':False},
                      {'t':'2026-10-20T00:00:00Z','a':None,'b':''},
                      {'t':'2026-10-20T00:00:00Z'}])
        report = LOG.profile(self.file,'t',required_fields=['a','b'])
        self.assertEqual(report['required_fields']['a']['present'],1)
        self.assertEqual(report['required_fields']['a']['null'],1)
        self.assertEqual(report['required_fields']['b']['present'],1)
        self.assertEqual(report['required_fields']['b']['empty_string'],1)
        self.assertEqual(report['required_fields']['a']['missing'],1)

    def test_clock_offsets_missing_invalid_and_negative_lag(self):
        self.records([{'t':'2026-10-20T00:00:00Z','i':'2026-10-20T00:00:05Z'},
                      {'t':'2026-10-20T01:00:00+01:00','i':'2026-10-20T00:00:10Z'},
                      {'t':'2026-10-20T00:00:00Z','i':'2026-10-19T23:59:59Z'},
                      {'t':'2026-10-20T00:00:00'}, {'t':123}, {}])
        report=LOG.profile(self.file,'t','i')
        self.assertEqual(report['counts']['event_timestamp_invalid'],2)
        self.assertEqual(report['counts']['event_timestamp_missing'],1)
        self.assertEqual(report['counts']['negative_lag_pairs'],1)
        self.assertEqual(report['ingestion_lag_seconds']['eligible_pairs'],3)
        self.assertEqual(report['ingestion_lag_seconds']['p50'],5)
        self.assertEqual(report['ingestion_lag_seconds']['p95'],10)

    def test_nested_and_literal_keys_composite_duplicates(self):
        self.records([{'host':{'id':'a'},'event.id':0},
                      {'host':{'id':'b'},'event.id':0},
                      {'host':{'id':'a'},'event.id':0}, {'host':{'id':'a'}}])
        report=LOG.profile(self.file,'t',id_fields=['host.id','event.id'])
        self.assertEqual(report['counts']['duplicate_candidates'],1)
        self.assertEqual(report['counts']['records_without_duplicate_key'],1)
        self.assertEqual(report['counts']['duplicate_eligible_records'],3)

    def test_malformed_and_nonobject_records_do_not_pollute_denominators(self):
        self.file.write_text('{}\n[]\nnot-json\n{"n":NaN}\n\n',encoding='utf-8')
        report=LOG.profile(self.file,'t',required_fields=['host'])
        self.assertEqual(report['counts']['input_records'],4)
        self.assertEqual(report['counts']['valid_objects'],1)
        self.assertEqual(report['counts']['malformed_json'],2)
        self.assertEqual(report['counts']['non_object_records'],1)

    def test_log_cli_produces_aggregates_without_event_payload(self):
        self.records([{'t':'2026-10-20T00:00:00Z','secret':'DO_NOT_ECHO_EVENT'}])
        result=subprocess.run([sys.executable,str(ROOT/LOG_PATH),str(self.file),
                               '--timestamp-field','t'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)['counts']['valid_objects'],1)
        self.assertNotIn('DO_NOT_ECHO_EVENT',result.stdout)

    def test_feed_normalization_duplicate_and_provider_overlap(self):
        self.records([self.observation(indicator='Example.ORG'),
                      self.observation(indicator='example.org.',provider='source-b')])
        report=FEED.profile(self.file,AS_OF,30)
        self.assertEqual(report['unique_valid_indicators'],1)
        self.assertEqual(report['issues']['duplicate_indicator_candidate'],1)
        self.assertEqual(report['indicators_seen_across_provider_labels'],1)
        self.assertNotIn('example.org',json.dumps(report))

    def test_feed_age_validity_revocation_and_confidence(self):
        self.records([self.observation(first_seen='2026-01-01T00:00:00Z',
                                       last_seen='2026-01-02T00:00:00Z',revoked=True,
                                       valid_until='2026-10-01T00:00:00Z'),
                      self.observation(first_seen='2026-10-22T00:00:00Z',
                                       last_seen='2026-10-21T00:00:00Z',confidence=True),
                      self.observation(first_seen=None,last_seen='2026-10-20T00:00:00',
                                       confidence=101,tlp=None)])
        report=FEED.profile(self.file,AS_OF,30)
        for issue in ('older_than_policy','expired_validity','revoked',
                      'future_observation','observation_order_invalid','age_unknown',
                      'sharing_restriction_unknown'):
            self.assertEqual(report['issues'][issue],1,issue)
        self.assertEqual(report['issues']['invalid_normalized_confidence'],2)

    def test_feed_types_url_case_and_unsupported_values(self):
        cases=[('ipv4','192.0.2.1'),('ipv6','2001:db8::1'),('sha256','a'*64),
               ('url','https://example.org/A'),('url','https://example.org/a'),
               ('ipv4','192[.]0[.]2[.]1'),('domain','example.org..'),
               ('cidr','192.0.2.0/24'),('url','https://example.org:99999/a')]
        self.records([self.observation(type=kind,indicator=value) for kind,value in cases])
        report=FEED.profile(self.file,AS_OF,30)
        self.assertEqual(report['counts']['valid_indicators'],5)
        self.assertEqual(report['unique_valid_indicators'],5)
        self.assertEqual(report['counts']['invalid_or_unsupported_indicators'],4)

    def test_feed_cli_rejects_invalid_policy(self):
        self.records([])
        for age in ('-1','nan','inf'):
            result=subprocess.run([sys.executable,str(ROOT/FEED_PATH),str(self.file),
                                   '--as-of','2026-10-20T00:00:00Z','--max-age-days',age],
                                  capture_output=True,text=True)
            self.assertEqual(result.returncode,2)

    def test_feed_input_errors_and_missing_time_do_not_claim_quality(self):
        self.file.write_text('bad\n[]\n{"type":"domain","indicator":"example.org"}\n',encoding='utf-8')
        report=FEED.profile(self.file,AS_OF,30)
        self.assertEqual(report['counts']['malformed_json'],1)
        self.assertEqual(report['counts']['non_object_records'],1)
        self.assertEqual(report['issues']['age_unknown'],1)
        self.assertEqual(report['issues']['missing_provider'],1)
        self.assertEqual(report['issues']['sharing_restriction_unknown'],1)


if __name__ == '__main__':
    unittest.main()
