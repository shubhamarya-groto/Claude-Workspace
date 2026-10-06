# Company page · plan

Written 23 Sep 2026. The task after the Job Seeker page. It takes the context parked at the end of
`03_CONTEXT_Job-Seeker-and-Company-Pages.md` and turns it into a build plan, re-checked against
Brian's mockup, the live gofindbuild.com/companies page (read again 23 Sep), the meeting
transcripts, the audits, and the Job Seeker page **as it was actually built** on 22 Sep.

---

## This task

- **Build:** the For companies marketing page in Figma. Desktop at 1440, phone at 375, plus the
  header's states. Same skeleton as the Job Seeker page (A-05).
- **Don't build:** the employer dashboard (audit sections B, C, D), the company sign-up flow, the
  Trade Partners / projects side of the product, a pricing page.
- **Read first:** `Design/HubSpot/For companies/01_CURRENT-PAGE_Teardown.md`, the live
  /companies page pulled apart band by band: what carries over, what dies, and the measured
  defects the new page has to clear.
- **Where, as built on 25 Sep:** file `aC59gtTG9nh2hwUraPnCXj`, page **Marketing website**
  (`1027:3073`), frame **Company · Hi-Fi** `1193:5591` at x 16365, beside Job Seeker · Hi-Fi.
  Shubham moved the page row into `aC59`, which settles question 16 in practice.

## The short version

1. **This page does not win a cold visitor. It finishes a handshake.** Brian has tried cold email,
   cold calling, Google Ads, LinkedIn and funnels: "nothing has worked for companies." Companies
   come from network meetings, industry groups and hardware stores. Many small firms have no
   website and are on no hiring site. So design for a phone screen opened from a link Brian just
   sent, with a way to reach a human, and don't spend the page explaining the category.
2. **The one action is post a job, and it is genuinely free today.** The live page says so. "See
   who's available" is the hook that gets them looking, which is Brian's own stated strategy: get
   businesses on, let the matches and emails pull them back.
3. **The bench is thin, and the hero must not pretend otherwise.** Just over 250 job seekers by
   July, growing 30 to 40 a month, "mostly all entry-level". Brian's hero card shows a Journeyman
   at 92%. Show a realistic mix instead, and design the empty state before the full one.
4. **Brian's page is only three bands:** hero, cost comparison, final CTA. No problem band, no
   steps, no proof, no FAQ. The rest comes from his homepage copy, the live /companies page and the
   parked FAQ seeds, all of which already exist.
5. **Pricing is the unresolved centre of this page,** and three models are live in three places:
   the site's per-applicant fees, Brian's flat monthly, and the three tiers someone added to R3
   after 19 Sep. Build the band so it can carry any of them, and treat it as the first band to cut
   (I-12, I-21).

---

## Who lands here

| | |
|---|---|
| **Who** | Owners and managers of construction firms, often small, often with no website and no LinkedIn. Busy, wary of recruiters, paying out of their own pocket |
| **How they arrive** | Warm and in person: Brian at a network meeting, an industry group, a hardware store. Google Ads never worked on this side. SEO is a long game, not this quarter |
| **What they must believe in five seconds** | Posting costs nothing. Real local workers, not résumés. No agency in the middle taking a cut. This is one person's product, and there is a person to call |
| **The one action** | Post a job, free |
| **Secondary** | See who's available near me |
| **The quiet objection** | "I've tried job boards and got nothing." The proof quote answers exactly this |

---

## What the product actually does today

Copy on this page gets checked against this table. Everything here comes from the July calls and
the live site, so anything that contradicts it needs Brian's or Jeff's yes before it ships.

