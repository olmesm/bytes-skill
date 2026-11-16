# Anatomy of an issue

Derived from the 528 Bytes issues with content (2020 to 2026; ten 2021 issues are empty on the site). The format settled around issue 100 and has barely moved since, which is the strongest evidence that it works: roughly 1,000 words, 20 links, 7 images, a title of about 4 words, one deep story and a dozen one-liners.

The Point keeps that skeleton and swaps the commercial slots for internal ones.

| # | Block (`id`) | Bytes equivalent | Budget |
|---|---|---|---|
| 1 | Masthead (`masthead`) | Banner, title, issue number, date | Title of 2 to 5 words |
| 2 | Teaser (`teaser`) | "Today's issue:" | One sentence, three items |
| 3 | The Main Thing (`main-thing`) | The Main Thing | 250 to 350 words |
| 4 | Spotlight (`spotlight`) | Our Friends (With Benefits) | 100 to 150 words |
| 5 | Spot the Bug (`spot-the-bug`) | Spot the Bug / Pop Quiz | 10 to 25 lines of code |
| 6 | Cool Bits (`cool-bits`) | Cool Bits | 8 to 12 items, 1 to 3 sentences each |
| 7 | Bug solution (`bug-solution`) | Spot the Bug: Solution | 2 to 4 sentences plus the fix |
| 8 | Receipts (`receipts`) | none | Collapsed list of source links |

## 1. Masthead
The issue title is the Main Thing's headline. It is the subject line, so it does the most work of any words in the issue. Under it: `Issue #N · date · N minute read`.

## 2. Teaser
`Today's issue:` followed by exactly three items in one sentence. Items one and two point obliquely at real stories in the issue without naming them. Item three is an absurd personal non sequitur from the narrator that is paid off, loosely, somewhere below. The reader should not be able to guess the stories, only want to.

Then one flat line: `Welcome to #N.`

## 3. The Main Thing
One story, the best of the fortnight. Fixed order:

1. **Hero image and caption.** A picture with a one-line "When you…" or "Me, …ing" caption about a feeling every engineer recognises. It is the meme, and it sits above the headline.
2. **Headline.** Same as the issue title.
3. **Hook.** One or two sentences that start somewhere outside the story (a news item, a shared experience, a confession) and arrive at the news by sentence two or three, with the link.
4. **Why.** What problem this solves and why anyone should care, in plain words. Often framed as a bold question: `**Why did the payments team do this?**`
5. **Three bullets.** Introduced by a line like "Here's what changed:". Each bullet is `**Bold label** – one or two sentences`. All three inform; one may end on a wry tail.
6. **Bottom line.** `**Bottom line:**` plus one or two sentences. A verdict, with an analogy or a callback to the hook. This is where the best joke goes.

Put the screenshot or animation between the why and the bullets, or after the bullet it illustrates.

## 4. Spotlight
Bytes uses this slot for a sponsor, written in the same voice as everything else. Here it advertises something internal that deserves more users or more thanks: a platform team's new tool, a migration people keep putting off, a team whose unglamorous work held everything up this fortnight. Same shape in miniature: small image and caption, linked headline, three short paragraphs, a clear call to action ("Try it on your service", "Go say thanks in #platform").

## 5 and 7. Spot the Bug
A short snippet with one real bug, taken from something actually fixed in the period and reduced to its essence. The puzzle sits mid-issue; the solution goes at the very bottom so the reader scrolls past Cool Bits to reach it. The solution names the bug in one sentence, explains why it bites in one or two more, and shows the fix. Link the real PR and credit the fixer. If no fix in the period makes a fair puzzle, run a `Pop Quiz` (what does this log?) or drop the block. Never use a security fix.

## 6. Cool Bits
A numbered list. Each item is one linked fact, optionally followed by one sentence of commentary.

- Mix about two thirds internal (smaller merges, releases, a nice refactor, a deleted pile of dead code, a new contributor's first PR) with one third outside links from the news pass.
- Start most items with who did it: "Priya rewrote…", "The search team shipped…".
- Only about half the items get a joke. The straight ones give the funny ones room. Three jokes in a row reads as trying.
- Put the strongest item first and the oddest or warmest one last. The last Cool Bit is the issue's send-off; there is no sign-off paragraph.

## 8. Receipts
A collapsed `<details>` list of every commit, PR, release and article the issue relied on. It keeps the prose free of link clutter and lets a reviewer check any claim in one click.
