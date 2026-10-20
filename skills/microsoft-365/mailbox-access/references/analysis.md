# Mailbox Access: analysis guide

## Evidence contract

Use mailbox audit operations, actor/app/session details, folders/messages and licensing/coverage context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Interpret the operation type and audit aggregation before counting messages.
- **Check 2:** Separate owner, delegate and application access.
- **Check 3:** Correlate access scope and timing with sessions, exports and forwarding changes.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider mail clients, eDiscovery and delegated assistants can access large message sets. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review access authorization and adjacent export/search activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return access assessment with audit sampling and aggregation limitations. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: audit volume is not a reliable count of unique messages read without operation semantics.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
