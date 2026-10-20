# Rule Migration: analysis guide

## Evidence contract

Use original rule, source/target schemas and versions, field mapping and expected test outcomes. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Document the original unit of detection and temporal/aggregation semantics.
- **Check 2:** Map null, case, regex and multivalue behavior explicitly.
- **Check 3:** Verify target scheduling, entity mapping and alert cardinality instead of transliterating syntax.

## Interpret the source

Freeze the target engine, schema/mapping, rule version and unit of detection before writing or translating logic. Preserve case, null, multivalue, time and cardinality semantics. Distinguish static/schema checks, compilation, backend result matches and alert-service behavior. Provide positive, near-miss and legitimate cases, plus missing-field/time-boundary cases where relevant. Do not report unexecuted tests as passed or enable a rule by merely generating its configuration.

## Discriminate and correlate

Consider local macros, accelerated models and custom functions can encode hidden behavior. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: deliver the translated rule with a semantic difference table and matched regression cases. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return target rule, dependency map and measured equivalence limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: successful conversion does not prove equivalent backend or alert behavior.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
