# K8s Audit: analysis guide

## Evidence contract

Use auditID, stage, requestURI, verb, objectRef, user/impersonation and response metadata. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Group audit stages for a single request instead of counting them as separate actions.
- **Check 2:** Resolve target object and namespace using exact UIDs where available.
- **Check 3:** Interpret status and admission outcomes while respecting configured audit level.

## Interpret the source

Use cluster, namespace, immutable pod UID, node and image digest rather than names alone. Resolve user, service account and impersonation separately. Audit stages can represent the same request more than once, and request-body visibility depends on policy. RBAC authorization, admission and runtime execution are different boundaries. Container-visible host paths or privileges indicate capability, while actual host effects require corroboration.

## Discriminate and correlate

Consider controllers, operators and retries produce high-volume or repeated API requests. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review related RBAC, secret, pod and logging-policy changes. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return aPI request timeline and coverage-qualified action assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: metadata-level auditing may omit request/response bodies needed to prove specific object changes.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
