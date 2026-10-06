# Job Seeker page · final plan

Written 22 Sep 2026. **Final version.** It replaces the first version of this file (same day) and
adds three things: Jeff's note on the preview cards, the header idea (A1 Welcome, `867:866`), and
the scope, which is the Job Seeker page only. The Company page's context is kept at the end, for
the task after this one.

Checked against Brian's mockup, the live site, the meeting transcripts, the audits, and both
Figma files as they stand today.

---

## This task

- **Build:** the Job Seeker marketing page in Figma. Desktop at 1440 and phone at 375, including
  the header's search states.
- **Don't build:** the rest of Flow A. A2's trade picker is drawn as a state of the page's header;
  A3 to A8 already exist and are not redrawn. The Company page is the next task. The homepage
  changes that follow from Jeff's note are listed at the end, not made.

## What changed from the first version

| Change | From | What it does to this page |
|---|---|---|
| The preview cards leave the homepage and go to the Job Seeker and Company pages | Jeff | The Job Match Card sits right under the header (band 02). The Job Seeker card goes to the Company page |
| The header is the A1 Welcome design | Shubham (`867:866`) | Dark header, centred trade + ZIP bar, popular trades. Brian's split hero with the card on the right is replaced; his copy moves into A1's layout |
| Only the Job Seeker page gets built | Shubham | The flow is context for where the page hands off |

**How Jeff's note is read here:** the component is the homepage's preview cards band (R3 band 06,
`1075:478`), which holds the Job Seeker card and the Job Match Card. If he meant a different
component, only band 02 and the knock-on list at the end change.

## Before you start: which Figma file

Two files are called **GofindBuild Website Redesign**:

- `aC59gtTG9nh2hwUraPnCXj`: the one every note, the work log and the HubSpot mapping point to.
- `eulu7Yq3gH7gaezVZbn0bi`: the one the header and flow links use.

Both have the same pages and the same node IDs, including R1 to R3 and Flow A, so one is a copy of
the other. Pick the working file before building, build only there, and record the choice in
`00_FIGMA-WORK-LOG.md`. Every node ID in this plan works in both.

---

## The short version

1. **It's the paid landing page.** Google Ads is the one channel that has worked for job seekers
   (30 to 40 a month, just over 250 in total by July). Nothing has worked for companies. Design for
   a cold visitor on a phone, with one action.
2. **The header is the product's first screen.** A1 asks for trade and ZIP before sign-up, and so
   does Brian's hero. With A1 as the page's header, the page does the welcome screen's job: pick
   trades, enter a ZIP, go straight to the email step (A3), which already shows the trades and ZIP
   as saved. One screen fewer for the worker, and it answers Brian's 1 Jul question "how does the
   job seeker get to this page?" (D-10).
3. **Jobs come first after the header.** Jeff's move puts the Job Match Card straight below the
   search. A worker sees what a job looks like, pay first, before reading a word of explanation.
4. **Brian's version is three bands:** hero, three steps, CTA. The problem, proof and FAQ copy
   already exists: the live /job-seekers page, Brian's homepage, and the parked FAQ seeds.
5. **Some lines promise more than the product does today,** in A1 as well as in Brian's copy:
   "Thousands of trade jobs, updated daily", "Join thousands of skilled trades professionals",
   "3 open jobs", anything "verified", and "instant notifications" (email only, no text alerts
   yet). Confirm each with Brian or soften it.

---

## Who lands here

| | |
|---|---|
| **Who** | Skilled-trades workers and labourers. Non-technical, on a phone, often on a job site. Many have no resume. Some have no licence or transport (Brian, 1 Jul). More young people are choosing trades over college (Brian, July) |
| **How they arrive** | Mostly paid: Google Ads. Check where the ads point today before any URL changes |
| **What they must believe in five seconds** | It's free. No resume. Real local jobs with the pay shown. My current boss won't see me looking |
| **The one action** | Pick a trade, enter a ZIP, see my matches |
| **Secondary** | Look at a job, to judge whether it's worth it |

---

## The header: A1's layout, Brian's copy

