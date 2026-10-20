# AWS SSO: analysis guide

## Evidence contract

Use identity Center/federation audit, role sessions, account assignments and identity-provider evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve user identity across federation and assumed-role session records.
- **Check 2:** Correlate assignment changes with new account/permission-set access.
- **Check 3:** Compare session source and service use with the relevant workload/user baseline.

## Interpret the source

Use account ID, ARN/principal identity, access key or session context, region, event ID/time, event source/name, errors and resource identifiers. A role session name alone does not identify the human actor. Control-plane records, service data events and guest logs provide different evidence. Check organization/account/region routing and data-event enablement. Request parameters express intent; operation result and downstream evidence establish effects.

## Discriminate and correlate

Consider permission-set rollout and legitimate cross-account administration create new sessions. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review identity-provider authentication and actions performed with the issued AWS session. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return federated identity-to-account session chain and affected access scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: federation success does not establish compromise without identity and action context.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
