## Assess the population

Inventory expected sources and distinguish coverage from volume. A supplied export can describe its own records; it cannot establish fleet-wide sensor coverage without an expected-asset population. Sampling, export truncation, query predicates, retention and role-based access can all bias the view.

Separate total input records from valid JSON objects and from records eligible for a particular measurement. Report missing, null, empty and type errors explicitly. A zero or false value is not missing. Trace field completeness to the detection that needs it; not every optional field should be universally required.

## Clocks and duplicates

Calculate event-to-ingest lag only when both clocks are defined and timezone-aware. Negative lag may indicate clock skew or swapped fields. Future timestamps, delayed batches and coarse timestamp precision need investigation. Do not substitute an observed timestamp for event time silently.

Exact duplicate records and repeated event identifiers are candidate duplicates. Namespace IDs with source/host when that is required by the producer. Repeated legitimate actions can have identical content. Deduplication policy is a separate decision and can remove real evidence if applied indiscriminately.

## Offline helper contract

Run `python scripts/profile_logs.py events.ndjson --timestamp-field event_time --ingest-field ingest_time --required-field host --required-field action`. Field paths first match a literal key, then traverse nested objects by dots; arrays are not traversed. Use repeated `--id-field` arguments for a composite key, otherwise duplicates use the canonical whole object. The script reads local data and emits aggregate JSON only; it never sends records externally.

Input is one JSON object per nonblank line. Timestamps must be ISO 8601 strings with an explicit offset; epoch numbers and naive timestamps are rejected. Percentiles use the nearest-rank method over eligible lag pairs. The helper keeps duplicate-key hashes and lag samples in memory; use bounded exports for large environments. A successful process exit means profiling completed, not that the data passed a quality policy.
