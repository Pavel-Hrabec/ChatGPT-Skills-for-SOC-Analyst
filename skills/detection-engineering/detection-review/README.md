# Review detection logic

**Skill ID:** `detection-review`

## Purpose

Goal, data dependencies, logic, test coverage, false positives and safe tuning proposals. This skill analyzes only evidence supplied by the user or retrieved through an explicitly available, authorized, read-only connection. It does not grant access to XDR, SIEM, EDR, directory, mail, cloud, or reputation services.

## Use

Install the matching `detection-review.zip` in ChatGPT Skills. In a new chat, describe the alert or evidence and name this skill, or ask ChatGPT to apply it to the attached material. The skill analyzes evidence supplied in the chat; it does not itself connect to your SOC tools.

Course prompts and training payloads are kept separately in the `SOC Skill Demos` folder.
