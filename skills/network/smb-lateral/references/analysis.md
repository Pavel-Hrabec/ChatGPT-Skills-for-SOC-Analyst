# SMB Lateral: analysis guide

## Evidence contract

Use sMB session/file records, network logons, share names and endpoint process/service events. Preserve original field names and record/object identifiers. If only an alert summary is supplied, identify which assertions originate from the alert and which are independently corroborated. The following checks define this skill's scope:

- **Check 1:** Resolve source identity, destination and accessed shares.
- **Check 2:** Distinguish file copying from remote service/process execution.
- **Check 3:** Correlate authentication with created files and destination execution.

## Interpret the source

Verify sensor location, clock, direction, sampled capture and NAT/proxy boundaries. Distinguish packets, flows, sessions and application transactions when counting. Correlate the originating process if evidence exists. Encrypted or absent payloads limit content claims. A passive metadata interpretation does not require contacting suspicious infrastructure, actively scanning a destination or detonating a file.

## Discriminate and correlate

Consider software distribution, backups and administrator access use administrative shares. Identify an observation that supports or contradicts that explanation, such as an approved change, expected owner, source-specific result or downstream artifact. An allowlisted tool name or a familiar account is not enough to close the case.

Next evidence: search adjacent targets for the same identity and execution artifacts. State the entity keys, start/end time and expected observation before proposing a search. Use actual schema samples; label field names that still require verification. Do not broaden an exact artifact or destination into an unrelated organization-wide hunt by default.

## Output and acceptance criteria

Return source-to-target movement chain and confirmed actions. Include evidence provenance, uncertainty and proportionate next checks. Explain the limitation: an admin-share connection or file transfer alone does not prove remote execution.

For an investigation example, the assessment should change when decisive corroboration is removed; an ambiguous input should remain inconclusive. For an engineering artifact, validate its actual target engine, schema and intended behavior. Reference review and correct packaging do not establish backend execution or measured production effectiveness.
