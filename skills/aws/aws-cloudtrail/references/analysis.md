# AWS CloudTrail: analysis guide

## Evidence contract

Use trail/event-data-store configuration, logging status, API records and organization/account context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify stop/delete/update requests and their actual success.
- **Check 2:** Distinguish management, data and organization coverage across regions.
- **Check 3:** Correlate visibility loss with subsequent independent service evidence.

## Interpret the source

Use account ID, ARN/principal identity, access key or session context, region, event ID/time, event source/name, errors and resource identifiers. A role session name alone does not identify the human actor. Control-plane records, service data events and guest logs provide different evidence. Check organization/account/region routing and data-event enablement. Request parameters express intent; operation result and downstream evidence establish effects.

## Discriminate and correlate

Consider trail migrations, centralized logging and retention changes can alter expected event location. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review actor sessions, destination storage and organization guardrails. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return logging coverage timeline and supported tampering hypothesis. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a gap in one queried trail does not prove account-wide logging was disabled.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
