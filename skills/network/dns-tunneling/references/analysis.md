# DNS Tunneling: analysis guide

## Evidence contract

Use dNS queries/responses, client identity, resolver path, timestamps and query types. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Group queries by effective client and parent domain.
- **Check 2:** Assess label structure, encoding consistency, volume and bidirectional response patterns.
- **Check 3:** Compare successful responses with process attribution and normal DNS-heavy services.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider cDNs, security agents, DNSSEC and service discovery can produce long or high-volume queries. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review resolver visibility and subsequent host/network activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return dNS-channel assessment with resolver and decoding limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: entropy or label length alone cannot prove data exfiltration or a decoded payload.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
