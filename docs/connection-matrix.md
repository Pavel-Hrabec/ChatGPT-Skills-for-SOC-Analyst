# Connection matrix

This matrix covers the cloud, identity, engineering, automation and intelligence skills with task-specific read-only evidence sources. A skill ZIP cannot authenticate a service; the named connector or API must be configured in the host. Public enrichment uses the optional [SOC Intel MCP](../integrations/soc-intel-mcp/README.md) only when an indicator can be disclosed.

| Skill | Primary evidence connection | Optional public lookup |
|---|---|---|
| [AWS Access Keys](../skills/aws/aws-access-keys/SKILL.md) | AWS CloudTrail and IAM | none by default |
| [AWS CloudTrail](../skills/aws/aws-cloudtrail/SKILL.md) | AWS CloudTrail | none by default |
| [AWS EC2](../skills/aws/aws-ec2/SKILL.md) | AWS CloudTrail and EC2 | none by default |
| [AWS IAM](../skills/aws/aws-iam/SKILL.md) | AWS CloudTrail and IAM | none by default |
| [AWS Lambda](../skills/aws/aws-lambda/SKILL.md) | AWS CloudTrail, Lambda and CloudWatch Logs | none by default |
| [AWS S3](../skills/aws/aws-s3/SKILL.md) | CloudTrail S3 data events and S3 metadata | none by default |
| [AWS SSO](../skills/aws/aws-sso/SKILL.md) | CloudTrail and IAM Identity Center | none by default |
| [Azure Key Vault](../skills/azure/azure-keyvault/SKILL.md) | Azure Monitor Key Vault diagnostic logs and ARM metadata | none by default |
| [Azure Logging](../skills/azure/azure-logging/SKILL.md) | Azure Activity Log and ARM diagnostic settings | none by default |
| [Azure Roles](../skills/azure/azure-roles/SKILL.md) | Azure Activity Log and ARM authorization | none by default |
| [Azure Storage](../skills/azure/azure-storage/SKILL.md) | Azure Storage diagnostic logs and ARM metadata | none by default |
| [Azure VM](../skills/azure/azure-vm/SKILL.md) | Azure Activity Log and Compute resource metadata | none by default |
| [Container Escape](../skills/containers/container-escape/SKILL.md) | EDR/runtime events and Kubernetes audit logs | none by default |
| [Container Images](../skills/containers/container-images/SKILL.md) | Container registry metadata, image-signature service and runtime inventory | hash |
| [K8s Audit](../skills/containers/k8s-audit/SKILL.md) | Kubernetes API audit sink or SIEM | none by default |
| [K8s RBAC](../skills/containers/k8s-rbac/SKILL.md) | Kubernetes API audit and RBAC read API | none by default |
| [Pod Exec](../skills/containers/pod-exec/SKILL.md) | Kubernetes API audit and runtime/terminal logs | none by default |
| [Coverage Review](../skills/detection-engineering/coverage-review/SKILL.md) | SIEM rule inventory and telemetry catalog | none by default |
| [Duplicate Rules](../skills/detection-engineering/duplicate-rules/SKILL.md) | Detection repository and SIEM rule inventory | none by default |
| [Elastic Detection](../skills/detection-engineering/elastic-detection/SKILL.md) | Elastic Security and Elasticsearch read APIs | none by default |
| [Query Performance](../skills/detection-engineering/query-performance/SKILL.md) | Target SIEM query profiler and sampled results | none by default |
| [Rule Migration](../skills/detection-engineering/rule-migration/SKILL.md) | Source/target detection repositories and schemas | none by default |
| [Suricata](../skills/detection-engineering/suricata/SKILL.md) | Suricata rule repository and packet/alert evidence | none by default |
| [Threat Coverage](../skills/detection-engineering/threat-coverage/SKILL.md) | Primary threat report, ATT&CK mapping and SIEM coverage inventory | cve |
| [YARA](../skills/detection-engineering/yara/SKILL.md) | Static sample metadata and YARA rule repository | hash |
| [BITS Jobs](../skills/endpoint/bits-jobs/SKILL.md) | Windows BITS operational logs and EDR process/network events | network |
| [Browser Theft](../skills/endpoint/browser-theft/SKILL.md) | EDR file-access and process telemetry | none by default |
| [COM Hijack](../skills/endpoint/com-hijack/SKILL.md) | Sysmon/EDR registry and image-load telemetry | none by default |
| [Defender Tampering](../skills/endpoint/defender-tampering/SKILL.md) | Microsoft Defender operational events and configuration read API | none by default |
| [DLL Loading](../skills/endpoint/dll-loading/SKILL.md) | EDR or Sysmon image-load events | hash |
| [Driver Abuse](../skills/endpoint/driver-abuse/SKILL.md) | Windows Code Integrity, driver-load and EDR events | hash, cve |
| [LSASS](../skills/endpoint/lsass/SKILL.md) | Sysmon Event 10/EDR credential-access telemetry | none by default |
| [Named Pipes](../skills/endpoint/named-pipes/SKILL.md) | Sysmon Event 17/18 and EDR process telemetry | none by default |
| [Remote Thread](../skills/endpoint/remote-thread/SKILL.md) | Sysmon Event 8/EDR injection telemetry | none by default |
| [Shadow Copies](../skills/endpoint/shadow-copy/SKILL.md) | Windows VSS, System and EDR command telemetry | none by default |
| [WMI Execution](../skills/endpoint/wmi-execution/SKILL.md) | WMI-Activity operational logs and EDR process trees | none by default |
| [WMI Persistence](../skills/endpoint/wmi-persistence/SKILL.md) | WMI-Activity logs and read-only WMI repository inventory | none by default |
| [GCP Audit](../skills/gcp/gcp-audit/SKILL.md) | Google Cloud Logging entries.list and logging settings read APIs | none by default |
| [GCP Compute](../skills/gcp/gcp-compute/SKILL.md) | Cloud Logging audit entries and Compute Engine read APIs | none by default |
| [GCP IAM](../skills/gcp/gcp-iam/SKILL.md) | Cloud Logging audit entries and IAM/Cloud Asset Inventory read APIs | none by default |
| [GCP Service Accounts](../skills/gcp/gcp-service-accounts/SKILL.md) | Cloud Logging audit entries and IAM service-account metadata | none by default |
| [GCP Storage](../skills/gcp/gcp-storage/SKILL.md) | Cloud Logging Storage Data Access and bucket metadata | none by default |
| [AD CS](../skills/identity/adcs/SKILL.md) | AD CS CA logs and directory template metadata | none by default |
| [AS-REP Roasting](../skills/identity/asrep-roasting/SKILL.md) | Domain Controller Security events and directory read API | none by default |
| [DCShadow](../skills/identity/dcshadow/SKILL.md) | Directory replication/configuration events and DC inventory | none by default |
| [DCSync](../skills/identity/dcsync/SKILL.md) | DC Security 4662 and replication telemetry | none by default |
| [Delegation Abuse](../skills/identity/delegation-abuse/SKILL.md) | Directory change events and AD attribute read API | none by default |
| [Golden Ticket](../skills/identity/golden-ticket/SKILL.md) | DC Kerberos events and endpoint logon telemetry | none by default |
| [GPO Abuse](../skills/identity/gpo-abuse/SKILL.md) | Directory change events and SYSVOL file telemetry | none by default |
| [Kerberoasting](../skills/identity/kerberoasting/SKILL.md) | DC Security 4769 and directory SPN inventory | none by default |
| [NTLM Relay](../skills/identity/ntlm-relay/SKILL.md) | Authentication, SMB/LDAP and network sensor logs | none by default |
| [Password Spray](../skills/identity/password-spray/SKILL.md) | Identity provider/Domain Controller sign-in logs | none by default |
| [Containment Plan](../skills/incident-response/containment-plan/SKILL.md) | Case record, XDR entity inventory and change management | none by default |
| [Evidence Preservation](../skills/incident-response/evidence-preservation/SKILL.md) | Case management and evidence store metadata | none by default |
| [Recovery Review](../skills/incident-response/recovery-review/SKILL.md) | EDR, identity, backup and change-management records | none by default |
| [Cron](../skills/linux/cron/SKILL.md) | Linux auditd/journald and read-only crontab inventory | none by default |
| [LD Preload](../skills/linux/ld-preload/SKILL.md) | Linux auditd/journald and loader config | hash |
| [Linux Audit](../skills/linux/linux-audit/SKILL.md) | auditd records and journald | none by default |
| [Linux Log Tampering](../skills/linux/linux-log-tampering/SKILL.md) | journald/auditd status and independent collector | none by default |
| [SSH](../skills/linux/ssh/SKILL.md) | sshd/journald authentication and session logs | none by default |
| [SSH Keys](../skills/linux/ssh-keys/SKILL.md) | auditd file-change events and authorized_keys metadata | none by default |
| [Sudo](../skills/linux/sudo/SKILL.md) | sudo/journald/auditd records and sudoers metadata | none by default |
| [Systemd](../skills/linux/systemd/SKILL.md) | systemd journal and read-only unit inventory | none by default |
| [Archive Analysis](../skills/malware-forensics/archive-analysis/SKILL.md) | Offline archive listing and static file metadata | hash |
| [Browser Artifacts](../skills/malware-forensics/browser-artifacts/SKILL.md) | Forensic browser history/download/profile export | network |
| [Disk Artifacts](../skills/malware-forensics/disk-artifacts/SKILL.md) | Forensic disk image or exported NTFS artifacts | none by default |
| [LNK Analysis](../skills/malware-forensics/lnk-analysis/SKILL.md) | Offline LNK parser output and file metadata | hash |
| [Memory Analysis](../skills/malware-forensics/memory-analysis/SKILL.md) | Preserved memory image parser output | hash |
| [PE Analysis](../skills/malware-forensics/pe-analysis/SKILL.md) | Offline PE parser and hash metadata | hash |
| [Ransomware](../skills/malware-forensics/ransomware/SKILL.md) | EDR, backup, file-change and case evidence | hash |
| [Conditional Access](../skills/microsoft-365/conditional-access/SKILL.md) | Microsoft Graph Entra auditLogs and signIns | none by default |
| [Entra Apps](../skills/microsoft-365/entra-apps/SKILL.md) | Microsoft Graph directoryAudits and application metadata | none by default |
| [Inbox Rules](../skills/microsoft-365/inbox-rules/SKILL.md) | Exchange/Purview audit and mailbox rule metadata | none by default |
| [Mailbox Access](../skills/microsoft-365/mailbox-access/SKILL.md) | Purview Unified Audit and Exchange mailbox audit | none by default |
| [MFA Fatigue](../skills/microsoft-365/mfa-fatigue/SKILL.md) | Microsoft Graph signIns and authentication-method audit | none by default |
| [OAuth Grants](../skills/microsoft-365/oauth-grants/SKILL.md) | Microsoft Graph directoryAudits and OAuth grant metadata | none by default |
| [SharePoint Access](../skills/microsoft-365/sharepoint-access/SKILL.md) | Purview audit, SharePoint/OneDrive sharing metadata | none by default |
| [Teams Abuse](../skills/microsoft-365/teams-abuse/SKILL.md) | Microsoft Teams audit connector and Purview audit | none by default |
| [Token Theft](../skills/microsoft-365/token-theft/SKILL.md) | Microsoft Graph signIns, directoryAudits and token/session logs | none by default |
| [Beaconing](../skills/network/beaconing/SKILL.md) | Proxy, DNS, Zeek and EDR network events | network |
| [Data Exfiltration](../skills/network/data-exfiltration/SKILL.md) | Proxy, NetFlow, DLP and cloud egress records | network |
| [DNS Tunneling](../skills/network/dns-tunneling/SKILL.md) | DNS resolver/Zeek logs | network |
| [RDP Lateral](../skills/network/rdp-lateral/SKILL.md) | Windows logon, TerminalServices and EDR events | none by default |
| [SMB Lateral](../skills/network/smb-lateral/SKILL.md) | Windows logon, SMB share access and EDR events | none by default |
| [TLS Analysis](../skills/network/tls-analysis/SKILL.md) | Zeek TLS/JA4, proxy and certificate metadata | network |
| [Web Attacks](../skills/network/web-attacks/SKILL.md) | WAF, reverse-proxy and application logs | network, cve |
| [WinRM Lateral](../skills/network/winrm-lateral/SKILL.md) | Windows PowerShell/WinRM and EDR process events | none by default |
| [CI/CD Abuse](../skills/saas-development/cicd-abuse/SKILL.md) | CI platform audit and workflow-run metadata | none by default |
| [GitHub Audit](../skills/saas-development/github-audit/SKILL.md) | GitHub organization audit log and repository REST read API | none by default |
| [Prompt Injection](../skills/saas-development/prompt-injection/SKILL.md) | Agent trace, retrieved document and tool-call logs | none by default |
| [Secret Exposure](../skills/saas-development/secret-exposure/SKILL.md) | Secret-scanning alert metadata and version-control history | none by default |
| [Alert Routing](../skills/security-automation/alert-routing/SKILL.md) | SIEM alert schema and case-management read APIs | none by default |
| [API Integration](../skills/security-automation/api-integration/SKILL.md) | Chosen vendor's official read API and auth metadata | none by default |
| [Enrichment Pipeline](../skills/security-automation/enrichment-pipeline/SKILL.md) | SOC Intel MCP or approved TI APIs | typed IOC/CVE tools |
| [SOAR Playbook](../skills/security-automation/soar-playbook/SKILL.md) | SOAR case connector and target-platform read APIs | none by default |
| [Campaign Review](../skills/threat-intelligence/campaign-review/SKILL.md) | Primary campaign report and local SIEM/EDR | network, passive DNS |
| [Indicator Expiry](../skills/threat-intelligence/indicator-expiry/SKILL.md) | Original provider reports and IOC inventory | network, passive DNS |
| [Infrastructure Links](../skills/threat-intelligence/infrastructure-links/SKILL.md) | Passive DNS, CT logs and existing TI reports | network, passive DNS |
| [Intel Dedup](../skills/threat-intelligence/intel-dedup/SKILL.md) | TI feed records and STIX bundle exports | network |
| [Intel to Hunt](../skills/threat-intelligence/intel-to-hunt/SKILL.md) | Primary threat report and local SIEM schema | network |
| [STIX Review](../skills/threat-intelligence/stix-review/SKILL.md) | STIX bundle and TAXII collection metadata | none by default |
| [CVE Review](../skills/vulnerability-management/cve-review/SKILL.md) | Vendor advisory, scanner inventory and SOC Intel MCP | cve |
| [Exposure Review](../skills/vulnerability-management/exposure-review/SKILL.md) | Asset inventory, scanner results and network control metadata | cve |
| [Patch Priority](../skills/vulnerability-management/patch-priority/SKILL.md) | Vendor advisory, asset inventory and SOC Intel MCP | cve |
| [Remediation Review](../skills/vulnerability-management/remediation-review/SKILL.md) | Patch/change records and rescan inventory | cve |
| [Vulnerability Validation](../skills/vulnerability-management/vulnerability-validation/SKILL.md) | Scanner output and product configuration read API | cve |