| Thing | Today | What it means for the page |
|---|---|---|
| Post a job | **Free**, live site | "Post a job free" is safe. "Post your **first** jobs free" reads as a trial and undersells it |
| Matching | Automatic, and **invisible to the worker**. A matched worker has no idea a company is looking | A true and unusual selling line: you can look without tipping anyone off |
| Invite a worker to apply | **$25 per invitation** | Brian asked for invitations to be free (D-23); Jeff flagged the spam risk. May change |
| Unlock a worker's contact details | **$99 / $199 / $399** by skill level | "Unlock" is contact details only. The profile itself is visible for free. Worth saying plainly |
| Message the worker | Messaging was "being integrated" in July | "Message them directly" and "Direct messaging to the worker" need Jeff's yes |
| Skill verification | AI quizzes and coworker validation were **being built** | "All worker skills are verified through GoFindBuild" is the single riskiest line on the page |
| Projects / Trade Partners | Live and free, and **empty**: "Nobody's posted any projects" | Keep it off the hero. One FAQ answer (H7) is the right size |
| Supply | 250+ job seekers, 30 to 40 a month, mostly entry level | Drives band 02's examples and the empty state |

**The contradiction to settle before copy is final.** Brian's hiring step 3 says "Contact goes
straight to the worker. No agency sitting in the middle taking a cut," while the product charges
$99 to $399 to unlock that contact. Both can be true, an unlock fee is not an agency markup, but
the page should not leave a reader thinking contact is free. Suggested line for Brian: "Contact
goes straight to the worker. No agency, no markup on their hours, no cut of their pay."

---

## The header

Rule A-05 says both sub-pages share one hero template. The Job Seeker page's header is built
(`3022:129`), so this page clones it and refills it. Brian's company hero is the same shape
already: label, headline, subhead, trade and ZIP, one button.

| Element | Job Seeker header, as built | Brian's company hero | Use |
|---|---|---|---|
| Background | Dark streak, ~55% scrim | White | **The streak.** Same as the worker page, so the pair reads as one site |
| Chip | "Always free for workers" | "For companies" overline + "No credit card required" | **"Posting is always free"**, sitting where the worker page's chip sits. "No credit card required" moves under the button |
| H1 | "Local trade jobs. Better pay. Less searching" | **"Build your workforce. Not your recruiting bill"** | **Brian's**, unchanged |
| Subhead | Brian's worker subhead | "Connect directly with local skilled-trades talent, build an always-on pipeline, and hire when you're ready." | **Brian's**, unchanged |
| Search bar | TRADE + NEAR + button (`3022:100`) | Trade "Journeyman Electrician" + Zip "75201" | **The same bar.** Label it with Brian's line, "Get matched with the skills you need". ZIP becomes 46204 (I-08) |
| Button | "See my matches" | "See who's available" | **Brian's "See who's available."** It names the result and stays true whatever the next screen is |
| Button colour | Orange fill, navy label, 5.09:1 | Orange fill, white label, 2.63:1, fails AA | **Orange with the navy label** (I-01), lighter hover `#F4811F` (I-18) |
| Popular trades | 7 chips | none | **Keep the chips.** One tap into the search. Same seven as the worker page until GTM says otherwise |
| Under the bar | Three checks | "No credit card required" + two stats | **Three checks:** Posting is free · No placement fee · You talk to the worker, not an agency. The two stats move into the band below |
| Right side | none, the card sits in band 02 | Worker card, "Matches near 75201" | **Moves to band 02**, per Jeff's note and Brian's own confirmation that the preview cards belong on the dedicated pages |

**Header states to draw**, the same seven as the worker page: default · trade picker open · typing,
filtered · trades selected · ZIP not recognised · button inactive · phone. Reuse the picker built
at `3047:152`.

**The state that matters most here is the eighth one: nothing found.** On a thin database, a
company owner typing "Journeyman Electrician" into a ZIP with no one in it is the likely case, not
the edge case. Design it as a capture, not a dead end: "No electricians near 46204 yet. Post the
job free and we'll email you the moment one joins." That answers A-30 (no way to stay in touch),
turns the weakest moment into the lead, and is honest.

---

## Page structure

