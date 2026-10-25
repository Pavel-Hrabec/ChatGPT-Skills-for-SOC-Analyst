Use the **Network Recon and SMB Discovery** skill if it is installed. Otherwise, analyze the attached evidence using the instructions below.

Task: Analyze the supplied network scanning or discovery activity. Do not run a scan, contact a target, authenticate to a service, or enumerate a live share.

Review the source process or scanner, scope, target and port counts, observed responses, service fingerprints, firewall/flow records, SMB evidence, and any supplied authorization or change record. Distinguish probes from completed connections, share enumeration from port reachability, and exposure from exploitation. Use ATT&CK technique mappings only when the context supports them. Preserve exact evidence and state what is unknown. Do not claim external checks that did not run.

## Output format

### Summary
Answer the request directly.

### Result or requested artifact
Describe the observed scan or discovery activity and its results.

### Evidence and reasoning
List key records, timestamps, fields, and how they support the assessment. Separate observations from inference.

### Assessment or validation status
Give a proportionate assessment and confidence, or state why the evidence is inconclusive.

### Unknowns and limitations
State missing records and checks that were not performed.

### Recommended next steps
Give prioritized, read-only checks. Mark live scanning or authentication as requiring authorization.

