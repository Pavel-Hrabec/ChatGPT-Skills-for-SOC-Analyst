# Community Skill Catalog

150 focused skills across security operations and engineering. Each upload contains one self-contained skill. Individual packages can be downloaded from `dist/chatgpt/`.

## AWS

7 skills

| Skill | Purpose | Package |
|---|---|---|
| [AWS Access Keys](skills/aws/aws-access-keys/) | Investigate suspicious AWS access-key creation and use | [ZIP](dist/chatgpt/aws-access-keys.zip) |
| [AWS CloudTrail](skills/aws/aws-cloudtrail/) | Investigate CloudTrail visibility changes and suspicious control-plane sequences | [ZIP](dist/chatgpt/aws-cloudtrail.zip) |
| [AWS EC2](skills/aws/aws-ec2/) | Investigate suspicious EC2 control-plane and instance activity | [ZIP](dist/chatgpt/aws-ec2.zip) |
| [AWS IAM](skills/aws/aws-iam/) | Investigate IAM policy, trust and privilege changes | [ZIP](dist/chatgpt/aws-iam.zip) |
| [AWS Lambda](skills/aws/aws-lambda/) | Investigate suspicious Lambda code, configuration and invocation activity | [ZIP](dist/chatgpt/aws-lambda.zip) |
| [AWS S3](skills/aws/aws-s3/) | Investigate suspicious S3 object access and exposure | [ZIP](dist/chatgpt/aws-s3.zip) |
| [AWS SSO](skills/aws/aws-sso/) | Investigate AWS federation and IAM Identity Center session activity | [ZIP](dist/chatgpt/aws-sso.zip) |

## Azure

5 skills

| Skill | Purpose | Package |
|---|---|---|
| [Azure Key Vault](skills/azure/azure-keyvault/) | Investigate suspicious secret, key or certificate access in Key Vault | [ZIP](dist/chatgpt/azure-keyvault.zip) |
| [Azure Logging](skills/azure/azure-logging/) | Investigate changes affecting Azure resource logging and visibility | [ZIP](dist/chatgpt/azure-logging.zip) |
| [Azure Roles](skills/azure/azure-roles/) | Investigate Azure role assignments and privilege changes | [ZIP](dist/chatgpt/azure-roles.zip) |
| [Azure Storage](skills/azure/azure-storage/) | Investigate suspicious Azure Storage access, sharing and token use | [ZIP](dist/chatgpt/azure-storage.zip) |
| [Azure VM](skills/azure/azure-vm/) | Investigate Azure VM remote execution and control-plane changes | [ZIP](dist/chatgpt/azure-vm.zip) |

## Containers

5 skills

| Skill | Purpose | Package |
|---|---|---|
| [Container Escape](skills/containers/container-escape/) | Assess evidence that a container crossed into host resources | [ZIP](dist/chatgpt/container-escape.zip) |
| [Container Images](skills/containers/container-images/) | Investigate suspicious container image provenance and runtime use | [ZIP](dist/chatgpt/container-images.zip) |
| [K8s Audit](skills/containers/k8s-audit/) | Reconstruct suspicious Kubernetes API activity from audit events | [ZIP](dist/chatgpt/k8s-audit.zip) |
| [K8s RBAC](skills/containers/k8s-rbac/) | Investigate Kubernetes role and binding changes | [ZIP](dist/chatgpt/k8s-rbac.zip) |
| [Pod Exec](skills/containers/pod-exec/) | Investigate interactive execution into Kubernetes containers | [ZIP](dist/chatgpt/pod-exec.zip) |

## Detection Engineering

16 skills

