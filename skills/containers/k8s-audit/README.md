# K8s Audit

Reconstruct suspicious Kubernetes API activity from audit events.

**Input:** AuditID, stage, requestURI, verb, objectRef, user/impersonation and response metadata.

**Result:** API request timeline and coverage-qualified action assessment.

Download [k8s-audit.zip](../../../dist/chatgpt/k8s-audit.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
