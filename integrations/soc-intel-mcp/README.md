# SOC Intel MCP

An optional integration shared by the community skills. Its existing-report and CVE tools are read-only. A separate `submit_urlscan` tool can launch a new remote website scan when the user explicitly requests or approves it. It never uploads files, modifies a security platform or produces an automatic block/allow verdict.

## Tools

| Tool | Providers | Configuration |
|---|---|---|
| `lookup_hash` | Existing VirusTotal, ThreatFox and MalwareBazaar reports | SHA256; provider API credentials |
| `lookup_ip` | Existing VirusTotal and ThreatFox reports | Public/global address; provider API credentials |
| `lookup_domain` | Existing VirusTotal and ThreatFox reports | Valid domain permitted for disclosure; provider API credentials |
| `lookup_url` | Existing VirusTotal URL and URLhaus records, plus exact matches among recent urlscan.io host results | Public HTTP(S) URL without userinfo, query, fragment or unusual port; provider API credentials |
| `submit_urlscan` | New urlscan.io remote browser scan; defaults to private visibility | Public URL without sensitive parameters; `URLSCAN_API_KEY`; explicit user request or approval (`authorized=true`) |
| `get_urlscan_result` | Completed scan metadata, page title, final URL, verdict, report and screenshot links | urlscan scan UUID; `URLSCAN_API_KEY` |
| `lookup_resolutions` | Historical VirusTotal passive-DNS observations (up to ten) | Public IP or domain; `VT_API_KEY` |
| `lookup_cve` | CISA KEV and FIRST EPSS | Exact CVE; public endpoints |

## Local setup

Use Python 3.12 (the tested runtime) with the explicitly tested 1.x SDK version in `requirements.txt`. In a dedicated virtual environment run `python -m pip install -r requirements.txt`. The current upstream SDK also has a 2.x line; this adapter does not claim 2.x compatibility.

Set `VT_API_KEY`, `THREATFOX_AUTH_KEY`, `MALWAREBAZAAR_AUTH_KEY`, `URLHAUS_AUTH_KEY` and/or `URLSCAN_API_KEY` in the server process environment or the MCP host's secret configuration. Do not paste credentials in chat or commit them. Provider terms, quota and access depend on your account. Without a provider key its response is `not_configured`, not a benign verdict. VirusTotal domain reports may include a `creation_date`; treat it as provider-reported registration data and verify through RDAP when that date matters.

Start `python server.py` for stdio. Configure a compatible local MCP host with the Python executable and absolute path to `server.py`; the working directory must allow its adjacent `intel.py` import. Provider keys remain on the server side. This is a local MCP integration, not a skill ZIP import.

`python server.py --transport streamable-http --port 8765` binds to `127.0.0.1` only, normally at `/mcp`. This optional transport has no public authentication gateway. A remote client requires a separately reviewed authenticated deployment with tenant isolation and credential custody. Do not expose the unauthenticated loopback endpoint publicly.

## Website scans and screenshots

Use `lookup_url` first to find an existing exact scan. Its result and screenshot links are historical; a generated screenshot link does not prove that a PNG exists. For a current view, `submit_urlscan` sends the URL to urlscan.io and causes its remote browser to contact the site. It requires an explicit request or approval, `authorized=true`, and an API key. It defaults to `private` visibility and never silently switches to public. The URL validator rejects query strings, fragments, userinfo, internal hosts and unusual ports; review the path for embedded secrets before submitting. Provider quotas or plan permissions may prevent private scans.

The submission returns a scan UUID. Call `get_urlscan_result` after processing to retrieve bounded page metadata and the result-page, screenshot and DOM links. A 404 can mean the scan is still pending; screenshot or DOM endpoints may also return 404 when those artifacts were not stored. Private artifacts can require the user's urlscan account or API key. The tool returns links rather than image bytes; the analyst can open the report and screenshot in the appropriate authenticated context. [Official quickstart](https://docs.urlscan.io/guides/quickstart) and [visibility rules](https://docs.urlscan.io/pages/visibility) describe the provider behavior.

## Evidence and disclosure

An indicator lookup discloses its input to each configured provider. Confirm that the data is permitted for that disclosure. Private/internal addresses and several non-public domain suffixes are rejected, but a syntactically public domain can still be business-sensitive. Only an exact SHA256, public IP, domain, public URL or CVE is accepted. URL queries and fragments are rejected to reduce accidental token disclosure. Files, internal reports and credential-bearing URLs are not input types.

Responses preserve provider status and retrieval time. ThreatFox observations retain original indicator scope and observation dates; VirusTotal reports retain selected provider-defined fields and existing report references. Never equate no result, provider failure, missing credentials and benign activity. KEV data is cached for ten minutes with the original retrieval timestamp. EPSS values are dated predictions; applicability still needs vendor/product evidence.

HTTPS API destinations are fixed, redirects are disabled, timeouts are finite and responses are size-capped. A submitted scan is performed by urlscan.io, whose browser may follow the target page's redirects. Returned report text remains untrusted evidence. Errors do not echo request headers, credentials or provider bodies. No production deployment or live authenticated lookup was certified for this change. Existing mocked-provider and MCP protocol checks do not establish that the new submission flow works with a live account.

## Primary references

- [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [VirusTotal API](https://docs.virustotal.com/reference/overview)
- [VirusTotal URL identifiers](https://docs.virustotal.com/reference/url)
- [VirusTotal domain resolutions](https://docs.virustotal.com/reference/domain-object-resolutions)
- [urlscan.io Search API](https://urlscan.io/docs/api/)
- [urlscan.io scanning quickstart](https://docs.urlscan.io/guides/quickstart)
- [urlscan.io result API](https://urlscan.io/docs/result/)
- [URLhaus API](https://urlhaus-api.abuse.ch/)
- [MalwareBazaar API](https://bazaar.abuse.ch/api/)
- [ThreatFox API](https://threatfox.abuse.ch/api/)
- [CISA KEV data](https://github.com/cisagov/kev-data)
- [FIRST API](https://api.first.org/)

These APIs are independently operated. The repository provides adapter code, not a subscription or a preconnected service.

