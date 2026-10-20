# Sudo: analysis guide

## Evidence contract

Use sudo logs, invoking user, target user, command/arguments, terminal and policy evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify the original identity and effective target account.
- **Check 2:** Compare the actual command with the applicable sudoers rule and time of policy changes.
- **Check 3:** Inspect execution success and session continuity rather than assuming every sudo request succeeded.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider approved automation and administrator maintenance commonly invoke privileged commands. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review adjacent audit execution and changes to privileged configuration. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return privilege-use timeline and policy-context assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a logged sudo request is not sufficient to prove an unauthorized successful privilege escalation.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
