## Semantic mapping contract

For every field record source path, source meaning/type, target path/type, transformation, null policy, enumeration policy, confidence/basis and any unresolved ambiguity. Check the actual target release rather than guessing numeric enum identifiers. Name similarity is a hypothesis, not evidence of equivalent semantics.

Differentiate initiating actor from affected account, observer from endpoint, and connection source from authentication target. NAT and proxy intermediaries may require distinct fields. Preserve both original and translated address information. A server-side field named client can mean the proxy, not the originating device. Use source documentation to establish direction.

## Transformation decisions

State timestamp precision, timezone, event/observed semantics and epoch units. Preserve original values when normalization is lossy. Map action and outcome from documented vendor values; an unmapped code stays unknown with its original value retained. Do not convert an empty field to a success or infer a process hash from a file hash field without context.

Preserve arrays, structured identities and numeric versus textual identifiers. Explicitly choose how nested objects and flat dotted keys are represented. ECS and OCSF are different models; class/activity and enum choices need more than mechanical renaming. Record custom extensions and their purpose when the schema cannot represent the source faithfully.

## Validate downstream impact

Check schema types and required fields, then exercise detections consuming the mapped fields. A syntactically valid mapping may reverse source/destination or collapse two actors. Compare old/new field population and match outcomes before migration. Version the mapping and record which parsers, queries and dashboards require updates. This skill supplies mapping guidance and artifacts; it does not install a collector or migrate stored events automatically.
