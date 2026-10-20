# ChatGPT Skills for SOC Analysts

**A practical course resource from the [AI & Cybersecurity Academy](https://www.skool.com/ai-cybersecurity-academy/about).**

Task-specific AI skills for SOC investigations, organized by the work analysts perform. The course provides the learning path and hands-on context; this repository provides the reusable skill files.

## Use the skills

1. Browse the catalog below and choose the skill that matches the alert or investigation task.
2. Download the skill ZIP from [`dist/chatgpt/`](dist/chatgpt/) and import it through ChatGPT’s Skills interface. Each ZIP contains one skill.
3. In a new chat, name the skill and attach the alert, log excerpt, report, or artifact you want analyzed.
4. Validate conclusions in your organization’s tools and follow incident procedures.

Example: `Use the LDAP skill to analyze the attached directory query events.`

## Skill catalog

### Endpoint
- [Inspect Office macro evidence](skills/endpoint/office-macros/) · [ZIP](dist/chatgpt/office-macros.zip) — Static source or scanner output, auto-run entrypoints, file/network/process behavior; never execute.
- [Analyze PowerShell evidence](skills/endpoint/powershell/) · [ZIP](dist/chatgpt/powershell.zip) — Event logs, encoded content supplied by user, behavior explanation, corroborating telemetry.
- [Analyze a process tree](skills/endpoint/process-tree/) · [ZIP](dist/chatgpt/process-tree.zip) — Parent-child relationships, signer, user, command line, timing, network child processes.
- [Analyze registry changes](skills/endpoint/registry/) · [ZIP](dist/chatgpt/registry.zip) — Changed key/value, process and user context, persistence or configuration hypotheses.
- [Decode suspicious script evidence](skills/endpoint/script-decode/) · [ZIP](dist/chatgpt/script-decode.zip) — Identify encoding/obfuscation, safely decode supplied text, explain behavior without execution.
- [Analyze scheduled tasks and services](skills/endpoint/tasks-services/) · [ZIP](dist/chatgpt/tasks-services.zip) — Creator, task/service path, trigger, signer, account, host and timeline context.
- [Interpret Windows command lines](skills/endpoint/windows-command/) · [ZIP](dist/chatgpt/windows-command.zip) — Command purpose, parent process, user context, suspicious flags, corroboration.
- [Investigate Windows event records](skills/endpoint/windows-events/) · [ZIP](dist/chatgpt/windows-events.zip) — Event ids, log source, identity, time, host, sequence and limitations.

### Identity and directory
- [Review Active Directory changes](skills/identity/ad-changes/) · [ZIP](dist/chatgpt/ad-changes.zip) — Account/group/policy changes, actor, target, authorization and surrounding activity.
- [Investigate Kerberos events](skills/identity/kerberos/) · [ZIP](dist/chatgpt/kerberos.zip) — Ticket request patterns, service accounts, encryption fields, source hosts and context.
- [Analyze LDAP activity](skills/identity/ldap/) · [ZIP](dist/chatgpt/ldap.zip) — Directory query source, account, target scope, volume, timing, baseline and related events.
- [Review privileged access](skills/identity/privileged-access/) · [ZIP](dist/chatgpt/privileged-access.zip) — Role assignment, elevation, actor, approval, scope, duration and audit trail.
- [Investigate sign-in anomalies](skills/identity/sign-in/) · [ZIP](dist/chatgpt/sign-in.zip) — Identity, device, ip, location, auth result, mfa details, session context.

### Email
- [Analyze suspicious email](skills/email/email-analysis/) · [ZIP](dist/chatgpt/email-analysis.zip) — Headers, authentication, sender/reply-to, urls, attachment metadata, bec context and verdict.

### Network
- [Analyze DNS events](skills/network/dns/) · [ZIP](dist/chatgpt/dns.zip) — Queried name, client, response, frequency, reputation evidence and surrounding telemetry.
- [Analyze network flows](skills/network/network-flow/) · [ZIP](dist/chatgpt/network-flow.zip) — Source/destination, ports, bytes, timing, directionality and baseline.
- [Interpret packet-analysis summaries](skills/network/pcap-summary/) · [ZIP](dist/chatgpt/pcap-summary.zip) — Supplied zeek/protocol summaries, dns/tls/http metadata, timing and limits.
- [Review proxy and URL events](skills/network/proxy-url/) · [ZIP](dist/chatgpt/proxy-url.zip) — Url components, user/host context, response, redirects, bytes and safe defanging.

### Threat intelligence
- [Review file-hash evidence](skills/threat-intelligence/hash-analysis/) · [ZIP](dist/chatgpt/hash-analysis.zip) — Hash format, exact source, match context, prevalence, recency and file metadata.
- [Analyze indicators of compromise](skills/threat-intelligence/ioc-analysis/) · [ZIP](dist/chatgpt/ioc-analysis.zip) — Normalize/defang indicators, source/time, enrichment, confidence, disposition and expiry.
- [Interpret malware sandbox reports](skills/threat-intelligence/sandbox-report/) · [ZIP](dist/chatgpt/sandbox-report.zip) — Behavior sequence, environment limitations, network/file/process activity and confidence.

### SIEM and query languages
- [Draft and explain ES|QL](skills/siem/esql/) · [ZIP](dist/chatgpt/esql.zip) — Question-to-query using stated elastic schema, field assumptions and read-only investigation.
- [Draft and explain KQL](skills/siem/kql/) · [ZIP](dist/chatgpt/kql.zip) — Question-to-query, named tables/fields, time bounds, safe read-only syntax and validation.
- [Interpret SIEM query results](skills/siem/query-results/) · [ZIP](dist/chatgpt/query-results.zip) — Result shape, grouping, time range, nulls, sampling and limits on conclusions.

### Vulnerability management
- [Analyze port-scan alerts](skills/vulnerability-management/scan-alert/) · [ZIP](dist/chatgpt/scan-alert.zip) — Scanner source, target range, ports, rate, allowlists and evidence of follow-on activity.
- [Review vulnerability scan results](skills/vulnerability-management/scan-results/) · [ZIP](dist/chatgpt/scan-results.zip) — Asset identity, plugin/evidence, version, exposure, confidence, duplicates and remediation.
- [Plan an authorized scan scope](skills/vulnerability-management/scan-scope/) · [ZIP](dist/chatgpt/scan-scope.zip) — Written authorization, in-scope assets, exclusions, timing, rate limits and contacts.

### Detection engineering
- [Review detection logic](skills/detection-engineering/detection-review/) · [ZIP](dist/chatgpt/detection-review.zip) — Goal, data dependencies, logic, test coverage, false positives and safe tuning proposals.
- [Explain Sigma and YARA rules](skills/detection-engineering/sigma-yara/) · [ZIP](dist/chatgpt/sigma-yara.zip) — Rule intent, matching logic, required telemetry, false positives and limitations.

### Incident response
- [Write an incident escalation](skills/incident-response/escalation/) · [ZIP](dist/chatgpt/escalation.zip) — Concise evidence-based handoff, severity rationale, impact, unknowns, owner and next update.
- [Draft an incident report](skills/incident-response/incident-report/) · [ZIP](dist/chatgpt/incident-report.zip) — Verified scope, executive summary, timeline, impact, response, gaps and follow-up actions.
- [Expand incident scope safely](skills/incident-response/incident-scope/) · [ZIP](dist/chatgpt/incident-scope.zip) — Generate bounded read-only searches for related identities, hosts, indicators and time window.
- [Build an incident timeline](skills/incident-response/timeline/) · [ZIP](dist/chatgpt/timeline.zip) — Normalize timezones, preserve source references, order events and mark uncertainty.
- [Interpret an XDR alert](skills/incident-response/xdr-alert/) · [ZIP](dist/chatgpt/xdr-alert.zip) — Alert fields, detection rationale, entities, confidence, missing context.

## Connections and safe use

Skills provide task instructions; they do not grant access to a SIEM, XDR, EDR, mail platform, directory, scanner, or threat-intelligence feed. Use connected services only when they are separately configured and authorized. Skills are designed for analyst assistance: they treat supplied evidence as untrusted data, distinguish observed facts from inference, and do not claim lookups or actions that were not performed.

## Repository contents

- `skills/<domain>/<skill-id>/SKILL.md` — the skill instructions.
- `skills/<domain>/<skill-id>/README.md` — purpose and import guidance.
- `dist/chatgpt/<skill-id>.zip` — individual ChatGPT upload packages.
- `catalog.yml` — machine-readable catalog.

Course demonstration prompts and sample payloads are maintained separately and are intentionally not included here.

Learn with the [AI & Cybersecurity Academy](https://www.skool.com/ai-cybersecurity-academy/about).

