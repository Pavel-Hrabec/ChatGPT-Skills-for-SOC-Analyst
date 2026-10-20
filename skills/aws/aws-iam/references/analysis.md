# AWS IAM: analysis guide

## Evidence contract

Use cloudTrail policy/role events, before/after documents, actor session and organization controls. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate identity policies, resource trust and applicable boundaries.
- **Check 2:** Resolve the effective scope of the change rather than policy name.
- **Check 3:** Correlate changes with role assumption and later successful APIs.

## Interpret the source

Use account ID, ARN/principal identity, access key or session context, region, event ID/time, event source/name, errors and resource identifiers. A role session name alone does not identify the human actor. Control-plane records, service data events and guest logs provide different evidence. Check organization/account/region routing and data-event enablement. Request parameters express intent; operation result and downstream evidence establish effects.

## Discriminate and correlate

Consider infrastructure deployment and approved role changes may broaden permissions temporarily. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the modifying principal's path and downstream use of new privileges. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return permission-change impact and observed privilege-use assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a permissive policy snippet alone is insufficient to establish effective access or exploitation.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
