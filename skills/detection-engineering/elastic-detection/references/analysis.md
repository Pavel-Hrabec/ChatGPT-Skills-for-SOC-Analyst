# Elastic Detection: analysis guide

## Evidence contract

Use detection hypothesis, Elastic version, ECS/raw events, index/data-view scope and desired rule type. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Select query, threshold, EQL or other supported rule type by behavior.
- **Check 2:** Verify fields, timestamp mapping and event-join semantics.
- **Check 3:** Define interval, lookback, grouping and suppression without assuming one rule type supports every feature.

## Interpret the source

Freeze the target engine, schema/mapping, rule version and unit of detection before writing or translating logic. Preserve case, null, multivalue, time and cardinality semantics. Distinguish static/schema checks, compilation, backend result matches and alert-service behavior. Provide positive, near-miss and legitimate cases, plus missing-field/time-boundary cases where relevant. Do not report unexecuted tests as passed or enable a rule by merely generating its configuration.

## Discriminate and correlate

Consider legitimate administrative patterns and parser differences need representative negative cases. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: generate version-compatible rule artifacts and backend-native tests for review. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return rule artifact, telemetry contract, test cases and readiness limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a valid query or imported rule does not establish successful alert generation.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
