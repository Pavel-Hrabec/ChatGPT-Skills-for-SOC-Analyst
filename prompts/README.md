Warning: truncated output (original token count: 6741)
Total output lines: 218

# Copyable prompts

One standalone prompt for each skill in this repository. Copy the prompt into ChatGPT and attach or paste the relevant evidence. The prompt still works as a task request when the corresponding skill ZIP is unavailable; installing the skill adds its fuller task guidance and references.

Every prompt uses the same output headings: Summary; Result or requested artifact; Evidence and reasoning; Assessment or validation status; Unknowns and limitations; Recommended next steps.

Prompts are grouped by the same category as the skills.

## Aws

- [AWS Access Keys](aws/aws-access-keys.md) — Investigate suspicious AWS access-key creation and use.
- [AWS CloudTrail](aws/aws-cloudtrail.md) — Investigate CloudTrail visibility changes and suspicious control-plane sequences.
- [AWS EC2](aws/aws-ec2.md) — Investigate suspicious EC2 control-plane and instance activity.
- [AWS IAM](aws/aws-iam.md) — Investigate IAM policy, trust and privilege changes.
- [AWS Lambda](aws/aws-lambda.md) — Investigate suspicious Lambda code, configuration and invocation activity.
- [AWS S3](aws/aws-s3.md) — Investigate suspicious S3 object access and exposure.
- [AWS SSO](aws/aws-sso.md) — Investigate AWS federation and IAM Identity Center session activity.

## Azure

- [Azure Key Vault](azure/azure-keyvault.md) — Investigate suspicious secret, key or certificate access in Key Vault.
- [Azure Logging](azure/azure-logging.md) — Investigate changes affecting Azure resource logging and visibility.
- [Azure Roles](azure/azure-roles.md) — Investigate Azure role assignments and privilege changes.
- [Azure Storage](azure/azure-storage.md) — Investigate suspicious Azure Storage access, sharing and token use.
- [Azure VM](azure/azure-vm.md) — Investigate Azure VM remote execution and control-plane changes.

## Containers

- [Container Escape](containers/container-escape.md) — Assess evidence that a container crossed into host resources.
- [Container Images](containers/container-images.md) — Investigate suspicious container image provenance and runtime use.
- [K8s Audit](containers/k8s-audit.md) — Reconstruct suspicious Kubernetes API activity from audit events.
- [K8s RBAC](containers/k8s-rbac.md) — Investigate Kubernetes role and binding changes.
- [Pod Exec](containers/pod-exec.md) — Investigate interactive execution into Kubernetes containers.

## Detection Engineering

- [Coverage Review](detection-engineering/coverage-review.md) — Assess security detection coverage using actual telemetry and validation.
- [Detection Replay](detection-engineering/detection-replay.md) — Replay an existing detection against recorded telemetry in a controlled backend and compare expected events, entities and alert groups..
- [Duplicate Rules](detection-engineering/duplicate-rules.md) — Identify overlapping detections without losing distinct coverage.
- [Elastic Detection](detection-engineering/elastic-detection.md) — Author Elastic Security detections for a specified engine and schema.
- [Explain Sigma and YARA rules](detection-engineering/sigma-yara.md) — Explain Sigma and YARA rules. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [KQL Detection](detection-engineering/kql-detection.md) — Build operational KQL detections for Defender XDR or Microsoft Sentinel, including result identifiers, scheduling, entities and backend-aware tests..
- [Query Performance](detection-engineering/query-performance.md) — Improve security query performance while checking result equivalence.
- [Review detection logic](detection-engineering/detection-review.md) — Review detection logic. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Rule Migration](detection-engineering/rule-migration.md) — Translate a detection between platforms while preserving its semantics.
- [Rule Tests](detection-engineering/rule-tests.md) — Create meaningful executable or backend-native tests for an existing security detection, with explicit expected matches and negative cases..
- [Rule Tuning](detection-engineering/rule-tuning.md) — Reduce noise in an existing detection using labeled evidence while measuring lost coverage, regression risk and exception scope..
- [Sigma](detection-engineering/sigma.md) — Author or convert Sigma detections from documented behavior and supplied telemetry, including backend mappings and validation requirements..
- [SPL Detection](detection-engineering/spl-detection.md) — Write Splunk SPL security detections with confirmed sourcetypes or CIM dependencies, operational search settings and controlled validation..
- [Suricata](detection-engineering/suricata.md) — Author Suricata signatures for observable network behavior.
- [Threat Coverage](detection-engineering/threat-coverage.md) — Assess defensive coverage against a specific reported threat sequence.
- [YARA](detection-engineering/yara.md) — Author and validate YARA rules for a defined file or memory target.

