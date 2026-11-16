# bytes-skill

A Claude skill for drafting **The Point**, a biweekly internal engineering newsletter written in the spirit of [Bytes](https://bytes.dev).

- `.claude/skills/the-point/` – the skill: workflow, anatomy, voice, guardrails, story selection, visuals, and the HTML template.
- `data/` – the Bytes archive: 538 raw pages in `html/`, 528 cleaned issues in `md/` and `index.json`. Ten 2021 issues (listed in `missing.json`) are served empty by bytes.dev, used as the reference corpus for the style analysis. Bytes content belongs to its publisher; keep this repository private.
- `scripts/fetch_archives.py` – re-runnable downloader (`pip install beautifulsoup4 markdownify`).

Usage: ask Claude to "draft The Point for `<org>` covering the last two weeks".
