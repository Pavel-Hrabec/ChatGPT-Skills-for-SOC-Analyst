# Community Skill Catalog

149 task-specific skills. Each upload contains one self-contained skill. Individual packages can be downloaded from `dist/chatgpt/`.

## Aws

7 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [AWS Access Keys](skills/aws/aws-access-keys/) | Investigate suspicious AWS access-key creation and use | [ZIP](dist/chatgpt/aws-access-keys.zip) | [Prompt](prompts/aws/aws-access-keys.md) |
| [AWS CloudTrail](skills/aws/aws-cloudtrail/) | Investigate CloudTrail visibility changes and suspicious control-plane sequences | [ZIP](dist/chatgpt/aws-cloudtrail.zip) | [Prompt](prompts/aws/aws-cloudtrail.md) |
| [AWS EC2](skills/aws/aws-ec2/) | Investigate suspicious EC2 control-plane and instance activity | [ZIP](dist/chatgpt/aws-ec2.zip) | [Prompt](prompts/aws/aws-ec2.md) |
| [AWS IAM](skills/aws/aws-iam/) | Investigate IAM policy, trust and privilege changes | [ZIP](dist/chatgpt/aws-iam.zip) | [Prompt](prompts/aws/aws-iam.md) |
| [AWS Lambda](skills/aws/aws-lambda/) | Investigate suspicious Lambda code, configuration and invocation activity | [ZIP](dist/chatgpt/aws-lambda.zip) | [Prompt](prompts/aws/aws-lambda.md) |
| [AWS S3](skills/aws/aws-s3/) | Investigate suspicious S3 object access and exposure | [ZIP](dist/chatgpt/aws-s3.zip) | [Prompt](prompts/aws/aws-s3.md) |
| [AWS SSO](skills/aws/aws-sso/) | Investigate AWS federation and IAM Identity Center session activity | [ZIP](dist/chatgpt/aws-sso.zip) | [Prompt](prompts/aws/aws-sso.md) |

## Azure

5 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Azure Key Vault](skills/azure/azure-keyvault/) | Investigate suspicious secret, key or certificate access in Key Vault | [ZIP](dist/chatgpt/azure-keyvault.zip) | [Prompt](prompts/azure/azure-keyvault.md) |
| [Azure Logging](skills/azure/azure-logging/) | Investigate changes affecting Azure resource logging and visibility | [ZIP](dist/chatgpt/azure-logging.zip) | [Prompt](prompts/azure/azure-logging.md) |
| [Azure Roles](skills/azure/azure-roles/) | Investigate Azure role assignments and privilege changes | [ZIP](dist/chatgpt/azure-roles.zip) | [Prompt](prompts/azure/azure-roles.md) |
| [Azure Storage](skills/azure/azure-storage/) | Investigate suspicious Azure Storage access, sharing and token use | [ZIP](dist/chatgpt/azure-storage.zip) | [Prompt](prompts/azure/azure-storage.md) |
| [Azure VM](skills/azure/azure-vm/) | Investigate Azure VM remote execution and control-plane changes | [ZIP](dist/chatgpt/azure-vm.zip) | [Prompt](prompts/azure/azure-vm.md) |

## Containers

5 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Container Escape](skills/containers/container-escape/) | Assess evidence that a container crossed into host resources | [ZIP](dist/chatgpt/container-escape.zip) | [Prompt](prompts/containers/container-escape.md) |
| [Container Images](skills/containers/container-images/) | Investigate suspicious container image provenance and runtime use | [ZIP](dist/chatgpt/container-images.zip) | [Prompt](prompts/containers/container-images.md) |
| [K8s Audit](skills/containers/k8s-audit/) | Reconstruct suspicious Kubernetes API activity from audit events | [ZIP](dist/chatgpt/k8s-audit.zip) | [Prompt](prompts/containers/k8s-audit.md) |
| [K8s RBAC](skills/containers/k8s-rbac/) | Investigate Kubernetes role and binding changes | [ZIP](dist/chatgpt/k8s-rbac.zip) | [Prompt](prompts/containers/k8s-rbac.md) |
| [Pod Exec](skills/containers/pod-exec/) | Investigate interactive execution into Kubernetes containers | [ZIP](dist/chatgpt/pod-exec.zip) | [Prompt](prompts/containers/pod-exec.md) |

## Detection Engineering

