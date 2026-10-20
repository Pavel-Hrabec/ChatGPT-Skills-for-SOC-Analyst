# Container Images: analysis guide

## Evidence contract

Use image digest, registry/source, scan/SBOM metadata, deployment manifest and runtime events. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Bind evidence to immutable digest rather than mutable tag.
- **Check 2:** Inspect provenance, packages and known vulnerability applicability.
- **Check 3:** Correlate deployed digest with actual runtime behavior and entrypoint changes.

## Interpret the source

Use cluster, namespace, immutable pod UID, node and image digest rather than names alone. Resolve user, service account and impersonation separately. Audit stages can represent the same request more than once, and request-body visibility depends on policy. RBAC authorization, admission and runtime execution are different boundaries. Container-visible host paths or privileges indicate capability, while actual host effects require corroboration.

## Discriminate and correlate

Consider custom build layers and stale scanner databases can create unexpected findings. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review build/push identity and related deployments using the same digest. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return image provenance and deployment/runtime relevance assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a malicious label or vulnerable package does not prove the deployed workload was exploited.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
