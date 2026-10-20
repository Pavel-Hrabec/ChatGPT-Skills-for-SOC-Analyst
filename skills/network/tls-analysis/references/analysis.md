# TLS Analysis: analysis guide

## Evidence contract

Use tLS handshake/certificate summaries, SNI where visible, addresses, timing and process context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify which metadata is actually observable with the negotiated protocol.
- **Check 2:** Inspect certificate validity and name/context inconsistencies.
- **Check 3:** Compare fingerprints and destinations with application baselines.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider private PKI, inspection proxies and unusual clients produce uncommon certificates or fingerprints. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: correlate DNS/proxy evidence and endpoint processes without contacting the suspicious endpoint. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return tLS metadata assessment with encryption and fingerprint limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: encrypted traffic cannot reveal payload semantics from a fingerprint alone.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
