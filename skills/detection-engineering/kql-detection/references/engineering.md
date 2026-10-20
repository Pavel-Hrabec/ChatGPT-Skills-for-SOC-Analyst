## Product and schema decisions

Defender hunting tables and Sentinel tables differ in timestamps, entities, data availability and detection packaging. Establish the product before selecting fields. For Defender event-backed detections, inspect current requirements for source timestamps, ReportId and device/account identifiers. Preserve a coherent original event when using arg_max; independently maximizing several fields can construct a record that never occurred. Never generate a fake ReportId to satisfy a wizard.

For Sentinel, use the actual analytics rule type and workspace schema. Include entity mappings only for confirmed columns and appropriate identifier types. Record custom functions and watchlists as dependencies. A query that runs in a hunting window is not automatically valid as a scheduled analytics rule or a near-real-time rule.

## Time, joins and aggregation

Distinguish event time from ingestion time. Follow the selected product's current scheduling and prefilter behavior; do not add a universal timestamp predicate by habit. For standalone replay queries, use explicit UTC bounds. Explain how overlapping schedules avoid gaps and how repeated results become alerts.

Select join keys that represent the same entity and scope. Process IDs can be reused; identity across hosts or time needs stronger keys. Check row counts before and after joins for multiplication. Set join flavor intentionally. Verify bin boundaries and whether one entity can produce multiple result rows. Missing values and case normalization can change matches.

## Operational handoff

Supply the query, parameters, verified schema, expected result columns, schedule rationale, grouping/suppression choices and any unresolved product restrictions. Compare observed results with expected case IDs; state whether the query compiled, returned evidence and produced intended alerts as separate findings. Backend execution and service rule execution are separate validation stages.
