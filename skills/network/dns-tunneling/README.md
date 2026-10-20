# DNS Tunneling

Investigate DNS traffic that may carry a covert channel.

**Input:** DNS queries/responses, client identity, resolver path, timestamps and query types.

**Result:** DNS-channel assessment with resolver and decoding limitations.

Download [dns-tunneling.zip](../../../dist/chatgpt/dns-tunneling.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
