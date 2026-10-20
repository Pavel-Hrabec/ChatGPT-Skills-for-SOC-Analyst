# Azure Roles: analysis guide

## Evidence contract

Use activity Log assignment events, principal/object IDs, scope, role definition and PIM evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve role definition and scope inheritance.
- **Check 2:** Separate eligible activation from persistent assignment.
- **Check 3:** Correlate the granting actor and new principal use with actual resource operations.

## Interpret the source

Preserve tenant, subscription, full resource ID, caller object/app identity, correlation ID and operation/result. Azure management events are not a substitute for each resource service diagnostic log. Resolve assignment scope and resource versions at the incident time. An operation status may describe one stage in an asynchronous request; guest execution and data-plane outcomes need their own corroboration.

## Discriminate and correlate

Consider pIM activation, managed identity deployment and approved administration alter roles. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the grantor session and high-impact APIs allowed by the assignment. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return role-change provenance, effective scope and observed use. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a role name without scope and effective conditions is not a complete access assessment.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