| Element | A1 today (`867:868`) | Brian's mockup | Use |
|---|---|---|---|
| Background | Dark streak | White | **A1's streak**, with the ~55% dark overlay Home band 03 uses. Today the orange part of the streak sits behind the subhead and the Plumber chip; every word has to reach 4.5:1 |
| Pill | "Thousands of trade jobs, updated daily" | "Always free for workers" | **Brian's.** A1's is a platform number Brian asked not to show yet (D-15), and it isn't true yet |
| H1 | "Find your next trade job." | "Local trade jobs. Better pay. Less searching" | **Brian's**, his approved copy. A1's line is the fallback if he prefers it |
| Subhead | "Get matched with companies hiring in your trade, no resume required." | "Create one private profile right from your phone and let local construction companies find you, even while you're working." | **Brian's** |
| Search bar | Trade "Search 151 trades…" + Near "ZIP code" + button | Two fields: [General labor] [97206] | **A1's bar.** Its placeholders need no example ZIP, so Brian's Portland ZIP problem (I-08) goes away here. Say "Search 150+ trades…" to match Brian's "150+ trade categories" on the homepage |
| Button label | "Continue" | "See jobs near me" | **[Copy] "See my matches".** It names the result, like Brian's, and it stays true: the next screen asks for an email, and A4's button already says "Verify & see my matches". "See jobs near me" promises jobs on the next screen, which is an email form |
| Button colour | Orange, white label, 3.05:1, fails | Blue, white label, 3.28:1, fails | **Orange with the navy label, 5.09:1.** A dark button disappears on a dark header. The orange-for-employers, dark-for-workers pairing only matters where both paths sit side by side, which is the homepage fork |
| Popular trades | Electrician · Plumber · HVAC · Carpenter · General Labor · Welder · Roofer | none | **Keep.** One tap to a trade. The final list waits on GTM (question 15) |
| Under the bar | "Free to join. We'll ask for your email next, that's the only other step." | Checks: No resume needed · Build a profile in minutes · You choose who sees you | **Brian's three checks under the chips.** A1's line moves into the trade picker's footer (today "3 trades selected · Continue is now active"), where it's read right before the click |
| Card on the right | none | Job card, "Jobs near 97206" | **Moves to band 02**, per Jeff |

A1 uses an em dash in the subhead and in the line under the bar. Both become commas.

**Header states to draw.** A2's note says the picker "opens over the landing page like a dropdown",
so these are states of this page, not flow screens:

1. Default.
2. Trade picker open: the browse tiles from A2 (`867:988`, "BROWSE BY TRADE").
3. Typing: a filtered list, like `823:2938`, **without** the open-job counts (D-15).
4. Trades selected: pills in the bar, button active.
5. ZIP not recognised: a message under the field.
6. Button inactive until there's a trade and a ZIP (A2: "Continue is now active").
7. Phone: fields stacked, a full-width 48px button (A-04), popular trades as one scrolling row.

---

## Page structure

**Bold** = not in Brian's mockup.

| # | Band | Job it does | Content from | Build from | Launch |
|---|---|---|---|---|---|
| 00 | Top Nav | Job Seekers shown as the active page (A-13) | Global | DS Top Nav `790:11423` | P0 |
| 01 | **Header** | The promise and the one action | A1's layout, Brian's copy | A1 hero `867:868` · search bar (new) · Chip · Button | P0 |
| 02 | **Jobs, pay first** | Shows what a job looks like, before anything else | Brian's job card + two more examples, [Copy] | Job Match Card `891:189` ×3, in A1's "Near You" slot `867:892` | P0 |
| 03 | **Problem → reality** | Problem awareness | Live /job-seekers, cut down, [Copy] | Home R3 band 03 layout `1075:400` | P0 if Brian agrees |
| 04 | How it works | Three steps to hired | Brian | Home R3 band 04–05, working column `1075:425` | P0 |
| 05 | **You choose who sees you** | Answers "will my boss see me" with the product itself | Brian's private card, new caption | Job Seeker card, Private variant (new) | P1, waits on question 2 |
| 06 | **Proof** | Another worker vouching | Matthew B. + the $58k+ and 90% stats | Home R3 band 07 `1075:510` + band 03 stat | P0 |
| 07 | **FAQ** | Objections, and something for search to find | Seeds W1–W3, W5–W8 | Home R3 band 09 `1075:584` | P0, with the answers that exist |
| 08 | **Browse jobs by trade** | A way in for someone who searched one trade | Brian's 12 trades | Footer trade column `1075:628` | P1 |
| 09 | Final CTA | Closes the page | Brian | Home R3 band 10 `1075:620` | P0 |
| 10 | Footer | | Global | Home R3 band 11 `1075:628` | P0 |
| + | **Sticky CTA on phones** | Keeps the action in reach on a long page (A-20) | "See my matches" | New | P0 |

