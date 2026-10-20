# Remote Thread: analysis guide

## Evidence contract

Use source/target process GUIDs, thread start metadata, access events, memory or module reports. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve both processes and their signers.
- **Check 2:** Compare start address/module information with the target's mapped modules.
- **Check 3:** Correlate prior process access and subsequent target behavior while accounting for telemetry gaps.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider debuggers, profilers, overlays and security products can create cross-process threads. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: examine supplied memory findings and target network/process activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return cross-process activity assessment with alternative explanations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a remote thread is one injection-related observation and does not establish payload semantics.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
