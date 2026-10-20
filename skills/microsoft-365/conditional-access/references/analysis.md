# Conditional Access: analysis guide

## Evidence contract

Use policy audit, before/after settings, assignments/exclusions and sign-in evaluation results. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Distinguish report-only from enforced policy states.
- **Check 2:** Determine the affected users/apps and exclusions.
- **Check 3:** Correlate the precise policy version and evaluation result with the access being investigated.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider staged policy rollouts, break-glass exclusions and approved troubleshooting may explain changes. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review actor sessions and affected resource access after policy modification. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return policy-impact assessment and event-specific enforcement explanation. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a policy edit or report-only failure does not prove an enforced control was bypassed.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