16 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Coverage Review](skills/detection-engineering/coverage-review/) | Assess security detection coverage using actual telemetry and validation | [ZIP](dist/chatgpt/coverage-review.zip) | [Prompt](prompts/detection-engineering/coverage-review.md) |
| [Detection Replay](skills/detection-engineering/detection-replay/) | Replay an existing detection against recorded telemetry in a controlled backend and compare expected events, entities and alert groups. | [ZIP](dist/chatgpt/detection-replay.zip) | [Prompt](prompts/detection-engineering/detection-replay.md) |
| [Review detection logic](skills/detection-engineering/detection-review/) | Review detection logic. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/detection-review.zip) | [Prompt](prompts/detection-engineering/detection-review.md) |
| [Duplicate Rules](skills/detection-engineering/duplicate-rules/) | Identify overlapping detections without losing distinct coverage | [ZIP](dist/chatgpt/duplicate-rules.zip) | [Prompt](prompts/detection-engineering/duplicate-rules.md) |
| [Elastic Detection](skills/detection-engineering/elastic-detection/) | Author Elastic Security detections for a specified engine and schema | [ZIP](dist/chatgpt/elastic-detection.zip) | [Prompt](prompts/detection-engineering/elastic-detection.md) |
| [KQL Detection](skills/detection-engineering/kql-detection/) | Build operational KQL detections for Defender XDR or Microsoft Sentinel, including result identifiers, scheduling, entities and backend-aware tests. | [ZIP](dist/chatgpt/kql-detection.zip) | [Prompt](prompts/detection-engineering/kql-detection.md) |
| [Query Performance](skills/detection-engineering/query-performance/) | Improve security query performance while checking result equivalence | [ZIP](dist/chatgpt/query-performance.zip) | [Prompt](prompts/detection-engineering/query-performance.md) |
| [Rule Migration](skills/detection-engineering/rule-migration/) | Translate a detection between platforms while preserving its semantics | [ZIP](dist/chatgpt/rule-migration.zip) | [Prompt](prompts/detection-engineering/rule-migration.md) |
| [Rule Tests](skills/detection-engineering/rule-tests/) | Create meaningful executable or backend-native tests for an existing security detection, with explicit expected matches and negative cases. | [ZIP](dist/chatgpt/rule-tests.zip) | [Prompt](prompts/detection-engineering/rule-tests.md) |
| [Rule Tuning](skills/detection-engineering/rule-tuning/) | Reduce noise in an existing detection using labeled evidence while measuring lost coverage, regression risk and exception scope. | [ZIP](dist/chatgpt/rule-tuning.zip) | [Prompt](prompts/detection-engineering/rule-tuning.md) |
| [Sigma](skills/detection-engineering/sigma/) | Author or convert Sigma detections from documented behavior and supplied telemetry, including backend mappings and validation requirements. | [ZIP](dist/chatgpt/sigma.zip) | [Prompt](prompts/detection-engineering/sigma.md) |
| [Explain Sigma and YARA rules](skills/detection-engineering/sigma-yara/) | Explain Sigma and YARA rules. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/sigma-yara.zip) | [Prompt](prompts/detection-engineering/sigma-yara.md) |
| [SPL Detection](skills/detection-engineering/spl-detection/) | Write Splunk SPL security detections with confirmed sourcetypes or CIM dependencies, operational search settings and controlled validation. | [ZIP](dist/chatgpt/spl-detection.zip) | [Prompt](prompts/detection-engineering/spl-detection.md) |
| [Suricata](skills/detection-engineering/suricata/) | Author Suricata signatures for observable network behavior | [ZIP](dist/chatgpt/suricata.zip) | [Prompt](prompts/detection-engineering/suricata.md) |
| [Threat Coverage](skills/detection-engineering/threat-coverage/) | Assess defensive coverage against a specific reported threat sequence | [ZIP](dist/chatgpt/threat-coverage.zip) | [Prompt](prompts/detection-engineering/threat-coverage.md) |
| [YARA](skills/detection-engineering/yara/) | Author and validate YARA rules for a defined file or memory target | [ZIP](dist/chatgpt/yara.zip) | [Prompt](prompts/detection-engineering/yara.md) |

## Email

1 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Analyze suspicious email](skills/email/email-analysis/) | Analyze suspicious email. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/email-analysis.zip) | [Prompt](prompts/email/email-analysis.md) |

## Endpoint

