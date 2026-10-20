# SharePoint Access: analysis guide

## Evidence contract

Use file audit, site/object identifiers, sharing-link metadata, user/app context and sessions. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate link creation, permission changes, file access and actual downloads.
- **Check 2:** Resolve audience and anonymous versus authenticated sharing.
- **Check 3:** Correlate bulk activity with business context and application identity.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider synchronization clients, migrations and approved collaboration produce high volumes. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review sensitive object exposure and later access by new recipients. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return file/share exposure timeline and supported access scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a sharing link or download audit does not independently prove an external recipient received data.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
