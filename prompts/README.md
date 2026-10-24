# Copyable prompts

Standalone prompts for the skills in this library. Copy a prompt into ChatGPT and attach or paste the relevant evidence. Each prompt uses the same output headings.

## Aws

- [AWS Access Keys](aws/aws-access-keys.md) — Investigate suspicious AWS access-key creation and use
- [AWS CloudTrail](aws/aws-cloudtrail.md) — Investigate CloudTrail visibility changes and suspicious control-plane sequences
- [AWS EC2](aws/aws-ec2.md) — Investigate suspicious EC2 control-plane and instance activity
- [AWS IAM](aws/aws-iam.md) — Investigate IAM policy, trust and privilege changes
- [AWS Lambda](aws/aws-lambda.md) — Investigate suspicious Lambda code, configuration and invocation activity
- [AWS S3](aws/aws-s3.md) — Investigate suspicious S3 object access and exposure
- [AWS SSO](aws/aws-sso.md) — Investigate AWS federation and IAM Identity Center session activity

## Azure

- [Azure Key Vault](azure/azure-keyvault.md) — Investigate suspicious secret, key or certificate access in Key Vault
- [Azure Logging](azure/azure-logging.md) — Investigate changes affecting Azure resource logging and visibility
- [Azure Roles](azure/azure-roles.md) — Investigate Azure role assignments and privilege changes
- [Azure Storage](azure/azure-storage.md) — Investigate suspicious Azure Storage access, sharing and token use
- [Azure VM](azure/azure-vm.md) — Investigate Azure VM remote execution and control-plane changes

## Containers

- [Container Escape](containers/container-escape.md) — Assess evidence that a container crossed into host resources
- [Container Images](containers/container-images.md) — Investigate suspicious container image provenance and runtime use
- [K8s Audit](containers/k8s-audit.md) — Reconstruct suspicious Kubernetes API activity from audit events
- [K8s RBAC](containers/k8s-rbac.md) — Investigate Kubernetes role and binding changes
- [Pod Exec](containers/pod-exec.md) — Investigate interactive execution into Kubernetes containers

## Detection Engineering

- [Coverage Review](detection-engineering/coverage-review.md) — Assess security detection coverage using actual telemetry and validation
- [Detection Replay](detection-engineering/detection-replay.md) — Replay an existing detection against recorded telemetry in a controlled backend and compare expected events, entities and alert groups.
- [Review detection logic](detection-engineering/detection-review.md) — Review detection logic. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Duplicate Rules](detection-engineering/duplicate-rules.md) — Identify overlapping detections without losing distinct coverage
- [Elastic Detection](detection-engineering/elastic-detection.md) — Author Elastic Security detections for a specified engine and schema
- [KQL Detection](detection-engineering/kql-detection.md) — Build operational KQL detections for Defender XDR or Microsoft Sentinel, including result identifiers, scheduling, entities and backend-aware tests.
- [Query Performance](detection-engineering/query-performance.md) — Improve security query performance while checking result equivalence
- [Rule Migration](detection-engineering/rule-migration.md) — Translate a detection between platforms while preserving its semantics
- [Rule Tests](detection-engineering/rule-tests.md) — Create meaningful executable or backend-native tests for an existing security detection, with explicit expected matches and negative cases.
- [Rule Tuning](detection-engineering/rule-tuning.md) — Reduce noise in an existing detection using labeled evidence while measuring lost coverage, regression risk and exception scope.
- [Sigma](detection-engineering/sigma.md) — Author or convert Sigma detections from documented behavior and supplied telemetry, including backend mappings and validation requirements.
- [Explain Sigma and YARA rules](detection-engineering/sigma-yara.md) — Explain Sigma and YARA rules. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [SPL Detection](detection-engineering/spl-detection.md) — Write Splunk SPL security detections with confirmed sourcetypes or CIM dependencies, operational search settings and controlled validation.
- [Suricata](detection-engineering/suricata.md) — Author Suricata signatures for observable network behavior
- [Threat Coverage](detection-engineering/threat-coverage.md) — Assess defensive coverage against a specific reported threat sequence
- [YARA](detection-engineering/yara.md) — Author and validate YARA rules for a defined file or memory target

## Email

- [Analyze suspicious email](email/email-analysis.md) — Analyze suspicious email. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.

## Endpoint