21 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [BITS Jobs](skills/endpoint/bits-jobs/) | Investigate suspicious Background Intelligent Transfer Service jobs | [ZIP](dist/chatgpt/bits-jobs.zip) | [Prompt](prompts/endpoint/bits-jobs.md) |
| [Browser Theft](skills/endpoint/browser-theft/) | Investigate access to browser credential and session stores | [ZIP](dist/chatgpt/browser-theft.zip) | [Prompt](prompts/endpoint/browser-theft.md) |
| [COM Hijack](skills/endpoint/com-hijack/) | Investigate COM registration changes that may redirect execution | [ZIP](dist/chatgpt/com-hijack.zip) | [Prompt](prompts/endpoint/com-hijack.md) |
| [Defender Tampering](skills/endpoint/defender-tampering/) | Investigate changes that impair Microsoft Defender or its visibility | [ZIP](dist/chatgpt/defender-tampering.zip) | [Prompt](prompts/endpoint/defender-tampering.md) |
| [DLL Loading](skills/endpoint/dll-loading/) | Assess suspicious DLL loading and potential side-loading | [ZIP](dist/chatgpt/dll-loading.zip) | [Prompt](prompts/endpoint/dll-loading.md) |
| [Driver Abuse](skills/endpoint/driver-abuse/) | Assess suspicious kernel driver loading and vulnerable-driver abuse | [ZIP](dist/chatgpt/driver-abuse.zip) | [Prompt](prompts/endpoint/driver-abuse.md) |
| [Local System Discovery](skills/endpoint/local-discovery/) | Analyze endpoint evidence showing commands or processes gathering local identity, system, network, process, service, session, or privilege information. | [ZIP](dist/chatgpt/local-discovery.zip) | [Prompt](prompts/endpoint/local-discovery.md) |
| [LSASS](skills/endpoint/lsass/) | Investigate suspected LSASS memory access and credential dumping | [ZIP](dist/chatgpt/lsass.zip) | [Prompt](prompts/endpoint/lsass.md) |
| [Named Pipes](skills/endpoint/named-pipes/) | Investigate suspicious named-pipe creation and connections | [ZIP](dist/chatgpt/named-pipes.zip) | [Prompt](prompts/endpoint/named-pipes.md) |
| [Inspect Office macro evidence](skills/endpoint/office-macros/) | Inspect Office macro evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/office-macros.zip) | [Prompt](prompts/endpoint/office-macros.md) |
| [Analyze PowerShell evidence](skills/endpoint/powershell/) | Analyze PowerShell evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/powershell.zip) | [Prompt](prompts/endpoint/powershell.md) |
| [Analyze a process tree](skills/endpoint/process-tree/) | Analyze a process tree. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/process-tree.zip) | [Prompt](prompts/endpoint/process-tree.md) |
| [Analyze registry changes](skills/endpoint/registry/) | Analyze registry changes. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/registry.zip) | [Prompt](prompts/endpoint/registry.md) |
| [Remote Thread](skills/endpoint/remote-thread/) | Investigate cross-process thread creation and injection hypotheses | [ZIP](dist/chatgpt/remote-thread.zip) | [Prompt](prompts/endpoint/remote-thread.md) |
| [Decode suspicious script evidence](skills/endpoint/script-decode/) | Decode suspicious script evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/script-decode.zip) | [Prompt](prompts/endpoint/script-decode.md) |
| [Shadow Copies](skills/endpoint/shadow-copy/) | Investigate deletion or disruption of backups and shadow copies | [ZIP](dist/chatgpt/shadow-copy.zip) | [Prompt](prompts/endpoint/shadow-copy.md) |
| [Analyze scheduled tasks and services](skills/endpoint/tasks-services/) | Analyze scheduled tasks and services. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/tasks-services.zip) | [Prompt](prompts/endpoint/tasks-services.md) |
| [Interpret Windows command lines](skills/endpoint/windows-command/) | Interpret Windows command lines. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/windows-command.zip) | [Prompt](prompts/endpoint/windows-command.md) |
| [Investigate Windows event records](skills/endpoint/windows-events/) | Investigate Windows event records. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/windows-events.zip) | [Prompt](prompts/endpoint/windows-events.md) |
| [WMI Execution](skills/endpoint/wmi-execution/) | Investigate remote or local process execution through WMI | [ZIP](dist/chatgpt/wmi-execution.zip) | [Prompt](prompts/endpoint/wmi-execution.md) |
| [WMI Persistence](skills/endpoint/wmi-persistence/) | Investigate permanent WMI event subscriptions and their execution evidence | [ZIP](dist/chatgpt/wmi-persistence.zip) | [Prompt](prompts/endpoint/wmi-persistence.md) |

## Gcp

