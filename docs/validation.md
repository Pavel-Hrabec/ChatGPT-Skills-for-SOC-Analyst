# Validation scope

The library validator checks all 150 skill frontmatters, source/package identity, local reference links and catalog/source/ZIP coverage. It verifies that ZIP contents match their source files, allowing newline-only differences in text files. These checks do not establish end-to-end model reliability or production detection accuracy.

The offline profiler suite covers parsing, timestamps and aggregate measurements. The optional intelligence server has mocked-provider and MCP protocol tests for input validation, error/missing-credential behavior, report minimization, CVE context and tool contracts. These tests do not contact external intelligence providers or certify credentials/rate-limit behavior in a deployed environment. The [validation report](../validation-report.json) records actual results.

Run standard-library tests with `python -m unittest discover -s tests/engineering -v`. Integration tests require the server's requirements and run with `python -m unittest discover -s tests/intel -v`. Test data is generated in temporary directories or supplied as mock responses; no demo payloads are bundled in the individual skill ZIPs.