- [BITS Jobs](endpoint/bits-jobs.md) — Investigate suspicious Background Intelligent Transfer Service jobs
- [Browser Theft](endpoint/browser-theft.md) — Investigate access to browser credential and session stores
- [COM Hijack](endpoint/com-hijack.md) — Investigate COM registration changes that may redirect execution
- [Defender Tampering](endpoint/defender-tampering.md) — Investigate changes that impair Microsoft Defender or its visibility
- [DLL Loading](endpoint/dll-loading.md) — Assess suspicious DLL loading and potential side-loading
- [Driver Abuse](endpoint/driver-abuse.md) — Assess suspicious kernel driver loading and vulnerable-driver abuse
- [Local System Discovery](endpoint/local-discovery.md) — Analyze endpoint evidence showing commands or processes gathering local identity, system, network, process, service, session, or privilege information.
- [LSASS](endpoint/lsass.md) — Investigate suspected LSASS memory access and credential dumping
- [Named Pipes](endpoint/named-pipes.md) — Investigate suspicious named-pipe creation and connections
- [Inspect Office macro evidence](endpoint/office-macros.md) — Inspect Office macro evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Analyze PowerShell evidence](endpoint/powershell.md) — Analyze PowerShell evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Analyze a process tree](endpoint/process-tree.md) — Analyze a process tree. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Analyze registry changes](endpoint/registry.md) — Analyze registry changes. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Remote Thread](endpoint/remote-thread.md) — Investigate cross-process thread creation and injection hypotheses
- [Decode suspicious script evidence](endpoint/script-decode.md) — Decode suspicious script evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Shadow Copies](endpoint/shadow-copy.md) — Investigate deletion or disruption of backups and shadow copies
- [Analyze scheduled tasks and services](endpoint/tasks-services.md) — Analyze scheduled tasks and services. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Interpret Windows command lines](endpoint/windows-command.md) — Interpret Windows command lines. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Investigate Windows event records](endpoint/windows-events.md) — Investigate Windows event records. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [WMI Execution](endpoint/wmi-execution.md) — Investigate remote or local process execution through WMI
- [WMI Persistence](endpoint/wmi-persistence.md) — Investigate permanent WMI event subscriptions and their execution evidence

## Gcp

- [GCP Audit](gcp/gcp-audit.md) — Investigate Google Cloud audit sequences and logging gaps
- [GCP Compute](gcp/gcp-compute.md) — Investigate suspicious Compute Engine instance and access changes
- [GCP IAM](gcp/gcp-iam.md) — Investigate Google Cloud IAM policy and privilege changes
- [GCP Service Accounts](gcp/gcp-service-accounts.md) — Investigate service-account keys, impersonation and workload identity use
- [GCP Storage](gcp/gcp-storage.md) — Investigate suspicious Cloud Storage access and exposure

## Identity

- [Review Active Directory changes](identity/ad-changes.md) — Review Active Directory changes. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Active Directory Discovery](identity/ad-discovery.md) — Analyze directory enumeration evidence from LDAP, native Windows utilities, and AD assessment tools, including queried objects, scope, identity, and surrounding activity.
- [AD CS](identity/adcs.md) — Investigate suspicious Active Directory certificate issuance and template changes
- [AS-REP Roasting](identity/asrep-roasting.md) — Investigate authentication requests involving accounts without Kerberos preauthentication
- [DCShadow](identity/dcshadow.md) — Investigate suspicious directory replication registration and object changes
- [DCSync](identity/dcsync.md) — Investigate directory replication requests from unexpected principals or hosts
- [Delegation Abuse](identity/delegation-abuse.md) — Investigate changes or use of Kerberos delegation relationships
- [Golden Ticket](identity/golden-ticket.md) — Assess forged Kerberos ticket hypotheses using corroborated authentication evidence
- [GPO Abuse](identity/gpo-abuse.md) — Investigate unauthorized Group Policy changes and resulting endpoint behavior
- [Kerberoasting](identity/kerberoasting.md) — Investigate suspicious Kerberos service-ticket requests
- [Investigate Kerberos events](identity/kerberos.md) — Investigate Kerberos events. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [NTLM Relay](identity/ntlm-relay.md) — Investigate suspected relayed NTLM authentication
- [Password Spray](identity/password-spray.md) — Investigate low-frequency authentication attempts spread across accounts
- [Review privileged access](identity/privileged-access.md) — Review privileged access. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Investigate sign-in anomalies](identity/sign-in.md) — Investigate sign-in anomalies. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.

