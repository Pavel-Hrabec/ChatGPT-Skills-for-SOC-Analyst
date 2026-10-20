# DCSync: analysis guide

## Evidence contract

Use directory access audit, replication-right GUIDs, caller identity, source host and DC inventory. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve requested control-access rights using authoritative mappings.
- **Check 2:** Compare the requester and source against legitimate replication participants.
- **Check 3:** Correlate authentication and network evidence with the directory operation.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider domain controllers, synchronization services and approved directory backups may replicate data. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review recent grants of replication rights and related identity use. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return replication-operation assessment with verified requester context. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: replication permission or a single generic directory-access event is not proof of secret replication.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
