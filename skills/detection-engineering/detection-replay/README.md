# Detection Replay

Replay an existing detection against recorded telemetry in a controlled backend and compare expected events, entities and alert groups.

## Use

Download [detection-replay.zip](../../../dist/chatgpt/detection-replay.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** Rule and mapping versions, recorded dataset with provenance, expected outcomes, target lab/backend and time-handling requirements.

**Outputs:** A reproducible replay plan or actual run record with input identity, transformations, matched evidence and validation gaps.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
