# Email Analysis

**Skill ID:** `email-analysis`

## Purpose

Analyze `.eml` files, sender authentication, reply paths, links, attachments, and business-email-compromise cues. The skill explicitly allows read-only local file parsing. With a connected SOC Intel MCP it can find existing urlscan.io results and their screenshot links; when the user explicitly requests a fresh scan, it can submit a public URL privately and retrieve the resulting page and screenshot links. It reports which checks actually ran.

## Use

Install the matching `email-analysis.zip` in ChatGPT Skills. In a new chat, attach the `.eml`, select **Email Analysis**, and ask for the message, URL, domain-age, and website assessment. The skill includes a local `.eml` parser, but external checks require browsing or connected providers in that chat. Never assume a scan ran without a returned result.

Example prompt:

```text
@Email Analysis Read the attached .eml with a read-only file tool. Analyze its headers, MIME body, attachments and every destination URL. Check RDAP registration age and existing urlscan.io or reputation reports. For public URLs without sensitive parameters, I authorize a new private urlscan.io scan if no relevant recent report exists. Give me the scan result and screenshot links, then assess the landing page. Separate observed facts from external results. Do not run attachments, submit forms or download files. Tell me exactly which external checks succeeded.
```

Course prompts and training payloads are kept separately in the `SOC Skill Demos` folder.

