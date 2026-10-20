# Enrichment Pipeline: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [VirusTotal API v3](https://docs.virustotal.com/reference/overview) — Existing indicator/file reports and provider-defined response semantics.
- [ThreatFox community API](https://threatfox.abuse.ch/api/) — Provider indicator observations, lookup operations and authentication requirements.
- [OpenCTI connectors](https://docs.opencti.io/latest/deployment/connectors/) — Ingestion/enrichment architecture and separately configured access.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
