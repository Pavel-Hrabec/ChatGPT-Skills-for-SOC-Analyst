# Golden Ticket: analysis guide

## Evidence contract

Use dC authentication records, service-ticket activity, account state, timing and endpoint context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Check identity/domain inconsistencies and unexpected ticket characteristics.
- **Check 2:** Account for DC visibility, retention and cross-domain paths before claiming missing issuance.
- **Check 3:** Correlate service access with host compromise and privileged identity evidence.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider log gaps, clock skew, referrals and account lifecycle changes can produce apparent inconsistencies. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review affected identity sessions and DC credential-exposure evidence. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return authentication-consistency assessment with explicit visibility limits. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: absence of a visible ticket request alone cannot prove forgery.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
