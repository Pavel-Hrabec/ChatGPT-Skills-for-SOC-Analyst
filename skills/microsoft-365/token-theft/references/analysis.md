# Token Theft: analysis guide

## Evidence contract

Use interactive/noninteractive sign-ins, session/correlation identifiers, device context and resource audit. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Compare device/session continuity across observed requests.
- **Check 2:** Distinguish refresh behavior and proxy egress from inconsistent session use.
- **Check 3:** Correlate suspicious sessions with resource access and prior endpoint or phishing evidence.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider vPN changes, token refresh and pooled cloud egress can alter apparent location. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: inspect resources accessed by the suspect session and available revocation history. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return session continuity assessment and affected resource scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: location changes or noninteractive sign-ins alone do not prove token theft.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
