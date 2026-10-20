# Suricata: analysis guide

## Evidence contract

Use packet/protocol evidence, capture context, deployment mode, engine version and existing rules. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Choose correct direction, application buffer and flow state.
- **Check 2:** Specify content/position/encoding logic and avoid mixing incompatible buffers.
- **Check 3:** Assign identifiers and define alert/no-alert packet cases with performance constraints.

## Interpret the source

Freeze the target engine, schema/mapping, rule version and unit of detection before writing or translating logic. Preserve case, null, multivalue, time and cardinality semantics. Distinguish static/schema checks, compilation, backend result matches and alert-service behavior. Provide positive, near-miss and legitimate cases, plus missing-field/time-boundary cases where relevant. Do not report unexecuted tests as passed or enable a rule by merely generating its configuration.

## Discriminate and correlate

Consider health checks, protocol variants and benign clients can contain similar content. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: produce signature and controlled offline PCAP test instructions for the installed engine. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return network signature, visibility requirements and engine-aware validation package. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: a syntax check or encrypted flow metadata cannot prove payload-level coverage.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
