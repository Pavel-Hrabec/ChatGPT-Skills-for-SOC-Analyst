# Beaconing: analysis guide

## Evidence contract

Use flow or proxy events with times, destinations, bytes, direction and process attribution. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Measure interval distribution and jitter across an explicit window.
- **Check 2:** Compare destination/process pairs and failed versus completed connections.
- **Check 3:** Inspect changing endpoints, payload size patterns and host baseline.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider monitoring, updates, time sync and cloud agents communicate periodically. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: correlate process lineage and permitted destination intelligence with the traffic. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return traffic timing profile and process-correlated beaconing assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: periodicity or a rare destination alone cannot establish command and control.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
