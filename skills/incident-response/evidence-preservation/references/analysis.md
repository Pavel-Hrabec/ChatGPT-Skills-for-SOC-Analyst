# Evidence Preservation: analysis guide

## Evidence contract

Use evidence sources, incident window, retention, acquisition capabilities and handling requirements. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Prioritize volatile and short-retention sources according to investigation need.
- **Check 2:** Record acquisition method, timestamps, timezone, hash and custodian.
- **Check 3:** Preserve original artifacts and document transformations and access separately.

## Interpret the source

Separate confirmed evidence, hypotheses and missing telemetry before planning action. Tie each recommendation to affected assets/identities, owner, evidence preservation, operational dependencies and success criteria. Preserve UTC/source timezone and acquisition provenance. Generated plans do not execute containment or recovery. Scope confidence to the sources available rather than promising complete eradication from partial observations.

## Discriminate and correlate

Consider clock skew, partial exports and changing cloud retention can affect evidence interpretation. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: specify bounded collection requests and integrity checks for available authorized tools. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return preservation plan, acquisition ledger and explicit integrity/completeness limits. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: an export or hash alone does not establish a complete chain of custody or collection completeness.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