5 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [GCP Audit](skills/gcp/gcp-audit/) | Investigate Google Cloud audit sequences and logging gaps | [ZIP](dist/chatgpt/gcp-audit.zip) | [Prompt](prompts/gcp/gcp-audit.md) |
| [GCP Compute](skills/gcp/gcp-compute/) | Investigate suspicious Compute Engine instance and access changes | [ZIP](dist/chatgpt/gcp-compute.zip) | [Prompt](prompts/gcp/gcp-compute.md) |
| [GCP IAM](skills/gcp/gcp-iam/) | Investigate Google Cloud IAM policy and privilege changes | [ZIP](dist/chatgpt/gcp-iam.zip) | [Prompt](prompts/gcp/gcp-iam.md) |
| [GCP Service Accounts](skills/gcp/gcp-service-accounts/) | Investigate service-account keys, impersonation and workload identity use | [ZIP](dist/chatgpt/gcp-service-accounts.zip) | [Prompt](prompts/gcp/gcp-service-accounts.md) |
| [GCP Storage](skills/gcp/gcp-storage/) | Investigate suspicious Cloud Storage access and exposure | [ZIP](dist/chatgpt/gcp-storage.zip) | [Prompt](prompts/gcp/gcp-storage.md) |

## Identity

15 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Review Active Directory changes](skills/identity/ad-changes/) | Review Active Directory changes. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/ad-changes.zip) | [Prompt](prompts/identity/ad-changes.md) |
| [Active Directory Discovery](skills/identity/ad-discovery/) | Analyze directory enumeration evidence from LDAP, native Windows utilities, and AD assessment tools, including queried objects, scope, identity, and surrounding activity. | [ZIP](dist/chatgpt/ad-discovery.zip) | [Prompt](prompts/identity/ad-discovery.md) |
| [AD CS](skills/identity/adcs/) | Investigate suspicious Active Directory certificate issuance and template changes | [ZIP](dist/chatgpt/adcs.zip) | [Prompt](prompts/identity/adcs.md) |
| [AS-REP Roasting](skills/identity/asrep-roasting/) | Investigate authentication requests involving accounts without Kerberos preauthentication | [ZIP](dist/chatgpt/asrep-roasting.zip) | [Prompt](prompts/identity/asrep-roasting.md) |
| [DCShadow](skills/identity/dcshadow/) | Investigate suspicious directory replication registration and object changes | [ZIP](dist/chatgpt/dcshadow.zip) | [Prompt](prompts/identity/dcshadow.md) |
| [DCSync](skills/identity/dcsync/) | Investigate directory replication requests from unexpected principals or hosts | [ZIP](dist/chatgpt/dcsync.zip) | [Prompt](prompts/identity/dcsync.md) |
| [Delegation Abuse](skills/identity/delegation-abuse/) | Investigate changes or use of Kerberos delegation relationships | [ZIP](dist/chatgpt/delegation-abuse.zip) | [Prompt](prompts/identity/delegation-abuse.md) |
| [Golden Ticket](skills/identity/golden-ticket/) | Assess forged Kerberos ticket hypotheses using corroborated authentication evidence | [ZIP](dist/chatgpt/golden-ticket.zip) | [Prompt](prompts/identity/golden-ticket.md) |
| [GPO Abuse](skills/identity/gpo-abuse/) | Investigate unauthorized Group Policy changes and resulting endpoint behavior | [ZIP](dist/chatgpt/gpo-abuse.zip) | [Prompt](prompts/identity/gpo-abuse.md) |
| [Kerberoasting](skills/identity/kerberoasting/) | Investigate suspicious Kerberos service-ticket requests | [ZIP](dist/chatgpt/kerberoasting.zip) | [Prompt](prompts/identity/kerberoasting.md) |
| [Investigate Kerberos events](skills/identity/kerberos/) | Investigate Kerberos events. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/kerberos.zip) | [Prompt](prompts/identity/kerberos.md) |
| [NTLM Relay](skills/identity/ntlm-relay/) | Investigate suspected relayed NTLM authentication | [ZIP](dist/chatgpt/ntlm-relay.zip) | [Prompt](prompts/identity/ntlm-relay.md) |
| [Password Spray](skills/identity/password-spray/) | Investigate low-frequency authentication attempts spread across accounts | [ZIP](dist/chatgpt/password-spray.zip) | [Prompt](prompts/identity/password-spray.md) |
| [Review privileged access](skills/identity/privileged-access/) | Review privileged access. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/privileged-access.zip) | [Prompt](prompts/identity/privileged-access.md) |
| [Investigate sign-in anomalies](skills/identity/sign-in/) | Investigate sign-in anomalies. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/sign-in.zip) | [Prompt](prompts/identity/sign-in.md) |

## Incident Response