Band numbers match the Job Seeker page, so the shared skeleton is visible at a glance.
**Bold** = not in Brian's mockup.

| # | Band | Job it does | Content from | Clone from | Launch |
|---|---|---|---|---|---|
| 00 | Top Nav | For companies marked active (A-13) | Global | `3022:61` | P0 |
| 01 | Header | The promise and the one action | Brian's copy in the worker page's layout | `3022:129` | P0 |
| 02 | **Workers near you** | Shows the bench before a word of explanation | Brian's worker card ×3 | Band `3029:86`, cards replaced | P0 |
| 03 | **Problem → reality** | Problem awareness (15 Sep order) | Live /companies "We know the struggle" + 88% | `3038:142` | P0 if Brian agrees |
| 04 | How it works | Three steps to a hire | Brian's homepage hiring column | `3030:165`, refilled | P0 |
| 05 | What it costs | Agency vs GoFindBuild | Brian's comparison | New, R3 band 08 as reference | P0 if pricing is settled, else cut |
| 06 | **Proof** | A peer vouching | Brothers Insulation & Construction | `3032:453` | P0, needs permission |
| 07 | **FAQ** | Objections, and something for search | Seeds H1, H3, H4, H5, H7, H8 | `3035:4939` | P0 |
| 08 | **Hire by trade** | A way in for one-trade searches | 12 trades | `3046:4928` | P1 |
| 09 | Final CTA | Closes the page | Brian | `3043:142`, light background | P0 |
| 10 | Footer | | Global | `3036:142`, no trade columns | P0 |
| + | **Sticky CTA on phones** | "Post a job" stays in reach (A-20) | | New, from the worker page's bar | P0 |

### Why each new band

- **02 Workers near you.** Three Job Seeker cards, captioned as what a company sees. Brian's card
  is one Journeyman at 92%. Show **a Journeyman, a skilled worker and a general laborer**, because
  that is what the database holds and because a general contractor hiring labour needs to see
  labour. Caption: what is visible free (trade, experience, area, availability) and what unlocking
  buys (contact details). A second caption is the page's best line and it is simply true:
  **workers are not told you looked.** Keep it plain, no "stealth" language.
- **03 Problem → reality.** Two columns, same shape as the worker page. Left, the live page's three
  pain points cut to one line each: finding the right talent is slow and expensive · training from
  scratch usually isn't an option · skilled tradespeople are hard to find. Right, "Let's change the
  game", cut to two lines. Under it the **88%** stat (construction firms reporting jobs are as hard
  or harder to fill than a year ago) with **723,000** beside it. The worker-facing stats ($58k+,
  90%) stay on the worker page.
- **05 What it costs.** Brian's two columns: the staffing-agency way (18 to 25% markup, résumés
  with no licence check, you never meet the bench, the rate goes up at renewal) against the
  GoFindBuild way (unlimited posts, verified licences and certs, direct messaging, the relationship
  stays yours). **The comparison works without a price** and can ship with the price line as a
  placeholder. That is the version to design first, because it survives every pricing outcome.
- **06 Proof.** Brothers Insulation & Construction, Indianapolis: "We tried job boards and
  everything else, and sometimes it took months just to find one qualified person. We're too busy
  to train from scratch, so GoFindBuild made it easy to connect with experienced workers who were
  ready to go." It lands directly on the live page's second pain point, so **07 sits under 03 in
  the reading order and answers it**. Worth knowing: the quote promises experienced workers ready
  to go, which the current bench may not match. Keep the quote, it is real, and keep the hero
  honest so the page does not oversell twice.
- **07 FAQ.** Six: 1 What does it cost to hire through GoFindBuild? (H1) · 2 How is this different
  from a staffing agency or a job board? (H3) · 3 How quickly will I start seeing applicants? (H4) ·
  4 Are workers' licences and certifications verified? (H5) · 5 Can I find subcontractors and
  crews, or only individual employees? (H7) · 6 Is there a contract or a minimum commitment? (H8).
  Question 5 is where projects and Trade Partners get their one mention. Questions 1 and 6 wait on
  pricing. **If pricing stays per-applicant, seed H2 comes back**: it was cut only because Brian's
  mockup dropped that model (I-16).
