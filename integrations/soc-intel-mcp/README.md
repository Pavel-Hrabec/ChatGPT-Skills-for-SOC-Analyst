# SOC Intel MCP

An optional read-only integration shared by the community skills. It retrieves existing indicator and URL reports plus public CVE context. It never submits files or URLs for scanning, contacts an indicator directly, modifies a security platform or produces an automatic block/allow verdict.

## Tools

| Tool | Providers | Configuration |
|---|---|---|
| `lookup_hash` | Existing VirusTotal, ThreatFox and MalwareBazaar reports | SHA256; provider API credentials |
| `lookup_ip` | Existing VirusTotal and ThreatFox reports | Public/global address; provider API credentials |
| `lookup_domain` | Existing VirusTotal and ThreatFox reports | Valid domain permitted for disclosure; provider API credentials |
| `lookup_url` | Existing VirusTotal URL and URLhaus records, plus exact matches among recent urlscan.io host results | Public HTTP(S) URL without userinfo, query, fragment or unusual port; provider API credentials |
| `lookup_cve` | CISA KEV and FIRST EPSS | Exact CVE; public endpoints |

## Local setup

Use Python 3.12 (the tested runtime) with the explicitly tested 1.x SDK version in `requirements.txt`. In a dedicated virtual environment run `python -m pip install -r requirements.txt`. The current upstream SDK also has a 2.x line; this adapter does not claim 2.x compatibility.

Set `VT_API_KEY`, `THREATFOX_AUTH_KEY`, `MALWAREBAZAAR_AUTH_KEY`, `URLHAUS_AUTH_KEY` and/or `URLSCAN_API_KEY` in the server process environment or the MCP host's secret configuration. Do not paste credentials in chat or commit them. Provider terms, quota and access depend on your account. Without a provider key its response is `not_configured`, not a benign verdict. VirusTotal domain reports may include a `creation_date`; treat it as provider-reported registration data and verify through RDAP when that date matters.

Start `python server.py` for stdio. Configure a compatible local MCP host with the Python executable and absolute path to `server.py`; the working directory must allow its adjacent `intel.py` import. Provider keys remain on the server side. This is a local MCP integration, not a skill ZIP import.

`python server.py --transport streamable-http --port 8765` binds to `127.0.0.1` only, normally at `/mcp`. This optional transport has no public authentication gateway. A remote client requires a separately reviewed authenticated deployment with tenant isolation and credential custody. Do not expose the unauthenticated loopback endpoint publicly.

## Evidence and disclosure

An indicator lookup discloses its input to each configured provider. Confirm that the data is permitted for that disclosure. Private/internal addresses and several non-public domain suffixes are rejected, but a syntactically public domain can still be business-sensitive. Only an exact SHA256, public IP, domain, public URL or CVE is accepted. URL queries and fragments are rejected to reduce accidental token disclosure. Files, internal reports and credential-bearing URLs are not input types.

Responses preserve provider status and retrieval time. ThreatFox observations retain original indicator scope and observation dates; VirusTotal reports retain selected provider-defined fields and existing report references. Never equate no result, provider failure, missing credentials and benign activity. KEV data is cached for ten minutes with the original retrieval timestamp. EPSS values are dated predictions; applicability still needs vendor/product evidence.

HTTPS destinations are fixed, redirects are disabled, timeouts are finite and responses are size-capped. Returned report text remains untrusted evidence. Errors do not echo request headers, credentials or provider bodies. No production deployment or live authenticated lookup was certified in this release; see `tests/intel` for mocked-provider and MCP protocol validation.

## Primary references

- [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [VirusTotal API](https://docs.virustotal.com/reference/overview)
- [VirusTotal URL identifiers](https://docs.virustotal.com/reference/url)
- [urlscan.io Search API](https://urlscan.io/docs/api/)
- [URLhaus API](https://urlhaus-api.abuse.ch/)
- [MalwareBazaar API](https://bazaar.abuse.ch/api/)
- [ThreatFox API](https://threatfox.abuse.ch/api/)
- [CISA KEV data](https://github.com/cisagov/kev-data)
- [FIRST API](https://api.first.org/)

These APIs are independently operated. The repository provides adapter code, not a subscription or a preconnected service.
