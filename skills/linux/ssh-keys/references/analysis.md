# SSH Keys: analysis guide

## Evidence contract

Use authorized-key files, key fingerprints, file-change records, sshd configuration and session logs. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify the account, effective AuthorizedKeysFile or external key command.
- **Check 2:** Compare key options and restrictions rather than fingerprint alone.
- **Check 3:** Correlate addition time and writer identity with later accepted-key sessions.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider access provisioning, key rotation and approved automation change authorized keys. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review identity ownership, change approvals and matching fingerprint logins. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return key-change provenance and evidence of new access. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a key addition can expand access but does not prove the key was subsequently used.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