- **08 Hire by trade.** Same treatment as the worker page's band, the employer half of I-11. Each
  trade opens the job-post form with that trade filled in, if Jeff can carry it (question 11). No
  counts, no dead links.
- **09 Final CTA.** Brian's copy, on a light background (Brian on the homepage: "not a fan of the
  dark color, prefer very subtle"). The button scrolls to the header or opens the post form, so
  every path starts with trade and ZIP.

### Brian's copy for this page, verbatim

Em dashes in his copy are shown here as commas. Raise it as a [Copy] note rather than changing it
silently.

| Band | Copy |
|---|---|
| 01 Header | Overline **For companies** · H1 **Build your workforce. Not your recruiting bill** · Sub "Connect directly with local skilled-trades talent, build an always-on pipeline, and hire when you're ready." · Search label "Get matched with the skills you need" · Button **See who's available** · "No credit card required" · Stats **Instant notifications** "Of matches and job applicants" and **0%** "Placement fee" · Card caption "All worker skills are verified through GoFindBuild" |
| 04 How it works | Overline "If you're hiring" · H2 **Automatically get matched to the skills you need** · **1 Post a job in 90 seconds**: "Identify trades, location, pay range, start date and immediately get matched to the best talent" · **2 Review matched workers, not resumes**: "Review detailed profiles, skills, experience, certifications, etc." · **3 Message them directly**: "Contact goes straight to the worker. No agency sitting in the middle taking a cut." |
| 05 What it costs | H2 **What it costs you today, and what it costs here** · **The staffing-agency way**, 18 to 25%: "Markup on every hour worked · Résumés with no license check · You never meet the bench · Rate goes up at renewal" · **The GoFindBuild way**, Flat monthly: "Unlimited posts · Verified licenses and certs · Direct messaging to the worker · The relationship stays yours" |
| 09 Final CTA | H2 **Post your first jobs free.** · "90 seconds to post. Matches the same day." · Button **Post a job** |
| 10 Footer | LinkedIn · Facebook · Instagram · © 2026 GoFindBuild. All rights reserved. · Terms and conditions · Privacy policy |

### Copy that needs a yes before it ships

| Line | Why | Ask |
|---|---|---|
| "All worker skills are verified through GoFindBuild" | Quizzes and coworker validation were being built in July | Brian: is it live? If not, "Licences and certs shown on every profile" |
| "0% placement fee" | True under either pricing model, it is not an agency | Brian: keep, it is the sharpest line on the page |
| "Instant notifications" | True for email. No text alerts yet | Keep, and never let the page say text |
| "Matches the same day" | A speed promise on a thin database | Brian and Jeff |
| "Post a job in 90 seconds" | Same | Jeff, against the real form |
| "Post your first jobs free" | Posting is free full stop, so this reads as a trial | Brian: "Posting is free. You only pay when you want to reach someone" |
| "Unlimited posts" + "Flat monthly" | Only true under the flat model | Waits on I-12 |
| "Direct messaging to the worker" | Messaging was being integrated | Jeff |

---

## Fix while building

