# DLL Loading: analysis guide

## Evidence contract

Use module-load records, parent executable, module path, signatures, hashes and directory permissions. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Compare the actual loaded module with expected deployment paths.
- **Check 2:** Distinguish a trusted executable signature from the trust of its loaded DLL.
- **Check 3:** Inspect write access and correlate module creation with the loading process.

## Interpret the source

Resolve process identity with host plus stable process GUID or creation time; a reused PID can join unrelated events. Check that the relevant Sysmon/EDR event category was enabled and retained. Preserve image, user, parent, command, signer and clock fields separately. A signed parent or an administrator account does not automatically legitimize its child action. Remote collection or sample execution is outside evidence interpretation unless the user requests that separate operation.

## Discriminate and correlate

Consider application plugins, local testing and vendor updaters may load unsigned modules. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: pivot through module hash, creator process and other hosts loading the same path. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return module provenance assessment and a bounded side-loading hypothesis. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a module-load record does not independently establish the loader search order or malicious functionality.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