### Why each new band

- **02 Jobs, pay first.** This replaces A1's "Companies hiring on GoFindBuild", whose cards carry
  "3 open jobs" counts and a Texas company. Three Job Match Cards, all in the Indianapolis area:
  Brian's General Laborer (Central Construction Group · $23/HR · Full-time · 5.8 mi · Posted
  today) plus two from the popular trades, for Brian to approve. Heading [Copy]: **"Every job shows
  the pay up front"**, with Brian's own homepage line under it: "Every post shows a pay range and a
  distance". That heading is true of static examples; "Companies hiring near you" isn't true until
  the app feeds the cards. Caption: "Get instant notifications of jobs in your area" (email). Apply
  leads to sign-up (question 12). A card at a third of 1200 is narrower than in R3 band 06, so
  check the title and the pay don't collide, or show two cards.
- **03 Problem → reality.** The 15 Sep order puts the problem second, and the copy is written and
  live: "We get it." (the job search feels overwhelming, is college the only way) and "Here's the
  reality..." (businesses need you now, the trades pay). Cut each to two lines and pair them with
  the 723,000 stat, which backs "they need you now".
- **05 You choose who sees you.** The worker's own card in its private state, captioned with what a
  company sees before it unlocks. Brian drew this state in his PDF (gear avatar, lock, "Private
  Profile"). It answers the fear behind "even while you're working". Waits on question 2.
- **06 Proof.** Matthew B. is the only worker testimonial, and the right one: "I didn't have the
  time while I was working all day" backs the subhead, and "surprised to see what companies were
  willing to pay" backs "Better pay". Use the two worker-facing stats, not the employer ones.
- **07 FAQ.** Seven questions: 1 Is GoFindBuild free for workers? · 2 Do I need a resume to get
  started? · 3 Who can see my profile and contact details? · 4 Which trades are on GoFindBuild? ·
  5 How do I know a company posting a job is legitimate? · 6 How long until I hear back after
  applying? · 7 What certifications help me get hired faster, and can I add them later? Brian's
  copy already answers 1 to 3. Nothing about paid training (I-16).
- **08 Browse jobs by trade.** Until `/jobs/{trade}` exists, each trade can open sign-up with that
  trade filled in (question 11). No job counts (D-15), no dead links (H-15).
- **09 Final CTA.** Brian's copy: "Your next opportunity could find you" · "One free profile. Local
  jobs. Better matches. You're always in control" · **Create my free profile**. The button scrolls
  back to the header's search bar instead of jumping to sign-up, so every path goes through trade
  and ZIP, which the email step expects. The sticky CTA does the same.

### Brian's copy for the bands that keep it, verbatim

| Band | Copy |
|---|---|
| 04 How it works | H2: **Your job search just got a whole lot easier** · Sub: "Get connected to better opportunities, even when you're not looking" · **1 Build your free profile**: "Tell us your trades, skills, and experience in just a few minutes. Build it once and let your experience speak for you." · **2 Get connected**: "Explore local jobs and get notified when new opportunities match your skills. Or sit back and let employers come to you." · **3 Get hired**: "Message employers directly, explore offers, and choose what's right for you. Better pay, better opportunities to build a bright future." |
| 09 Final CTA | As above |
| 10 Footer | LinkedIn · Facebook · Instagram · © 2026 GoFindBuild. All rights reserved. · Terms and conditions · Privacy policy |

Brian's how-it-works subhead uses an em dash; shown here with a comma. Raise it as a [Copy] note.

---

## Where the page ends and the flow begins

- **On the page:** header, picker, trades selected, ZIP, **See my matches**.
- **Then the existing screens, not rebuilt:** A3 email `867:1012` (its chip shows the trades and
  ZIP as "saved, we won't ask again") → A4 verify code `867:1036` → A5 dashboard `868:1079` → A6 job
  matches `879:1193` → A7 job detail `879:1397` → A8 applied `879:1601`.
- **What the page has to hand over:** the chosen trades and the ZIP (question 11).
- **To flag in A3 and A4, not to fix in this task:** "Join thousands of skilled trades
  professionals" (about 250 by July) · the chip's ZIP 78701 is Austin, TX, use 46204 · "Continue
  with Google" only if the app supports it (question 13) · the em dash in the chip.
- **Product dependencies:** open to work has to start on, or "let employers come to you" isn't true
  (question 14) · an empty state for ZIPs with no jobs yet, e.g. "No jobs near 46204 yet. We'll
  email you the first one." · Brian's sign-up minimum stays as it is: name, email, ZIP, over 18,
  trades, with the phone number later (D-11).

---

## Fix while building

| Item | What | Fix |
|---|---|---|
| I-01 | The header button is orange with white (3.05:1). Brian's buttons are blue with white (3.28:1). The nav's Get Started is orange with white | Orange fill with a navy label (5.09:1), lighter hover `#F4811F` (I-18) |
| I-08 | Brian's 97206 is Portland; A3's 78701 is Austin; A1 has a Texas company | 46204 and Indianapolis in every example. A1's placeholders need no ZIP at all |
| New | A1's pill and cards, and A3's "Join thousands" | Brian's pill; no counts; a softer line in A3 when it's next touched |
| New | Orange streak behind white text in the header | Dark overlay, then check every line at 4.5:1 |
| New | The homepage's worker steps (Pick your trades / See job details / Let employers come to you) differ from this page's (Build your profile / Get connected / Get hired) | One three-step story for workers (question 5) |
| New | "Get instant notifications of jobs in your area" | Fine if it means email. Nothing on the page should say text |
| New | "150+ trades" on the homepage, "151 trades" in A1 | One number. "150+" matches Brian's copy |
| New | "Less searching" and "You're always in control" end without a period, other lines have one | [Copy] consistency, for Brian |
| New | The H1 at phone size is likely three lines | Check at 375. Headings at most two lines (A-03) |

---

## Components

**Reuse:** Top Nav `790:11423` · Button `787:10782` · Chip `790:11387` (Glass for the popular
trades, Subtle for the pill) · Job Match Card `891:189` · the Home R3 bands listed above.

**Build, in this order:**

1. **Input field** (I-13). Default, Focus, Filled, Error. Label, placeholder, leading icon.
2. **Search bar**, promoted from A1: trade typeahead after three characters over the 150+ trades
   (D-14), ZIP, button, and the seven header states above.
3. **Job Match Card**, checked as the merge of Brian's Job Post card and `891:189`, with three
   example fills.
4. **Sticky CTA bar** for phones.
5. **Job Seeker card, Private variant** (P1). The Company page needs the Public variant next, so
   build both variants in one set.
6. **Home's step, testimonial card, FAQ row, final CTA and footer** as components (the list in
   `02_HIFI-PLAN.md` Phase 2), so the Company page reuses them.

