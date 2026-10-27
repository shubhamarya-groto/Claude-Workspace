# Issues log, marketing site

Running log. Opened 19 Sep 2026 against **R1 structure**, section `1032:3`
("2026-09-19 · Marketing Site R1 · Homepage Structure").
R2 (section `1061:134`, 21 Sep) applies I-04, I-05, I-08, I-10 and I-17. Band
numbers differ in R2, see the translation table in the R2 section at the bottom.

Severity: **A** blocks approval or ships a defect · **B** weakens the page,
fix before hi-fi · **C** tidy-up.

| ID | Sev | Band | Issue | Fix | Status |
|---|---|---|---|---|---|
| **I-01** | **A** | 01, 11, nav | **Orange CTAs fail WCAG AA.** `#f16c0e` + white is 3.05:1 at 16px Medium. Affects Get Started (nav), Post a job (band 11), every orange button that lands later | Navy `#16243D` label on orange (~5.1:1), or navy fill with white. Decide once, apply everywhere | Open, needs Brian |
| **I-02** | **A** | 01 vs 11 | **The two fork buttons are styled differently in the two places they appear.** Band 01 has both dark and identical. Band 11 has one orange, one dark. Same two choices, two treatments | Pick one and mirror it. The fork is where the visitor self-selects, so the two paths should be visually distinct in both places | Open |
| **I-03** | **C** | 08 | **Testimonials flip the side convention.** Every other two-column band is employer left, worker right (hero fork, 05/06, 07, 10). Band 08 is worker left, employer right. **Inherited from Brian's mockup order, not introduced in R1.** Why it matters: each quote is peer proof for its own side. Matthew B. is a worker persuading workers ("surprised what companies were willing to pay"), Brothers Insulation is an employer persuading employers ("experienced workers ready to go"). Peer proof lands best in the reader's own column | Swap, so each quote sits in its own audience's column. Or keep worker-first deliberately, as a stated choice. **Downgraded B to C, 21 Sep** | Open |
| **I-04** | **B** | 03 | **"WHY WE BUILT GOFINDBUILD" re-imports the inward frame.** The stats were moved up to be evidence for the visitor's problem. That overline makes them company backstory again, which is the exact thing the move was meant to fix | Re-head outward, or drop the overline and let the stats sit under the problem line | **Resolved in R2** (overline now WHAT'S AT STAKE) |
| **I-05** | **B** | 03, 04 | **Two consecutive centred type-only bands.** Problem statement then framing statement, back to back, no change of form between them. Band 04 is really the intro to how-it-works | Absorb band 04 into the top of 05/06 as its section header. Removes a band and fixes the rhythm | **Resolved in R2** (framing line folded into how it works) |
| **I-06** | **B** | 09 | **Pricing is company-only on a deliberately two-sided page.** A worker scrolling hits a band that has nothing for them, right after testimonials that did | Label it explicitly for employers, or move it to the For Companies page. Brian may cut it anyway | Open, tied to pricing decision |
| **I-07** | **B** | 07 | **Preview cards are not labelled by whose view they are,** and are structurally asymmetric: the seeker card has two actions (Send job, View profile), the job card has one (Apply) | Add "What you see as an employer" / "What you see as a worker". Give both cards the same action count | Open |
| **I-08** | **B** | 07 | **Zip codes do not match the cities.** "Matches near 75201" is Dallas and "Jobs near 97206" is Portland, but both cards say Indianapolis, IN. Inherited from Brian's mockup | Use Indianapolis zips, or drop the zip from the label | **Resolved in R2** (both zips 46204). Carry to the sub-pages |
| **I-09** | **C** | 01 | **Hero emphasis shifts the meaning.** Brian set only "and" in orange, highlighting the joining of two sides. R1 sets "and workers meet" in orange, which tilts a deliberately balanced headline toward the worker side | Return the accent to "and", or accent a word on each side | **Withdrawn 21 Sep.** Brian's mockup does accent "and workers meet". My earlier reading was wrong |
| **I-10** | **C** | 10 | Sixteen accordion rows is a tall band (860px) and becomes sixteen stacked rows on mobile | **Superseded by the single curated FAQ proposal, 21 Sep:** one column of 7, audience named in each question, cost split into two adjacent rows, remaining seeds move to For companies / For workers. Same pattern Wellfound uses (6 questions, one list) | **Resolved in R2** (one curated list of 7) |
| **I-11** | **C** | 12 | Hire-by-trade and Jobs-by-trade list the identical twelve trades | Probably fine, but GTM may want different sets per side | Open, GTM |
| **I-16** | **B** | 10 | **Two FAQ seeds are stale against Brian's copy.** "What if I do not want to interview anyone I am sent?" only makes sense under per-applicant pricing, which his mockup drops for flat monthly. "How does the paid training work?" refers to a feature only the old live site mentions, Brian's copy never does | Cut the first. Confirm paid training still exists before the second goes anywhere | Both left out of R2. Confirm paid training exists before it goes on the For workers page |
| **I-17** | **C** | 05/06 | **The two how-it-works flows did not line up.** The hiring title wraps to two lines (100px header), the working title to one (64px), so the working steps sat 36px higher, and unequal step heights made the gap grow by step 3 | Same header height on both, same row height per pair of steps | **Fixed in R2**, 21 Sep. Step tops now identical |