| Skill | Purpose | Package |
|---|---|---|
| [Coverage Review](skills/detection-engineering/coverage-review/) | Assess security detection coverage using actual telemetry and validation | [ZIP](dist/chatgpt/coverage-review.zip) |
| [Detection Replay](skills/detection-engineering/detection-replay/) | Replay an existing detection against recorded telemetry in a controlled backend and compare expected events, entities and alert groups. | [ZIP](dist/chatgpt/detection-replay.zip) |
| [Review detection logic](skills/detection-engineering/detection-review/) | Review detection logic | [ZIP](dist/chatgpt/detection-review.zip) |
| [Duplicate Rules](skills/detection-engineering/duplicate-rules/) | Identify overlapping detections without losing distinct coverage | [ZIP](dist/chatgpt/duplicate-rules.zip) |
| [Elastic Detection](skills/detection-engineering/elastic-detection/) | Author Elastic Security detections for a specified engine and schema | [ZIP](dist/chatgpt/elastic-detection.zip) |
| [KQL Detection](skills/detection-engineering/kql-detection/) | Build operational KQL detections for Defender XDR or Microsoft Sentinel, including result identifiers, scheduling, entities and backend-aware tests. | [ZIP](dist/chatgpt/kql-detection.zip) |
| [Query Performance](skills/detection-engineering/query-performance/) | Improve security query performance while checking result equivalence | [ZIP](dist/chatgpt/query-performance.zip) |
| [Rule Migration](skills/detection-engineering/rule-migration/) | Translate a detection between platforms while preserving its semantics | [ZIP](dist/chatgpt/rule-migration.zip) |
| [Rule Tests](skills/detection-engineering/rule-tests/) | Create meaningful executable or backend-native tests for an existing security detection, with explicit expected matches and negative cases. | [ZIP](dist/chatgpt/rule-tests.zip) |
| [Rule Tuning](skills/detection-engineering/rule-tuning/) | Reduce noise in an existing detection using labeled evidence while measuring lost coverage, regression risk and exception scope. | [ZIP](dist/chatgpt/rule-tuning.zip) |
| [Sigma](skills/detection-engineering/sigma/) | Author or convert Sigma detections from documented behavior and supplied telemetry, including backend mappings and validation requirements. | [ZIP](dist/chatgpt/sigma.zip) |
| [Explain Sigma and YARA rules](skills/detection-engineering/sigma-yara/) | Explain Sigma and YARA rules | [ZIP](dist/chatgpt/sigma-yara.zip) |
| [SPL Detection](skills/detection-engineering/spl-detection/) | Write Splunk SPL security detections with confirmed sourcetypes or CIM dependencies, operational search settings and controlled validation. | [ZIP](dist/chatgpt/spl-detection.zip) |
| [Suricata](skills/detection-engineering/suricata/) | Author Suricata signatures for observable network behavior | [ZIP](dist/chatgpt/suricata.zip) |
| [Threat Coverage](skills/detection-engineering/threat-coverage/) | Assess defensive coverage against a specific reported threat sequence | [ZIP](dist/chatgpt/threat-coverage.zip) |
| [YARA](skills/detection-engineering/yara/) | Author and validate YARA rules for a defined file or memory target | [ZIP](dist/chatgpt/yara.zip) |

## Email

1 skill

| Skill | Purpose | Package |
|---|---|---|
| [Analyze suspicious email](skills/email/email-analysis/) | Analyze suspicious email | [ZIP](dist/chatgpt/email-analysis.zip) |

## Endpoint

20 skills

