# Pod Exec: analysis guide

## Evidence contract

Use audit events for pod subresources, user/impersonation, namespace, pod UID and container process logs. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify exec/attach/port-forward requests and the audit stage.
- **Check 2:** Distinguish request admission from established execution and process results.
- **Check 3:** Correlate user/RBAC context with container commands and network activity.

## Interpret the source

Use cluster, namespace, immutable pod UID, node and image digest rather than names alone. Resolve user, service account and impersonation separately. Audit stages can represent the same request more than once, and request-body visibility depends on policy. RBAC authorization, admission and runtime execution are different boundaries. Container-visible host paths or privileges indicate capability, while actual host effects require corroboration.

## Discriminate and correlate

Consider troubleshooting, deployment health checks and authorized support use pod access. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the same principal's other pod and secret operations. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return user-to-container access timeline and observed execution scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a request to an exec endpoint does not prove the requested command ran successfully.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
