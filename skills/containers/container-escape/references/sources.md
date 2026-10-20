# Container Escape: primary sources

Source pages reviewed on 2026-10-20. This is original defensive workflow guidance. The references cover source interpretation and relevant context, not a claim that every provider/API or backend was exercised. Follow linked product-specific definitions for the actual version before using an exact field, operation name or policy setting.

- [Kubernetes auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) — Request identity, audit stages and configured body visibility.
- [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) — Role/binding scope and API authorization semantics.
- [MITRE ATT&CK data and tools](https://attack.mitre.org/resources/attack-data-and-tools/) — Behavior definitions and current structured technique references; verify any individual mapping before using it.

Record the exact upstream release/commit when adapting code or rule content and preserve its attribution. Refresh mutable intelligence at analysis time when authorized access is available. If browsing is unavailable, disclose the reference date and unverified version-sensitive assumptions.