| Item | What | Fix |
|---|---|---|
| I-01 | Every orange button with a white label fails AA. Brian's company page has four of them | Orange fill, navy label, 5.09:1. Hover `#F4811F` (I-18) |
| I-08 | Brian's "Matches near 75201" is Dallas; his card says Indianapolis | 46204 and Indianapolis everywhere |
| New | **Brian's card contradicts itself.** The search says Journeyman Electrician, "Looking for" says Welding and Structural steel, "Experience" says Electrical and Low voltage | One trade story per card. Make the search, the chips and the experience rows agree |
| New | **Two versions of the same card exist.** The PDF card is 96%, Fishers IN, Part-time, gear avatar, Private. The HTML card is 92%, Indianapolis, Full-time, photo, public | Pick one as canonical, build it as a component with Public and Private variants, and use it on both sub-pages (blocker 2) |
| New | A named worker with a photo here, against "You choose who sees you" on the worker page | Use the Public variant deliberately and say what is public: trade, experience, area, availability. Contact details unlock. That is what the product does |
| I-06 | Pricing sat on the homepage where half the audience had nothing to gain from it | It belongs on this page. If it also stays on the homepage, label it for employers |
| I-12 · I-21 | Three pricing stories in three places, and R3 band 08's heading still describes Brian's comparison while the band shows $49 / $149 / Custom | Design the comparison first, price line as a placeholder. Don't repeat R3's mismatch |
| I-14 | Nav labels: For companies vs Companies | Whatever the homepage ships with. Sets the URL |
| A-13 | The nav needs an active state | Underline on For companies, as the worker page does |
| A-03 · A-04 | Headings at most two lines, phone buttons full width and 48px | Check the H1 at 375. "Build your workforce. Not your recruiting bill" is long |
| A-20 | Long page on a phone | Sticky "Post a job" bar |
| New | No phone number or human route, on a page whose entire channel is a person | Recommend a "Talk to Brian" line or a booking link. Needs his yes |

---

## Components

**Reuse:** Top Nav `790:11423` · Button `787:10782` · Chip `790:11387` · the Job Seeker page's
header `3022:129`, search bar `3022:100`, picker states `3047:152`, problem band `3038:142`,
steps `3030:165`, testimonial `3032:453`, FAQ `3035:4939`, trade grid `3046:4928`, final CTA
`3043:142`, footer `3036:142`.

**Build:**

1. **Job Seeker card**, as a proper component with **Public** and **Private** variants. The Private
   concept exists on the worker page at `3046:151`. This page needs Public, with the unlock state
   shown. One component, both pages, one canonical anatomy (blocker 2).
2. **Comparison block** for band 05, two columns, agency and GoFindBuild, price line as a slot.
3. **Empty state** for the search: no results, with the email capture.
4. **Sticky CTA bar**, reuse the worker page's, label "Post a job".
5. **Input field** (I-13) is still missing from the design system. The search bar borrows from the
   worker page until it exists.

---

## Open questions, with owners

Numbering continues from `Read me/03_BLOCKERS_for-Harpreet.md`, which stops at 16.

| # | Question | Owner | Blocks |
|---|---|---|---|
| 17 | Is there a company sign-up flow designed, and what does "See who's available" open? Sign-up with trade and ZIP carried in, or a results page? | Jeff | The header's whole promise |
| 18 | Flat monthly or per-applicant, and what exactly is free? | Brian | Band 05, FAQ 1 and 6, the hero chip |
| 19 | Is skill and licence verification live today? | Brian | The card caption, FAQ 4 |
| 20 | Is messaging live? | Jeff | Step 3, band 05 bullet |
| 21 | Are invitations still $25, or free as you asked (D-23)? | Brian and Jeff | FAQ 1, the unlock caption |
| 22 | Do Trade Partners and projects belong on this page at all, or only in FAQ 5? | Brian | Band 07, scope |
| 23 | Permission to use the Brothers Insulation quote, name and city, and is there a logo? | Brian | Band 06 |
| 24 | A phone number, a booking link, or nothing? | Brian | Header and final CTA |
| 25 | Which worker card is canonical, the PDF one or the HTML one? | Brian | The component |
| 26 | Can a trade tile open the job-post form prefilled? | Jeff | Band 08 |
| 27 | Trade list and keywords for the employer side (the other half of I-11) | GTM | Band 08, chips |

---

## Order of work

0. **Figma.** New page **Marketing page · Company** after Marketing page · Job Seeker, one dated
   section, "Created by Claude" credit row, notes rail on the right.
