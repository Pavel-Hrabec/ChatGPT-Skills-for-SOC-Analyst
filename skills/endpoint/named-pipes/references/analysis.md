# Named Pipes: analysis guide

## Evidence contract

Use pipe creation/connection events, host, process identities, pipe name and session time. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Join creation and connection on host, name and time rather than name alone.
- **Check 2:** Identify server and client processes from actual event fields.
- **Check 3:** Compare recurrence and peer processes with the host's normal software.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider browsers, management tools and EDR components use many legitimate pipes. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: correlate involved process trees and any remote SMB session. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return pipe communication relationship and process-based assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a pipe name matching a published example is an indicator to investigate rather than proof of a specific framework.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
