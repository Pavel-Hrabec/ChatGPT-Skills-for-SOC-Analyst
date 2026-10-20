# OAuth Grants: analysis guide

## Evidence contract

Use consent audit, app/service-principal identity, permissions, consenting user/admin and sign-ins. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify delegated versus application permissions and the actual grant object.
- **Check 2:** Compare requested access with app ownership/publisher and business purpose.
- **Check 3:** Correlate grant time with application use and resource operations.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider approved SaaS onboarding and application upgrades change grants. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review app credentials, later grant changes and affected mail/files. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return grant provenance, effective permission scope and observed access. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a consent prompt or permission request is not evidence a grant was approved or used.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