| Skill | Purpose | Package |
|---|---|---|
| [BITS Jobs](skills/endpoint/bits-jobs/) | Investigate suspicious Background Intelligent Transfer Service jobs | [ZIP](dist/chatgpt/bits-jobs.zip) |
| [Browser Theft](skills/endpoint/browser-theft/) | Investigate access to browser credential and session stores | [ZIP](dist/chatgpt/browser-theft.zip) |
| [COM Hijack](skills/endpoint/com-hijack/) | Investigate COM registration changes that may redirect execution | [ZIP](dist/chatgpt/com-hijack.zip) |
| [Defender Tampering](skills/endpoint/defender-tampering/) | Investigate changes that impair Microsoft Defender or its visibility | [ZIP](dist/chatgpt/defender-tampering.zip) |
| [DLL Loading](skills/endpoint/dll-loading/) | Assess suspicious DLL loading and potential side-loading | [ZIP](dist/chatgpt/dll-loading.zip) |
| [Driver Abuse](skills/endpoint/driver-abuse/) | Assess suspicious kernel driver loading and vulnerable-driver abuse | [ZIP](dist/chatgpt/driver-abuse.zip) |
| [LSASS](skills/endpoint/lsass/) | Investigate suspected LSASS memory access and credential dumping | [ZIP](dist/chatgpt/lsass.zip) |
| [Named Pipes](skills/endpoint/named-pipes/) | Investigate suspicious named-pipe creation and connections | [ZIP](dist/chatgpt/named-pipes.zip) |
| [Inspect Office macro evidence](skills/endpoint/office-macros/) | Inspect Office macro evidence | [ZIP](dist/chatgpt/office-macros.zip) |
| [Analyze PowerShell evidence](skills/endpoint/powershell/) | Analyze PowerShell evidence | [ZIP](dist/chatgpt/powershell.zip) |
| [Analyze a process tree](skills/endpoint/process-tree/) | Analyze a process tree | [ZIP](dist/chatgpt/process-tree.zip) |
| [Analyze registry changes](skills/endpoint/registry/) | Analyze registry changes | [ZIP](dist/chatgpt/registry.zip) |
| [Remote Thread](skills/endpoint/remote-thread/) | Investigate cross-process thread creation and injection hypotheses | [ZIP](dist/chatgpt/remote-thread.zip) |
| [Decode suspicious script evidence](skills/endpoint/script-decode/) | Decode suspicious script evidence | [ZIP](dist/chatgpt/script-decode.zip) |
| [Shadow Copies](skills/endpoint/shadow-copy/) | Investigate deletion or disruption of backups and shadow copies | [ZIP](dist/chatgpt/shadow-copy.zip) |
| [Analyze scheduled tasks and services](skills/endpoint/tasks-services/) | Analyze scheduled tasks and services | [ZIP](dist/chatgpt/tasks-services.zip) |
| [Interpret Windows command lines](skills/endpoint/windows-command/) | Interpret Windows command lines | [ZIP](dist/chatgpt/windows-command.zip) |
| [Investigate Windows event records](skills/endpoint/windows-events/) | Investigate Windows event records | [ZIP](dist/chatgpt/windows-events.zip) |
| [WMI Execution](skills/endpoint/wmi-execution/) | Investigate remote or local process execution through WMI | [ZIP](dist/chatgpt/wmi-execution.zip) |
| [WMI Persistence](skills/endpoint/wmi-persistence/) | Investigate permanent WMI event subscriptions and their execution evidence | [ZIP](dist/chatgpt/wmi-persistence.zip) |

## GCP

5 skills

| Skill | Purpose | Package |
|---|---|---|
| [GCP Audit](skills/gcp/gcp-audit/) | Investigate Google Cloud audit sequences and logging gaps | [ZIP](dist/chatgpt/gcp-audit.zip) |
| [GCP Compute](skills/gcp/gcp-compute/) | Investigate suspicious Compute Engine instance and access changes | [ZIP](dist/chatgpt/gcp-compute.zip) |
| [GCP IAM](skills/gcp/gcp-iam/) | Investigate Google Cloud IAM policy and privilege changes | [ZIP](dist/chatgpt/gcp-iam.zip) |
| [GCP Service Accounts](skills/gcp/gcp-service-accounts/) | Investigate service-account keys, impersonation and workload identity use | [ZIP](dist/chatgpt/gcp-service-accounts.zip) |
| [GCP Storage](skills/gcp/gcp-storage/) | Investigate suspicious Cloud Storage access and exposure | [ZIP](dist/chatgpt/gcp-storage.zip) |

## Identity

15 skills

