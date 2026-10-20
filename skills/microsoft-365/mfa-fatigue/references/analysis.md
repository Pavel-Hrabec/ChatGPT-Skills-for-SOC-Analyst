# MFA Fatigue: analysis guide

## Evidence contract

Use sign-in request IDs, authentication steps/results, method, device and user context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Group prompts into the actual sign-in transaction where identifiers allow.
- **Check 2:** Separate challenge initiation from successful completion.
- **Check 3:** Compare any approval with device, session and resource access evidence.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider network retries, stale applications and legitimate repeated access can trigger many prompts. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the successful session and affected user's reported activity through approved records. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return challenge-to-session timeline and compromise assessment. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: many prompts alone do not demonstrate a successful bypass or user approval.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
