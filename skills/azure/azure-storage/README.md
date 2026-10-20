# Azure Storage

Investigate suspicious Azure Storage access, sharing and token use.

**Input:** Storage resource logs, operations, authentication mode, account/container scope and policy changes.

**Result:** Storage-authentication timeline and observed object exposure.

Download [azure-storage.zip](../../../dist/chatgpt/azure-storage.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
