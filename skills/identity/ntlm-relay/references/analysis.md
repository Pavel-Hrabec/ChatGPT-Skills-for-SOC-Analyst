# NTLM Relay: analysis guide

## Evidence contract

Use nTLM authentication, SMB/HTTP sessions, service actions, source hosts and signing/channel-binding context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Reconstruct the authenticating account and actual destination service.
- **Check 2:** Correlate coerced or unexpected authentication with a distinct privileged service action.
- **Check 3:** Inspect protocol protections and service configuration without attempting a relay.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider proxies, scanners and normal integrated authentication can create unexpected source/destination pairs. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review account-triggering activity and object/file changes at the destination. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return authentication-to-service-action chain with protection context. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: an NTLM logon does not establish that credentials were relayed.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
