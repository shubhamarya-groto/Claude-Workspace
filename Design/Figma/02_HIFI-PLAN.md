# High fidelity plan

Written 19 Sep 2026 (Sat evening), after R1 structure landed in section
`1032:3`. Draft due **Mon 21 Sep EOD**. Sunday and Monday remain.

Structure came in ahead of schedule, which buys back most of a day. Spend it on
components, not on styling bands one at a time.

---

## The one rule that decides how long this takes

**Build components first, place them second.** There are seven new blocks to
make and twelve bands to fill. Styling each band inline means building the same
card five times and rebuilding all of them when a colour changes. Every hour
spent on a proper component with variants pays back twice on Monday.

Corollary: **nothing gets a hex value and nothing gets a manual font size.**
Bind to the Color Mode variables and the type tokens. That is what makes a late
decision from Brian a one-edit change instead of a Monday night rebuild.

---

## Phase 0 · Lock three decisions before any pixel

Thirty minutes, and it saves hours.

1. **Button colour (I-01).** Orange on white fails AA. Every band has buttons.
   Decide now or restyle twelve bands later. Recommendation: navy label on the
   orange fill.
2. **Fork treatment (I-02).** Band 01 has two identical dark buttons, band 11
   has one orange and one dark. Same choice, two treatments. Pick one.
3. **Does band 04 merge into 05/06 (I-05)?** Affects the band count and the
   whole vertical rhythm. Cheap now, annoying later.

If Brian is not reachable, take the accessible option and annotate it as a
recommendation. A draft that passes contrast and gets corrected is better than
one that fails and has to be redone.

---

## Phase 1 · Foundations (Sunday, first hour)

1. **Marketing text styles.** The tokens exist (`text-4xl` 72 down to
   `text-xs` 12, Instrument Sans for display, Inter below). Create the four
   ladder styles as real Figma text styles if they are not already published:

   | Style | Desktop | Mobile | Face |
   |---|---|---|---|
   | Display / H1 | `text-4xl` 72 | `text-3xl` 48 | Instrument Sans |
   | Heading / H2 | `text-2xl` 30 | `text-xl` 24 | Inter Bold |
   | Subhead / H3 | `text-xl` 24 | `text-lg` 18 | Inter SemiBold |
   | Body | `text-md` 16 | `text-sm` 13 | Inter Regular |

2. **Audit the R1 file for loose values.** Anything typed as a hex or a raw px
   in the structure round gets bound now, before it multiplies.

3. **Grid and rhythm.** 1440 frame, one content width, one section padding
   value, one gap value, all off the spacing tokens. Decide once so twelve
   bands do not each invent their own.

---

## Phase 2 · Components (Sunday, the bulk of the day)

Build in this order. Earlier ones are used by later ones.

| # | Component | Variants / properties | Used by |
|---|---|---|---|
| 1 | **Input field** | Default, Focus, Filled, Error · label, placeholder, icon | Sub-page search widgets. **The system's biggest gap** |
| 2 | **Step card** | Number, title, body · numbered / plain | Bands 05, 06 |
| 3 | **Stat block** | Value, caption, rule on/off | Band 03 |
| 4 | **Testimonial card** | Voice = Worker / Employer · quote, name, location, avatar on/off | Band 08 |
| 5 | **FAQ row** | Collapsed / Expanded · question, answer | Band 10 |
| 6 | **Pricing column** | Style = Problem / Solution · heading, value, list | Band 09 |
| 7 | **Footer trade column** | Heading, URL stub, trade list | Band 12 |

Plus the two cards already half-done in R1:

- **Job Seeker preview card**, Brian's design, promote to a real component
- **Job Match Card**, the merge of Brian's Job Post card and DS `891:189`,
  publish the merged version back to the Design System page so the product and
  the marketing site stop diverging

**Build them on the Design System page next to the existing five**, not loose on
the Presentation page. That is what makes the trade page templates possible
later, and it is what Brian asked for when he said he wants the cards built as
components to stop the endless feedback loop.

