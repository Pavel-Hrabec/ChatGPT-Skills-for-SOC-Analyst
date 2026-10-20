# AWS S3

Investigate suspicious S3 object access and exposure.

**Input:** Bucket policy/ACL configuration, CloudTrail data events where enabled, object and principal context.

**Result:** Bucket/object exposure assessment with logging coverage limits.

Download [aws-s3.zip](../../../dist/chatgpt/aws-s3.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
