# YARA: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [YARA maintainer repository](https://github.com/VirusTotal/yara) — Engine and module documentation; do not silently substitute YARA-X semantics.
- [Microsoft PE format](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format) — Executable structure and field meanings, without establishing file behavior or maliciousness.
- [Volatility 3 documentation](https://volatility3.readthedocs.io/en/stable/) — Memory acquisition analysis context and version-dependent plugin operation.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