| Skill | Purpose | Package |
|---|---|---|
| [Review Active Directory changes](skills/identity/ad-changes/) | Review Active Directory changes | [ZIP](dist/chatgpt/ad-changes.zip) |
| [AD CS](skills/identity/adcs/) | Investigate suspicious Active Directory certificate issuance and template changes | [ZIP](dist/chatgpt/adcs.zip) |
| [AS-REP Roasting](skills/identity/asrep-roasting/) | Investigate authentication requests involving accounts without Kerberos preauthentication | [ZIP](dist/chatgpt/asrep-roasting.zip) |
| [DCShadow](skills/identity/dcshadow/) | Investigate suspicious directory replication registration and object changes | [ZIP](dist/chatgpt/dcshadow.zip) |
| [DCSync](skills/identity/dcsync/) | Investigate directory replication requests from unexpected principals or hosts | [ZIP](dist/chatgpt/dcsync.zip) |
| [Delegation Abuse](skills/identity/delegation-abuse/) | Investigate changes or use of Kerberos delegation relationships | [ZIP](dist/chatgpt/delegation-abuse.zip) |
| [Golden Ticket](skills/identity/golden-ticket/) | Assess forged Kerberos ticket hypotheses using corroborated authentication evidence | [ZIP](dist/chatgpt/golden-ticket.zip) |
| [GPO Abuse](skills/identity/gpo-abuse/) | Investigate unauthorized Group Policy changes and resulting endpoint behavior | [ZIP](dist/chatgpt/gpo-abuse.zip) |
| [Kerberoasting](skills/identity/kerberoasting/) | Investigate suspicious Kerberos service-ticket requests | [ZIP](dist/chatgpt/kerberoasting.zip) |
| [Investigate Kerberos events](skills/identity/kerberos/) | Investigate Kerberos events | [ZIP](dist/chatgpt/kerberos.zip) |
| [Analyze LDAP activity](skills/identity/ldap/) | Analyze LDAP activity | [ZIP](dist/chatgpt/ldap.zip) |
| [NTLM Relay](skills/identity/ntlm-relay/) | Investigate suspected relayed NTLM authentication | [ZIP](dist/chatgpt/ntlm-relay.zip) |
| [Password Spray](skills/identity/password-spray/) | Investigate low-frequency authentication attempts spread across accounts | [ZIP](dist/chatgpt/password-spray.zip) |
| [Review privileged access](skills/identity/privileged-access/) | Review privileged access | [ZIP](dist/chatgpt/privileged-access.zip) |
| [Investigate sign-in anomalies](skills/identity/sign-in/) | Investigate sign-in anomalies | [ZIP](dist/chatgpt/sign-in.zip) |

## Incident Response

8 skills

| Skill | Purpose | Package |
|---|---|---|
| [Containment Plan](skills/incident-response/containment-plan/) | Develop a scoped containment plan from confirmed incident evidence | [ZIP](dist/chatgpt/containment-plan.zip) |
| [Write an incident escalation](skills/incident-response/escalation/) | Write an incident escalation | [ZIP](dist/chatgpt/escalation.zip) |
| [Evidence Preservation](skills/incident-response/evidence-preservation/) | Plan and document defensible preservation of security evidence | [ZIP](dist/chatgpt/evidence-preservation.zip) |
| [Draft an incident report](skills/incident-response/incident-report/) | Draft an incident report | [ZIP](dist/chatgpt/incident-report.zip) |
| [Expand incident scope safely](skills/incident-response/incident-scope/) | Expand incident scope safely | [ZIP](dist/chatgpt/incident-scope.zip) |
| [Recovery Review](skills/incident-response/recovery-review/) | Review whether recovery evidence supports safe restoration and monitoring | [ZIP](dist/chatgpt/recovery-review.zip) |
| [Build an incident timeline](skills/incident-response/timeline/) | Build an incident timeline | [ZIP](dist/chatgpt/timeline.zip) |
| [Interpret an XDR alert](skills/incident-response/xdr-alert/) | Interpret an XDR alert | [ZIP](dist/chatgpt/xdr-alert.zip) |

## Linux

8 skills

| Skill | Purpose | Package |
|---|---|---|
| [Cron](skills/linux/cron/) | Investigate suspicious cron-based execution and persistence | [ZIP](dist/chatgpt/cron.zip) |
| [LD Preload](skills/linux/ld-preload/) | Investigate dynamic-loader configuration that may inject shared libraries | [ZIP](dist/chatgpt/ld-preload.zip) |
| [Linux Audit](skills/linux/linux-audit/) | Reconstruct security-relevant activity from Linux audit records | [ZIP](dist/chatgpt/linux-audit.zip) |
| [Linux Log Tampering](skills/linux/linux-log-tampering/) | Investigate disruption or manipulation of Linux security logging | [ZIP](dist/chatgpt/linux-log-tampering.zip) |
| [SSH](skills/linux/ssh/) | Investigate suspicious SSH authentication and session activity | [ZIP](dist/chatgpt/ssh.zip) |
| [SSH Keys](skills/linux/ssh-keys/) | Investigate unauthorized SSH key and trust configuration changes | [ZIP](dist/chatgpt/ssh-keys.zip) |
| [Sudo](skills/linux/sudo/) | Investigate privilege changes through sudo | [ZIP](dist/chatgpt/sudo.zip) |
| [Systemd](skills/linux/systemd/) | Investigate suspicious systemd units, timers and drop-ins | [ZIP](dist/chatgpt/systemd.zip) |

