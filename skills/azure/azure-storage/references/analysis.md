# Azure Storage: analysis guide

## Evidence contract

Use storage resource logs, operations, authentication mode, account/container scope and policy changes. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Distinguish account-key, SAS and identity-based access where evidence permits.
- **Check 2:** Correlate sharing or key changes with later object operations.
- **Check 3:** Separate listing, reads and writes and inspect response outcomes.

## Interpret the source

Preserve tenant, subscription, full resource ID, caller object/app identity, correlation ID and operation/result. Azure management events are not a substitute for each resource service diagnostic log. Resolve assignment scope and resource versions at the incident time. An operation status may describe one stage in an asynchronous request; guest execution and data-plane outcomes need their own corroboration.

## Discriminate and correlate

Consider data pipelines, backups and legitimate SAS sharing can look unusual. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review token scope/validity and object activity without exposing credential-bearing URLs. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return storage-authentication timeline and observed object exposure. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a SAS issuance or permissive setting does not prove the token was used or data retrieved.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
