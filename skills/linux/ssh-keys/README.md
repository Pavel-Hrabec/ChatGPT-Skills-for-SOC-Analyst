# SSH Keys

Investigate unauthorized SSH key and trust configuration changes.

**Input:** Authorized-key files, key fingerprints, file-change records, sshd configuration and session logs.

**Result:** Key-change provenance and evidence of new access.

Download [ssh-keys.zip](../../../dist/chatgpt/ssh-keys.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
