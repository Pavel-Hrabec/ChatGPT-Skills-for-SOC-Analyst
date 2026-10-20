# Enrichment Pipeline: analysis guide

## Evidence contract

Use typed indicators, permitted providers, authentication method, rate limits and output schema. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Validate indicator scope before selecting a provider.
- **Check 2:** Distinguish missing credentials, no result, stale response and provider errors.
- **Check 3:** Retain retrieval/observation dates and source lineage while minimizing disclosed data.

## Interpret the source

Specify input/output schema, permitted destinations, credential storage, idempotency keys, limits and observable errors. Distinguish a timeout from a negative provider result. Retries must match operation semantics; a failed response to a write does not prove the write failed. Preserve audit history without emitting secrets. Generate consequential actions as reviewable plans unless the user has authorized execution for the named environment.

## Discriminate and correlate

Consider copied reports and shared infrastructure can inflate apparent corroboration. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: use the optional SOC Intel integration or configured providers and generate mocked error-path tests. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return pipeline code/configuration with provider contracts and auditable results. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: enrichment output is evidence rather than an automatic block or benign verdict.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
