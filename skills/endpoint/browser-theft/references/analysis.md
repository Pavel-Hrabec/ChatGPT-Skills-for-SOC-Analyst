# Browser Theft: analysis guide

## Evidence contract

Use file-access or endpoint alerts, browser profile paths, caller process, archive/network evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Determine which user's profile and store were accessed.
- **Check 2:** Distinguish the browser's normal database reads from unrelated process access.
- **Check 3:** Correlate copied stores with staging, key-access telemetry and outbound transfer.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider profile migration, password managers and endpoint backups may access the same databases. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: pivot through the accessing process, staged files and affected account sessions. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return profile exposure scope and evidence of subsequent credential/session misuse. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: database access alone does not prove successful decryption or token reuse.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
