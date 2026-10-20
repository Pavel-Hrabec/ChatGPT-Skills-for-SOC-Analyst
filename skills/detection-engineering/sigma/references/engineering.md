## Selectors and data contracts

Choose the Sigma logsource from the actual telemetry: process creation, script logging and network events observe different behavior. A downloaded command in a process command line does not prove successful network execution. Record which observation the rule actually detects.

Within a selector, field mappings normally combine with AND; alternative values normally combine with OR. Use modifiers such as `contains`, `endswith` and `all` intentionally and check their semantics against the selected specification. Review the order of chained modifiers. Quote paths and regexes with YAML escaping in mind. Explain how absent, null and empty values affect each selector and filter.

Prefer the narrowest combination of behavioral signals supported by the input. A binary name alone is often weak; a relationship or command pattern may improve specificity. Avoid turning public report hashes into permanent behavior detectors. Do not add a broad management-agent exclusion without evidence and a stated coverage cost.

## Conversion and correlation

A processing pipeline determines source restrictions, field mapping and environment details. Save its identity/version alongside the rule. Inspect the converted query for missing index restrictions, changed wildcard behavior, dropped selectors and null handling. Compilation is not a behavioral test.

Use the correlation specification when counting or ordering events is necessary. Keep base-rule and correlation identities explicit and verify the installed backend supports the selected correlation type. Do not force temporal semantics into an ordinary single-event condition or promise identical portability across backends.

## Review package

Provide the rule, dependencies, cited behavior, analyst triage notes, intended test outcomes and exact tools actually used. Validate ATT&CK IDs against the current official dataset when lookup is available; label unverified mappings. Retain attribution when adapting an upstream rule and identify the changes. A generated rule starts as experimental; evidence from the target environment determines readiness.
