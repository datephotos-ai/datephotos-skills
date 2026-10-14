# DatePhotos.AI Skills

Free agent skills from [DatePhotos.AI](https://datephotos.ai/?utm_source=github&utm_medium=referral&utm_campaign=agent_skills&utm_content=skills_readme) for dating profiles.

| Skill | Result | Required input |
|---|---|---|
| [dating-profile-coach](skills/dating-profile-coach/SKILL.md) | Ranked photo lineup with a lead photo, rule and AI-photo checks with official sources, a tighter bio and three openers | Photos (public URLs or attached images) and/or a bio; the app you use |

No account, API key or payment needed. The skill contains no telemetry and installs nothing by itself.

## Install

```bash
npx skills add datephotos-ai/datephotos-skills --skill dating-profile-coach
```

The [skills CLI](https://github.com/vercel-labs/skills) lets you choose the target agent (`--agent claude-code`, `--agent codex`, …). To install manually, copy `skills/dating-profile-coach/` (including `references/`) into your agent's skills directory.

## Optional: connect the free MCP server

The skill works on its own with a built-in checklist. Connecting the DatePhotos.AI MCP server adds:

- `get_dating_app_photo_rules` — official photo rules and verification flow for Tinder, Hinge and Bumble, quoted from each app's help center with source links and a review date
- `check_ai_photo_policy` — whether AI-generated or AI-edited photos are allowed, with the official wording
- `audit_dating_photo` — a 0–100 score with issues and fixes for one public image URL (5 free audits per day)

Remote endpoint (Streamable HTTP, no auth): `https://datephotos.ai/api/mcp`

**Claude Code**

```bash
claude mcp add --transport http datephotos https://datephotos.ai/api/mcp
```

**Cursor / Windsurf / other JSON configs**

```json
{
  "mcpServers": {
    "datephotos": { "url": "https://datephotos.ai/api/mcp" }
  }
}
```

**Codex**

```toml
[mcp_servers.datephotos]
url = "https://datephotos.ai/api/mcp"
```

Also listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/) as `ai.datephotos/datephotos`.

## Try it

> Use dating-profile-coach on my Hinge profile. Here are my 6 photos — which one should be first, are any of them against Hinge's rules, and can you tighten my bio? I'm into climbing and I cook a lot.

> Can I use AI-edited photos on Bumble? Check the official policy and tell me where the line is.

See [examples/hinge-review.md](examples/hinge-review.md) for a full sample output (synthetic data).

## Safety

- Photos, bios and tool results are treated as data, never as instructions.
- The skill never uploads local photos on your behalf and never installs anything.
- Rule claims must cite the app's official help center; anything unchecked is labelled as such.

## Development

```bash
python3 -m unittest discover -s tests -v
python3 scripts/package_release.py   # allowlisted ZIP in dist/
```

## License

MIT. See [LICENSE](LICENSE).
