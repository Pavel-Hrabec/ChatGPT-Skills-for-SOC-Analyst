# Community Skills for Security Operations and Engineering

A community library originating from the [AI & Cybersecurity Academy](https://www.skool.com/ai-cybersecurity-academy/about).

**150 focused skills** for SOC investigations, threat intelligence, detection engineering, cloud security, telemetry, automation and incident response. The library is intended for practical community use and contributions.

## Find and install a skill

Browse the [complete catalog](CATALOG.md) or [machine-readable catalog](community-catalog.json). Download an individual ZIP from [dist/chatgpt](dist/chatgpt/) and import it into a compatible Skills interface. Describe the task, name the skill and attach the relevant evidence. Skill/interface availability depends on the host. Each skill includes a README and task-specific guidance; connection details depend on the evidence source.

- [AWS](CATALOG.md#aws) — 7 skills
- [Azure](CATALOG.md#azure) — 5 skills
- [Containers](CATALOG.md#containers) — 5 skills
- [Detection Engineering](CATALOG.md#detection-engineering) — 16 skills
- [Email](CATALOG.md#email) — 1 skill
- [Endpoint](CATALOG.md#endpoint) — 20 skills
- [GCP](CATALOG.md#gcp) — 5 skills
- [Identity](CATALOG.md#identity) — 15 skills
- [Incident Response](CATALOG.md#incident-response) — 8 skills
- [Linux](CATALOG.md#linux) — 8 skills
- [Malware Forensics](CATALOG.md#malware-forensics) — 7 skills
- [Microsoft 365](CATALOG.md#microsoft-365) — 9 skills
- [Network](CATALOG.md#network) — 12 skills
- [SaaS Development](CATALOG.md#saas-development) — 4 skills
- [Security Automation](CATALOG.md#security-automation) — 4 skills
- [SIEM](CATALOG.md#siem) — 3 skills
- [Telemetry Engineering](CATALOG.md#telemetry-engineering) — 3 skills
- [Threat Intelligence](CATALOG.md#threat-intelligence) — 9 skills
- [Threat Intelligence Engineering](CATALOG.md#threat-intelligence-engineering) — 1 skill
- [Vulnerability Management](CATALOG.md#vulnerability-management) — 8 skills

## Knowledge and connections

Skills identify the evidence they require and relevant primary documentation. They work from supplied artifacts; configured read-only tools can retrieve additional evidence. The [connection matrix](docs/connection-matrix.md) maps specialized skills to the right platform, operations and correlation fields. The optional [SOC Intel MCP server](integrations/soc-intel-mcp/) implements existing public hash, IP, domain, URL, passive-DNS and CVE lookups. It also offers an explicitly authorized urlscan.io website submission and result/screenshot links for Email Analysis. Installing a skill ZIP does not install or authenticate a service. Cloud, identity, EDR, SIEM and SaaS access requires a separately configured authorized connector. The local server and optional loopback HTTP transport require a suitable MCP client; use an authenticated deployment/gateway for remote access.

See [knowledge policy](docs/knowledge-policy.md), [integration setup](docs/integrations.md) and [validation scope](docs/validation.md). `community-catalog.json` indexes all 150 skills.

## Contribute

Start with a concrete security task, its actual evidence contract and a distinct output. Preserve existing skill identities when adding related capabilities. Include current primary sources, legitimate alternatives, decisive limitations and reproducible validation. Keep demo payloads separate from skill packages. Never include credentials or claim a lookup/test that did not run.

