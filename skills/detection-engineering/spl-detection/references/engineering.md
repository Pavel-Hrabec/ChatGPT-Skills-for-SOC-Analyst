## Raw events or CIM

Use confirmed index and sourcetype restrictions; an unrestricted search is not a portable default. Before using tstats against a security data model, verify mapping, acceleration state, relevant field population and summary coverage. Missing acceleration or summaries outside retention can look like an absence of attacks. Do not invent a local macro or lookup name; define each dependency or use explicit logic.

Review text matching with actual quoting, escaping, case and tokenization. Evaluate whether fields are single-valued or multivalued. Nulls interact with filters and aggregations; preserve near-miss cases where a field is absent. Treat field aliases and calculated fields as part of the rule's environment contract.

## Search behavior and cost

Filter sources and time before expensive transformations. Prefer a justified stats-based approach over transaction for grouping when it preserves the necessary sequence semantics. Document what evidence a count or distinct count represents. Do not calculate event rate from grouped row count without a consistent denominator.

Keep event time, index time, scheduler execution and search time bounds distinct. Define overlap and late-arrival allowance. Scope throttling to the right entity; global suppression can hide unrelated activity. Select result fields that let an analyst recover underlying evidence. Use reviewable saved-search settings tied to the actual installed product version.

## Validation and connections

Splunk Security Content and contentctl demonstrate repository conventions, but CLI names and content schemas can change. Inspect the installed release and repository configuration before proposing executable commands. An authorized search connector can check field coverage and run bounded searches; it does not automatically grant permissions to create a saved search. Exclude commands that write data or trigger actions from a purported read-only validation query.
