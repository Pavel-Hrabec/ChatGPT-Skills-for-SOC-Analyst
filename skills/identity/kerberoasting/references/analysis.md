# Kerberoasting: analysis guide

## Evidence contract

Use domain-controller ticket events, requesting identity/host, target service, encryption fields and account context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Group service-ticket requests by requester and target over explicit windows.
- **Check 2:** Interpret encryption and target selection against account/service baselines.
- **Check 3:** Correlate directory discovery and endpoint tooling with the ticket activity.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider inventory systems, service deployment and legacy encryption can produce unusual ticket volumes. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review affected service-account privilege and subsequent authentication evidence. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return ticket-request assessment and service-account exposure scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: service-ticket requests and RC4 use do not prove offline cracking or recovered passwords.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
