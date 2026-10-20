# SOAR Playbook: analysis guide

## Evidence contract

Use trigger schema, available actions, permissions, decision criteria and platform constraints. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate enrichment, triage and consequential response stages.
- **Check 2:** Define idempotency, timeout, retry and partial-failure behavior per action.
- **Check 3:** Preserve an auditable human decision before actions not already authorized by the workflow.

## Interpret the source

Specify input/output schema, permitted destinations, credential storage, idempotency keys, limits and observable errors. Distinguish a timeout from a negative provider result. Retries must match operation semantics; a failed response to a write does not prove the write failed. Preserve audit history without emitting secrets. Generate consequential actions as reviewable plans unless the user has authorized execution for the named environment.

## Discriminate and correlate

Consider repeated alerts, delayed responses and legitimate business exceptions must be handled explicitly. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: produce a platform-aware state graph and mocked action tests. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return playbook specification or code, action contracts and failure/recovery tests. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a generated playbook does not authorize deployment or expand connected service permissions.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
