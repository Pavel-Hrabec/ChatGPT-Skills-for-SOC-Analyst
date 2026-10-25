# Validation scope

The library validator checks every skill frontmatter, source/package identity, local reference links and catalog/source/ZIP coverage. Skill guidance has differentiated inputs, analysis checks, legitimate alternatives, task-specific pivots and output/decision boundaries. These checks do not establish end-to-end model reliability or production detection accuracy.

The offline profiler regression suite is retained. The optional intelligence server has mocked-provider and MCP protocol tests for input validation, error/missing-credential behavior, report minimization, CVE context and tool contracts. These tests do not contact external intelligence providers or certify credentials/rate-limit behavior in a deployed environment. Run the validator and applicable integration checks after changes; prior results do not certify a later revision.

Run standard-library tests with `python -m unittest discover -s tests/engineering -v`. Integration tests require the server's requirements and run with `python -m unittest discover -s tests/intel -v`. Test data is generated in temporary directories or supplied as mock responses; no demo payloads are bundled in the individual skill ZIPs.