## Incident Response

- [Containment Plan](incident-response/containment-plan.md) — Develop a scoped containment plan from confirmed incident evidence
- [Write an incident escalation](incident-response/escalation.md) — Write an incident escalation. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Evidence Preservation](incident-response/evidence-preservation.md) — Plan and document defensible preservation of security evidence
- [Draft an incident report](incident-response/incident-report.md) — Draft an incident report. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Expand incident scope safely](incident-response/incident-scope.md) — Expand incident scope safely. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Recovery Review](incident-response/recovery-review.md) — Review whether recovery evidence supports safe restoration and monitoring
- [Build an incident timeline](incident-response/timeline.md) — Build an incident timeline. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Interpret an XDR alert](incident-response/xdr-alert.md) — Interpret an XDR alert. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.

## Linux

- [Cron](linux/cron.md) — Investigate suspicious cron-based execution and persistence
- [LD Preload](linux/ld-preload.md) — Investigate dynamic-loader configuration that may inject shared libraries
- [Linux Audit](linux/linux-audit.md) — Reconstruct security-relevant activity from Linux audit records
- [Linux Log Tampering](linux/linux-log-tampering.md) — Investigate disruption or manipulation of Linux security logging
- [SSH](linux/ssh.md) — Investigate suspicious SSH authentication and session activity
- [SSH Keys](linux/ssh-keys.md) — Investigate unauthorized SSH key and trust configuration changes
- [Sudo](linux/sudo.md) — Investigate privilege changes through sudo
- [Systemd](linux/systemd.md) — Investigate suspicious systemd units, timers and drop-ins

## Malware Forensics

- [Archive Analysis](malware-forensics/archive-analysis.md) — Assess archive contents and delivery risks without executing members
- [Browser Artifacts](malware-forensics/browser-artifacts.md) — Investigate browser history, downloads and profile artifacts
- [Disk Artifacts](malware-forensics/disk-artifacts.md) — Correlate filesystem forensic artifacts into an activity hypothesis
- [LNK Analysis](malware-forensics/lnk-analysis.md) — Analyze Windows shortcut artifacts without opening their targets
- [Memory Analysis](malware-forensics/memory-analysis.md) — Interpret memory forensic output for suspicious processes and artifacts
- [PE Analysis](malware-forensics/pe-analysis.md) — Perform static triage of Windows PE files or supplied parser output
- [Ransomware](malware-forensics/ransomware.md) — Investigate ransomware behavior and impact from correlated evidence

## Microsoft 365

- [Conditional Access](microsoft-365/conditional-access.md) — Investigate Conditional Access changes and unexpected access outcomes
- [Entra Apps](microsoft-365/entra-apps.md) — Investigate application and service-principal credential changes
- [Inbox Rules](microsoft-365/inbox-rules.md) — Investigate mailbox rules that conceal or redirect messages
- [Mailbox Access](microsoft-365/mailbox-access.md) — Investigate anomalous mailbox content access
- [MFA Fatigue](microsoft-365/mfa-fatigue.md) — Investigate repeated MFA prompts and a possibly coerced approval
- [OAuth Grants](microsoft-365/oauth-grants.md) — Investigate suspicious application consent and delegated access
- [SharePoint Access](microsoft-365/sharepoint-access.md) — Investigate suspicious SharePoint and OneDrive access or sharing
- [Teams Abuse](microsoft-365/teams-abuse.md) — Investigate suspicious Teams collaboration or application activity
- [Token Theft](microsoft-365/token-theft.md) — Investigate suspicious reuse of cloud sessions or tokens

## Network

- [Beaconing](network/beaconing.md) — Investigate periodic outbound communication and command-and-control hypotheses
- [Data Exfiltration](network/data-exfiltration.md) — Investigate suspected outbound data transfer
- [Analyze DNS events](network/dns.md) — Analyze DNS events. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [DNS Tunneling](network/dns-tunneling.md) — Investigate DNS traffic that may carry a covert channel
- [Network Recon and SMB Discovery](network/network-discovery.md) — Analyze authorized scan scope and results, scanning alerts, remote host and service discovery, and SMB share enumeration from supplied evidence.
- [Analyze network flows](network/network-flow.md) — Analyze network flows. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Interpret packet-analysis summaries](network/pcap-summary.md) — Interpret packet-analysis summaries. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Review proxy and URL events](network/proxy-url.md) — Review proxy and URL events. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [RDP Lateral](network/rdp-lateral.md) — Investigate suspicious Remote Desktop sessions
- [SMB Lateral](network/smb-lateral.md) — Investigate suspicious SMB-based movement between hosts
- [TLS Analysis](network/tls-analysis.md) — Assess suspicious TLS metadata and certificate relationships
- [Web Attacks](network/web-attacks.md) — Investigate suspected exploitation attempts in HTTP or WAF evidence
- [WinRM Lateral](network/winrm-lateral.md) — Investigate remote management execution through WinRM

