# Cron: analysis guide

## Evidence contract

Use crontab contents, file metadata, owner, schedule, process events and change history. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Parse the actual schedule format and user context.
- **Check 2:** Resolve referenced scripts and writable locations without executing them.
- **Check 3:** Correlate the configuration change with scheduled launches and their child/network behavior.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider backups, certificate renewal and monitoring commonly use scheduled cron jobs. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: inspect the writer process and compare the job with configuration-management records. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return schedule-to-execution assessment and affected account scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a suspicious crontab entry alone does not prove the job has run.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
