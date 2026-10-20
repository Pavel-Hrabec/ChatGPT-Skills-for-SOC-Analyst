# Data Exfiltration: analysis guide

## Evidence contract

Use dLP, proxy/flow, file staging, destination and endpoint/account evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Establish direction and the meaning of byte counters.
- **Check 2:** Connect sensitive-source access to staging and outbound transfer.
- **Check 3:** Compare destination, volume and authorization with baseline activity.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider backups, cloud sync and approved exports can move large data volumes. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review affected objects, initiating identity and receiver context through existing records. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return evidence-linked transfer timeline and defensible data scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: volume alone does not identify content, recipient possession or unauthorized disclosure.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
