# Linux Audit: analysis guide

## Evidence contract

Use raw audit records, serial/event identifiers, host, syscall, architecture and identity fields. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Group related records by event identity rather than individual line.
- **Check 2:** Distinguish login identity from real/effective IDs and interpret syscall success.
- **Check 3:** Join EXECVE, PATH, CWD and SYSCALL context without inventing missing arguments.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider administrative tooling and service startup can resemble attacker execution. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: pivot to associated login sessions, file changes and network telemetry. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return reconstructed audit events with identity and success semantics. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: an audit rule's absence or lost records limits conclusions; isolated PATH lines do not establish executed commands.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
