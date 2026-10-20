# AWS Access Keys

Investigate suspicious AWS access-key creation and use.

**Input:** CloudTrail identity/accessKeyId, API events, source context, IAM credential metadata and asset inventory.

**Result:** Credential issuance/use chain and affected resource scope.

Download [aws-access-keys.zip](../../../dist/chatgpt/aws-access-keys.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
