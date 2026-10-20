# Alert Routing: analysis guide

## Evidence contract

Use alert schema, ownership rules, severity policy, destination contracts and historical routing evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Normalize stable incident/alert identities and track source lineage.
- **Check 2:** Define tenant/customer boundaries and fallback ownership.
- **Check 3:** Handle deduplication, reopen/escalation and delivery failures without silently dropping alerts.

## Interpret the source

Specify input/output schema, permitted destinations, credential storage, idempotency keys, limits and observable errors. Distinguish a timeout from a negative provider result. Retries must match operation semantics; a failed response to a write does not prove the write failed. Preserve audit history without emitting secrets. Generate consequential actions as reviewable plans unless the user has authorized execution for the named environment.

## Discriminate and correlate

Consider reopened incidents, merged cases and delayed updates can resemble duplicate alerts. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: produce routing rules, test cases and an auditable delivery/retry model. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return routing configuration, decision table and loss/duplication safeguards. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: routing or severity changes must follow the organization's policy rather than invented SLAs.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
