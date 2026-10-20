# Inbox Rules: analysis guide

## Evidence contract

Use mailbox rule audit, rule actions/conditions, forwarding destinations, actor and mailbox sessions. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Reconstruct effective rule conditions and actions.
- **Check 2:** Distinguish creation, modification and deletion with audit coverage limits.
- **Check 3:** Correlate the change with sign-ins and subsequent message handling.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider vacation handling, workflow routing and approved forwarding can be legitimate. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review matching messages, forwarding settings and nearby mailbox actions. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return mailbox rule behavior, actor context and affected message scope. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a rule's existence does not prove specific messages were exfiltrated.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
