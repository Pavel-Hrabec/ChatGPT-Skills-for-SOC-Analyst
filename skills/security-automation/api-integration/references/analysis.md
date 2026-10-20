# API Integration: analysis guide

## Evidence contract

Use provider documentation/version, authorized endpoints, credential storage, pagination and result contract. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Use provider-supported authentication without embedding secrets in artifacts.
- **Check 2:** Validate identifiers and restrict outbound destinations.
- **Check 3:** Implement pagination, rate-limit handling, timeouts and structured errors without unsafe retries of writes.

## Interpret the source

Specify input/output schema, permitted destinations, credential storage, idempotency keys, limits and observable errors. Distinguish a timeout from a negative provider result. Retries must match operation semantics; a failed response to a write does not prove the write failed. Preserve audit history without emitting secrets. Generate consequential actions as reviewable plans unless the user has authorized execution for the named environment.

## Discriminate and correlate

Consider expired credentials and permission-limited empty results must remain distinct from clean findings. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: generate adapter code with mocked request/response tests and deployment prerequisites. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return scoped API adapter, authentication setup and observable failure behavior. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: aPI availability and a successful HTTP response do not establish complete security evidence.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
