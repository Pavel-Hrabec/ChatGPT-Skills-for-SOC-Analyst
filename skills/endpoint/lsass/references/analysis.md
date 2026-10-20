# LSASS: analysis guide

## Evidence contract

Use process-access events, source/target process identities, access rights, signer details and file creation evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve the target image and initiating process with stable process identifiers.
- **Check 2:** Interpret granted rights and call-trace context without treating one access mask as a verdict.
- **Check 3:** Correlate resulting dump files, child processes and subsequent authentication.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider eDR inspection, crash diagnostics and approved credential providers can access LSASS. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: pivot from the initiating process to dump artifacts, outbound transfers and later use of the affected identity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return evidence-linked assessment of the access chain and credential exposure scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: access telemetry establishes an attempted interaction; it does not prove credentials were successfully extracted.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
