"""Measure normalized, bounded feed exports without network access.

Python 3.10+. Input is NDJSON, not arbitrary STIX, MISP or provider JSON.
See references/engineering.md for the input contract and normalization limits.
Exit 0 means profiling completed, not a feed quality or maliciousness verdict.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import ipaddress
import json
import math
from pathlib import Path
import re
from urllib.parse import urlsplit


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError('Timestamp must be an ISO string')
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('Timestamp requires an explicit timezone')
    return parsed.astimezone(timezone.utc)


def normalize_domain(value):
    if value.endswith('.'):
        value = value[:-1]
    value = value.encode('idna').decode('ascii').lower()
    labels = value.split('.')
    if (len(value) > 253 or len(labels) < 2
            or any(not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', label)
                   for label in labels)):
        raise ValueError('Unsupported domain')
    return value


def normalize(kind, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Missing indicator')
    value = value.strip()
    if any(token in value for token in ('[.]','[:]','(dot)')):
        raise ValueError('Defanged indicator')
    if kind in ('ipv4','ipv6'):
        address = ipaddress.ip_address(value)
        if address.version != (4 if kind == 'ipv4' else 6) or '%' in value:
            raise ValueError('Type mismatch or scoped address')
        return str(address)
    if kind == 'domain':
        return normalize_domain(value)
    if kind == 'sha256':
        if not re.fullmatch(r'[0-9a-fA-F]{64}', value):
            raise ValueError('Invalid SHA256')
        return value.lower()
    if kind == 'url':
        parsed = urlsplit(value)
        if (parsed.scheme not in ('http','https') or not parsed.hostname
                or parsed.username is not None or parsed.password is not None
                or re.search(r'\s', value)):
            raise ValueError('Unsupported URL')
        _ = parsed.port  # Trigger validation; do not remove a meaningful port.
        try:
            address = ipaddress.ip_address(parsed.hostname)
            if '%' in str(address):
                raise ValueError('Scoped address is unsupported')
        except ValueError:
            normalize_domain(parsed.hostname)
        return value
    raise ValueError('Unsupported type')


def reject_constant(value):
    raise ValueError('Non-standard JSON numeric constant')


def profile(path, as_of, max_age_days):
    counts = Counter()
    issue_counts = Counter()
    seen = set()
    source_by_indicator = {}
    issue_lines = []
    with Path(path).open(encoding='utf-8-sig') as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            counts['input_records'] += 1
            try:
                record = json.loads(line, parse_constant=reject_constant)
            except ValueError:
                counts['malformed_json'] += 1
                issue_counts['malformed_json'] += 1
                if len(issue_lines) < 100:
                    issue_lines.append({'line':line_number,'issues':['malformed_json']})
                continue
            if not isinstance(record, dict):
                counts['non_object_records'] += 1
                issue_counts['non_object_record'] += 1
                if len(issue_lines) < 100:
                    issue_lines.append({'line':line_number,'issues':['non_object_record']})
                continue
            counts['valid_objects'] += 1
            issues = []
            kind = record.get('type')
            key = None
            try:
                normalized = normalize(kind, record.get('indicator'))
                key = hashlib.sha256(json.dumps([kind, normalized]).encode()).digest()
                counts['valid_indicators'] += 1
                if key in seen:
                    issues.append('duplicate_indicator_candidate')
                seen.add(key)
            except (ValueError, TypeError, UnicodeError):
                counts['invalid_or_unsupported_indicators'] += 1
                issues.append('invalid_or_unsupported_indicator')
            provider = record.get('provider')
            if not isinstance(provider, str) or not provider.strip():
                issues.append('missing_provider')
            elif key is not None:
                providers = source_by_indicator.setdefault(key, set())
                providers.add(hashlib.sha256(provider.strip().encode()).digest())
            reference = record.get('reference')
            if not isinstance(reference, str) or not reference.strip():
                issues.append('missing_reference')
            clocks = {}
            for field in ('first_seen','last_seen','valid_until'):
                value = record.get(field)
                if value in (None, ''):
                    if field != 'valid_until':
                        issues.append('missing_'+field)
                    continue
                try:
                    clocks[field] = parse_time(value)
                except (ValueError, OverflowError):
                    issues.append('invalid_'+field)
            if ('first_seen' in clocks and 'last_seen' in clocks
                    and clocks['first_seen'] > clocks['last_seen']):
                issues.append('observation_order_invalid')
            age_clock = clocks.get('last_seen', clocks.get('first_seen'))
            if any(clocks[field] > as_of for field in ('first_seen','last_seen') if field in clocks):
                issues.append('future_observation')
            if age_clock is None:
                issues.append('age_unknown')
            else:
                counts['age_eligible_records'] += 1
                counts['age_from_last_seen' if 'last_seen' in clocks else 'age_from_first_seen'] += 1
                if (as_of - age_clock).total_seconds() > max_age_days * 86400:
                    issues.append('older_than_policy')
            if 'valid_until' in clocks and clocks['valid_until'] <= as_of:
                issues.append('expired_validity')
            confidence = record.get('confidence')
            if confidence is None:
                issues.append('missing_confidence')
            elif (isinstance(confidence, bool) or not isinstance(confidence, (float,int))
                    or not math.isfinite(confidence) or not 0 <= confidence <= 100):
                issues.append('invalid_normalized_confidence')
            revoked = record.get('revoked')
            if revoked is True:
                issues.append('revoked')
            elif revoked is not None and not isinstance(revoked, bool):
                issues.append('invalid_revoked_value')
            tlp = record.get('tlp')
            if tlp is None or tlp == '':
                issues.append('sharing_restriction_unknown')
            elif not isinstance(tlp, str) or tlp not in (
                    'TLP:CLEAR','TLP:GREEN','TLP:AMBER','TLP:AMBER+STRICT','TLP:RED'):
                issues.append('unrecognized_tlp_value')
            if issues:
                counts['records_with_issues'] += 1
                issue_counts.update(issues)
                if len(issue_lines) < 100:
                    issue_lines.append({'line':line_number,'issues':issues})
    for key in ('input_records','malformed_json','non_object_records','valid_objects',
                'valid_indicators','invalid_or_unsupported_indicators',
                'age_eligible_records','records_with_issues'):
        counts.setdefault(key,0)
    return {'schema_version':1,'as_of_utc':as_of.isoformat(),
            'max_age_days_policy':max_age_days,'counts':dict(counts),
            'unique_valid_indicators':len(seen),
            'indicators_seen_across_provider_labels':sum(len(v)>1 for v in source_by_indicator.values()),
            'issues':dict(issue_counts),'issue_lines_first_100':issue_lines,
            'limitations':['Normalized NDJSON only; no automatic provider/STIX field mapping.',
                           'Provider labels do not establish independent evidence.',
                           'URL normalization is deliberately conservative.',
                           'No network lookup or malicious/benign classification performed.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Local normalized NDJSON')
    parser.add_argument('--as-of', required=True, help='Timezone-aware ISO evaluation time')
    parser.add_argument('--max-age-days', type=float, default=30)
    args = parser.parse_args()
    try:
        as_of = parse_time(args.as_of)
        if not math.isfinite(args.max_age_days) or args.max_age_days < 0:
            raise ValueError('max-age-days must be finite and nonnegative')
    except (ValueError,OverflowError) as exc:
        parser.error(str(exc))
    try:
        result = profile(args.input,as_of,args.max_age_days)
    except (OSError,UnicodeError) as exc:
        parser.exit(2,f'Input error: {type(exc).__name__}\n')
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__ == '__main__':
    main()
