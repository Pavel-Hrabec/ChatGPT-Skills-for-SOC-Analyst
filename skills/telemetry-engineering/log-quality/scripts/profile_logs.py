"""Profile bounded local NDJSON exports; emit aggregates without event contents.

Python 3.10+. No network access or external dependencies. Exit 0 means the
profile completed, not that a data quality threshold was passed.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


MISSING = object()


def get_field(record, path):
    if path in record:
        return record[path]
    value = record
    for part in path.split('.'):
        if not isinstance(value, dict) or part not in value:
            return MISSING
        value = value[part]
    return value


def absent(value):
    return value is MISSING or value is None or value == ''


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError('Timestamp must be a string')
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('Timestamp requires an explicit timezone')
    return parsed.astimezone(timezone.utc)


def percentile(values, fraction):
    if not values:
        return None
    ordered = sorted(values)
    return ordered[max(0, math.ceil(len(ordered) * fraction) - 1)]


def reject_constant(value):
    raise ValueError('Non-standard JSON numeric constant')


def profile(path, timestamp_field, ingest_field=None, required_fields=(), id_fields=()):
    counts = Counter()
    field_counts = {field: Counter() for field in dict.fromkeys(required_fields)}
    seen = set()
    lags = []
    first = None
    last = None
    with Path(path).open(encoding='utf-8-sig') as stream:
        for line in stream:
            if not line.strip():
                continue
            counts['input_records'] += 1
            try:
                record = json.loads(line, parse_constant=reject_constant)
            except ValueError:
                counts['malformed_json'] += 1
                continue
            if not isinstance(record, dict):
                counts['non_object_records'] += 1
                continue
            counts['valid_objects'] += 1
            for field, fc in field_counts.items():
                value = get_field(record, field)
                state = ('missing' if value is MISSING else 'null' if value is None
                         else 'empty_string' if value == '' else 'present')
                fc[state] += 1
            if id_fields:
                key_values = [get_field(record, field) for field in id_fields]
                if any(absent(value) for value in key_values):
                    counts['records_without_duplicate_key'] += 1
                    key = None
                else:
                    key = json.dumps(key_values, sort_keys=True, ensure_ascii=False)
            else:
                key = json.dumps(record, sort_keys=True, ensure_ascii=False)
            if key is not None:
                counts['duplicate_eligible_records'] += 1
                digest = hashlib.sha256(key.encode()).digest()
                if digest in seen:
                    counts['duplicate_candidates'] += 1
                seen.add(digest)
            clocks = {}
            selected = [('event', timestamp_field)]
            if ingest_field:
                selected.append(('ingest', ingest_field))
            for label, field in selected:
                value = get_field(record, field)
                if absent(value):
                    counts[label + '_timestamp_missing'] += 1
                    continue
                try:
                    clocks[label] = parse_time(value)
                    counts[label + '_timestamp_valid'] += 1
                except (ValueError, OverflowError):
                    counts[label + '_timestamp_invalid'] += 1
            event_time = clocks.get('event')
            if event_time is not None:
                first = min(first, event_time) if first else event_time
                last = max(last, event_time) if last else event_time
            if 'event' in clocks and 'ingest' in clocks:
                lag = (clocks['ingest'] - clocks['event']).total_seconds()
                lags.append(lag)
                if lag < 0:
                    counts['negative_lag_pairs'] += 1
    for key in ('input_records','malformed_json','non_object_records','valid_objects',
                'duplicate_eligible_records','duplicate_candidates','records_without_duplicate_key',
                'event_timestamp_valid','event_timestamp_missing','event_timestamp_invalid',
                'negative_lag_pairs'):
        counts.setdefault(key, 0)
    if ingest_field:
        for key in ('ingest_timestamp_valid','ingest_timestamp_missing','ingest_timestamp_invalid'):
            counts.setdefault(key, 0)
    field_report = {}
    denominator = counts['valid_objects']
    for field, fc in field_counts.items():
        field_report[field] = {key: fc[key] for key in ('present','missing','null','empty_string')}
        field_report[field]['present_fraction'] = fc['present']/denominator if denominator else None
    return {
        'schema_version': 1,
        'counts': dict(counts),
        'required_fields_denominator': 'valid_objects',
        'required_fields': field_report,
        'event_time_range_utc': {'first': first.isoformat() if first else None,
                                 'last': last.isoformat() if last else None},
        'duplicate_key_mode': list(id_fields) if id_fields else 'canonical_whole_object',
        'ingestion_lag_seconds': {'eligible_pairs': len(lags),
                                  'min': min(lags) if lags else None,
                                  'max': max(lags) if lags else None,
                                  'p50': percentile(lags, .5),
                                  'p95': percentile(lags, .95),
                                  'method': 'nearest_rank'},
        'limitations': ['Sample describes supplied records only.',
                        'Duplicate candidates require source context.',
                        'No backend, network or reputation lookups performed.'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Local NDJSON export')
    parser.add_argument('--timestamp-field', required=True)
    parser.add_argument('--ingest-field')
    parser.add_argument('--required-field', action='append', default=[])
    parser.add_argument('--id-field', action='append', default=[])
    args = parser.parse_args()
    try:
        report = profile(args.input, args.timestamp_field, args.ingest_field,
                         args.required_field, args.id_field)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f'Input error: {type(exc).__name__}\n')
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
