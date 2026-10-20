## Normalization and provenance

Preserve type, raw value, normalized value, original object/provider ID and source reference. An IP:port observation has a different scope from an IP-only indicator. CIDRs, STIX patterns and domain wildcards need their own typed parsers. Do not silently strip ports or flatten compound patterns to a broader block candidate.

Separate first/last observed time from feed publication, object modification, retrieval and indicator validity times. In STIX, valid_from/valid_until describe indicator validity; they do not automatically identify first/last observed malicious activity. Revocation, expiry, age and removal are different states.

Confidence scales need provider-specific interpretation. Do not average incomparable scores or count derivative reports as independent confirmations. Preserve TLP and other sharing restrictions during enrichment and export; a TLP label is not a numerical confidence or severity. Unknown sharing restrictions require resolution before forwarding an artifact externally.

## Offline helper contract

`python scripts/profile_feed.py normalized.ndjson --as-of 2026-10-20T00:00:00Z --max-age-days 30` profiles normalized records only, not arbitrary STIX/MISP/OpenCTI exports. Supported `type` values are `ipv4`, `ipv6`, `domain`, `url`, `sha256`; `indicator` is the value. Optional fields are `provider`, `reference`, `first_seen`, `last_seen`, `valid_until`, `confidence` (already normalized 0..100), `revoked` (boolean), and `tlp`. Use an explicit field mapping from provider documentation; do not infer these fields from similar names.

Domains normalize to lower-case IDNA and IPs to canonical addresses; URL values retain their original spelling/path/query after trimming surrounding whitespace. Unsupported types and defanged values are reported without auto-repair. The helper emits aggregate counts and line-level issue labels without raw indicators. It performs no reputation lookup and makes no malicious/benign classification. The age threshold is the user's policy, not a feed-independent measure of indicator truth. Hashes used for deduplication and per-indicator state require bounded input sizes.
