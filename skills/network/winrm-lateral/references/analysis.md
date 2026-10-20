# WinRM Lateral: analysis guide

## Evidence contract

Use winRM/PowerShell operational logs, source authentication, target process and network events. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify the authenticated requester and target session.
- **Check 2:** Correlate host-provider child processes with script or command records.
- **Check 3:** Separate configuration/health probes from executed commands.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider configuration management and approved PowerShell remoting are common. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review source session provenance and resulting file/network activity on target hosts. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return remote management execution chain and authorization context. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a management connection or provider process alone does not establish unauthorized execution.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