8 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Containment Plan](skills/incident-response/containment-plan/) | Develop a scoped containment plan from confirmed incident evidence | [ZIP](dist/chatgpt/containment-plan.zip) | [Prompt](prompts/incident-response/containment-plan.md) |
| [Write an incident escalation](skills/incident-response/escalation/) | Write an incident escalation. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/escalation.zip) | [Prompt](prompts/incident-response/escalation.md) |
| [Evidence Preservation](skills/incident-response/evidence-preservation/) | Plan and document defensible preservation of security evidence | [ZIP](dist/chatgpt/evidence-preservation.zip) | [Prompt](prompts/incident-response/evidence-preservation.md) |
| [Draft an incident report](skills/incident-response/incident-report/) | Draft an incident report. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/incident-report.zip) | [Prompt](prompts/incident-response/incident-report.md) |
| [Expand incident scope safely](skills/incident-response/incident-scope/) | Expand incident scope safely. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/incident-scope.zip) | [Prompt](prompts/incident-response/incident-scope.md) |
| [Recovery Review](skills/incident-response/recovery-review/) | Review whether recovery evidence supports safe restoration and monitoring | [ZIP](dist/chatgpt/recovery-review.zip) | [Prompt](prompts/incident-response/recovery-review.md) |
| [Build an incident timeline](skills/incident-response/timeline/) | Build an incident timeline. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/timeline.zip) | [Prompt](prompts/incident-response/timeline.md) |
| [Interpret an XDR alert](skills/incident-response/xdr-alert/) | Interpret an XDR alert. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/xdr-alert.zip) | [Prompt](prompts/incident-response/xdr-alert.md) |

## Linux

8 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Cron](skills/linux/cron/) | Investigate suspicious cron-based execution and persistence | [ZIP](dist/chatgpt/cron.zip) | [Prompt](prompts/linux/cron.md) |
| [LD Preload](skills/linux/ld-preload/) | Investigate dynamic-loader configuration that may inject shared libraries | [ZIP](dist/chatgpt/ld-preload.zip) | [Prompt](prompts/linux/ld-preload.md) |
| [Linux Audit](skills/linux/linux-audit/) | Reconstruct security-relevant activity from Linux audit records | [ZIP](dist/chatgpt/linux-audit.zip) | [Prompt](prompts/linux/linux-audit.md) |
| [Linux Log Tampering](skills/linux/linux-log-tampering/) | Investigate disruption or manipulation of Linux security logging | [ZIP](dist/chatgpt/linux-log-tampering.zip) | [Prompt](prompts/linux/linux-log-tampering.md) |
| [SSH](skills/linux/ssh/) | Investigate suspicious SSH authentication and session activity | [ZIP](dist/chatgpt/ssh.zip) | [Prompt](prompts/linux/ssh.md) |
| [SSH Keys](skills/linux/ssh-keys/) | Investigate unauthorized SSH key and trust configuration changes | [ZIP](dist/chatgpt/ssh-keys.zip) | [Prompt](prompts/linux/ssh-keys.md) |
| [Sudo](skills/linux/sudo/) | Investigate privilege changes through sudo | [ZIP](dist/chatgpt/sudo.zip) | [Prompt](prompts/linux/sudo.md) |
| [Systemd](skills/linux/systemd/) | Investigate suspicious systemd units, timers and drop-ins | [ZIP](dist/chatgpt/systemd.zip) | [Prompt](prompts/linux/systemd.md) |

## Malware Forensics

7 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Archive Analysis](skills/malware-forensics/archive-analysis/) | Assess archive contents and delivery risks without executing members | [ZIP](dist/chatgpt/archive-analysis.zip) | [Prompt](prompts/malware-forensics/archive-analysis.md) |
| [Browser Artifacts](skills/malware-forensics/browser-artifacts/) | Investigate browser history, downloads and profile artifacts | [ZIP](dist/chatgpt/browser-artifacts.zip) | [Prompt](prompts/malware-forensics/browser-artifacts.md) |
| [Disk Artifacts](skills/malware-forensics/disk-artifacts/) | Correlate filesystem forensic artifacts into an activity hypothesis | [ZIP](dist/chatgpt/disk-artifacts.zip) | [Prompt](prompts/malware-forensics/disk-artifacts.md) |
| [LNK Analysis](skills/malware-forensics/lnk-analysis/) | Analyze Windows shortcut artifacts without opening their targets | [ZIP](dist/chatgpt/lnk-analysis.zip) | [Prompt](prompts/malware-forensics/lnk-analysis.md) |
| [Memory Analysis](skills/malware-forensics/memory-analysis/) | Interpret memory forensic output for suspicious processes and artifacts | [ZIP](dist/chatgpt/memory-analysis.zip) | [Prompt](prompts/malware-forensics/memory-analysis.md) |
| [PE Analysis](skills/malware-forensics/pe-analysis/) | Perform static triage of Windows PE files or supplied parser output | [ZIP](dist/chatgpt/pe-analysis.zip) | [Prompt](prompts/malware-forensics/pe-analysis.md) |
| [Ransomware](skills/malware-forensics/ransomware/) | Investigate ransomware behavior and impact from correlated evidence | [ZIP](dist/chatgpt/ransomware.zip) | [Prompt](prompts/malware-forensics/ransomware.md) |

