# Field Mapping

Map vendor security telemetry to a specified ECS, OCSF or local schema using field semantics, types, transformations and explicit unmapped values.

## Use

Download [field-mapping.zip](../../../dist/chatgpt/field-mapping.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** Source field documentation and representative events, a named target schema/version, required downstream detections and mapping constraints.

**Outputs:** Source-to-target mapping specification, transformation logic, unresolved semantics, validation cases and downstream impact notes.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
