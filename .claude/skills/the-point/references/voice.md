# Voice

The narrator is one person: a sharp, slightly unwell senior engineer who loves this stuff, reads every changelog, and cannot get through a paragraph without a tangent about their own life. They write "I", occasionally "we". They are on the reader's side against complexity, hype and YAML.

The ratio is about 70% straight information to 30% jokes. Strip every joke out and the issue should still be a clear, accurate briefing. The jokes are the reason people open it; the facts are the reason they keep it.

## How Bytes does it

Patterns observed across the archive, with short examples for calibration. Learn the move, write your own line.

### Titles
Two to five words. A pun on the product name, a pop-culture riff, or deadpan drama.
- Pun: "TanStack Attack", "Remix takes a SPA day", "CSS Panda-monium"
- Personification: "Hono wants it all", "Angular becomes an adult", "Storybook 9 thinks it can change me"
- Blunt question: "wtf is e18e?"
- Mock epic: "King Hejlsberg's Decree", "The Runtime Rumble", "War of the Bundlers"

For The Point: "The Monolith Loses a Limb", "Checkout Goes on a Diet", "wtf is the new deploy bot?"

### Teasers
Two real stories in disguise, then a personal absurdity.
- "Vite takes a stand, how to hack a credit card terminal, and things that taste like JavaScript."
- "How to quantify tech debt, how SvelteKit jumped on the View Transitions hype train, and how I made $75k at Burning Man."

### Hero captions
First person, present tense, a feeling rather than a description.
- "When QA'ing the code takes longer than writing the code"
- "Me trying to explain what a JavaScript bundler is to my family at Thanksgiving."
- "My test suite might be flaky, but it's also slow"

### Hooks
Open away from the subject and swerve into it.
- A riddle: "*How do you eat an elephant?* One bite at a time, obviously. *How do you rewrite SQLite from scratch in Rust?* No idea tbh, but…"
- A confession: "There's nothing worse than feeling out of the loop about a hip new numeronym."
- The calendar: "The Winter Olympics might've just ended, but the Petty Olympics kicked off again on Tuesday when…"

### Explaining
Once the hook lands, the prose turns plain and competent. Short sentences. Real numbers. A bold question to pivot ("**Why did they do this?**"), a signpost into the bullets ("Let's take a closer look at how the sausage gets made:"), and scare quotes around anyone's marketing claims, including the org's own.

### Bottom lines
A verdict the reader can repeat in a meeting, wrapped in an analogy.
- "…the IKEA of JS runtimes – giving you a minimal box of parts, some loose instructions, and the freedom to build exactly what you need…"
- "…either one of the most ambitious open-source projects of our time, or it's the greatest nerd honeypot ever devised. Either way, you have to respect the hustle."
- Occasionally a pure punchline that reframes the story: "I always knew I had a valid strategic reason for never writing unit tests."

### Cool Bit tails
Fact first, joke after, and the joke exaggerates the fact's own logic.
- "…comes with a whopping 84 new features, and Jen Simmons promised to perform an original ballad at my birthday party explaining each one in detail."
- "Do all these agent skills actually do anything? Unclear. But they do make humans feel like we're helping."

## The toolbox

| Device | How it works | Use |
|---|---|---|
| Strikethrough correction | Say the true thing, cross it out, say the polite thing: "in the eye of the ~~beholder~~ shareholder" | Once per issue at most |
| Buzzword™ | A trademark sign on a phrase everyone is tired of: "The Edge™" | Once or twice |
| Fictional autobiography | The narrator's implausible life: bids on eBay, a weird neighbour, a failed side hustle | The teaser's third item and one tail |
| Mundane analogy | Explain the abstract with the domestic: IKEA, a gym membership, a group chat | The bottom line |
| Mock grandeur | Treat a minor release like a coronation or a prize fight | Titles, hooks |
| Understatement | "It's not the *flashiest* release ever" for something huge or tiny | Anywhere |
| Callback | Return to the hook's image in the bottom line, or to a previous issue ("back in #12 we…") | The bottom line |
| Parenthetical aside | The narrator muttering: "(again)", "(mostly)", "kind of" | Sparingly |
| Faux-weary sign-off | "Either way, you have to respect the hustle." | Ends of paragraphs |

## Adapting it to an internal audience

Bytes teases public companies and famous maintainers. The Point's readers work with the people in the stories, so the targets move:

**Fair game:** the narrator; the codebase and its geology ("a file last touched when the office had a fax machine"); legacy systems; CI, YAML, flaky tests, dependency upgrades; meetings, ticket trackers, acronyms; industry hype; the abstract concept of estimates.

**Praise only:** every named colleague and team. The comedy about a person is how heroic the work was, never how the mess got there. "Tomás deleted 14,000 lines and the app got faster, which raises questions about the 14,000 lines" teases the lines, not whoever wrote them.

## Mechanics
- Write for readers whose first language may not be English: one idea per sentence, no slang that needs a decoder, idioms only when the meaning survives a literal reading. A joke that depends on a US-only reference needs a second route in or it goes.
- Contractions, yes. Exclamation marks, almost never. Emoji, at most two per issue.
- Bold for labels and the one phrase per paragraph that carries it. Italics for stress and for the narrator's asides.
- Inline `code` for every identifier, flag, file and command.
- Link the noun phrase that names the thing, not "here".
- Never explain a joke, never apologise for one, never stack two on the same fact.
