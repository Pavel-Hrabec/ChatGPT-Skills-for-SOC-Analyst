# Query Performance: analysis guide

## Evidence contract

Use exact query, engine/version, execution metrics, schema, dataset window and expected results. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify expensive joins, scans, grouping and materialization using observed plans where available.
- **Check 2:** Preserve filtering and null/time semantics when optimizing.
- **Check 3:** Compare output identities and cardinality on the same bounded dataset.

## Interpret the source

Freeze the target engine, schema/mapping, rule version and unit of detection before writing or translating logic. Preserve case, null, multivalue, time and cardinality semantics. Distinguish static/schema checks, compilation, backend result matches and alert-service behavior. Provide positive, near-miss and legitimate cases, plus missing-field/time-boundary cases where relevant. Do not report unexecuted tests as passed or enable a rule by merely generating its configuration.

## Discriminate and correlate

Consider different cache state or sampling can distort timing comparisons. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: deliver a minimal query diff and repeatable before/after measurement plan. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return optimization diff, result-equivalence checks and measured cost limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: faster execution is not an improvement if expected security findings are removed.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
