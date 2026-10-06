# For companies · redesign and build plan

Written 23 Sep 2026. Two deliverables: a hi-fi **Figma page Brian approves**, and **the same page
live in HubSpot**. This file is only the plan: what happens, in what order, who owns it, how long it
takes, and what gets cut if the week tightens.

- Design detail, band by band: `../../Figma/04_CONTEXT_Company-Page.md`
- Defects the new page has to clear: `01_CURRENT-PAGE_Teardown.md`

---

**Progress, 25 Sep:** steps 1 and 3 are done for desktop. The page is built at `1193:5591` in
`aC59`, with a changes card beside it (see the Figma work log). Still to do: phone frames, the
header states, step 2's components, and all of step 4.

## The shape of it

| Step | What | Owner | Effort | Can start |
|---|---|---|---|---|
| 0 | Unblock the build: portal, file, five decisions | Harpreet, Brian, Jeff | ongoing | now |
| 1 | Figma structure, cloned from the Job Seeker page | Shubham | 3h | **now** |
| 2 | Components | Shubham | 3h | now |
| 3 | Hi-fi desktop, phone, notes rail | Shubham | 5h | after 1 and 2 |
| 4 | HubSpot build | Shubham, Jeff if modules | 1 to 2 days | after Brian's yes |
| 5 | QA and publish | Shubham | 3h | after 4 |

**Design is about a day and a half and nothing in step 0 blocks it.** Step 0 blocks the build only.

---

## Step 0 · What has to be true before we build

### Three hard blockers, build cannot start without them

| # | Blocker | Owner | Why it stops everything |
|---|---|---|---|
| B1 | **Which HubSpot portal.** Everything so far is in Shubham's sandbox (1 Meter House, 247469662). GoFindBuild's own portal, with the theme and the domain, does not exist as far as this project knows | Harpreet with Brian | The page cannot go live in a sandbox |
| B2 | **The Squarespace to HubSpot move.** The live site is Squarespace. A single new page in HubSpot has nowhere to live until the domain question is answered | Harpreet with Brian and Jeff | Decides whether this page launches alone or with the site |
| B3 | **Which Figma file.** The Job Seeker page was built in `eulu7…`, every note points at `aC59…` | Shubham, Harpreet | Two files drift into two sources of truth |

Default if nobody answers: **build the Company page in `eulu7…` beside the Job Seeker page**, and
keep the HubSpot build in the sandbox as a demo, exactly as Home is today.

### Five decisions, each with the default I will use

| # | Decision | Who | If no answer by Thursday |
|---|---|---|---|
| D1 | Pricing model (I-12) | Brian | Ship Brian's comparison **with no numbers**. If he wants numbers, band 05 is the last thing built |
| D2 | Is skill verification live? | Brian | Soften to "Licences and certs shown on every profile" |
| D3 | Button treatment (I-01) | Brian | Orange fill, navy label, 5.09:1. Hover `#F4811F` |
| D4 | Nav labels and URL (I-14) | Brian | Follow the homepage demo, keep the URL `/companies` |
| D5 | Testimonial permission | Brian | Ship the quote as a grey labelled placeholder, the rule already agreed on 19 Sep |

**None of these stop the design.** Each one changes a band's content, not its shape.

---

## Step 1 · Figma structure, 3 hours

New page **Marketing page · Company**, one dated section, notes rail on the right, same conventions
as the Job Seeker page.

1. Clone the Job Seeker page's eleven bands so the two pages are structurally identical (A-05).
   Node IDs for each band are listed in the plan.
2. Refill each band with Brian's company copy.
3. Reorder nothing. The band numbers stay matched to the Job Seeker page so the pair reads as one
   site and so HubSpot reuses the same presets.
4. Write one note per band as it is built, rather than at the end.

**Done when:** eleven bands exist with real copy, nothing is lorem, and every band has a note.

## Step 2 · Components, 3 hours

Four things, in this order. Everything else is reused.

1. **Job Seeker card**, one component, **Public and Private variants**. Private exists as a concept
   on the Job Seeker page; this page needs Public with the unlock state. One component serves both
   pages and settles which of Brian's two card versions is canonical.
2. **Comparison block** for band 05, two columns, price line as a slot so it survives any pricing
   outcome.
3. **Search empty state**: no results, with the email capture. This is the likely case on a thin
   database, not the edge case.
4. **Sticky CTA bar** for phones, reused from the Job Seeker page, relabelled "Post a job".

**Done when:** all four are components with variants, bound to variables and text styles, sitting
on the design system page rather than loose on the canvas.

## Step 3 · Hi-fi, 5 hours

