# LD Preload: analysis guide

## Evidence contract

Use environment evidence, ld.so.preload contents, shared-library paths, caller process and ownership. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Separate per-process LD_PRELOAD from system-wide loader configuration.
- **Check 2:** Inspect library provenance, permissions and the actual affected dynamic executable.
- **Check 3:** Correlate the configuration writer with observed library loading or process anomalies.

## Interpret the source

Group Linux audit records by host and audit event serial before interpreting actions. Keep login identity, real UID and effective UID separate. Shell history is mutable and incomplete. Resolve the effective configuration, distribution-specific paths and timezone from the source rather than assuming one Linux layout. File modification, attempted execution and a successful action require different evidence.

## Discriminate and correlate

Consider instrumentation, compatibility shims and performance profilers may preload libraries. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: inspect sibling processes and related configuration changes without loading the library. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return loader-modification scope and supported execution hypothesis. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: loader behavior depends on executable and secure-execution rules; configuration presence is not universal execution proof.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
