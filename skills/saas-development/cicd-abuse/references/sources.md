# CI/CD Abuse: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [GitHub Actions secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — Workflow trust boundaries, tokens and untrusted execution inputs.
- [GitHub organization audit documentation](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) — Audit access, event context and organization-level visibility.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — Incident risk, analysis, response and recovery considerations.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
