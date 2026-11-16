# bytes-skill

A Claude skill for drafting **The Point**, a biweekly internal engineering newsletter written in the spirit of [Bytes](https://bytes.dev).

- `.claude/skills/the-point/` – the skill: workflow, anatomy, voice, guardrails, story selection, visuals, and the HTML template.
- `data/` – all 538 Bytes issues (`html/` raw, `md/` cleaned, `index.json`), used as the reference corpus for the style analysis. Bytes content belongs to its publisher; keep this repository private.
- `scripts/fetch_archives.py` – re-runnable downloader (`pip install beautifulsoup4 markdownify`).

Usage: ask Claude to "draft The Point for `<org>` covering the last two weeks".
