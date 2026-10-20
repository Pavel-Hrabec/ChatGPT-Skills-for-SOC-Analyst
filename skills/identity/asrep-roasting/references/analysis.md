# AS-REP Roasting: analysis guide

## Evidence contract

Use authentication-service events, preauthentication fields, requester source and account settings. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Verify the preauthentication setting at the relevant time.
- **Check 2:** Correlate requests across target accounts and source hosts.
- **Check 3:** Separate returned authentication material from evidence of later account use.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider legacy services and controlled audits may use accounts with exceptional authentication configuration. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review configuration-change provenance and later sessions for targeted accounts. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return preauthentication exposure and request/use correlation. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a request for an affected account does not prove password recovery.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
