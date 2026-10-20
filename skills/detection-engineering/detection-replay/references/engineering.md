## Replay choices

Prefer an isolated environment with known schema and content versions. Existing indexed datasets can support read-only replay. Loading new records changes a backend and needs a defined destination, routing, retention and cleanup plan. Avoid sending replay telemetry to production alert routing or response actions. Inspect available test tooling and its current configuration before choosing commands.

## Clock handling

Historical data may fall outside current scheduled lookbacks. A bounded historical query can avoid modifying evidence. If testing the scheduler requires shifting time, document why, which fields change, a common offset and how joins remain consistent. Distinguish event time, observed/ingested time and execution time. Late-arrival tests need intentionally different clocks; shifting all clocks does not create lag.

Do not regenerate entity identifiers or reorder records silently. Events with equal timestamps may lack an intrinsic order. Preserve links across process, network and authentication records. Record parser and lookup versions, source routing and replay ingestion completeness.

## Compare and diagnose

Inspect input record count and eligible time range before the rule. Separate no relevant data, parser mismatch, unsupported fields, result truncation and true predicate nonmatches. Verify grouped detections with expected entity/window identities, not only row counts. Distinguish a successful query match from successful downstream alert generation. Idempotent ingestion and duplicate alerts require separate checks.

Datasets are selected evidence, not a complete production population. Public attack data is useful for regression tests but cannot alone establish false-positive rate or detection recall in a customer environment. Report the scope of each replay and keep a run record that another engineer can reproduce.