## Malware Forensics

7 skills

| Skill | Purpose | Package |
|---|---|---|
| [Archive Analysis](skills/malware-forensics/archive-analysis/) | Assess archive contents and delivery risks without executing members | [ZIP](dist/chatgpt/archive-analysis.zip) |
| [Browser Artifacts](skills/malware-forensics/browser-artifacts/) | Investigate browser history, downloads and profile artifacts | [ZIP](dist/chatgpt/browser-artifacts.zip) |
| [Disk Artifacts](skills/malware-forensics/disk-artifacts/) | Correlate filesystem forensic artifacts into an activity hypothesis | [ZIP](dist/chatgpt/disk-artifacts.zip) |
| [LNK Analysis](skills/malware-forensics/lnk-analysis/) | Analyze Windows shortcut artifacts without opening their targets | [ZIP](dist/chatgpt/lnk-analysis.zip) |
| [Memory Analysis](skills/malware-forensics/memory-analysis/) | Interpret memory forensic output for suspicious processes and artifacts | [ZIP](dist/chatgpt/memory-analysis.zip) |
| [PE Analysis](skills/malware-forensics/pe-analysis/) | Perform static triage of Windows PE files or supplied parser output | [ZIP](dist/chatgpt/pe-analysis.zip) |
| [Ransomware](skills/malware-forensics/ransomware/) | Investigate ransomware behavior and impact from correlated evidence | [ZIP](dist/chatgpt/ransomware.zip) |

## Microsoft 365

9 skills

| Skill | Purpose | Package |
|---|---|---|
| [Conditional Access](skills/microsoft-365/conditional-access/) | Investigate Conditional Access changes and unexpected access outcomes | [ZIP](dist/chatgpt/conditional-access.zip) |
| [Entra Apps](skills/microsoft-365/entra-apps/) | Investigate application and service-principal credential changes | [ZIP](dist/chatgpt/entra-apps.zip) |
| [Inbox Rules](skills/microsoft-365/inbox-rules/) | Investigate mailbox rules that conceal or redirect messages | [ZIP](dist/chatgpt/inbox-rules.zip) |
| [Mailbox Access](skills/microsoft-365/mailbox-access/) | Investigate anomalous mailbox content access | [ZIP](dist/chatgpt/mailbox-access.zip) |
| [MFA Fatigue](skills/microsoft-365/mfa-fatigue/) | Investigate repeated MFA prompts and a possibly coerced approval | [ZIP](dist/chatgpt/mfa-fatigue.zip) |
| [OAuth Grants](skills/microsoft-365/oauth-grants/) | Investigate suspicious application consent and delegated access | [ZIP](dist/chatgpt/oauth-grants.zip) |
| [SharePoint Access](skills/microsoft-365/sharepoint-access/) | Investigate suspicious SharePoint and OneDrive access or sharing | [ZIP](dist/chatgpt/sharepoint-access.zip) |
| [Teams Abuse](skills/microsoft-365/teams-abuse/) | Investigate suspicious Teams collaboration or application activity | [ZIP](dist/chatgpt/teams-abuse.zip) |
| [Token Theft](skills/microsoft-365/token-theft/) | Investigate suspicious reuse of cloud sessions or tokens | [ZIP](dist/chatgpt/token-theft.zip) |

## Network

12 skills

