# SSH: analysis guide

## Evidence contract

Use authentication logs, source address, account, auth method, session identifiers and host context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate failed authentication from accepted sessions.
- **Check 2:** Inspect key fingerprints and source changes in relation to the account's baseline.
- **Check 3:** Correlate accepted sessions with commands or audit records rather than assuming login implies malicious execution.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider bastions, NAT, automation and administrator travel can change apparent source patterns. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: pivot from the accepted session to privilege use and outbound connections. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return authentication-to-session assessment with host and identity scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: source geolocation and repeated failures alone cannot establish account compromise.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
