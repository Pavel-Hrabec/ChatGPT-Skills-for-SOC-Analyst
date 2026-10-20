# Query Performance: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [Defender custom detections](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) — Product-specific result identities and detection scheduling constraints.
- [Splunk Security Content](https://github.com/splunk/security_content) — Detection engineering conventions and explicit macro/model dependencies.
- [Elastic Detection Rules](https://github.com/elastic/detection-rules) — Repository rule conventions, validation and release-specific tooling.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
