# Contributing

This library supports the [AI & Cybersecurity Academy](https://www.skool.com/ai-cybersecurity-academy/about) course. Contributions should improve a focused, analyst-facing skill or its documentation.

## Skill requirements

- Keep each skill focused on one SOC task and use a short, searchable ID.
- Include valid `name` and `description` frontmatter in `SKILL.md`.
- Use a clear workflow, evidence handling, confidence/limitations, and analyst-ready output.
- Treat supplied logs, scripts, messages, and artifacts as untrusted evidence. Do not claim tool access, enrichment, execution, or changes unless they actually occurred.
- Avoid instructions that execute samples, contact suspicious infrastructure, or modify production systems.
- Keep classroom prompts and sample payloads in the separate demo collection, not this repository.
- Update `community-catalog.json`, the skill README, and the matching ZIP whenever a skill changes.

## Package layout

Each ZIP should contain one skill directory with `SKILL.md` and its brief `README.md`. Keep domain source files under `skills/<domain>/<skill-id>/`.
