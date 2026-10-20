# Validation scope

The release validation checks all 150 skill frontmatters, source/package identity, local reference links, catalog/source/ZIP coverage and preservation of the original 44 skill files and ZIPs. New skill guidance has differentiated inputs, analysis checks, legitimate alternatives, task-specific pivots and output/decision boundaries. These checks do not establish end-to-end model reliability or production detection accuracy.

The original offline profiler regression suite is retained. The optional intelligence server has mocked-provider and MCP protocol tests for input validation, error/missing-credential behavior, report minimization, CVE context and tool contracts. These tests do not contact external intelligence providers or certify credentials/rate-limit behavior in a deployed environment. The release report records actual results after execution.

Run standard-library tests with `python -m unittest discover -s tests/engineering -v`. Integration tests require the server's requirements and run with `python -m unittest discover -s tests/intel -v`. Test data is generated in temporary directories or supplied as mock responses; no demo payloads are bundled in the individual skill ZIPs.
