# AWS Lambda: analysis guide

## Evidence contract

Use function version/configuration changes, CloudTrail, execution logs and role/resource metadata. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Bind evidence to a specific function version or alias.
- **Check 2:** Correlate code/layer/environment changes with actor identity and later invocations.
- **Check 3:** Distinguish invocation requests from handler outcome and downstream role use.

## Interpret the source

Use account ID, ARN/principal identity, access key or session context, region, event ID/time, event source/name, errors and resource identifiers. A role session name alone does not identify the human actor. Control-plane records, service data events and guest logs provide different evidence. Check organization/account/region routing and data-event enablement. Request parameters express intent; operation result and downstream evidence establish effects.

## Discriminate and correlate

Consider deployments, observability layers and normal workload bursts change function behavior. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review referenced artifacts, execution-role privileges and external destinations. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return function-version timeline and confirmed execution/resource effects. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a function configuration change alone does not prove its new code ran.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
