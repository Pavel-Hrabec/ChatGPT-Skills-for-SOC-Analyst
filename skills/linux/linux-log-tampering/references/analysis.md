# Linux Log Tampering: analysis guide

## Evidence contract

Use audit/journal status, file modifications, service events, collector health and command evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Distinguish rotation/retention from truncation or deletion.
- **Check 2:** Identify service stops, audit-policy changes and the responsible identity.
- **Check 3:** Compare host logs with independently received collector records.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider log rotation, storage incidents and planned collector maintenance cause gaps. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: check remote ingestion continuity and adjacent privileged sessions. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return logging-impact timeline and supported tampering assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a local time gap alone cannot establish intentional evidence destruction.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