## Saas Development

- [CI/CD Abuse](saas-development/cicd-abuse.md) — Investigate suspicious workflow modifications and build execution
- [GitHub Audit](saas-development/github-audit.md) — Investigate suspicious GitHub organization and repository activity
- [Prompt Injection](saas-development/prompt-injection.md) — Investigate untrusted content that attempts to redirect an AI security workflow
- [Secret Exposure](saas-development/secret-exposure.md) — Assess exposed credentials without disclosing or using them

## Security Automation

- [Alert Routing](security-automation/alert-routing.md) — Design routing and deduplication for security alerts
- [API Integration](security-automation/api-integration.md) — Implement an authenticated security API integration with bounded operations
- [Enrichment Pipeline](security-automation/enrichment-pipeline.md) — Build a bounded intelligence enrichment workflow with provenance
- [SOAR Playbook](security-automation/soar-playbook.md) — Design a reviewable automation playbook for a defined security workflow

## Siem

- [Draft and explain ES|QL](siem/esql.md) — Draft and explain ES|QL. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Draft and explain KQL](siem/kql.md) — Draft and explain KQL. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Interpret SIEM query results](siem/query-results.md) — Interpret SIEM query results. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.

## Telemetry Engineering

- [Field Mapping](telemetry-engineering/field-mapping.md) — Map vendor security telemetry to a specified ECS, OCSF or local schema using field semantics, types, transformations and explicit unmapped values.
- [Log Parser](telemetry-engineering/log-parser.md) — Build or repair parsers for supplied security logs, preserving raw evidence and handling timestamps, framing, escapes and malformed records.
- [Log Quality](telemetry-engineering/log-quality.md) — Assess security log completeness, parsing, timestamps, duplicate candidates and ingestion delay from supplied records or bounded authorized queries.

## Threat Intelligence

- [Campaign Review](threat-intelligence/campaign-review.md) — Evaluate whether observed incident evidence matches a reported campaign
- [Review file-hash evidence](threat-intelligence/hash-analysis.md) — Review file-hash evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Indicator Expiry](threat-intelligence/indicator-expiry.md) — Propose evidence-based indicator retention and review policies
- [Infrastructure Links](threat-intelligence/infrastructure-links.md) — Assess relationships among suspicious domains, IPs and certificates
- [Intel Dedup](threat-intelligence/intel-dedup.md) — Deduplicate intelligence while preserving distinct observations and source lineage
- [Intel to Hunt](threat-intelligence/intel-to-hunt.md) — Translate a threat report into testable defensive hunt hypotheses
- [Analyze indicators of compromise](threat-intelligence/ioc-analysis.md) — Analyze indicators of compromise. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [Interpret malware sandbox reports](threat-intelligence/sandbox-report.md) — Interpret malware sandbox reports. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool.
- [STIX Review](threat-intelligence/stix-review.md) — Review STIX intelligence objects and relationships for semantic validity

## Threat Intelligence Engineering

- [Feed Quality](threat-intelligence-engineering/feed-quality.md) — Evaluate threat intelligence feed quality through indicator validity, provenance, observation age, duplication, confidence semantics and sharing restrictions.

## Vulnerability Management

- [CVE Review](vulnerability-management/cve-review.md) — Assess a CVE's applicability and investigation relevance
- [Exposure Review](vulnerability-management/exposure-review.md) — Review whether a vulnerable service is reachable in its actual environment
- [Patch Priority](vulnerability-management/patch-priority.md) — Prioritize remediation using exploitation evidence and asset context
- [Remediation Review](vulnerability-management/remediation-review.md) — Verify remediation evidence and detect incomplete fixes
- [Vulnerability Validation](vulnerability-management/vulnerability-validation.md) — Validate scanner findings through version and configuration evidence

