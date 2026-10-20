# RDP Lateral: analysis guide

## Evidence contract

Use authentication and RDP session records, source/destination, account, reconnect and endpoint events. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Distinguish authentication, session establishment and reconnect events.
- **Check 2:** Correlate destination session identity with launched processes.
- **Check 3:** Compare source host and user path against jump-host policy and timing.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider helpdesk support, jump servers and administrator maintenance use RDP. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review lateral source compromise and destination account activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return rDP session timeline and identity-linked endpoint scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a TCP connection to an RDP port does not prove a successful interactive session.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
