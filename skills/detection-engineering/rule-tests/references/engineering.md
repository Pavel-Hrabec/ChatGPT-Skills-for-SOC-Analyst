## Test levels

Distinguish document/schema validation, conversion/compilation, semantic execution, replay on representative data and alert service integration. A successful earlier stage cannot establish success at a later stage. Match the harness to the actual deliverable and its release; contentctl and Elastic's repository tooling are platform-specific examples.

## The test oracle

Use externally specified expected case IDs and alert entities. Exact event-level comparison is appropriate for event rules; grouped rules need expected entity/window tuples and alert cardinality. A case may contain ten matching source events but legitimately produce one grouped alert. Avoid expecting one output row per input line as a universal assertion.

Cover each logical branch and exclusion, case/escaping behavior, missing/null fields, duplicates, counts just below/at/above a threshold, temporal ordering, out-of-order arrivals and window boundaries where relevant. Include a legitimate case resembling the attack. A single all-positive fixture cannot demonstrate selectivity. Synthetic fixtures must be labeled synthetic; public datasets need their own provenance and usage review.

Keep modifications minimal: change one decisive predicate in a near-miss fixture where possible. Test benign and malicious outcomes through the same normalization pipeline. Keep fixture records inert; never execute captured commands or attachments to make an event appear realistic.

## Result reporting

List rule/fixture hashes or commit IDs, engine and dependency versions, normalization, exact command, exit status, expected keys and actual keys. Report failures and skips separately. Precision requires adjudicated alert labels; false-positive rate requires a defined negative population. A small fixture suite supports regression confidence and does not measure production detection rates.
