# Marketing homepage structure, v2

Rewritten 19 Sep 2026 after reading **Brian's actual mockup** (the emailed
`GoFindBuild-Marketing-Site-All-Pages.html`, now in `Design/Figma/Source files/`) and his brief
in `Project Context/2026-09-11_Brian-Mockup-Brief.md`.

Supersedes v1. Four things in v1 were wrong, listed at the bottom.

---

## The brief, in Brian's own words

> "my goal is to have you re-create this in Figma with all standard practices to
> optimize the font, layout, user journey and overall let me know if there are
> any changes you strongly recommend so we can discuss."

**This is not a redesign. It is a re-creation plus optimisation, with
recommendations.** Brian has already built the structure, written the copy he
wants ("I've included all the copy that I like"), and drawn three preview cards.
That is a much smaller Monday than v1 assumed, and it is what he actually asked
for.

His three specific notes:
1. The welder-with-sparks photo should be **better integrated into the page
   instead of in its own little card**. Anywhere else a photo could help, he is
   interested.
2. The pricing diagram is a **placeholder**. It was for the Tuesday discussion
   and **may be left out initially**.
3. Some of the informative cards are **too static or dull**, optimise them.

He also asks for the three preview cards to be built as Figma components, and
says expanded profiles and dashboard finals are next.

---

## What Brian's mockup already contains

Three pages, all with finished copy.

**Home:** nav · hero with a built-in **two-sided fork** (I'm hiring / I'm
looking for work) · trust bar (direct employer connections, no recruiter
middlemen, 150+ trade categories) · framing line · **two separate three-step
flows**, one per audience · **two real testimonials** · four stats · a problem
statement · split final CTA · footer with legal links.

**For companies:** "Build your workforce. Not your recruiting bill" · trade and
zip search · 0% placement fee · a live **worker preview card** (Marcus Bell, 92%
profile score) · the pricing comparison · CTA.

**For workers:** "Always free for workers" · trade and zip search · a live **job
preview card** (General Laborer, $23/HR) · three steps · CTA.

**The structure is sound.** The fork is already there, the dual three-step flows
are already there, the legal links the audit asked for are already there. Most
of what v1 proposed, Brian had already done.

---

## The four moves I would recommend

Everything else is re-creation. These are the changes worth arguing for, and
Brian explicitly asked for them.

### 1. Move the problem up. It is currently last.

The page runs hero, fork, solution, how it works, testimonials, stats, and only
then reaches:

> "The workers are out there. The opportunities are out there.
> **The connection between them is broken.**"

That is the best line on the site and it is sitting in second-to-last position.
The meeting logged the page as missing problem awareness. It is not missing, it
is at the bottom, which is the same thing from a conversion point of view. Move
it up behind the trust bar and let the four stats sit under it as evidence.

Costs nothing. It is a re-order of copy that already exists.

### 2. Put the preview cards on the homepage.

The job card and the worker card only appear on the sub-pages. They are the
strongest assets on the site: they show the product working rather than
describing it. A visitor who never clicks through never sees the thing they are
being sold. Put one of each on the homepage after the how-it-works flows.

### 3. Add an FAQ. There is none anywhere.

Sixteen seeds are in `Read me/01_NEXT-ACTIONS_Marketing-Site.md`; the nine not used on the homepage are parked in `Read me/04_FAQ-SEEDS_sub-pages.md`. This is also the only band on the page
that gives GTM anything to rank on, which matters given the trade pages coming.

### 4. Fix the button contrast. Details below, it is the big one.

---

## The contrast problem, measured

Brian asked to "follow the best guidelines proven to work best". Measured
against WCAG on his own mockup:

| Button | Colours | Size | Ratio | Verdict |
|---|---|---|---|---|
| Get started, Hire workers, Post a job, See who's available, Full-time pill | `#F77F00` + white | 14 to 16px, 700 | **2.63:1** | Fails AA **and** AA-Large |
| Apply now, Send job, See jobs near me, Create my free profile, View, View profile | `#0095E2` + white | 14 to 16px, 600 | **3.28:1** | Fails AA. Clears 3.0 but the text is not large enough for AA-Large to apply |
| **Find jobs** | `#003049` + white | 14px, 700 | **13.82:1** | **Passes comfortably** |

AA needs 4.5:1 for normal text. Large text means 24px regular or 18.7px bold and
up, which none of these are.

**So every orange and every blue call to action on the site fails. The only
compliant primary action is the navy one Brian already drew.**

That is also the fix, and it is a good one: **promote the navy `#003049` button
to be the primary action everywhere, and keep orange for accents that do not
carry text.** It is not a request to change the brand, it is a request to use
the button he already designed. The orange stays exactly where it is strong, in
the wordmark, the icons, the progress dashes, the hero accent word.

