# Defender Tampering: analysis guide

## Evidence contract

Use configuration audit events, exclusion changes, service state, tamper-protection results and actor context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Distinguish a requested change from a successfully applied change.
- **Check 2:** Compare exclusions and protection settings before and after the event.
- **Check 3:** Correlate the modifying identity and process with new execution in affected paths.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider approved troubleshooting and centrally managed policy deployments can change protection settings. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: verify actual policy source and endpoint protection status through available read-only evidence. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return protection-impact assessment with confirmed and attempted changes separated. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a command line requesting disablement does not prove the control was disabled.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
