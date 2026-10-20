# K8s RBAC: analysis guide

## Evidence contract

Use audit role/binding objects, subjects, API groups/resources/verbs and admission context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve namespace versus cluster scope and aggregated-role effects.
- **Check 2:** Distinguish a subject's binding from permissions granted by the referenced role.
- **Check 3:** Correlate updates with impersonation or newly allowed API requests.

## Interpret the source

Use cluster, namespace, immutable pod UID, node and image digest rather than names alone. Resolve user, service account and impersonation separately. Audit stages can represent the same request more than once, and request-body visibility depends on policy. RBAC authorization, admission and runtime execution are different boundaries. Container-visible host paths or privileges indicate capability, while actual host effects require corroboration.

## Discriminate and correlate

Consider operators and deployment systems routinely create roles and service-account bindings. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the modifying principal and sensitive actions by newly privileged subjects. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return rBAC relationship map and observed privilege-use assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a wildcard or role name alone does not fully establish effective access under admission and authorization context.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