## Microsoft 365

9 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Conditional Access](skills/microsoft-365/conditional-access/) | Investigate Conditional Access changes and unexpected access outcomes | [ZIP](dist/chatgpt/conditional-access.zip) | [Prompt](prompts/microsoft-365/conditional-access.md) |
| [Entra Apps](skills/microsoft-365/entra-apps/) | Investigate application and service-principal credential changes | [ZIP](dist/chatgpt/entra-apps.zip) | [Prompt](prompts/microsoft-365/entra-apps.md) |
| [Inbox Rules](skills/microsoft-365/inbox-rules/) | Investigate mailbox rules that conceal or redirect messages | [ZIP](dist/chatgpt/inbox-rules.zip) | [Prompt](prompts/microsoft-365/inbox-rules.md) |
| [Mailbox Access](skills/microsoft-365/mailbox-access/) | Investigate anomalous mailbox content access | [ZIP](dist/chatgpt/mailbox-access.zip) | [Prompt](prompts/microsoft-365/mailbox-access.md) |
| [MFA Fatigue](skills/microsoft-365/mfa-fatigue/) | Investigate repeated MFA prompts and a possibly coerced approval | [ZIP](dist/chatgpt/mfa-fatigue.zip) | [Prompt](prompts/microsoft-365/mfa-fatigue.md) |
| [OAuth Grants](skills/microsoft-365/oauth-grants/) | Investigate suspicious application consent and delegated access | [ZIP](dist/chatgpt/oauth-grants.zip) | [Prompt](prompts/microsoft-365/oauth-grants.md) |
| [SharePoint Access](skills/microsoft-365/sharepoint-access/) | Investigate suspicious SharePoint and OneDrive access or sharing | [ZIP](dist/chatgpt/sharepoint-access.zip) | [Prompt](prompts/microsoft-365/sharepoint-access.md) |
| [Teams Abuse](skills/microsoft-365/teams-abuse/) | Investigate suspicious Teams collaboration or application activity | [ZIP](dist/chatgpt/teams-abuse.zip) | [Prompt](prompts/microsoft-365/teams-abuse.md) |
| [Token Theft](skills/microsoft-365/token-theft/) | Investigate suspicious reuse of cloud sessions or tokens | [ZIP](dist/chatgpt/token-theft.zip) | [Prompt](prompts/microsoft-365/token-theft.md) |

## Network

13 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Beaconing](skills/network/beaconing/) | Investigate periodic outbound communication and command-and-control hypotheses | [ZIP](dist/chatgpt/beaconing.zip) | [Prompt](prompts/network/beaconing.md) |
| [Data Exfiltration](skills/network/data-exfiltration/) | Investigate suspected outbound data transfer | [ZIP](dist/chatgpt/data-exfiltration.zip) | [Prompt](prompts/network/data-exfiltration.md) |
| [Analyze DNS events](skills/network/dns/) | Analyze DNS events. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/dns.zip) | [Prompt](prompts/network/dns.md) |
| [DNS Tunneling](skills/network/dns-tunneling/) | Investigate DNS traffic that may carry a covert channel | [ZIP](dist/chatgpt/dns-tunneling.zip) | [Prompt](prompts/network/dns-tunneling.md) |
| [Network Recon and SMB Discovery](skills/network/network-discovery/) | Analyze authorized scan scope and results, scanning alerts, remote host and service discovery, and SMB share enumeration from supplied evidence. | [ZIP](dist/chatgpt/network-discovery.zip) | [Prompt](prompts/network/network-discovery.md) |
| [Analyze network flows](skills/network/network-flow/) | Analyze network flows. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/network-flow.zip) | [Prompt](prompts/network/network-flow.md) |
| [Interpret packet-analysis summaries](skills/network/pcap-summary/) | Interpret packet-analysis summaries. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/pcap-summary.zip) | [Prompt](prompts/network/pcap-summary.md) |
| [Review proxy and URL events](skills/network/proxy-url/) | Review proxy and URL events. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/proxy-url.zip) | [Prompt](prompts/network/proxy-url.md) |
| [RDP Lateral](skills/network/rdp-lateral/) | Investigate suspicious Remote Desktop sessions | [ZIP](dist/chatgpt/rdp-lateral.zip) | [Prompt](prompts/network/rdp-lateral.md) |
| [SMB Lateral](skills/network/smb-lateral/) | Investigate suspicious SMB-based movement between hosts | [ZIP](dist/chatgpt/smb-lateral.zip) | [Prompt](prompts/network/smb-lateral.md) |
| [TLS Analysis](skills/network/tls-analysis/) | Assess suspicious TLS metadata and certificate relationships | [ZIP](dist/chatgpt/tls-analysis.zip) | [Prompt](prompts/network/tls-analysis.md) |
| [Web Attacks](skills/network/web-attacks/) | Investigate suspected exploitation attempts in HTTP or WAF evidence | [ZIP](dist/chatgpt/web-attacks.zip) | [Prompt](prompts/network/web-attacks.md) |
| [WinRM Lateral](skills/network/winrm-lateral/) | Investigate remote management execution through WinRM | [ZIP](dist/chatgpt/winrm-lateral.zip) | [Prompt](prompts/network/winrm-lateral.md) |

