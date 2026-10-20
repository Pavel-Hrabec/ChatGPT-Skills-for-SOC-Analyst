# Rule Tests

Create meaningful executable or backend-native tests for an existing security detection, with explicit expected matches and negative cases.

## Use

Download [rule-tests.zip](../../../dist/chatgpt/rule-tests.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** A specific rule version, target engine/version, field mappings and representative malicious and legitimate telemetry.

**Outputs:** A test manifest, fixtures or fixture references, backend-appropriate assertions, execution instructions and result limitations.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