## Rules carried from the homepage

- One skeleton and one header template for both sub-pages (A-05). The Company page follows this
  page's band order.
- Everything bound to variables and text styles. No loose colours or font sizes.
- Type is the design system: Instrument Sans for display, Inter for the rest.
- No claim the product can't back yet: verified skills, text alerts, paid training, platform
  numbers, same-day matches.
- No stock faces beside real customer names (H-05). Only the welder photo is real (I-15): spec
  boxes, not stock.
- HubSpot, learned on the homepage: a real page title and description, language en-US, the logo as
  a proper file with alt text, no dead links, images under about 300 KB (H-12 to H-17). Every band
  maps to an Elevate preset already used on Home; the new modules are the search bar and the Job
  Match Card.

---

## Open questions, with owners

Harpreet carries these. They belong in `Read me/03_BLOCKERS_for-Harpreet.md`.

| # | Question | Owner | Blocks |
|---|---|---|---|
| 1 | Nav label (For workers or Job Seekers). Keep the live URL `/job-seekers`? Where do the Google Ads point? | Brian | Nav, URL, trade pages |
| 2 | What does a private profile hide, and what does a company see before it unlocks? Is private the default? | Brian | Band 05, FAQ 3 |
| 3 | OK to add the problem band from the live page? | Brian | Band 03 |
| 4 | Header copy: his H1, subhead and pill in A1's layout, and the button as "See my matches"? | Brian | Band 01 |
| 5 | One three-step story for workers: the homepage's or this page's? | Brian | Band 04, Home 04–05 |
| 6 | A second worker testimonial, and crew photos? | Brian | Band 06, photos |
| 7 | Is paid training still offered? | Brian | Nothing if not (I-16) |
| 8 | Approve the two extra example jobs in band 02 | Brian | Band 02 |
| 9 | Confirm the note means the preview cards band | Jeff | Band 02, the homepage knock-ons |
| 10 | Can the job cards be fed live from the app later? | Jeff | Band 02 heading |
| 11 | Can the sign-up link take the trades and ZIP from the page? | Jeff | The handoff, band 08 |
| 12 | Can Apply remember the job through sign-up? Can a visitor get job alerts with only an email (A-30)? | Jeff | Band 02 action |
| 13 | Is "Continue with Google" real? | Jeff | A3, later |
| 14 | Does open to work start on? | Jeff | "Let employers come to you" |
| 15 | Trade list and keywords for workers | GTM | Popular trades, band 08 (I-11) |
| 16 | Which Figma file is the working one? | Shubham / Harpreet | Where this gets built |

