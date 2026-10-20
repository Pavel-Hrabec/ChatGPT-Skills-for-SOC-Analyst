# AD CS: analysis guide

## Evidence contract

Use cA issuance records, certificate/template properties, enrollment rights, subject identity and authentication events. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve who requested and who the certificate represents.
- **Check 2:** Inspect authentication usage, subject control and template permissions together.
- **Check 3:** Correlate issuance or template changes with later certificate-based sessions.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider pKI renewals, device enrollment and approved template maintenance create similar records. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the CA/template change history and identities using the issued certificate. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return certificate identity chain and evidence-supported abuse assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a permissive template indicates exposure; exploitation requires request/issuance/use evidence.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
