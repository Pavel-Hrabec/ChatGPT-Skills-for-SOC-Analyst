# GCP IAM: analysis guide

## Evidence contract

Use audit policy-change records, resource hierarchy, bindings/conditions, caller and effective policy evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve project/folder/organization inheritance and conditional bindings.
- **Check 2:** Identify exactly which principal gained which permissions.
- **Check 3:** Correlate the change with subsequent successful resource requests.

## Interpret the source

Preserve organization/project/resource scope, service/method, principal and delegation chain, status and audit category. Admin Activity, Data Access and other categories differ in availability. A request payload is not its effective result. Resolve inherited policies and conditional bindings from actual evidence. Collector or sink access restrictions can hide records even when source logging was active.

## Discriminate and correlate

Consider infrastructure deployment and approved access reviews change bindings. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review grantor identity, service-account impersonation and affected resource actions. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return iAM-change scope and observed privilege-use chain. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a single binding does not establish the entire effective permission set.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