**Desktop, in the order that wins approval:** 01 header · 02 workers · 04 steps · 06 proof ·
09 final CTA · 07 FAQ · 03 problem · 00 and 10 nav and footer · then 05 pricing and 08 trades.

**Header states:** seven as on the Job Seeker page, plus the eighth that matters here, nothing
found.

**Phone at 375:** header and picker, workers (cards stack), steps, FAQ, sticky bar. Same selective
approach as R3 and the Job Seeker page, not every band.

**Done when:** every button passes 4.5:1, no heading runs past two lines at 375, nothing claims what
the product cannot do, and the notes rail is complete.

**Then:** to Brian, with D1 to D5 attached as questions rather than as a separate email.

---

## Step 4 · HubSpot build, 1 to 2 days

**The good news: this page is mostly assembly.** Every band uses an Elevate preset already
configured for the homepage, so the theme-settings pass is done and does not repeat.

| Band | Elevate preset | Already proved on Home | New work |
|---|---|---|---|
| 00 Top Nav | Site header, global | yes | active state only |
| 01 Header | Hero banner + search | partly | **search bar** |
| 02 Workers near you | Products and services shell | yes, band 06 | **Job Seeker card** |
| 03 Problem | Metrics, centered | yes, band 03 | none |
| 04 How it works | Features | yes, bands 04 to 05 | none |
| 05 What it costs | Pricing | yes, band 08 | two columns not three |
| 06 Proof | Testimonial cards | yes, band 07 | one card not two |
| 07 FAQ | FAQ v2 | yes, band 09 | none |
| 08 Hire by trade | Menu modules | yes, band 11 | none |
| 09 Final CTA | Call to action, centered | yes, band 10 | light, not dark |
| 10 Footer | Site footer, global | yes | none |

**Only two things are genuinely new: the search bar and the Job Seeker card.** Both are custom
modules and both are Jeff's kind of work.

**The no-dev path, if Jeff has no room this week.** The page still ships:

- The Job Seeker cards are built from Elevate's Card module and a few lines of CSS, with static
  content. Slower to update, identical to look at.
- The header drops the live search and carries two buttons instead: **Post a job, free** as the
  primary and **See who's available** as the secondary. Do not ship fields that look like a search
  and are not one.

## Step 5 · QA and publish, 3 hours

Run against the teardown, so the new page does not repeat what the old one does:

- [ ] One H1, and it is the headline
- [ ] Page title and a real meta description, og:image set
- [ ] Every button and every price label at 4.5:1 or better
- [ ] Phone: first screen carries the promise, not a photo. Buttons full width, 48px
- [ ] No dead links, no `utm_source=null`, no trailing spaces in links
- [ ] Alt text on every image, hero image under about 300 KB, no upscaled photos
- [ ] Footer carries the right year, Terms and Privacy
- [ ] Old `/companies` URL redirects, it does not 404. Companies Brian met have that link
- [ ] Page weight and requests no worse than the Squarespace page it replaces
- [ ] Nothing claims verification, messaging or same-day matches without D2

---

## What ships, and the cut order

| Ships at launch | After launch |
|---|---|
| 00 nav · 01 header · 02 workers · 04 steps · 06 proof · 07 FAQ · 09 CTA · 10 footer · sticky bar | 05 pricing until D1 lands · 08 hire by trade · live cards · the human contact route |

**If the week tightens, cut in this order:** 05 pricing, then 08 trades, then 03 problem, then the
phone frames for anything below the fold. The eight bands above are the page. Do not cut band 02,
it is the only thing on the page that shows the product.

## The week, if it is live on Wed 30 Sep

| Day | What |
|---|---|
| Wed 23 | Steps 1 and 2. Structure and components |
| Thu 24 | Step 3. Hi-fi, phone, notes. To Brian end of day with D1 to D5 |
| Fri 25 | Brian's comments applied. HubSpot assembly starts on the bands that need no decision |
| Mon 28 | Modules or the no-dev path. Page assembled |
| Tue 29 | Step 5. QA, fixes, redirect |
| Wed 30 | Publish |

**The honest risk:** the same window also holds the Job Seeker page's HubSpot build and the 24 fixes
on the homepage demo. Three pages cannot ship in one week by one person. Either the Company page is
the priority in that window, or the launch is the homepage alone with the two sub-pages following.
That is a call for Harpreet, and it is better made on Wednesday than on Monday.

## What I need from you to start

1. **Go on B3:** build in `eulu7…` beside the Job Seeker page. One word is enough.
2. **B1 and B2 into Harpreet's hands today,** because they take the longest to come back.
3. **Which day you want it live.** The plan above assumes Wed 30 Sep.
