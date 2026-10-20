# WMI Execution: analysis guide

## Evidence contract

Use wMI operational logs, process creation, authentication events and source/target host context. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Identify the WMI caller and namespace from available records.
- **Check 2:** Connect WmiPrvSE child creation to the authenticated source session.
- **Check 3:** Separate a process query from an execution request and establish whether a child actually ran.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider inventory agents and endpoint management commonly use WMI. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: correlate source logon, target process lineage and downstream network activity. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return caller-to-target execution chain with uncertainty and corroborating searches. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a WMI provider process or query alone is insufficient evidence of remote execution.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
