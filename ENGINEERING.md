# Community Security Engineering Skills

Ten new skills extend the SOC investigation library into detection authoring, testing, tuning, replay, telemetry engineering and threat intelligence quality. Existing skills and packages are preserved. This extension is intended for community use and contributions.

| Skill | Use | Upload |
|---|---|---|
| [Sigma](skills/detection-engineering/sigma/) | Author or convert Sigma detections from documented behavior and supplied telemetry, including backend mappings and validation requirements. | [ZIP](dist/chatgpt/sigma.zip) |
| [KQL Detection](skills/detection-engineering/kql-detection/) | Build operational KQL detections for Defender XDR or Microsoft Sentinel, including result identifiers, scheduling, entities and backend-aware tests. | [ZIP](dist/chatgpt/kql-detection.zip) |
| [SPL Detection](skills/detection-engineering/spl-detection/) | Write Splunk SPL security detections with confirmed sourcetypes or CIM dependencies, operational search settings and controlled validation. | [ZIP](dist/chatgpt/spl-detection.zip) |
| [Rule Tests](skills/detection-engineering/rule-tests/) | Create meaningful executable or backend-native tests for an existing security detection, with explicit expected matches and negative cases. | [ZIP](dist/chatgpt/rule-tests.zip) |
| [Rule Tuning](skills/detection-engineering/rule-tuning/) | Reduce noise in an existing detection using labeled evidence while measuring lost coverage, regression risk and exception scope. | [ZIP](dist/chatgpt/rule-tuning.zip) |
| [Detection Replay](skills/detection-engineering/detection-replay/) | Replay an existing detection against recorded telemetry in a controlled backend and compare expected events, entities and alert groups. | [ZIP](dist/chatgpt/detection-replay.zip) |
| [Log Parser](skills/telemetry-engineering/log-parser/) | Build or repair parsers for supplied security logs, preserving raw evidence and handling timestamps, framing, escapes and malformed records. | [ZIP](dist/chatgpt/log-parser.zip) |
| [Field Mapping](skills/telemetry-engineering/field-mapping/) | Map vendor security telemetry to a specified ECS, OCSF or local schema using field semantics, types, transformations and explicit unmapped values. | [ZIP](dist/chatgpt/field-mapping.zip) |
| [Log Quality](skills/telemetry-engineering/log-quality/) | Assess security log completeness, parsing, timestamps, duplicate candidates and ingestion delay from supplied records or bounded authorized queries. | [ZIP](dist/chatgpt/log-quality.zip) |
| [Feed Quality](skills/threat-intelligence-engineering/feed-quality/) | Evaluate threat intelligence feed quality through indicator validity, provenance, observation age, duplication, confidence semantics and sharing restrictions. | [ZIP](dist/chatgpt/feed-quality.zip) |

## Install and use

Import one ZIP from `dist/chatgpt/` into a compatible ChatGPT Skills interface. Provide the target product/version, schema or sample evidence and the artifact you want produced. Each skill has its own README and progressively loaded engineering references. Skill descriptions distinguish the new authoring workflows from the existing KQL query and Sigma/YARA explanation skills.

## Knowledge and integrations

Each source list records primary pages opened on 2026-10-20; refresh mutable product documentation for the target deployment. References include Sigma, Microsoft Defender/Sentinel, Splunk, Elastic, OCSF, OpenTelemetry, MITRE, OASIS, FIRST, ThreatFox and OpenCTI. New instructions are original task-specific synthesis, not copied upstream skills.

The skills use supplied evidence and, when available, authorized documentation or backend tools. No live MCP server, credentials or provider subscription is bundled. The Log Quality and Feed Quality packages include standard-library Python profilers for bounded local NDJSON exports. They provide measurements and never query reputation services or classify an indicator as malicious.

## Validation and limits

All ten skills passed the bundled skill validator using PyYAML 6.0.3. All ten ZIPs matched their source contents, and local documentation links resolved. Ten offline helper regression tests passed, covering malformed input, missing values, timezone handling, duplicates, age/expiry and aggregate measurements. Run the standard-library helper suite from the repository root with `python -m unittest discover -s tests/engineering -v`.

The GitHub extension is constructed additively from the existing library tree; existing file hashes are preserved. Backend-specific instructions and generated queries still require validation in the user's actual engine/version. No live Splunk, Defender, Sentinel, Elastic or threat-feed API was exercised for this extension. Skill packaging validation does not establish end-to-end behavior in ChatGPT or a SIEM.

## Community contributions

Use `engineering-catalog.json` to discover the new skills; the original catalog remains intact. Additions should state the investigation or engineering question, required inputs, concrete outputs, primary sources and compatibility limits. Include actual validation evidence when claiming a tool or backend works. Preserve the distinction between static review, local helper execution, query validation and live alert-service behavior. Keep classroom/demo payloads outside skill packages; ordinary task-specific reference guidance belongs with the skill.
