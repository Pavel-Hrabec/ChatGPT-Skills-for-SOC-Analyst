# AWS EC2: analysis guide

## Evidence contract

Use cloudTrail instance/network/SSM operations, instance identity, image/user-data metadata and endpoint logs. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve the instance lifecycle and initiating session.
- **Check 2:** Distinguish control-plane commands from confirmed guest execution.
- **Check 3:** Correlate security-group, instance-profile and remote-management changes.

## Interpret the source

Use account ID, ARN/principal identity, access key or session context, region, event ID/time, event source/name, errors and resource identifiers. A role session name alone does not identify the human actor. Control-plane records, service data events and guest logs provide different evidence. Check organization/account/region routing and data-event enablement. Request parameters express intent; operation result and downstream evidence establish effects.

## Discriminate and correlate

Consider autoscaling, patching and automation routinely create and control instances. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review guest telemetry and accessed resources associated with the instance role. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return control-plane-to-guest assessment and instance/resource scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a successful API request does not by itself describe command success inside a guest OS.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
