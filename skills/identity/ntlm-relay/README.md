# NTLM Relay

Investigate suspected relayed NTLM authentication.

**Input:** NTLM authentication, SMB/HTTP sessions, service actions, source hosts and signing/channel-binding context.

**Result:** Authentication-to-service-action chain with protection context.

Download [ntlm-relay.zip](../../../dist/chatgpt/ntlm-relay.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
