# KQL Detection

Build operational KQL detections for Defender XDR or Microsoft Sentinel, including result identifiers, scheduling, entities and backend-aware tests.

## Use

Download [kql-detection.zip](../../../dist/chatgpt/kql-detection.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** The target Microsoft detection product, verified tables and fields, representative events, detection hypothesis and intended schedule.

**Outputs:** KQL query, product-specific rule configuration, telemetry requirements, entity mapping, test plan and deployment-readiness assessment.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
