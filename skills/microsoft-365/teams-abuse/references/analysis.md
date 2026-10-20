# Teams Abuse: analysis guide

## Evidence contract

Use teams audit, guest/member changes, app permissions, messages or file metadata supplied by the user. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Determine the actual tenant/team/channel and actor identity.
- **Check 2:** Correlate membership/app changes with message or file activity.
- **Check 3:** Distinguish external participants and impersonation evidence from display-name similarity.

## Interpret the source

Join identity and resource records using available immutable identities and session/correlation context; display names and IPs are weak cross-service keys. Interactive, noninteractive, workload and resource audits have different semantics. Licensing, aggregation and retention can limit observations. Authentication success, authorization and content access are distinct stages. Preserve tenant boundaries and minimize unrelated mailbox/person data.

## Discriminate and correlate

Consider partner collaboration and approved bots create legitimate external and app activity. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review linked SharePoint files, app grants and account sessions. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return collaboration activity assessment and bounded identity/resource pivots. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a display name, invitation or message preview alone does not establish successful compromise.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
