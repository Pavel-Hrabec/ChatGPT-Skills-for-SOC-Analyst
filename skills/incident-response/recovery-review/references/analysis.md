# Recovery Review: analysis guide

## Evidence contract

Use restoration records, known-good provenance, identity/control changes and post-recovery telemetry. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Verify the affected persistence/access paths were addressed rather than only symptoms.
- **Check 2:** Distinguish restored availability from restored trust.
- **Check 3:** Define recurrence checks, rollback triggers and accountable owners.

## Interpret the source

Separate confirmed evidence, hypotheses and missing telemetry before planning action. Tie each recommendation to affected assets/identities, owner, evidence preservation, operational dependencies and success criteria. Preserve UTC/source timezone and acquisition provenance. Generated plans do not execute containment or recovery. Scope confidence to the sources available rather than promising complete eradication from partial observations.

## Discriminate and correlate

Consider backups may contain the same persistence or vulnerable configuration as the affected system. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review restored assets, credential changes and monitoring evidence across the incident scope. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return recovery readiness assessment and evidence-supported residual risk. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a successful restore or clean scan alone does not establish eradication.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
