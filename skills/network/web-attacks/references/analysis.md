# Web Attacks: analysis guide

## Evidence contract

Use raw request fields, normalization context, response metadata, application logs and host telemetry. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Preserve raw and decoded request representations separately.
- **Check 2:** Identify the attempted server-side behavior and reachable endpoint.
- **Check 3:** Correlate response and backend execution/error evidence rather than treating a WAF signature as success.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider scanners, malformed clients and security testing can generate exploit-like requests. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review application version/exposure and subsequent process/file/network activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return request-to-backend assessment separating attempt from impact. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: an attack string or successful HTTP status does not prove exploitation.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
