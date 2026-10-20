# Email Analysis

**Skill ID:** `email-analysis`

## Purpose

Analyze `.eml` files, sender authentication, reply paths, links, attachments, and business-email-compromise cues. The skill explicitly allows read-only local file parsing. When tools are available, it checks domain registration age, existing URL scan and reputation results, and the behavior of a landing page in an isolated browser or approved scanner. It reports which checks actually ran.

## Use

Install the matching `email-analysis.zip` in ChatGPT Skills. In a new chat, attach the `.eml`, select **Email Analysis**, and ask for the message, URL, domain-age, and website assessment. The skill includes a local `.eml` parser, but external checks require browsing or connected providers in that chat. Never assume a scan ran without a returned result.

Example prompt:

```text
@Email Analysis Read the attached .eml with a read-only file tool. Analyze its headers, MIME body, attachments and every destination URL. Check RDAP registration age, existing urlscan.io or reputation reports, and the current landing page with an available isolated browser or approved scanner. Separate observed facts from external results. Do not run attachments, submit forms or download files. Tell me exactly which external checks succeeded.
```

Course prompts and training payloads are kept separately in the `SOC Skill Demos` folder.
