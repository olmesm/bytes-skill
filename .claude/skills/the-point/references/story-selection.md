# Finding the stories in a commit log

A fortnight of commits is noise. The job is to find the handful of changes a person in another team would be glad to hear about, and to say why.

## What makes a story

Score each candidate on these. The Main Thing should hit at least three.

| Signal | Looks like |
|---|---|
| **A reader can feel it** | Faster builds, a page that loads sooner, a step removed from a workflow, an error message that finally says what is wrong |
| **A number moved** | 40% fewer, 3x faster, 14,000 lines deleted, p95 from 900ms to 200ms. Take it from the PR or the benchmark, never estimate |
| **Something ended** | A migration finished, a legacy service switched off, the last use of an old library removed |
| **Something began** | A new service, a first release, a new team's first merge, a new contributor |
| **It has a plot** | A long-running PR, several attempts, a clever trick, an unexpected cause |
| **It is visible** | There is a UI, a dashboard, a CLI output or a diagram you can show |
| **Many hands** | A change that spans teams or repos |

Weak candidates: dependency bumps, formatting, config churn, routine version releases, anything whose honest summary is "maintenance continued". Several of these together can make one Cool Bit ("412 dependency updates merged themselves this fortnight, and nobody had to watch").

## Turning a change into a story

For each pick, answer four questions from the PR description, the diff and the discussion before writing a word:

1. **What was it like before?** The pain, in the user's or developer's terms.
2. **What changed?** One sentence a new joiner would understand.
3. **How?** The one or two interesting technical decisions. This becomes the bullets.
4. **So what?** What a reader can now do, stop doing, or steal for their own team.

If you cannot answer 1 and 4, it is a Cool Bit, not a Main Thing.

## Balance across the issue
- Spread the credit: different teams, repos, regions and seniority levels. Check the list of names before drafting. If one team has four mentions and another large one has none, look again.
- One visible front-end story and one deep back-end or infrastructure story, where the period allows.
- At least one item celebrating deletion, clean-up or documentation. That work is rarely thanked.
- At least one first-time contributor if there was one.
- The Spotlight goes to something other than the Main Thing's team.

## Keeping the thread
If earlier issues exist in `issues/`, skim the last two. Avoid repeating a lead team, follow up on anything promised ("back in #7 we said the migration was half done"), and keep the narrator's running jokes alive. Take the issue number from the last one plus one.

## Slow fortnights
If nothing clears the bar for a Main Thing, do not inflate a small change. Options, in order: a "how it actually works" explainer of a system people depend on and do not understand, built from the code; a retrospective on something that shipped a quarter ago and now has numbers; a round-up issue with a longer Cool Bits list and an honest title.
