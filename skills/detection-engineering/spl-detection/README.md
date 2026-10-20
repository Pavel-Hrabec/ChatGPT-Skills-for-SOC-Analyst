# SPL Detection

Write Splunk SPL security detections with confirmed sourcetypes or CIM dependencies, operational search settings and controlled validation.

## Use

Download [spl-detection.zip](../../../dist/chatgpt/spl-detection.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** Splunk deployment and detection type, indexes/sourcetypes or CIM data model, sample events, existing macros/lookups and a behavior hypothesis.

**Outputs:** SPL search, dependencies, scheduling and grouping choices, validation evidence and a reviewable detection content package.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
