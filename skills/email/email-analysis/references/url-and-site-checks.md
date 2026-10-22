# URL and website checks for Email Analysis

This is an investigation sequence, not a guarantee that a particular provider is connected. Always distinguish an extracted URL from a URL actually checked. Do not invent a scan result or registration date.

## 1. Normalize and select the destination

- Preserve the exact URL for tool queries and evidence. Defang only the displayed copy.
- Parse the scheme and hostname. Record the original URL, any redirection service, final URL, hostname, and registrable domain separately.
- Historical domains or URLs may no longer resolve or serve the reported content. Use the original dated report and state that current page content could not be observed.
- Avoid sending URL query strings containing email addresses, credentials, session tokens, or internal identifiers to public services. If a lookup on a sanitized URL would change its meaning, report that the exact URL was not checked.

## 2. Existing scan and reputation results

- Search existing [urlscan.io scans](https://urlscan.io/docs/api/) for the exact URL or hostname. Check the task URL, final page URL, scan timestamp, visibility, and whether the result is for the same destination. Review the result JSON, screenshot, and DOM when available. A past scan is historical evidence, not proof of current content.
- If an authorized VirusTotal connection/API is available, retrieve the [URL report](https://docs.virustotal.com/reference/url-info). Use its required URL identifier. Record the report's observation time and detections; vendor counts alone are not a verdict. Domain and URL reports answer different questions.
- If the optional SOC Intel MCP is connected, `lookup_url` reads existing VirusTotal, URLhaus and urlscan.io results. Exact urlscan matches include a result link and a screenshot link whose availability has not been verified. This lookup never launches a new scan.
- Existing third-party reports can be searched without visiting the suspicious site from the analyst environment. Provider lookups may still disclose the searched indicator to that provider.

## 3. Domain registration age

- Query the registrable domain with an RDAP source such as [ICANN Lookup](https://lookup.icann.org/). The domain response `events` entry with `eventAction: registration` is the creation/registration date in the [ICANN RDAP profile](https://www.icann.org/en/contracted-parties/registry-operators/registration-data-access-protocol/rdap-operational-profile-for-gtld-registries-and-registrars-26-07-2016-en).
- Report the registration date, age as of the analysis date, lookup time, domain queried, and source. Do not use the certificate issuance date, site first-seen date, or last-updated date as domain creation date.
- RDAP can be unavailable or incomplete, and registration age cannot establish that the page is safe or malicious. Avoid guessing.

## 4. Current website behavior

- If the user requests current website analysis and an approved isolated browser or URL scanner is available, inspect the landing page, redirects, forms, requested information, brand cues, scripts/requests visible to the tool, and downloads offered. Observe only; do not log in, submit data, install extensions, or execute downloaded files.
- A new [urlscan.io submission](https://docs.urlscan.io/guides/quickstart) causes the provider to visit the URL. Use `submit_urlscan` only when the user explicitly requests or approves a fresh scan; pass `authorized=true` and default to `private`. Do not submit internal URLs, query strings, tokens or credential-bearing paths. Do not silently fall back to public visibility if private submission is unavailable. Public results are visible publicly; unlisted results can be seen by vetted researchers; private results are limited to the account or people given the scan ID. [Visibility details](https://docs.urlscan.io/pages/visibility).
- Use the returned UUID with `get_urlscan_result`. A 404 may mean processing is incomplete; a 410 means the result is gone. Once ready, cite the result-page link, scan time, final URL, page title and screenshot link. The PNG at `https://urlscan.io/screenshots/<UUID>.png` or DOM snapshot may return 404, and private artifacts can require authentication. Do not report that you viewed a screenshot merely because a link was generated.
- Capture the final URL, redirect chain, scan/visit timestamp, screenshot or page text, any credential form or file offered, and visible network requests. A page may vary by location, user agent, time, or authentication state.

## Output evidence table

| Item | Value | Source and time | What it shows | Limit |
| --- | --- | --- | --- | --- |
| Email URL | Defanged URL | `.eml` body | What recipient was asked to open | Does not prove site behavior |
| RDAP | Registration date and age, or unknown | RDAP lookup | Domain registration history | Old domains can be compromised |
| URL report | Detections/scan findings, or unavailable | Provider and report time | Historical reputation/page evidence | May be stale or a near match |
| Website | Final URL, page/forms/redirects, or not inspected | Browser/scanner and visit time | Observed page behavior | Content can change |

