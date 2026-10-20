# YARA: analysis guide

## Evidence contract

Use representative benign/malicious artifact descriptions, byte/string evidence, target format and YARA version. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Choose stable content/structure features with explicit size/type guards.
- **Check 2:** Handle offsets, encoding and modules against the selected engine.
- **Check 3:** Test near misses and legitimate files and account for expensive wildcard or regex patterns.

## Interpret the source

Freeze the target engine, schema/mapping, rule version and unit of detection before writing or translating logic. Preserve case, null, multivalue, time and cardinality semantics. Distinguish static/schema checks, compilation, backend result matches and alert-service behavior. Provide positive, near-miss and legitimate cases, plus missing-field/time-boundary cases where relevant. Do not report unexecuted tests as passed or enable a rule by merely generating its configuration.

## Discriminate and correlate

Consider shared libraries, packers and copied strings may occur in unrelated benign software. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: provide a rule and reproducible offline validation plan using inert supplied samples. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return yARA rule, rationale, dependency/performance notes and measured test status. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: one matching string or a successful compile does not establish family attribution or production accuracy.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
