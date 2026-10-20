# Threat Coverage: analysis guide

## Evidence contract

Use cited campaign behavior, environment exposure, telemetry and validated detection inventory. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Break the report into observable steps with prerequisites.
- **Check 2:** Connect each relevant step to actual telemetry and tested rules.
- **Check 3:** Assess sequence gaps and plausible alternate attacker paths.

## Interpret the source

Freeze the target engine, schema/mapping, rule version and unit of detection before writing or translating logic. Preserve case, null, multivalue, time and cardinality semantics. Distinguish static/schema checks, compilation, backend result matches and alert-service behavior. Provide positive, near-miss and legitimate cases, plus missing-field/time-boundary cases where relevant. Do not report unexecuted tests as passed or enable a rule by merely generating its configuration.

## Discriminate and correlate

Consider a report's tooling or indicators may be absent while equivalent behavior remains relevant. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: prioritize environment-specific hunts, detector tests and collection improvements. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return threat-specific coverage map with evidence strength and action priorities. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a full technique checklist does not prove that a particular intrusion path would be detected.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