## Saas Development

4 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [CI/CD Abuse](skills/saas-development/cicd-abuse/) | Investigate suspicious workflow modifications and build execution | [ZIP](dist/chatgpt/cicd-abuse.zip) | [Prompt](prompts/saas-development/cicd-abuse.md) |
| [GitHub Audit](skills/saas-development/github-audit/) | Investigate suspicious GitHub organization and repository activity | [ZIP](dist/chatgpt/github-audit.zip) | [Prompt](prompts/saas-development/github-audit.md) |
| [Prompt Injection](skills/saas-development/prompt-injection/) | Investigate untrusted content that attempts to redirect an AI security workflow | [ZIP](dist/chatgpt/prompt-injection.zip) | [Prompt](prompts/saas-development/prompt-injection.md) |
| [Secret Exposure](skills/saas-development/secret-exposure/) | Assess exposed credentials without disclosing or using them | [ZIP](dist/chatgpt/secret-exposure.zip) | [Prompt](prompts/saas-development/secret-exposure.md) |

## Security Automation

4 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Alert Routing](skills/security-automation/alert-routing/) | Design routing and deduplication for security alerts | [ZIP](dist/chatgpt/alert-routing.zip) | [Prompt](prompts/security-automation/alert-routing.md) |
| [API Integration](skills/security-automation/api-integration/) | Implement an authenticated security API integration with bounded operations | [ZIP](dist/chatgpt/api-integration.zip) | [Prompt](prompts/security-automation/api-integration.md) |
| [Enrichment Pipeline](skills/security-automation/enrichment-pipeline/) | Build a bounded intelligence enrichment workflow with provenance | [ZIP](dist/chatgpt/enrichment-pipeline.zip) | [Prompt](prompts/security-automation/enrichment-pipeline.md) |
| [SOAR Playbook](skills/security-automation/soar-playbook/) | Design a reviewable automation playbook for a defined security workflow | [ZIP](dist/chatgpt/soar-playbook.zip) | [Prompt](prompts/security-automation/soar-playbook.md) |

## Siem

3 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Draft and explain ES|QL](skills/siem/esql/) | Draft and explain ES|QL. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/esql.zip) | [Prompt](prompts/siem/esql.md) |
| [Draft and explain KQL](skills/siem/kql/) | Draft and explain KQL. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/kql.zip) | [Prompt](prompts/siem/kql.md) |
| [Interpret SIEM query results](skills/siem/query-results/) | Interpret SIEM query results. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/query-results.zip) | [Prompt](prompts/siem/query-results.md) |

## Telemetry Engineering

3 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Field Mapping](skills/telemetry-engineering/field-mapping/) | Map vendor security telemetry to a specified ECS, OCSF or local schema using field semantics, types, transformations and explicit unmapped values. | [ZIP](dist/chatgpt/field-mapping.zip) | [Prompt](prompts/telemetry-engineering/field-mapping.md) |
| [Log Parser](skills/telemetry-engineering/log-parser/) | Build or repair parsers for supplied security logs, preserving raw evidence and handling timestamps, framing, escapes and malformed records. | [ZIP](dist/chatgpt/log-parser.zip) | [Prompt](prompts/telemetry-engineering/log-parser.md) |
| [Log Quality](skills/telemetry-engineering/log-quality/) | Assess security log completeness, parsing, timestamps, duplicate candidates and ingestion delay from supplied records or bounded authorized queries. | [ZIP](dist/chatgpt/log-quality.zip) | [Prompt](prompts/telemetry-engineering/log-quality.md) |