## Email

- [Analyze suspicious email](email/email-analysis.md) — Analyze suspicious email. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..

## Endpoint

- [Analyze a process tree](endpoint/process-tree.md) — Analyze a process tree. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, o…3741 tokens truncated…uplication for security alerts.
- [API Integration](security-automation/api-integration.md) — Implement an authenticated security API integration with bounded operations.
- [Enrichment Pipeline](security-automation/enrichment-pipeline.md) — Build a bounded intelligence enrichment workflow with provenance.
- [SOAR Playbook](security-automation/soar-playbook.md) — Design a reviewable automation playbook for a defined security workflow.

## Siem

- [Draft and explain ES|QL](siem/esql.md) — Draft and explain ES|QL. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Draft and explain KQL](siem/kql.md) — Draft and explain KQL. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Interpret SIEM query results](siem/query-results.md) — Interpret SIEM query results. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..

## Telemetry Engineering

- [Field Mapping](telemetry-engineering/field-mapping.md) — Map vendor security telemetry to a specified ECS, OCSF or local schema using field semantics, types, transformations and explicit unmapped values..
- [Log Parser](telemetry-engineering/log-parser.md) — Build or repair parsers for supplied security logs, preserving raw evidence and handling timestamps, framing, escapes and malformed records..
- [Log Quality](telemetry-engineering/log-quality.md) — Assess security log completeness, parsing, timestamps, duplicate candidates and ingestion delay from supplied records or bounded authorized queries..

## Threat Intelligence

- [Analyze indicators of compromise](threat-intelligence/ioc-analysis.md) — Analyze indicators of compromise. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Campaign Review](threat-intelligence/campaign-review.md) — Evaluate whether observed incident evidence matches a reported campaign.
- [Indicator Expiry](threat-intelligence/indicator-expiry.md) — Propose evidence-based indicator retention and review policies.
- [Infrastructure Links](threat-intelligence/infrastructure-links.md) — Assess relationships among suspicious domains, IPs and certificates.
- [Intel Dedup](threat-intelligence/intel-dedup.md) — Deduplicate intelligence while preserving distinct observations and source lineage.
- [Intel to Hunt](threat-intelligence/intel-to-hunt.md) — Translate a threat report into testable defensive hunt hypotheses.
- [Interpret malware sandbox reports](threat-intelligence/sandbox-report.md) — Interpret malware sandbox reports. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Review file-hash evidence](threat-intelligence/hash-analysis.md) — Review file-hash evidence. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [STIX Review](threat-intelligence/stix-review.md) — Review STIX intelligence objects and relationships for semantic validity.

## Threat Intelligence Engineering

- [Feed Quality](threat-intelligence-engineering/feed-quality.md) — Evaluate threat intelligence feed quality through indicator validity, provenance, observation age, duplication, confidence semantics and sharing restrictions..

## Vulnerability Management

- [Analyze port-scan alerts](vulnerability-management/scan-alert.md) — Analyze port-scan alerts. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [CVE Review](vulnerability-management/cve-review.md) — Assess a CVE's applicability and investigation relevance.
- [Exposure Review](vulnerability-management/exposure-review.md) — Review whether a vulnerable service is reachable in its actual environment.
- [Patch Priority](vulnerability-management/patch-priority.md) — Prioritize remediation using exploitation evidence and asset context.
- [Plan an authorized scan scope](vulnerability-management/scan-scope.md) — Plan an authorized scan scope. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Remediation Review](vulnerability-management/remediation-review.md) — Verify remediation evidence and detect incomplete fixes.
- [Review vulnerability scan results](vulnerability-management/scan-results.md) — Review vulnerability scan results. Use when an analyst provides relevant alert, log, query, or artifact evidence and asks for this specific analysis. Do not claim data access, enrichment, execution, or changes unless actually performed through an available authorized tool..
- [Vulnerability Validation](vulnerability-management/vulnerability-validation.md) — Validate scanner findings through version and configuration evidence.

