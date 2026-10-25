Use the **Active Directory Discovery** skill if it is installed. Otherwise, analyze the attached evidence using the instructions below.

Task: Analyze the supplied Active Directory discovery activity, including LDAP events, endpoint records, or directory assessment output.

Identify the client host and account. Explain what the base DN, search scope, filters, requested attributes, and result counts show. Correlate with the supplied process, authentication, and change context. A query does not prove that its results were accessed or used. Use ATT&CK mappings only when supported. Do not query a live directory or claim checks that did not run.

## Output format

### Summary
Answer the request directly.

### Result or requested artifact
Explain what was queried or enumerated.

### Evidence and reasoning
List the relevant records, timestamps, query fields, identities, and supporting context. Separate observations from inference.

### Assessment or validation status
Give a proportionate assessment and confidence, or explain why the evidence is inconclusive.

### Unknowns and limitations
State which records, baselines, or query results are missing.

### Recommended next steps
Suggest prioritized, read-only checks for the account, source process, domain-controller events, and authorization context.

