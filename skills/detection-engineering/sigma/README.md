# Sigma

Author or convert Sigma detections from documented behavior and supplied telemetry, including backend mappings and validation requirements.

## Use

Download [sigma.zip](../../../dist/chatgpt/sigma.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** A behavior description or cited report, representative events, logging source, target backend, and any existing processing pipeline.

**Outputs:** Sigma YAML, source-to-rule rationale, field dependencies, conversion assumptions, positive/negative test requirements and validation status.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
