# Entra Apps: analysis guide

## Evidence contract

Use application audit events, credential metadata, owners, permissions and workload sign-ins. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Distinguish application object and tenant service principal.
- **Check 2:** Identify key/secret addition without exposing secret material.
- **Check 3:** Correlate actor privileges, credential validity and later workload sessions.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider certificate rotation, app deployment and managed identity maintenance change credentials. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review permission grants and resource operations attributable to the changed app. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return app-change provenance, credential-use evidence and access scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a newly added credential does not prove it was used.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
