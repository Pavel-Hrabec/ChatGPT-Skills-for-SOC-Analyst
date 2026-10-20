# GCP Audit: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [Google Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) — Audit categories, API caller context and service-dependent data-access coverage.
- [OpenTelemetry logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — Event versus observed timestamps and structured record context.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — Incident risk, analysis, response and recovery considerations.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
