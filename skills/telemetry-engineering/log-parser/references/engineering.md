## Framing first

Determine whether a record is a JSON object, RFC-style syslog message, delimiter-separated row or a multiline envelope. A stack trace may span lines; line-oriented splitting can create false events. Handle vendor prefixes and transport envelopes explicitly. Use JSON/CSV libraries where applicable rather than regexes that ignore quoting or escaped delimiters.

For text extraction, anchor patterns to the intended grammar and bound expensive matching. Include long near-miss input in performance checks if regex backtracking is plausible. Do not use eval or execute a field as code. Preserve bytes or the original event under the target system's raw-event convention when possible.

## Types and clocks

Retain identifiers as strings when leading zeroes matter. Preserve booleans and numeric zero as values. Validate ports and sizes with explicit types; do not confuse hexadecimal PIDs with decimal values. Parse timestamps using the format and timezone established by source evidence. A timezone-free timestamp is unresolved until the source timezone is known; epoch unit must be explicit. Preserve both event and observed time when available.

## Failures and validation

Give unparseable records an explicit failure path with enough raw context for authorized troubleshooting. Quarantine, retention and redaction requirements depend on the environment; do not discard by default. Do not copy credentials or full sensitive payloads into routine error messages.

An Elasticsearch pipeline can be evaluated through the simulate pipeline API without indexing the documents. Check privileges, processors and version before calling it. For other engines use their supported parser harness. Verify exact field values, types and record cardinality, including no-match and malformed inputs. State which runtime was used; a Python prototype does not validate a Grok or collector configuration.
