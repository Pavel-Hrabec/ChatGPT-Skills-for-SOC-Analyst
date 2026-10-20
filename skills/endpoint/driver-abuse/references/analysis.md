# Driver Abuse: analysis guide

## Evidence contract

Use driver-load events, service installation, driver hash/signature, OS build and endpoint detections. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve the exact driver file and service identity.
- **Check 2:** Check an actual hash or vendor advisory rather than trusting a filename.
- **Check 3:** Correlate loading with device access, security control failures and the initiating account.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider oEM utilities, security agents and hardware maintenance may load uncommon signed drivers. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: inspect the installer chain and subsequent host activity using existing telemetry. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return driver provenance, observed abuse indicators and exposure limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a valid signature is not a safety verdict and a vulnerability reference does not prove exploitation.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
