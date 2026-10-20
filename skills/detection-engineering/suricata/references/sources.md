# Suricata: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [Suricata EVE JSON](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html) — Protocol/event output. The reviewed latest branch is development documentation; select an installed release before implementation.
- [Suricata rule format](https://docs.suricata.io/en/latest/rules/intro.html) — Signature structure. The reviewed latest branch is development documentation; confirm options against the deployed release.
- [Zeek common logs](https://docs.zeek.org/en/current/reference/logs/index.html) — Protocol log families and field documentation; follow the specific log reference used.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