---

## Order of work

0. **Figma.** In the working file: a new page **Marketing page · Job Seeker**, placed after
   Marketing website, holding a dated section (`2026-09-22 · Job Seeker Page · …`). This is the
   separate folder for the page.
1. **Structure.** Low-fi bands, one note per band, plus the header table above. To Brian with
   questions 1 to 8.
2. **Components.** Input field, search bar and its states, Job Match Card examples, sticky CTA.
3. **Hi-fi, desktop**, in the order that wins approval: 01 header · 02 jobs · 04 steps · 06 proof ·
   09 final CTA · 07 FAQ · 03 problem · 00 and 10 nav and footer · then the P1 bands, 05 and 08.
4. **Phone at 375.** Header and picker, jobs (cards stack), steps, FAQ, sticky CTA.
5. **Annotate like R3.** Per band: source, Elevate preset, modules, what changed from Brian,
   tagged [Theme] [Editor] [CSS] [Module] [Copy].
6. **Hand to HubSpot** after approval. Same theme settings as Home. New modules: search bar, Job
   Match Card (static examples).

### Launch cut

| Ships at launch | After launch |
|---|---|
| 00 · 01 · 02 · 04 · 06 · 07 (the answers that exist) · 09 · 10 · sticky CTA · 03 if Brian agrees | 05 (question 2) · 08 (questions 11 and 15) · live job cards (question 10) |

**Not in this task:** A3 to A8, the Company page, the trade pages, the homepage changes below.

---

## Knock-on changes from Jeff's note (not part of this task)

- **Homepage:** band 06, the preview cards (`1075:478`), comes out in the next homepage round. R3
  stays as it is: rounds are never edited in place.
- **Live demo:** H-04 becomes "remove the band", not "replace the sample cards".
- **HubSpot mapping:** Home needs one custom module instead of three (only the hero visual). The two
  card modules move to the sub-pages, which lightens the homepage build.
- **Issues log:** I-07 mostly goes away, because the two cards no longer sit side by side. The card
  ZIPs (I-08) move with them.
- **`01_STRUCTURE_Marketing-Homepage.md`:** move 2 ("put the preview cards on the homepage") is
  reversed.
- **Homepage product visual:** the hero's frosted card becomes the only one. Worth a look when the
  next homepage round is laid out.
- **Company page:** the Job Seeker card goes back to Brian's placement, its hero.

---

## Done means

- [ ] Built in the agreed Figma file, on its own page, in a dated section
- [ ] The header uses A1's layout and Brian's copy, with all seven states drawn
- [ ] Band 02 carries the Job Match Card, Indiana examples, no counts
- [ ] Every button passes 4.5:1, every line on the header passes 4.5:1
- [ ] Nothing claims what the product can't do yet
- [ ] The search bar is one component, the same one the product's welcome screen uses
- [ ] Phone frames for header and picker, jobs, steps, FAQ and sticky CTA; headings at most two lines
- [ ] One note per band: source, preset, modules, what changed
- [ ] Every open question has an owner
- [ ] Bound to variables and text styles, no loose values
- [ ] Figma work log updated

---

## Next task: Company page (context kept, not part of this task)

**Superseded 23 Sep by `04_CONTEXT_Company-Page.md`,** which carries this forward and adds the
live pricing, the supply reality and the node IDs to clone. Kept here as written.

**Who lands there.** Owners and managers of construction firms: often small, often without a website
or LinkedIn (Brian, July), busy, and wary of recruiters. They arrive warm, after meeting Brian at
network meetings, industry groups or hardware stores; Google Ads never worked for this side. The one
action: **post a job, free.** Secondary: see who's available.

