# Linux Audit

Reconstruct security-relevant activity from Linux audit records.

**Input:** Raw audit records, serial/event identifiers, host, syscall, architecture and identity fields.

**Result:** Reconstructed audit events with identity and success semantics.

Download [linux-audit.zip](../../../dist/chatgpt/linux-audit.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
