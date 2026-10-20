# Containment Plan: analysis guide

## Evidence contract

Use affected assets/identities, ongoing activity, business dependencies and authorized response options. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate confirmed compromise from related hypotheses.
- **Check 2:** Evaluate control points, operational impact and evidence-preservation order.
- **Check 3:** Define rollback, owner and success criteria for each proposed action.

## Interpret the source

Separate confirmed evidence, hypotheses and missing telemetry before planning action. Tie each recommendation to affected assets/identities, owner, evidence preservation, operational dependencies and success criteria. Preserve UTC/source timezone and acquisition provenance. Generated plans do not execute containment or recovery. Scope confidence to the sources available rather than promising complete eradication from partial observations.

## Discriminate and correlate

Consider shared infrastructure and critical service dependencies can make broad containment disproportionate. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: prepare a reviewable action sequence tied to existing runbooks and current authorization. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return prioritized containment plan with dependencies, ownership and verification criteria. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: planning containment does not authorize isolating hosts, disabling identities or blocking infrastructure.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