| Skill | Purpose | Package |
|---|---|---|
| [Beaconing](skills/network/beaconing/) | Investigate periodic outbound communication and command-and-control hypotheses | [ZIP](dist/chatgpt/beaconing.zip) |
| [Data Exfiltration](skills/network/data-exfiltration/) | Investigate suspected outbound data transfer | [ZIP](dist/chatgpt/data-exfiltration.zip) |
| [Analyze DNS events](skills/network/dns/) | Analyze DNS events | [ZIP](dist/chatgpt/dns.zip) |
| [DNS Tunneling](skills/network/dns-tunneling/) | Investigate DNS traffic that may carry a covert channel | [ZIP](dist/chatgpt/dns-tunneling.zip) |
| [Analyze network flows](skills/network/network-flow/) | Analyze network flows | [ZIP](dist/chatgpt/network-flow.zip) |
| [Interpret packet-analysis summaries](skills/network/pcap-summary/) | Interpret packet-analysis summaries | [ZIP](dist/chatgpt/pcap-summary.zip) |
| [Review proxy and URL events](skills/network/proxy-url/) | Review proxy and URL events | [ZIP](dist/chatgpt/proxy-url.zip) |
| [RDP Lateral](skills/network/rdp-lateral/) | Investigate suspicious Remote Desktop sessions | [ZIP](dist/chatgpt/rdp-lateral.zip) |
| [SMB Lateral](skills/network/smb-lateral/) | Investigate suspicious SMB-based movement between hosts | [ZIP](dist/chatgpt/smb-lateral.zip) |
| [TLS Analysis](skills/network/tls-analysis/) | Assess suspicious TLS metadata and certificate relationships | [ZIP](dist/chatgpt/tls-analysis.zip) |
| [Web Attacks](skills/network/web-attacks/) | Investigate suspected exploitation attempts in HTTP or WAF evidence | [ZIP](dist/chatgpt/web-attacks.zip) |
| [WinRM Lateral](skills/network/winrm-lateral/) | Investigate remote management execution through WinRM | [ZIP](dist/chatgpt/winrm-lateral.zip) |

## SaaS Development

4 skills

| Skill | Purpose | Package |
|---|---|---|
| [CI/CD Abuse](skills/saas-development/cicd-abuse/) | Investigate suspicious workflow modifications and build execution | [ZIP](dist/chatgpt/cicd-abuse.zip) |
| [GitHub Audit](skills/saas-development/github-audit/) | Investigate suspicious GitHub organization and repository activity | [ZIP](dist/chatgpt/github-audit.zip) |
| [Prompt Injection](skills/saas-development/prompt-injection/) | Investigate untrusted content that attempts to redirect an AI security workflow | [ZIP](dist/chatgpt/prompt-injection.zip) |
| [Secret Exposure](skills/saas-development/secret-exposure/) | Assess exposed credentials without disclosing or using them | [ZIP](dist/chatgpt/secret-exposure.zip) |

## Security Automation

4 skills

| Skill | Purpose | Package |
|---|---|---|
| [Alert Routing](skills/security-automation/alert-routing/) | Design routing and deduplication for security alerts | [ZIP](dist/chatgpt/alert-routing.zip) |
| [API Integration](skills/security-automation/api-integration/) | Implement an authenticated security API integration with bounded operations | [ZIP](dist/chatgpt/api-integration.zip) |
| [Enrichment Pipeline](skills/security-automation/enrichment-pipeline/) | Build a bounded intelligence enrichment workflow with provenance | [ZIP](dist/chatgpt/enrichment-pipeline.zip) |
| [SOAR Playbook](skills/security-automation/soar-playbook/) | Design a reviewable automation playbook for a defined security workflow | [ZIP](dist/chatgpt/soar-playbook.zip) |

## SIEM

3 skills