## Carried from earlier, still true

| ID | Sev | Issue | Status |
|---|---|---|---|
| **I-12** | **A** | Pricing model unresolved. Brian's mockup shows flat monthly, the live site shows per-applicant $25/$99/$199/$399. The 15 Sep notes record no decision | Open, Brian |
| **I-13** | **B** | Design system has **no input component**, and the two sub-page search widgets need one | Open, build |
| **I-14** | **B** | Nav mismatch. Brian's mockup uses Home / For companies / For workers, the DS nav uses Companies / Job Seekers / Pricing. R1 uses the DS nav. Sets the URL structure | Open, Brian |
| **I-15** | **C** | Only one real photo exists (welder, 1400 x 799). Every other image slot is a grey spec box | Open, Brian |

## Closed

| ID | Issue | Resolution |
|---|---|---|
| I-00a | Problem section "missing" | Not missing, was last. Moved to band 03 in R1 |
| I-00b | Job card designed twice (Brian's vs DS `891:189`) | Merged in R1 band 07 |
| I-00c | No FAQ anywhere | Added as band 10 with 16 seeds |
| I-00d | Trade pages had no home in the sitemap | Footer now carries `/hire/{trade}` and `/jobs/{trade}` |

## Verification notes, 19 Sep evening (checked against Brian's source file and R1)

- **I-09 premise is wrong.** Brian's mockup colours the whole phrase "and
  workers meet" orange (a span around that phrase inside the h1). R1 matches it
  exactly. Accenting "and" alone would be a deliberate departure from Brian's
  design, not a return to it. The balance argument may still be worth making,
  but as a recommendation to Brian. Not applied.
- **I-02 description does not match R1 as built.** R1 has two identical dark
  buttons in band 01 and two identical dark buttons in band 11: consistent, but
  the two paths are not visually distinct. "One orange, one dark" describes
  Brian's own band 11 (orange Post a job, outlined Find work, on a navy band).
  The fix still stands: distinct paths, the same pair in both places.
- **Brian's colour coding, for the I-01 / I-02 fix.** Employer paths are orange
  (Hire workers, Post a job, Get started), worker paths are navy (Find jobs).
  Keeping that mapping with a navy label on the orange fill (5.09:1 measured,
  `#16243D` on `#F16C0E`) satisfies both issues at once.

## R2 pass, applied 21 Sep

Section `1061:134` ("2026-09-21 · Marketing Site R2 · Homepage Structure"), a copy
of R1 placed to its right at X 2560, Y 0. R1 (`1032:3`) is untouched. Applied on
the copy only:

| Issue | What changed in R2 |
|---|---|
| I-04 | Stats overline is "WHAT’S AT STAKE" (alternative held back: "THE GAP, IN NUMBERS"), centred over the stats row |
| I-05 | Band 04's headline and subhead are now the shared header of the merged how-it-works band. Old band 04 and its note deleted. One hairline on top of the merged band so it does not blend into white band 03 |
| I-17 | Both flow headers 100px, each pair of steps the same row height. Step tops match at 2839, 2950 and 3035 |
| I-08 | "Matches near 46204" and "Jobs near 46204". The same two zips still need fixing on the For companies and For workers pages when they are built |
| I-10 | One centred column of seven questions, no group subheads. Flag reads "6 OF 7 ANSWERS FROM BRIAN’S COPY · COST WAITS ON PRICING". Band is 753px, was 860. The other nine seeds are in `04_FAQ-SEEDS_sub-pages.md` |
| Notes and header | Rail rebuilt for 11 bands with the new numbers, aligned to each band. Header summary, moves list (now five) and sequence comparison updated |

**Band numbers changed in R2.** Every R1 number in this log stays as written. To
translate: R1 04 is folded into R2 04/05 · R1 05 is R2 04 · R1 06 is R2 05 ·
R1 07 is R2 06 · R1 08 is R2 07 · R1 09 is R2 08 · R1 10 is R2 09 · R1 11 is R2
10 · R1 12 is R2 11. Bands 00 to 03 are unchanged.

**Found while working.** R1's band 09 (pricing) had been edited after Saturday:
it is now three tiers ($49 a month, $149 a month, Custom) instead of the
agency-versus-flat-monthly comparison. R2 copies it as it stands and its note
says so. The figures are not in Brian's copy, and the heading still reads as the
agency comparison, so heading and cards no longer match. Side effect in R1,
left alone: band 09 grew by 110px, so R1's notes rail is misaligned from that
band down and the section is 110px too short for its content.

**Deliberately not in this pass:** I-01 and I-02 (fork buttons, both severity A,
settle before any button is styled), I-03, I-06, I-07, I-09 (premise wrong, see
the verification notes), I-11, and the two waiting on Brian, I-12 and I-14.

## Client feedback tracker (Figma comments, from 22 Oct 2026)

A running list of client comments from the hi-fi frames. When a new comment
comes in, add a row to the work queue and a row to the verbatim table, then
re-rank. Dates are worked out from the relative times Figma showed on 22 Oct
("3 days ago" is about 19 Oct, "13 to 18 hours ago" is 21 Oct).

**Priority:** P0 is first. Each item has its own rank, so the queue is the
working order. Live-site defects come first because people can see them now.
After that, small asks with copy or direction already settled, then work that
needs sourcing or design time.
**Effort:** **Fast** is under about an hour, once access or a decision is in
place. **Takes time** is half a day or more, or it waits on sourcing or on
rounds of review.

### Work queue

| Pri | ID | Item | Where | Effort | Estimate | Waiting on | Status |
|---|---|---|---|---|---|---|---|
| **P0** | I-22 | "Less searching." on its own third line in the Job Seeker hero headline | Live HubSpot | **Fast** | 15 min | – | **Done, published 22 Oct** |
| **P1** | I-23 | "For Companies / For Job Seekers" section is stretched on HubSpot; make it match Figma | Live HubSpot | **Fast** (if it's a width or column setting) / **Takes time** (if the module needs rebuilding) | 30 min to 2 h | – | **Done, published 22 Oct** |
| **P2** | I-24 | Add a small "Our Vision" section to the **About Us page**, using Brian's copy word for word | Figma, then HubSpot | **Fast** | 1 h (Figma) + 1 h (HubSpot) | – | **Done, published 22 Oct** (About Us only) |
| **P3** | I-20 | Swap the Company hero photo for a real jobsite shot with less polished workers | Figma, then HubSpot | **Takes time** (the swap itself is fast; finding a photo that passes is the slow part) | 2 to 4 h incl. sourcing | – | **Done, published 23 Oct** (C1) |
| **P4** | I-21 | Swap the Job Seeker hero photo, same brief as I-20 | Figma, then HubSpot | **Takes time** (same as I-20) | Shared with I-20 | – | **Done, published 23 Oct** (J1) |
| **P5** | I-18 | Plumbing page is a campaign landing page, so the header is logo only with no main nav | Figma | **Fast** | 15 min + a reply to Brian | – | **Done 23 Oct**: treated as a campaign landing page. Shubham's Figma redesign (`1528:10672`) is built on HubSpot; the header is the logo only, no main nav |
| **P6** | I-19 | Redesign the Plumbing hero (approved, no direction given) | Figma | **Takes time** | 1 day incl. explorations | – | **Done, published 23 Oct**: Shubham redesigned it in Figma (`1528:10672`), built as `gfb_hero_signup` |

**Fast fixes, can go out together:** I-22, I-24, I-18, and I-23 if the
cause is a setting.
**Takes time:** I-19, plus I-20 and I-21 because of photo sourcing.

### Verbatim threads

| ID | Pri | Sev | Frame | Thread (verbatim) | What it means / action |
|---|---|---|---|---|---|
| **I-18** | P5 | **B** | Plumbing · Hi-Fi, top of page (logo bar) | **Team Groto, ~19 Oct:** "@Brian Oltmanns I am not sure where Plumbing page sits in Sitemap, is it interal page for companies or how does someone reaches it. Knowing it will help me set the top nav for this page." **Jeff Keller, ~19 Oct:** "I'm pretty sure that's a landing page for ads and promotional emails" | Treat Plumbing as a **campaign landing page** (traffic from ads and email), not a page in the main nav. That supports keeping the header to the logo only, with no main nav, so visitors stay on the page and its form. Brian hasn't confirmed this; Jeff's answer is a "pretty sure". Linked to I-14 (nav / URL structure) |
| **I-19** | P6 | **B** | Plumbing · Hi-Fi, hero (photo, headline, claim-profile form) | **Team Groto, ~19 Oct:** "I am considering redesigning the hero section. let me know if I can proceed with it, or should we keep it same as it is now. Also if you have any ideas in mind for Hero section of Plumbing do share." **Brian Oltmanns, 21 Oct:** "Yes, please proceed with the redesign" | Brian approved the hero redesign. He shared no direction, so the design is ours. Keep what the page already has: the `{{ company name }}` claim-profile form, the Indianapolis plumbing positioning, and the jobsite photo (Brian holds it up as the standard in I-20) |
| **I-20** | P3 | **B** | Company · Hi-Fi, hero photo | **Brian Oltmanns, 21 Oct:** "@Team Groto we do still want to change this photo to something similar to the plumbing marketing page, something more jobsite related where the workers look less clean and polished" | Replace the hero photo (two men in suits and hard hats). New brief: a real jobsite, with workers who look like they're working, not posed or polished. The Plumbing page photo (three plumbers with a clipboard, among exposed pipework) is the reference. Linked to I-15 (photography) |
| **I-21** | P4 | **B** | Job Seeker · Hi-Fi, hero photo | **Brian Oltmanns, 21 Oct:** "@Team Groto would like to change this photo as well, same standards as prior comment" | Same brief as I-20: replace the posed, smiling worker with a jobsite shot that looks less polished. Choose I-20 and I-21 together so the two heroes match. Linked to I-15 |
| **I-22** | P0 | **B** | Job Seeker · Hi-Fi, hero headline (**live HubSpot site**) | **Brian Oltmanns, 21 Oct:** "@Team Groto On the Hubspot site, could you make "Less searching" on its own third line? I cannot figure out how to do it" | This change is on the **live HubSpot page**, not in Figma. The headline should break as: "Local trade jobs." / "Better pay." / "Less searching." At the moment "Less" wraps with "Better pay." and "searching." drops to a line on its own. Fix it with a forced line break (a `<br>`, or a block span for each line in the module) so the three lines hold at every width. The Figma frame should break the same way. Brian asked for help because he can't do it in HubSpot himself |
| **I-23** | P1 | **B** | Homepage · Hi-Fi, "Better opportunities. Better workers. One construction network." band (For Companies / For Job Seekers cards) (**live HubSpot site**) | **Brian Oltmanns, 21 Oct:** "@Team Groto this section in Hubspot is stretched for some reason, could you make it look like this in Figma?" | The live HubSpot band doesn't match the Figma layout. Figma has two equal cards, each a titled list of three icon + heading + line steps, inside the page's content width. Check the module's max-width, the column or flex settings, and whether the section is set to full width. Then match the Figma spacing and card widths. Frame name isn't visible in the screenshot; it sits above the "What our m[embers say]" testimonials band |
| **I-24** | P2 | **B** | Homepage · Hi-Fi, between the final CTA band ("Find the people you need…", Post a job / Find work) and the footer | **Brian Oltmanns, 21 Oct:** "@Team Groto could you add another small "Our Vision"section above the footer with the text: "We believe every skilled worker deserves access to better opportunities, and every construction company deserves a simpler way to find the people they need. Our vision is to build a connected industry where workers, contractors, and trade partners can discover new possibilities, develop lasting relationships, and grow together. Because when the right people connect, everyone has more opportunity to build something better."" | New small band directly above the footer, below the final CTA. Overline or heading "Our Vision", then Brian's paragraph exactly as written (copy is final). Keep it light: one centred column of text, no buttons, so it doesn't compete with the CTA above. Design in Figma first, then build on HubSpot. He didn't say whether it goes only on the homepage or on every page; confirm when replying |

### Work notes

**I-22, 22 Oct.** The page is "GFB Job Seekers (staging)", HubSpot content ID
`224337738564`, at `/job-seekers-staging`. The hero is the custom module
`gfb_hero_v2` (`main-module-2`). It has two plain-text fields: `headline`, and
`highlight` (the orange words, which must match the headline exactly). The
module's source isn't available through the connector. A `<br>` in a text
field might render as literal text, so the fix uses non-breaking spaces
instead: "Better pay." and "Less searching." each have a U+00A0 between the
words, in both fields. Each pair now wraps as one unit, which forces
"Less searching." onto line 3.
Saved to the draft only, not published. Not yet checked visually: the
container can't load hs-sites.com. If the line doesn't break in the preview,
the lasting fix is to change the `gfb_hero_v2` source to allow a line break
in the highlight. That change hits every page using the module (Home,
Companies, Job Seekers), so it needs its own check.
**Update, 22 Oct:** checked in preview, it breaks correctly. Published.

**I-23, 22 Oct.** The band is on "GFB Home (staging)", content ID
`223806550529`, module `gfb_what_you_get` (`main-module-2`). The spec
(`Design/HubSpot/Home/04_FINAL-DESIGN_Home-Page.md`) is a 1200 container
with two cards of 568 and a 64 gap. Found: the "If you're hiring" card image
was set to **1136 × 880**, which is the 2x export at its full pixel size. The
"If you're looking for work" card image is set to 568 × 440. Most likely
cause of the stretch: the first card renders an image twice the intended
width. Fix: set the first image's display size to 568 × 440, keeping the
same 2x file so it stays sharp. Section and module styles are empty, so
nothing forces full width there. Saved to the draft, not published, and not
checked visually (the container can't load hs-sites.com).
**Copy differs from Figma, left alone:** heading "Better jobs…" (Figma:
"Better opportunities…"), card titles "If you're hiring" / "If you're
looking for work" (Figma: "For Companies" / "For Job Seekers"), an extra
sub-header, and longer feature lines. These look like edits made in HubSpot.
Brian asked for the layout to match, so the copy was not touched. Confirm
with him if he wants the copy to match Figma too.
**Correction, 22 Oct:** the copy is Brian's own. On 19 Oct he asked for the
centred heading, the sub-header and the "If you're hiring" titles
(commit `bd845fd`, branch `claude/ecstatic-albattani-5e2sv8`), so there's
nothing to ask him.
**Update, 22 Oct, after preview:** still stretched. The image size wasn't
the cause. The real cause is in the module: `.gfb-wyg__media` (the card image) is
its own grid row under the features (`align-self: end`, `min-height: 120px`),
so its full height (about 440px) is added to every card. In Figma the
image is a faint background behind the features. Fix: page head CSS on
GFB Home (staging) only, which pins `.gfb-wyg__media` with absolute
positioning to the card bottom, behind the features (features already sit
at `z-index: 1`), and sets the card's bottom padding to 12px so the card
ends just after the last feature. Draft only.
Source used: `Design/HubSpot/Home/code/gfb-what-you-get-and-testimonials.html`
on that branch (a preview of the module's CSS). The Figma connector hit its
seat limit, so the frame was matched from Brian's screenshot.
**Update 2, 22 Oct (Shubham: still doesn't match Figma):** measured the Figma
frame from Brian's screenshot (scale 1.10 to 1440). Each card is **568 × 440, the
same size as the image**, so the image is the full card background. Figma also
has left-aligned card titles (semibold, about 22px) over a thin grey rule,
28px icon badges stacked *above* each title (18px semibold) and description
(14px), 24px card padding, a 64px gap, a grey band background (#F8F9FB) and a
left-aligned heading. HubSpot had centred titles, accent rules, icons beside
the text and 40px padding. The head CSS was rewritten to all of these values;
source: `Design/HubSpot/Home/code/i23-what-you-get/head-override.css`.
**Verified** by rebuilding the band locally from the module CSS and the live
field values, then screenshotting it with Playwright at 1440 and 390 and
comparing it with the Figma crop (`figma-vs-replica.png`, `replica-mobile-390.png`
in the same folder). The live page can't be reached from the container, so
the real HubSpot render still needs one look in preview. The card images were
stand-ins, since hubfs is blocked too. **Remaining differences are copy only:** the
sub-header (Brian's request, 19 Oct) and the longer first feature line in the
hiring card (+20px card height). The headline and titles also differ in
wording. Copy was left alone.
**Follow-up:** move this rule into the `gfb_what_you_get` module CSS when
the module source is next edited, so it doesn't depend on page head HTML.
**Update 3, 22 Oct:** checked in preview, matches. Published.

**I-24, 22 Oct.** New custom module `gfb_vision` (code and previews in
`Design/HubSpot/Home/code/gfb-vision/`), inserted on GFB Home (staging) as
`main-module-11`, between the final CTA and the footer. Brian's copy is word
for word: the main paragraph in the body, and his last sentence ("Because
when the right people connect…") as a bold closing line. It's a light grey
band, centred, with no buttons. Draft only. **Home page only:** Brian didn't
say whether every page gets it; confirm with him before adding it to
Companies and Job Seekers.
**Figma, 22 Oct:** added as `10b · Our Vision` (`1569:3096`) in Home Page
`1259:9027`, between `10 · Final CTA` and the footer. It matches the HubSpot
module and uses the file's colour and spacing variables and text styles.
Home Page grew from 5543 to 5974 tall. Checked by screenshot.

**I-24 correction, 22 Oct (Shubham):** Our Vision belongs on the **About Us
page, not Home**. Done:
- HubSpot Home (staging): `main-module-11` removed from the draft. It was
  never published, so the live Home page never had it.
- HubSpot About Us (staging) `224339429033`: `gfb_vision` inserted as
  `main-module-7`, row 4, after the three alternating rows and before the
  final CTA and footer. Draft only.
- Figma: the band `1569:3096` is already inside About Us · Hi-Fi
  `1259:9158`, between the alternating rows and `09 · Final CTA` (moved in
  the file). Home Page has no Our Vision layer and is back to 5543 tall.
  HubSpot follows this Figma placement (above the CTA rather than directly
  above the footer).

**I-24 published 22 Oct** on About Us (staging).

**I-20 / I-21, 22 Oct.** Shortlist of 30 Freepik stock photos (15 crew shots
for Company, 15 single-tradesperson shots for Job Seeker) in
`Design/Assets/HERO-PHOTO-SHORTLIST_I-20_I-21.md`. **Picked by title only:**
the container can't load img.magnific.com, downloadscdn*.magnific.com,
Unsplash search or the HubSpot hosts, so no photo has been seen or fetched.
One test download (40 credits) confirmed that the file host is blocked too.
Waiting on: a pick per page, plus either network access to those hosts or
the two files added to `Design/Assets/Testing assets/`.

**I-20 / I-21, 23 Oct.** Six AI options generated in Magnific (3 crew shots
for Company, 3 single-tradesperson shots for Job Seeker), in the style of the
Plumbing reference: `Design/Assets/AI-HERO-PHOTOS_I-20_I-21.md` has the links
and briefs. They haven't been reviewed here because the image host is blocked.
Putting them on the Figma Presentation page was blocked three ways: the
connector account has view-only access to this file for uploads, the image
host is blocked by network policy, and the Figma call limit was hit. The board
script `Design/Figma/scripts/hero-photo-options-board.js` is ready to run.

**I-22 follow-up, 23 Oct (Shubham):** the hero headline is now one rich-text
field in the shared `gfb_hero_v2` module (`headline_rich`). Paragraphs are
lines, and bold words are orange. The old headline and highlight fields remain
as a fallback. This replaces the non-breaking-space workaround. Content is set
in the drafts of Home, Companies and Job Seekers, not yet published. Source:
`Design/HubSpot/Home/code/gfb-hero/`.

**Figma sync, 23 Oct (Shubham):** Home Page testimonials band `1259:9068`
rebuilt to match the HubSpot `gfb_testimonials` module on GFB Home (staging).
It has a centred "What our members say" heading (Display 3xl), then two stacked
quote cards: Matthew B. - Carpenter, Noblesville, IN, and Brothers Insulation &
Construction, Indianapolis, IN. Each card has an initials badge, a name and a
place. The background is the light grey surface, and colours and spacing use
the file variables. The Elevate sample content (stock photo, placeholder
quote, slider arrows and dashes) was removed. The band is now 726 tall, was 826.
Renamed "08 · Testimonials (HubSpot gfb_testimonials)".

**23 Oct (Shubham): Plumbing header, hero photos, publish.**
- Plumbing LP header rebuilt from Figma `1528:10672` as the new module
  `gfb_hero_signup`. The old row-0 modules were removed. See
  `Design/HubSpot/Landing pages/code/gfb-hero-signup/README.md`. The form
  now shows an inline thank-you message instead of redirecting to google.com.
- Hero photos taken from Figma: Company uses **C1 framing crew**
  (`hero-companies-ai-c1-1200x800.jpg`) and Job Seeker uses **J1 carpenter**
  (`hero-job-seekers-ai-j1-1200x800.jpg`). Both are hosted from this repo, like the earlier hero
  photos. Closes I-20 and I-21.
- **Published:** Plumbing LP, Home, Companies, Job Seekers. This also put the
  rich-text hero headlines live.

**23 Oct (Shubham): Plumbing LP stats, CTA, footer. Published.**
- **Stats band looked faded:** `gfb_stats_dark` lays a navy gradient (92% to 72%
  opacity) over its background image. On this page the image was Home's light
  peach-and-blue band, which showed through the 72% end and washed the navy out.
  The image is removed on the LP (`dnd_area-module-4`), so the band is solid navy `#16243D`.
- **CTA was boxed:** the `gfb_final_cta` section (`widget_1792135074421`) is now full width
  with no section padding, matching the other pages.
- **Footer was boxed, padded and had a short rule, and About Us went to the live
  `/about-us` (404):** the footer sits in the Elevate LP footer partial, which can't be styled
  from the page. Fixed in the shared `gfb_footer` module: it runs full bleed in any container
  and treats any address containing `-staging` as staging. Source:
  `Design/HubSpot/Home/code/gfb-footer/`. Module updates are live at once, on every page.

**27 Oct (Shubham): Plumbing LP complete. All client items I-18 to I-24 closed.**
- Footer checked. Link fields on the LP: About Us `/about-us` and the logo `/` resolve to
  `/about-us-staging` and `/home-staging` on any `-staging` address. Terms and Privacy keep their own pages.
- Layout checked in a local render of the module CSS inside a boxed, padded footer wrapper (1440, 1000,
  390 wide): the footer runs edge to edge, the wrapper's padding and rule are gone, and there is no sideways scroll.
  The live staging page couldn't be opened from the build environment (hs-sites.com is blocked there), so this
  is the local check, not a screenshot of the live page.
- Header (logo only, I-18), hero (I-19), stats, CTA and footer all published. Marked done on Shubham's call;
  Brian's confirmation of the logo-only header is still welcome but not blocking.
