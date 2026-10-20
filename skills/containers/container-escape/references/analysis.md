# Container Escape: analysis guide

## Evidence contract

Use pod security context, mounts, runtime/process telemetry, host artifacts and node identity. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Establish privileges and host-resource exposure before interpreting behavior.
- **Check 2:** Correlate container-origin activity with independently observed host processes/files.
- **Check 3:** Distinguish an exposed host mount from proof of host command execution.

## Interpret the source

Use cluster, namespace, immutable pod UID, node and image digest rather than names alone. Resolve user, service account and impersonation separately. Audit stages can represent the same request more than once, and request-body visibility depends on policy. RBAC authorization, admission and runtime execution are different boundaries. Container-visible host paths or privileges indicate capability, while actual host effects require corroboration.

## Discriminate and correlate

Consider privileged agents, storage drivers and authorized node diagnostics legitimately access host resources. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review admission/deployment provenance and related node/credential activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return container-to-node boundary assessment with confirmed host effects. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a privileged pod or hostPath mount establishes exposure rather than a successful escape.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