| Skill | Purpose | Package |
|---|---|---|
| [Draft and explain ES&#124;QL](skills/siem/esql/) | Draft and explain ES&#124;QL | [ZIP](dist/chatgpt/esql.zip) |
| [Draft and explain KQL](skills/siem/kql/) | Draft and explain KQL | [ZIP](dist/chatgpt/kql.zip) |
| [Interpret SIEM query results](skills/siem/query-results/) | Interpret SIEM query results | [ZIP](dist/chatgpt/query-results.zip) |

## Telemetry Engineering

3 skills

| Skill | Purpose | Package |
|---|---|---|
| [Field Mapping](skills/telemetry-engineering/field-mapping/) | Map vendor security telemetry to a specified ECS, OCSF or local schema using field semantics, types, transformations and explicit unmapped values. | [ZIP](dist/chatgpt/field-mapping.zip) |
| [Log Parser](skills/telemetry-engineering/log-parser/) | Build or repair parsers for supplied security logs, preserving raw evidence and handling timestamps, framing, escapes and malformed records. | [ZIP](dist/chatgpt/log-parser.zip) |
| [Log Quality](skills/telemetry-engineering/log-quality/) | Assess security log completeness, parsing, timestamps, duplicate candidates and ingestion delay from supplied records or bounded authorized queries. | [ZIP](dist/chatgpt/log-quality.zip) |

## Threat Intelligence

9 skills

| Skill | Purpose | Package |
|---|---|---|
| [Campaign Review](skills/threat-intelligence/campaign-review/) | Evaluate whether observed incident evidence matches a reported campaign | [ZIP](dist/chatgpt/campaign-review.zip) |
| [Review file-hash evidence](skills/threat-intelligence/hash-analysis/) | Review file-hash evidence | [ZIP](dist/chatgpt/hash-analysis.zip) |
| [Indicator Expiry](skills/threat-intelligence/indicator-expiry/) | Propose evidence-based indicator retention and review policies | [ZIP](dist/chatgpt/indicator-expiry.zip) |
| [Infrastructure Links](skills/threat-intelligence/infrastructure-links/) | Assess relationships among suspicious domains, IPs and certificates | [ZIP](dist/chatgpt/infrastructure-links.zip) |
| [Intel Dedup](skills/threat-intelligence/intel-dedup/) | Deduplicate intelligence while preserving distinct observations and source lineage | [ZIP](dist/chatgpt/intel-dedup.zip) |
| [Intel to Hunt](skills/threat-intelligence/intel-to-hunt/) | Translate a threat report into testable defensive hunt hypotheses | [ZIP](dist/chatgpt/intel-to-hunt.zip) |
| [Analyze indicators of compromise](skills/threat-intelligence/ioc-analysis/) | Analyze indicators of compromise | [ZIP](dist/chatgpt/ioc-analysis.zip) |
| [Interpret malware sandbox reports](skills/threat-intelligence/sandbox-report/) | Interpret malware sandbox reports | [ZIP](dist/chatgpt/sandbox-report.zip) |
| [STIX Review](skills/threat-intelligence/stix-review/) | Review STIX intelligence objects and relationships for semantic validity | [ZIP](dist/chatgpt/stix-review.zip) |

## Threat Intelligence Engineering

1 skill

| Skill | Purpose | Package |
|---|---|---|
| [Feed Quality](skills/threat-intelligence-engineering/feed-quality/) | Evaluate threat intelligence feed quality through indicator validity, provenance, observation age, duplication, confidence semantics and sharing restrictions. | [ZIP](dist/chatgpt/feed-quality.zip) |

## Vulnerability Management

8 skills

| Skill | Purpose | Package |
|---|---|---|
| [CVE Review](skills/vulnerability-management/cve-review/) | Assess a CVE's applicability and investigation relevance | [ZIP](dist/chatgpt/cve-review.zip) |
| [Exposure Review](skills/vulnerability-management/exposure-review/) | Review whether a vulnerable service is reachable in its actual environment | [ZIP](dist/chatgpt/exposure-review.zip) |
| [Patch Priority](skills/vulnerability-management/patch-priority/) | Prioritize remediation using exploitation evidence and asset context | [ZIP](dist/chatgpt/patch-priority.zip) |
| [Remediation Review](skills/vulnerability-management/remediation-review/) | Verify remediation evidence and detect incomplete fixes | [ZIP](dist/chatgpt/remediation-review.zip) |
| [Analyze port-scan alerts](skills/vulnerability-management/scan-alert/) | Analyze port-scan alerts | [ZIP](dist/chatgpt/scan-alert.zip) |
| [Review vulnerability scan results](skills/vulnerability-management/scan-results/) | Review vulnerability scan results | [ZIP](dist/chatgpt/scan-results.zip) |
| [Plan an authorized scan scope](skills/vulnerability-management/scan-scope/) | Plan an authorized scan scope | [ZIP](dist/chatgpt/scan-scope.zip) |
| [Vulnerability Validation](skills/vulnerability-management/vulnerability-validation/) | Validate scanner findings through version and configuration evidence | [ZIP](dist/chatgpt/vulnerability-validation.zip) |
