---
name: the-point
description: Draft an issue of "The Point", a cheeky Bytes-style internal engineering newsletter, from an organisation's recent commits and pull requests plus a light pass over outside tech and mainstream news. Produces a single HTML page with screenshots and animations, ready for comments. Use when asked to write, draft or revise the newsletter, an engineering digest, or a "what did we ship" roundup for a GitHub/GitLab/other org over a period.
---

# The Point

An internal engineering newsletter in the spirit of Bytes: genuinely informative, short, and funny enough that people open the next one. The reader is a busy engineer at a multinational who owes you nothing. Every issue has to earn the scroll.

**Inputs:** an organisation (any git host), a period (default: the last 14 days, the newsletter is biweekly), and optionally a theme, an issue number, or stories the user wants in. If the org or period is missing, ask once; assume the rest.

**Output:** `issues/<YYYY-MM-DD>/index.html` with its images beside it, built from `assets/template.html`, then shared for comments.

The work is the editing and the writing. Gathering is a means: use whatever git, API or search tooling the session has and move on.

## Workflow

### 1. Gather (keep it light)
Pull merged PRs, notable commits, releases and tags for the period. Read titles and descriptions first; open diffs only for candidates. Record a link for everything you might mention. Stop gathering once you have roughly 20 candidates. You need one great story and a dozen small ones, not a census.

### 2. Pick the stories
Read `references/story-selection.md`. Choose one Main Thing, one Spotlight, 8 to 12 Cool Bits, and one bug for Spot the Bug. Drop anything sensitive (see guardrails) before you get attached to it.

### 3. Collect outside colour (5 to 8 searches, no more)
Skim the Hacker News front page, two or three engineering blogs relevant to the org's stack, and mainstream headlines from the period. You are looking for:
- hooks and analogies for your internal stories ("the same week Chrome shipped X, we…"),
- 2 to 4 outside links worth a Cool Bit on their own merit,
- one or two shared-culture references everyone has seen (a film release, a sports final, a viral product launch).

Outside news is seasoning. An issue is about what the org shipped. Never use news that fails the guardrails as a punchline, however topical.

### 4. Draft
Read `references/anatomy.md` (structure and budgets) and `references/voice.md` (how it sounds), then write the whole issue in Markdown-ish notes first. Facts before jokes: get each story correct and clear in plain words, then add the voice. Run `references/guardrails.md` as a checklist on the finished draft, joke by joke.

### 5. Visuals
Read `references/visuals.md`. Every issue needs a hero image for the Main Thing, at least one real screenshot, and at least one animation that explains something. Decoration that explains nothing gets cut.

### 6. Build and verify
Copy `assets/template.html`, fill the blocks, delete the ones you do not use. Keep each block's `id`, because comments refer to them. Open the page in a browser at desktop and phone width, light and dark, and look at a screenshot before you share it: check for broken images, overflowing code, and animations that actually run.

### 7. Share for comments, then revise
Publish the page wherever the session supports commenting (an artifact if available, otherwise hand over the file) and give the user a five-line summary: the title, the Main Thing, anything you left out on purpose and why, and any joke you were unsure about. When comments come back, change what was asked and nothing else, and republish at the same address.

## Rules that do not bend
- **True first.** Every statement about the org traces to a commit, PR or release you read. Numbers come from the source, never from vibes. The Receipts block at the foot of the page lists the links. If you cannot verify it, cut it.
- **Credit generously, tease never.** Name the people who did the work when praising. Jokes land on the narrator, the codebase, the tooling and the industry.
- **Its own newsletter.** Borrow Bytes' craft, not its words, branding, section artwork or jokes. Nothing is copied from `data/`.
- **Short.** 700 to 1,000 words. If it is longer, a story has to go, not the margins.
