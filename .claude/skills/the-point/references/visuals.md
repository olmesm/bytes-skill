# Visuals

Bytes averages seven images an issue and almost every one is either a meme with a caption or a logo. The pictures set the pace: they break the text every screen or so and tell the reader a section is starting. The Point keeps the rhythm and makes more of the pictures carry information.

Aim for 5 to 8 visuals: one hero, one small Spotlight image, one or two screenshots, one or two animations.

## Hero image (the meme slot)
The caption is the joke; the image only has to give it a face. Do not use film stills, celebrity photos or scraped memes: a company newsletter cannot rely on "everyone does it" for image rights, and a recognisable person is a guardrail problem.

In order of preference:
1. **Generate one** if the session has an image tool. Ask for an animal, object or anonymous figure in an absurdly specific situation ("a capybara in a hard hat staring at a wall of server racks, flash photo, slightly too close"). Animals and inanimate objects with emotions are reliably funny and offend nobody.
2. **Use the org's own material**: a screenshot of the thing itself, cropped tight, with a deadpan caption.
3. **Draw it** as an inline SVG or CSS scene. Simple and flat beats elaborate.

Give every image descriptive alt text.

## Screenshots
Show the real thing: the new UI, the CLI output, the dashboard after the fix, the before and after.

- Capture at 2x device scale, at a viewport of about 1200px wide, and crop to the part that matters.
- Use the template's `.shot` frame so screenshots look deliberate and are distinguishable from memes.
- Use seeded or demo data. Inspect every capture for names, emails, customer data, tokens, internal URLs and unreleased features before it goes in. If in doubt, redraw the UI as a simplified mock instead.
- One annotation at most (an arrow or a highlighted region). If it needs three, it needs an animation.

When the app cannot be run, a PR's own screenshots, a rendered docs page, or a styled terminal block built from real output are all fine. Say what it is in the caption.

## Animations
Each one should make a point faster than a sentence could. Prefer CSS and inline SVG over GIFs: they are sharp, tiny, theme-aware and easy to revise from a comment. The template includes working patterns:

| Pattern (class) | Shows | Typical use |
|---|---|---|
| Before/after wipe (`.wipe`) | Two screenshots, one sliding over the other | A redesign, a visual fix |
| Racing bars (`.race`) | Two or more bars growing to different lengths | Build time, latency, bundle size |
| Count-up stat (`.stat`) | A number ticking to its final value | Lines deleted, requests served |
| Typed terminal (`.term`) | A command typing itself, then its output | A new CLI, a one-line migration |
| Flow diagram (`.flow`) | Dots travelling along SVG paths | A new architecture, a removed hop |

For a real interaction (a drag, a transition, a multi-step flow), record the screen with the browser automation available and convert to a short looping video or GIF: under 8 seconds, under 2 MB, no cursor wandering.

Rules:
- Every animation states its numbers and its source in the caption, and the final frame alone must be truthful and readable.
- Bars and counts use real, proportional values. No dramatised scales.
- Honour `prefers-reduced-motion` (the template does): the reader sees the final state.
- Loops pause on the final state for a couple of seconds. Nothing flashes.

## Placement
- Hero above the Main Thing headline.
- The explaining visual directly after the paragraph it supports.
- Never two visuals back to back without text between them.
- Nothing after the last Cool Bit except the bug solution and the Receipts.
