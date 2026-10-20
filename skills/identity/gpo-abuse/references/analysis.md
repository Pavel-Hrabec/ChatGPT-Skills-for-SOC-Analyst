# GPO Abuse: analysis guide

## Evidence contract

Use gPO directory/SYSVOL change records, editor identity, linked OUs and endpoint policy evidence. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Compare policy content and links before/after the change.
- **Check 2:** Resolve affected computer/user scope including filters.
- **Check 3:** Correlate policy retrieval/application with any resulting process or configuration changes.

## Interpret the source

Preserve domain, principal SID/object ID, source host, destination service, authentication result and time. Resolve domain-controller coverage and audit policy before drawing conclusions from an absent event. Distinguish an exposed configuration, a requested authentication operation, a returned credential/token and actual subsequent resource use. Directory permissions and object attributes need effective-scope analysis rather than display-name matching.

## Discriminate and correlate

Consider software deployments, baseline updates and emergency administrator actions modify GPOs. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: review the editor session, ACL changes and impacted endpoints. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return policy-change blast radius and observed endpoint effects. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a GPO edit does not prove every linked endpoint applied it.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