1. **Clone the skeleton** from the Job Seeker page, band by band, so the two pages are structurally
   identical (A-05). Then refill.
2. **Components:** the Job Seeker card with both variants, the comparison block, the empty state.
3. **Hi-fi desktop**, in the order that wins approval: 01 header · 02 workers · 04 steps · 06 proof ·
   09 final CTA · 07 FAQ · 03 problem · 00 and 10 · then 05 pricing and 08.
4. **Phone at 375:** header and picker, workers (cards stack), steps, FAQ, sticky CTA. Same
   selective-mobile approach as R3 and the worker page.
5. **Annotate** one note per band: source, Elevate preset, modules, what changed from Brian, tagged
   [Theme] [Editor] [CSS] [Module] [Copy].
6. **Hand to HubSpot.** Every band maps to an Elevate preset already used on Home. New modules:
   the search bar and the Job Seeker card. Page folder is `Design/HubSpot/For companies/`.

### Launch cut

| Ships at launch | After launch |
|---|---|
| 00 · 01 · 02 · 04 · 06 · 07 · 09 · 10 · sticky CTA · 03 if Brian agrees | 05 until pricing lands (question 18) · 08 (questions 26 and 27) · live worker cards · the human-contact route if Brian says no for now |

---

## Done means

- [ ] Built in the agreed file, on its own page, in a dated section
- [ ] The header is the worker page's template, refilled with Brian's copy
- [ ] Band 02 shows a realistic mix, not three journeymen, and says what unlocking buys
- [ ] The no-results state exists and captures an email
- [ ] Nothing on the page claims verification, messaging or same-day matches without a yes
- [ ] Every button passes 4.5:1, every header line passes 4.5:1
- [ ] The Job Seeker card is one component with Public and Private variants, used on both pages
- [ ] Phone frames for header, workers, steps, FAQ and the sticky bar; headings at most two lines
- [ ] One note per band; every open question has an owner
- [ ] Bound to variables and text styles, no loose values
- [ ] `00_FIGMA-WORK-LOG.md` updated

---

## Housekeeping found while writing this

`I-18` (button hover), `I-19` and `I-20` (Hi Fi B's fonts and typos), `I-21` (pricing tiers against
the comparison heading) and `I-22` (pricing card buttons) are cited in the work log, the Job Seeker
plan and the live-page fix list, but `Read me/02_ISSUES-LOG.md` stops at I-17. The numbers are
real and in use; the log needs the five rows so the references resolve.

---

**Sources.** Brian's mockup page 02, For companies, and his homepage hiring column
(`Design/Figma/Source files/GoFindBuild-Marketing-Site-All-Pages.html`) · his brief
(`Project Context/2026-09-11_Brian-Mockup-Brief.md`, the three preview cards) ·
gofindbuild.com/companies, read 23 Sep 2026, torn down in
`Design/HubSpot/For companies/01_CURRENT-PAGE_Teardown.md` · Meeting 1 (supply is
mostly entry level, what companies see, vetting by quiz) · Meeting 2 (acquisition is a ground game,
Trade Partners and projects, invisible matching, $25 invite, pay to unlock) · Meeting 5 (quizzes
both sides) · `Project Context/2026-09-15_Meeting-Notes.md` (band order, FAQs for both ICPs,
trade pages) · `Audit/Audit list.md` (A-03, A-04, A-05, A-13, A-20, A-30, D-23) ·
`Read me/02_ISSUES-LOG.md` (I-01, I-06, I-08, I-11, I-12, I-13, I-14, I-16) ·
`Read me/04_FAQ-SEEDS_sub-pages.md` (H1, H3, H4, H5, H7, H8) ·
`Design/Figma/03_CONTEXT_Job-Seeker-and-Company-Pages.md` and the built page
(`eulu7Yq3gH7gaezVZbn0bi`, `3021:320`) · `Design/HubSpot/Home/01_R3_HubSpot-Elevate-Mapping.md`.
