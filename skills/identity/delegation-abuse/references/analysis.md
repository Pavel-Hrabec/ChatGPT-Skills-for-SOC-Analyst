# Delegation Abuse: analysis guide

## Evidence contract

Use account delegation attributes, object ACL changes, service-ticket records and source/target identities. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify unconstrained, constrained or resource-based delegation scope from actual attributes.
- **Check 2:** Reconstruct the principal that changed the relationship.
- **Check 3:** Correlate delegated service use with intended services and account privileges.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider application onboarding and service migrations legitimately change delegation. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the writer's access path and resulting service sessions. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return delegation relationship, authorization provenance and observed use. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a risky delegation configuration does not independently prove impersonation occurred.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