## Threat Intelligence

9 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Campaign Review](skills/threat-intelligence/campaign-review/) | Evaluate whether observed incident evidence matches a reported campaign | [ZIP](dist/chatgpt/campaign-review.zip) | [Prompt](prompts/threat-intelligence/campaign-review.md) |
| [Review file-hash evidence](skills/threat-intelligence/hash-analysis/) | Review file-hash evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/hash-analysis.zip) | [Prompt](prompts/threat-intelligence/hash-analysis.md) |
| [Indicator Expiry](skills/threat-intelligence/indicator-expiry/) | Propose evidence-based indicator retention and review policies | [ZIP](dist/chatgpt/indicator-expiry.zip) | [Prompt](prompts/threat-intelligence/indicator-expiry.md) |
| [Infrastructure Links](skills/threat-intelligence/infrastructure-links/) | Assess relationships among suspicious domains, IPs and certificates | [ZIP](dist/chatgpt/infrastructure-links.zip) | [Prompt](prompts/threat-intelligence/infrastructure-links.md) |
| [Intel Dedup](skills/threat-intelligence/intel-dedup/) | Deduplicate intelligence while preserving distinct observations and source lineage | [ZIP](dist/chatgpt/intel-dedup.zip) | [Prompt](prompts/threat-intelligence/intel-dedup.md) |
| [Intel to Hunt](skills/threat-intelligence/intel-to-hunt/) | Translate a threat report into testable defensive hunt hypotheses | [ZIP](dist/chatgpt/intel-to-hunt.zip) | [Prompt](prompts/threat-intelligence/intel-to-hunt.md) |
| [Analyze indicators of compromise](skills/threat-intelligence/ioc-analysis/) | Analyze indicators of compromise. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/ioc-analysis.zip) | [Prompt](prompts/threat-intelligence/ioc-analysis.md) |
| [Interpret malware sandbox reports](skills/threat-intelligence/sandbox-report/) | Interpret malware sandbox reports. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool. | [ZIP](dist/chatgpt/sandbox-report.zip) | [Prompt](prompts/threat-intelligence/sandbox-report.md) |
| [STIX Review](skills/threat-intelligence/stix-review/) | Review STIX intelligence objects and relationships for semantic validity | [ZIP](dist/chatgpt/stix-review.zip) | [Prompt](prompts/threat-intelligence/stix-review.md) |

## Threat Intelligence Engineering

1 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [Feed Quality](skills/threat-intelligence-engineering/feed-quality/) | Evaluate threat intelligence feed quality through indicator validity, provenance, observation age, duplication, confidence semantics and sharing restrictions. | [ZIP](dist/chatgpt/feed-quality.zip) | [Prompt](prompts/threat-intelligence-engineering/feed-quality.md) |

## Vulnerability Management

5 skills

| Skill | Purpose | Package | Copyable prompt |
|---|---|---|---|
| [CVE Review](skills/vulnerability-management/cve-review/) | Assess a CVE's applicability and investigation relevance | [ZIP](dist/chatgpt/cve-review.zip) | [Prompt](prompts/vulnerability-management/cve-review.md) |
| [Exposure Review](skills/vulnerability-management/exposure-review/) | Review whether a vulnerable service is reachable in its actual environment | [ZIP](dist/chatgpt/exposure-review.zip) | [Prompt](prompts/vulnerability-management/exposure-review.md) |
| [Patch Priority](skills/vulnerability-management/patch-priority/) | Prioritize remediation using exploitation evidence and asset context | [ZIP](dist/chatgpt/patch-priority.zip) | [Prompt](prompts/vulnerability-management/patch-priority.md) |
| [Remediation Review](skills/vulnerability-management/remediation-review/) | Verify remediation evidence and detect incomplete fixes | [ZIP](dist/chatgpt/remediation-review.zip) | [Prompt](prompts/vulnerability-management/remediation-review.md) |
| [Vulnerability Validation](skills/vulnerability-management/vulnerability-validation/) | Validate scanner findings through version and configuration evidence | [ZIP](dist/chatgpt/vulnerability-validation.zip) | [Prompt](prompts/vulnerability-management/vulnerability-validation.md) |

