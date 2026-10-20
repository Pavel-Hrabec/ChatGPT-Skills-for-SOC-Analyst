# DLL Loading

Assess suspicious DLL loading and potential side-loading.

**Input:** Module-load records, parent executable, module path, signatures, hashes and directory permissions.

**Result:** Module provenance assessment and a bounded side-loading hypothesis.

Download [dll-loading.zip](../../../dist/chatgpt/dll-loading.zip) and import one package in a compatible Skills interface. Name the skill and attach relevant evidence. The package includes the workflow, a focused analysis guide, reviewed primary-source links and optional connection guidance. It contains no classroom/demo payloads, API keys or active service connection.

**Validation:** Source and package review; no claim of end-to-end model or SIEM effectiveness. Configure integrations separately and validate any generated queries/configuration against your actual backend. See [analysis guidance](references/analysis.md) for meaningful acceptance criteria and limitations.
