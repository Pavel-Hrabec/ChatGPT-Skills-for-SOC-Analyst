# Password Spray: analysis guide

## Evidence contract

Use authentication results, target identities, source/client information, time windows and success events. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Group attempts by credible source/client identity and target diversity.
- **Check 2:** Separate spray-like breadth from brute-force depth while checking result codes.
- **Check 3:** Identify any subsequent successes and compare device/session context.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider misconfigured shared clients, health checks and stale passwords can affect multiple accounts. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: pivot successful identities to MFA/device/session activity and resource access. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return attempt pattern and success-linked account scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: nAT aggregation and failure counts alone do not prove a shared attacker or compromised account.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
