# Integrations

Skill ZIPs contain instructions and references. The optional server at `integrations/soc-intel-mcp/` supplies implemented report/CVE lookup tools to a separately configured MCP client. It performs no active scanning, sample upload, blocking, collection or SIEM query. See its README for provider credentials, disclosure boundaries and tested dependency versions.

Internal SIEM/XDR, mail, directory, cloud and knowledge-base access remains separately configured. Verify actual tool capabilities, least-privilege scope and logging before using them. A desired connector is not a connected service. Never put API credentials into a skill, prompt or committed configuration.

The bundled server defaults to stdio and optionally binds HTTP to loopback only. It does not implement a public multi-user gateway. Remote service integration requires authentication, tenant boundaries, credential custody, rate limits, deployment controls and review appropriate to that environment. Do not expose a local unauthenticated endpoint publicly as an installation shortcut.
