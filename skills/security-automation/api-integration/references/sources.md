# API Integration: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) — Protocol/tool implementation; this release explicitly targets the tested 1.x SDK line.
- [VirusTotal API v3](https://docs.virustotal.com/reference/overview) — Existing indicator/file reports and provider-defined response semantics.
- [OpenCTI connectors](https://docs.opencti.io/latest/deployment/connectors/) — Ingestion/enrichment architecture and separately configured access.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