**Avatar note for the testimonial card:** build it for the thinnest content,
quote plus name plus location, with the avatar as a layer you can switch off.
Photos may never arrive.

---

## Phase 3 · Bands to high fidelity

Order by what wins the approval, not by page order. If Monday runs out, the
bottom of this list is what goes unfinished, and that is the right thing to lose.

1. **01 Hero + fork.** The whole argument. Includes the photo treatment.
2. **07 Preview cards.** The product shown rather than described. Fix I-07 here.
3. **03 Problem + stats.** Fix I-04 while you are in it.
4. **05 / 06 How it works.** Absorb band 04 if Phase 0 said yes.
5. **08 Testimonials.** Swap the sides, I-03.
6. **11 Final CTA.** Must mirror band 01, I-02.
7. **10 FAQ.**
8. **12 Footer.**
9. **02 Trust bar.** Small.
10. **09 Pricing.** Last, deliberately. Brian may cut it, so it is the cheapest
    thing to leave rough.

---

## Phase 4 · The photo layer (Monday morning)

**One real asset exists:** the welder, 1400 x 799, currently shown at 380 x 326
inside a rounded card in Brian's mockup. His note 1 asks for it integrated
rather than boxed. There is 3.7x more image than is being used, so:

- Bleed it off the right edge of the hero, overlapping the type block.
- Mask it into a shape rather than a rectangle, so it reads as part of the page
  rather than a placed picture.
- Keep the headline off the photo entirely. The mobile audit rates white text on
  that photo a **Critical** contrast failure, and the fix is not to overlay it
  better, it is to not overlay it.

**Every other image slot stays a spec box**, not stock. A grey frame reading
"PHOTO · crew on site · 2400px min · subject with 20% breathing room" is honest
and tells Brian exactly what to send. Fake stock in a client draft gets approved
and then cannot be matched.

---

## Phase 5 · Mobile (Monday afternoon)

Full mobile for twelve bands will not fit in the time. Do these four at 375,
which is where the audit found Critical failures and where the two-sided
argument either survives or breaks:

1. **01 Hero + fork.** Headline capped at two lines, `text-3xl` 48. Fork cards
   stack. This is the Critical contrast finding.
2. **07 Preview cards.** Card rows stack or scroll horizontally.
3. **05 / 06 How it works.** Two columns become one, and the employer-first
   order has to survive the stack.
4. **08 Testimonials.** Same stacking question.

Note on the rest: annotate the stacking rule rather than drawing it. A written
rule Brian can agree to is worth more on Monday than four more drawn frames.

---

## Phase 6 · Make it approvable (Monday, last two hours)

This is what turns a layout into a one-pass approval, and it is the part people
skip when they run late. Protect it.

1. **Annotation frame above each band**: what the band does, where the copy came
   from, and what changed from Brian's mockup. Four of the twelve bands are
   changes he has not seen yet, so each needs its reason attached.
2. **A recommendations frame** at the top of the section, listing the four moves
   and the contrast fix, each with the evidence. Brian asked for exactly this:
   "let me know if there are any changes you strongly recommend".
3. **A contrast redline**: the three measured ratios (2.63, 3.28, 13.82) next to
   the buttons they describe. A number is harder to argue with than an opinion,
   and he asked for guidelines proven to work.
4. **Placeholders labelled honestly**: what is grey, and who it is waiting on.

File conventions from `00_FIGMA-WORK-LOG.md`: new top-level section on the Presentation
page, never edit R1 in place, annotation text light on the dark grey section
background, "Created by Claude" attribution where it applies.

---

## What will not be finished, and that is fine

Say this out loud on Monday rather than letting it be discovered:

- Mobile beyond the four bands above, annotated instead of drawn.
- Photography beyond the hero, spec boxes instead.
- Testimonial avatars, pending Brian.
- Pricing band, deliberately rough pending the model decision.
- The two sub-pages. R1 and hi-fi are the homepage only. For companies and For
  workers are a separate round, and they are where the search widgets and the
  company preview card live.

That last one is worth flagging early. Brian's mockup is three pages. This draft
is one of them.
