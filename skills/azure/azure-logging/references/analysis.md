# Azure Logging: analysis guide

## Evidence contract

Use activity Log, diagnostic settings, destinations, resource scope and ingestion evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Compare diagnostic categories and destinations before/after change.
- **Check 2:** Separate source logging, export routing and queried workspace visibility.
- **Check 3:** Correlate the actor and timing with independent resource activity.

## Interpret the source

Preserve tenant, subscription, full resource ID, caller object/app identity, correlation ID and operation/result. Azure management events are not a substitute for each resource service diagnostic log. Resolve assignment scope and resource versions at the incident time. An operation status may describe one stage in an asynchronous request; guest execution and data-plane outcomes need their own corroboration.

## Discriminate and correlate

Consider workspace migration, retention changes and policy remediation modify diagnostics. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review destination access, collector health and coverage at child resources. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return resource-specific visibility assessment and logging-impact timeline. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: missing records in one workspace do not prove logging was disabled at the source.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