**Brian's mockup (For companies), verbatim.**

| Band | Copy |
|---|---|
| Hero | Overline: **For companies** · H1: **Build your workforce. Not your recruiting bill** · Sub: "Connect directly with local skilled-trades talent, build an always-on pipeline, and hire when you're ready." · Search label: "Get matched with the skills you need" · Search: [Journeyman Electrician] [75201] **See who's available** · "No credit card required" · Stats: **Instant notifications**, "Of matches and job applicants" · **0%**, "Placement fee" · Right: "Matches near 75201" + worker card (Marcus Bell · Journeyman · 92% Profile score · Looking for / Experience: Electrical, Journeyman · Low voltage, Skilled · Indianapolis, IN · Seeking Full-time · Send job · View profile) · Caption: "All worker skills are verified through GoFindBuild" |
| Cost comparison | H2: **What it costs you today, and what it costs here** · **The staffing-agency way**: 18–25%, "Markup on every hour worked · Résumés with no license check · You never meet the bench · Rate goes up at renewal" · **The GoFindBuild way**: Flat monthly, "Unlimited posts · Verified licenses and certs · Direct messaging to the worker · The relationship stays yours" |
| Final CTA | H2: **Post your first jobs free.** · "90 seconds to post. Matches the same day." · Button: **Post a job** |

**From the live /companies page:** "We know the struggle": built by a 20 year construction veteran,
plus three pain points (finding talent is time-consuming and expensive · training entry-level
employees from scratch often isn't an option · skilled tradespeople are hard to come by). Don't use
its old per-applicant pricing ($25 / $99 / $199 / $399). "Find your next project: Free" is the
trade-partner side of the product, which Brian's mockup leaves out.

**Structure, mirroring this page:** 00 nav · 01 the same header template, with Brian's company copy
and **See who's available** · 02 **Workers near you**, Job Seeker cards ×3 (Jeff's move), shown as a
company sees them before unlocking · 03 problem, the live copy + the 88% stat · 04 how it works, the
homepage hiring steps · 05 cost comparison (Brian, soft, I-12) · 06 proof, Brothers Insulation &
Construction · 07 FAQ (seeds H1, H3–H8) · 08 hire by trade · 09 final CTA · 10 footer · sticky
"Post a job" on phones.

**Worth knowing before that task:**

- The live pain point "training entry-level employees from scratch often isn't an option" and the
  Brothers quote "We're too busy to train from scratch" say the same thing. On one page, the proof
  lands directly on the problem.
- The cost comparison can ship without a price if Brian confirms flat monthly. R3 band 08 now shows
  three tiers ($49 / $149 / Custom) that someone added after 19 Sep, under a heading that still
  describes the comparison (I-21). Use Brian's comparison unless he says otherwise; it's also the
  first band to cut.
- Fixes: employer buttons orange with a navy label · 75201 is Dallas, use 46204 · the search says
  Electrician while the card says Electrical in Brian's version and Welding in R3, so pick one trade ·
  a named worker with a headshot contradicts the worker page's privacy promise · "verified",
  "0% placement fee" and "Matches the same day" need Brian's yes · "first jobs free", "unlimited
  posts" and "flat monthly" need to read as one clear sentence.
- Company-side questions for Brian: is flat monthly confirmed and what exactly is free · is skill
  and licence verification live · are trade partners and projects part of the pitch · a phone
  number or a call with Brian on the page.

---

**Sources.** Brian's mockup, pages 02 and 03 (`Design/Figma/Source files/GoFindBuild-Marketing-Site-All-Pages.html`)
and his brief (`Project Context/2026-09-11_Brian-Mockup-Brief.md`) · gofindbuild.com/job-seekers and
/companies, read 22 Sep · Meeting 2 (acquisition, invite and unlock, open to work) · Meeting 5
(quizzes, text alerts, onboarding minimums, the welcome-screen question) · `Audit/Audit list.md`
(A-03, A-04, A-05, A-13, A-20, A-30, D-10, D-11, D-14, D-15) · `Read me/02_ISSUES-LOG.md` ·
`Read me/04_FAQ-SEEDS_sub-pages.md` · Figma Flow A Hi-Fi `867:833` (A1 `867:866` to A8 `879:1601`),
R3 `1075:228`, Hi Fi `823:4275`, Design System `790:11512` · Jeff's note on the preview cards, via
Shubham, 22 Sep.
