# COM Hijack: analysis guide

## Evidence contract

Use registry value changes, CLSID or ProgID, per-user and machine registration, invoking process. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify affected registration view and user scope.
- **Check 2:** Compare InprocServer32 or LocalServer32 paths with approved registration.
- **Check 3:** Connect the modified class to an observed application activation and server process.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider software installation and COM component upgrades legitimately change registrations. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the writer process, target binary metadata and repeated activation after the change. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return registration-to-activation evidence chain and scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a registry write alone demonstrates configuration change rather than successful execution.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