Same defect exists in the design system, and slightly less badly:
`primary/default` `#f16c0e` measures 3.05:1, with a 16px Medium label. So this
needs fixing in **both** places or they drift further apart.

---

## Reconciling the mockup with the design system

They are closer than they look. The page background is an exact match.

| Role | Brian's mockup | Built Bold DS | Call |
|---|---|---|---|
| Page background | `#F6F7F9` | Blue ramp step 0 `#F6F7F9` | **Identical already** |
| Muted text | `#525E77` | `muted/foreground` `#525c70` | Near identical, take the DS value |
| Brand dark | `#003049` | Navy 780 `#16243D` | **Needs a decision.** Brian's is more teal, the DS is more blue |
| Primary accent | `#F77F00` | `primary/default` `#f16c0e` | **Needs a decision.** Both fail contrast on white |
| Action blue | `#0095E2` | **nothing** | **New to the system.** Either adopt it as a token or drop it in favour of navy |
| Display face | Open Sans | **Instrument Sans** | Take the DS. Brian asked to optimise the font |
| Body face | Inter | Inter | Identical |

Recommendation: build Monday on the **design system** values, since Brian asked
for standard practice and font optimisation, and show the mockup and the
system-built version side by side so the swap is a visible, arguable choice
rather than a silent one.

---

## Components

**Reuse as-is:** Top Nav `790:11423`, Button `787:10782`, Chip `790:11387`.

**Reconcile, do not duplicate.** Brian's three preview cards overlap what the
system already has:

| Brian's card | System equivalent | Action |
|---|---|---|
| Job Post preview (AC, $38/HR, Full-time, Apply now / View) | **Job Match Card `891:189`** (94% Match, $28/hr, Apply) | Same component designed twice. Merge into one, keep Brian's pay-and-distance emphasis and the system's match percentage |
| Job Seeker preview (Private Profile, 96% profile score, Looking for / Experience) | **Profile Checklist Item `890:179`** | Related but not the same. Build the seeker card new, reuse the checklist item inside the expanded profile later |
| Company preview (Ironside GC, Services, Residential/Commercial/Industrial) | nothing | Build new |

**Still to build:** hero, stat block, step card, testimonial card, FAQ accordion,
footer, pricing comparison, and **an input field**. The two search widgets
(trade + zip) need one and the system has no form component at all.

---

## The structure to build

| # | Band | Source | Change from Brian |
|---|---|---|---|
| 0 | Top Nav | `790:11423` | Use system nav. His has Home / For companies / For workers, the system's has Companies / Job Seekers / Pricing. Reconcile |
| 1 | Hero + fork | Mockup | Keep. Integrate the welder photo per his note 1 |
| 2 | Trust bar | Mockup | Keep |
| 3 | **Problem + stats** | Mockup, **moved up** | **Move 1.** Currently sits at position 8 |
| 4 | Framing line | Mockup | Keep |
| 5 | How it works, hiring | Mockup | Keep |
| 6 | How it works, working | Mockup | Keep |
| 7 | **Preview cards** | Sub-pages, **promoted** | **Move 2.** Currently sub-pages only |
| 8 | Testimonials | Mockup | Keep. **Two real quotes already exist** |
| 9 | Pricing comparison | Mockup | **Soft.** Brian calls it a placeholder and may cut it |
| 10 | **FAQ** | New | **Move 3.** None exists anywhere |
| 11 | Final CTA | Mockup | Keep |
| 12 | Footer + Browse by trade | Mockup + new | Legal links already there. Add the trade columns |

---

## The hero photo

Brian's note 1 is the one visual ask he made directly. The welder photo is
**1400 x 799**, currently displayed at **380 x 326 inside a 12px rounded card**
on the right of the hero.

So there is roughly 3.7x more image than is being shown. Plenty of headroom to
take it out of the card: bleed it off the right edge, mask it into a shape that
overlaps the type block, or run it as a wide band under the fork. The constraint
I flagged in v1 does not apply here, that was the live site's excavator photo.

---

## What v1 got wrong

1. **The HTML is Brian's mockup, not a capture of the live site.** Everything v1
   inferred from "the current site" was reading his proposal as the status quo.
2. **Testimonials exist.** Two real ones, Matthew B. a carpenter in Noblesville,
   and Brothers Insulation & Construction in Indianapolis. Band 8 is not grey.
3. **Pricing is not the $99 / $199 / $399 unlock model.** Brian's mockup replaces
   it with flat monthly against a staffing agency's 18 to 25% markup. Lifting the
   old numbers onto the page would have pushed a model the business is moving off.
4. **The hero is not capped at 1024px.** That was the live site's photo. Brian
   supplied a 1400 x 799 one.

Also obsolete: the "023" stat typo and the profanity banner are both already
gone from Brian's copy. The stats are updated too, 94% became 88% and $55k
became $58k.
