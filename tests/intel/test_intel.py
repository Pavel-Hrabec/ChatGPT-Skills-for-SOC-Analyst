"""Deterministic mocked-provider and MCP protocol tests; no live API calls."""
import asyncio
from datetime import datetime
from io import BytesIO
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
INTEGRATION=ROOT/'integrations'/'soc-intel-mcp'
sys.path.insert(0,str(INTEGRATION))
import intel


def ok(data):
    return {'status':'ok','retrieved_at':'2026-10-20T00:00:00+00:00','data':data}


class Response:
    def __init__(self,body): self.body=body
    def __enter__(self): return self
    def __exit__(self,*args): pass
    def read(self,size): return self.body[:size]


class IntelTests(unittest.TestCase):
    def test_invalid_or_nonpublic_input_never_requests(self):
        def forbidden(*args,**kwargs): self.fail('Unexpected provider call')
        client=intel.IntelClient(vt_key='set',threatfox_key='set',requester=forbidden)
        for kind,value in [('ip','127.0.0.1'),('ip','10.0.0.1'),('ip','192.0.2.1'),
                           ('ip','::1'),('domain','host.local'),('domain','https://example.org'),
                           ('domain','example.org/secret'),('sha256','x'*64)]:
            self.assertEqual(client.lookup(kind,value)['status'],'invalid_input')

    def test_domain_idna_and_hash_case(self):
        self.assertEqual(intel.domain_name('Example.ORG.'),'example.org')
        self.assertEqual(intel.domain_name('b\u00fccher.de'),'xn--bcher-kva.de')
        self.assertEqual(intel.normalized_hash('A'*64),'a'*64)
        for value in ('example.org..','localhost','8.8.8.8',' x.org','x.org?token'):
            with self.assertRaises((ValueError,UnicodeError)): intel.domain_name(value)

    def test_missing_keys_are_not_clean_findings(self):
        def forbidden(*args,**kwargs): self.fail('Unexpected provider call')
        result=intel.IntelClient(vt_key='',threatfox_key='',requester=forbidden).lookup('ip','8.8.8.8')
        self.assertEqual([x['status'] for x in result['reports']],['not_configured','not_configured'])
        self.assertNotIn('benign',result)

    def test_vt_existing_report_is_minimized(self):
        calls=[]
        def provider(url,**kwargs):
            calls.append((url,kwargs))
            return ok({'data':{'id':'a'*64,'attributes':{'last_analysis_stats':{'malicious':2},
                       'last_analysis_date':1234,'unneeded_sensitive_payload':'omit'}}})
        result=intel.IntelClient(vt_key='test-only-key',threatfox_key='',requester=provider).lookup('sha256','A'*64)
        self.assertEqual(result['reports'][0]['status'],'ok')
        self.assertEqual(result['reports'][0]['attributes']['last_analysis_stats']['malicious'],2)
        self.assertNotIn('unneeded_sensitive_payload',json.dumps(result))
        self.assertNotIn('test-only-key',json.dumps(result))
        self.assertIn('/files/'+'a'*64,calls[0][0])
        self.assertNotIn('payload',calls[0][1])

    def test_provider_error_does_not_erase_other_provider_result(self):
        def provider(url,**kwargs):
            return {'status':'rate_limited','retrieved_at':'now'} if 'virustotal' in url else ok({'query_status':'no_result'})
        result=intel.IntelClient(vt_key='a',threatfox_key='b',requester=provider).lookup('domain','example.org')
        self.assertEqual([x['status'] for x in result['reports']],['rate_limited','no_result'])

    def test_threatfox_retains_scope_and_caps_output(self):
        calls=[]
        rows=[{'id':i,'ioc':'8.8.8.8:443','ioc_type':'ip:port','last_seen':'2026-10-19',
               'confidence_level':75,'extra':'omit'} for i in range(12)]
        def provider(url,**kwargs): calls.append(kwargs); return ok({'query_status':'ok','data':rows})
        report=intel.IntelClient(vt_key='',threatfox_key='b',requester=provider).lookup('ip','8.8.8.8')['reports'][1]
        self.assertEqual(report['records_returned'],10)
        self.assertTrue(report['truncated'])
        self.assertEqual(report['records'][0]['ioc'],'8.8.8.8:443')
        self.assertTrue(calls[0]['payload']['exact_match'])
        self.assertNotIn('extra',report['records'][0])

    def test_cve_context_and_cache_preserve_retrieval_time(self):
        calls=[]
        def provider(url,**kwargs):
            calls.append(url)
            if 'cisa.gov' in url:
                return ok({'dateReleased':'2026-10-19','vulnerabilities':[{'cveID':'CVE-2025-12345','dateAdded':'2026-01-01'}]})
            return ok({'data':[{'cve':'CVE-2025-12345','epss':'0.75','percentile':'0.99','date':'2026-10-19'}]})
        client=intel.IntelClient(requester=provider)
        first=client.lookup_cve('cve-2025-12345')
        second=client.lookup_cve('CVE-2025-12345')
        self.assertTrue(first['reports'][0]['listed'])
        self.assertTrue(second['reports'][0]['cache_hit'])
        self.assertEqual(first['reports'][0]['retrieved_at'],second['reports'][0]['retrieved_at'])
        self.assertEqual(sum('cisa.gov' in url for url in calls),1)
        self.assertEqual(first['reports'][1]['records'][0]['date'],'2026-10-19')

    def test_kev_failure_is_not_absence(self):
        def provider(url,**kwargs): return {'status':'network_error','retrieved_at':'now'} if 'cisa.gov' in url else ok({'data':[]})
        result=intel.IntelClient(requester=provider).lookup_cve('CVE-2025-12345')
        self.assertEqual(result['reports'][0]['status'],'network_error')
        self.assertNotIn('listed',result['reports'][0])
        self.assertEqual(result['reports'][1]['status'],'no_result')

    def test_invalid_provider_shapes_are_rejected(self):
        for data in ([],{'data':[]},{'data':{'attributes':[]}}):
            report=intel.IntelClient(vt_key='a',threatfox_key='',requester=lambda *a,**k:ok(data)).lookup('ip','8.8.8.8')['reports'][0]
            self.assertEqual(report['status'],'invalid_response')
        result=intel.IntelClient(requester=lambda *a,**k:ok({'vulnerabilities':[None]})).kev('CVE-2025-12345')
        self.assertEqual(result['status'],'invalid_response')

    def test_transport_errors_do_not_echo_bodies_or_headers(self):
        error=HTTPError('https://www.virustotal.com/api/v3/files/x',401,'invalid',{},BytesIO(b'SECRET_PAYLOAD'))
        with patch.object(intel,'build_opener') as opener:
            opener.return_value.open.side_effect=error
            result=intel.request_json('https://www.virustotal.com/api/v3/files/x',headers={'x-apikey':'SECRET_KEY'})
        self.assertEqual(result['status'],'unauthorized')
        self.assertNotIn('SECRET',json.dumps(result))

    def test_transport_limits_size_and_accepts_json(self):
        with patch.object(intel,'build_opener') as opener:
            opener.return_value.open.return_value=Response(b'x'*33)
            self.assertEqual(intel.request_json('https://api.first.org/data/v1/epss',max_bytes=32)['status'],'response_too_large')
            opener.return_value.open.return_value=Response(b'{"data":[]}')
            self.assertEqual(intel.request_json('https://api.first.org/data/v1/epss')['status'],'ok')
            self.assertEqual(opener.return_value.open.call_args.kwargs['timeout'],10)

    def test_destination_and_redirect_controls(self):
        with patch.object(intel,'build_opener') as opener:
            self.assertEqual(intel.request_json('http://api.first.org/data/v1/epss')['status'],'blocked_destination')
            self.assertEqual(intel.request_json('https://example.org/data')['status'],'blocked_destination')
            opener.assert_not_called()
        self.assertIsNone(intel.NoRedirects().redirect_request(None,None,302,'',{},'https://example.org'))

    def test_invalid_cve_does_not_request(self):
        def forbidden(*args,**kwargs): self.fail('Unexpected provider call')
        self.assertEqual(intel.IntelClient(requester=forbidden).lookup_cve('CVE-2025-12345?secret')['status'],'invalid_input')

    def test_network_failure_remains_explicit(self):
        with patch.object(intel,'build_opener') as opener:
            opener.return_value.open.side_effect=URLError('sensitive details omitted')
            result=intel.request_json('https://api.first.org/data/v1/epss')
        self.assertEqual(result['status'],'network_error')
        self.assertNotIn('sensitive',json.dumps(result))

    def test_actual_stdio_mcp_handshake_and_tool_contracts(self):
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
        async def exercise():
            env=dict(os.environ,VT_API_KEY='',THREATFOX_AUTH_KEY='',PYTHONDONTWRITEBYTECODE='1')
            params=StdioServerParameters(command=sys.executable,args=['-B',str(INTEGRATION/'server.py')],env=env)
            async with stdio_client(params) as (read,write):
                async with ClientSession(read,write) as session:
                    await session.initialize()
                    tools=(await session.list_tools()).tools
                    self.assertEqual({tool.name for tool in tools},{'lookup_hash','lookup_ip','lookup_domain','lookup_cve'})
                    self.assertTrue(all(tool.annotations.readOnlyHint for tool in tools))
                    result=await session.call_tool('lookup_ip',{'ip':'127.0.0.1'})
                    payload=result.structuredContent or json.loads(result.content[0].text)
                    self.assertEqual(payload['status'],'invalid_input')
                    result=await session.call_tool('lookup_hash',{'sha256':'a'*64})
                    payload=result.structuredContent or json.loads(result.content[0].text)
                    self.assertEqual([x['status'] for x in payload['reports']],['not_configured','not_configured'])
        asyncio.run(exercise())


if __name__=='__main__': unittest.main()
