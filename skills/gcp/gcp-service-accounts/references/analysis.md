# GCP Service Accounts: analysis guide

## Evidence contract

Use key lifecycle audit, token/impersonation records, caller delegation and workload metadata. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate key-based use from short-lived impersonated credentials.
- **Check 2:** Preserve service-account identity and caller delegation chain.
- **Check 3:** Correlate credential creation or token issuance with downstream APIs.

## Interpret the source

Preserve organization/project/resource scope, service/method, principal and delegation chain, status and audit category. Admin Activity, Data Access and other categories differ in availability. A request payload is not its effective result. Resolve inherited policies and conditional bindings from actual evidence. Collector or sink access restrictions can hide records even when source logging was active.

## Discriminate and correlate

Consider workload federation, build systems and scheduled jobs legitimately impersonate service accounts. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review key creator, workload ownership and resources accessed by the resulting identity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return credential/delegation chain and resource-access scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: an issued token or created key does not independently establish malicious use.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
