# Rule Tuning

Reduce noise in an existing detection using labeled evidence while measuring lost coverage, regression risk and exception scope.

## Use

Download [rule-tuning.zip](../../../dist/chatgpt/rule-tuning.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** Current rule/version, adjudicated alerts, sampled underlying events, intended behavior, environment context and candidate exceptions.

**Outputs:** A minimal tuning diff, before/after cohort metrics, positive regressions, exception ownership/expiry and rollout/rollback guidance.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
