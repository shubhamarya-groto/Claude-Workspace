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
