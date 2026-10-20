# Log Parser

Build or repair parsers for supplied security logs, preserving raw evidence and handling timestamps, framing, escapes and malformed records.

## Use

Download [log-parser.zip](../../../dist/chatgpt/log-parser.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** Representative raw records including malformed and multiline examples, source format/version, target parser engine and expected output contract.

**Outputs:** Parser code or pipeline, field/type contract, explicit failure handling, reproducible parser tests and operational limits.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
