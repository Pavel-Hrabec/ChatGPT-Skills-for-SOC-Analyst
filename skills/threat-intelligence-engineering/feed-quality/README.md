# Feed Quality

Evaluate threat intelligence feed quality through indicator validity, provenance, observation age, duplication, confidence semantics and sharing restrictions.

## Use

Download [feed-quality.zip](../../../dist/chatgpt/feed-quality.zip) and import it as one skill in a compatible ChatGPT Skills interface. Name the skill when describing your task and attach the required evidence. Availability depends on the host's skill support.

**Inputs:** An intelligence export or authorized feed connection, provider field definitions, evaluation date, indicator types and the intended operational use.

**Outputs:** A feed quality assessment, normalization and provenance gaps, overlap/age metrics, policy recommendations and limitations on maliciousness claims.

## Resources and connections

The package contains task-specific instructions, engineering guidance and [reviewed primary sources](references/sources.md). It works from supplied artifacts. Browsing can refresh documentation; separately configured authenticated tools can support the bounded checks described in the skill. No MCP server, API key or live service connection is bundled.

Includes an offline Python 3.10+ profiler using the standard library. Code execution must be available in the host to run it. The helper performs no network requests.

**Validation status:** Reference-reviewed instructions; packaging and helper validation are recorded in [ENGINEERING.md](../../../ENGINEERING.md). No live SIEM/XDR deployment is certified. Community contributions should include reproducible evidence for any additional compatibility claim.
