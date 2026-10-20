# DCShadow: analysis guide

## Evidence contract

Use directory object-change records, server/NTDS registration, replication metadata and privileged sessions. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify transient server or replication objects and their creator.
- **Check 2:** Distinguish ordinary DC promotion/demotion from short-lived registrations.
- **Check 3:** Correlate unexpected replicated changes with the initiating host and account.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider planned DC lifecycle work and recovery procedures can change replication objects. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review change approvals, DC inventory and downstream modified directory objects. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return registration/change relationship and bounded replication-abuse hypothesis. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a changed directory object alone does not identify the replication mechanism.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
