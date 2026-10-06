# GoFindBuild marketing site: plan off the 15 Sep meeting

Written 19 Sep 2026. Source: `Project Context/2026-09-15_Meeting-Notes.md`,
the three audits in `Audit/` (one checklist: `Audit/Audit list.md`), and the live site as it stands today.

**Roles.** Harpreet is the manager and owns the client and GTM conversations.
Shubham is the designer and owns the draft. The action items in the 15 Sep
summary are addressed to Harpreet as commitments; the design execution is
Shubham's. The split is at the bottom of this doc.

**Decisions locked 19 Sep:**
- Delivery: **first Figma draft Monday 21 Sep EOD.** Working Sat, Sun, Mon.
- Approach: **structure first.** Sequence approved before pixels.
- Typography: **keep the existing design system.** Instrument Sans for display,
  Inter for heading/body/UI. The audit's 4-level ladder gets applied on top of
  it, so no design system rework.
- Social proof: ~~grey labelled placeholder, no real quotes yet~~ **Corrected 19 Sep: two real testimonials exist in Brian's mockup.** Build the band for real.

> **Status, Sat 19 Sep:** Saturday's "decide the page" step is done. All 13 bands
> (00 to 12, per `Design/Figma/01_STRUCTURE_Marketing-Homepage.md` v2) are laid out low-fi on
> the **Marketing website** page of the Figma file, with a sequence comparison
> and a per-band notes rail. Section `1032:3`,
> https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign?node-id=1032-3
> Next: Sunday, hero + fork to hi-fi (welder photo still a grey placeholder),
> as a new Round 2 section.


> ## Partly superseded, 19 Sep
>
> Written before Brian's 11 Sep mockup was read. Where this file and
> **`Design/Figma/01_STRUCTURE_Marketing-Homepage.md` v2** disagree, **v2 is right.**
> Specifically, these claims below are wrong:
>
> - The HTML is **Brian's mockup**, not a capture of the live site. Anything
>   here reasoning from "the current site" is reading his proposal as the
>   status quo.
> - **Testimonials exist.** Two real ones in the mockup. Not a grey placeholder.
> - **Pricing is not the $99 / $199 / $399 model.** Brian's mockup moves to flat
>   monthly against an agency markup, and he may cut the band entirely. Do not
>   lift the old numbers onto the page.
> - **The hero is not capped at 1024px.** That was the live site's excavator.
>   Brian supplied a 1400 x 799 welder photo.
> - The **"023" stat typo and the profanity banner are already gone** from
>   Brian's copy. They are not P0 items.
>
> What still holds: the schedule, the role split, the FAQ seeds, the trade page
> IA, the design system component gap, and the Squarespace to HubSpot point.

---

## Read this first. Three things change the shape of this job.

### 1. The schedule now fits, with zero slack

Delivery was re-agreed to **Monday 21 Sep EOD** for the first Figma draft.
That is the number this plan is built around.

| | |
|---|---|
| Today | Sat 19 Sep |
| First Figma draft due | **Mon 21 Sep EOD** |
| Direction approved, best case | Tue 22 Sep |
| HubSpot implementation, ~1 week | Tue 23 Sep to Mon 29 / Tue 30 Sep |
| Launch target | end of Sep, about 30 Sep |

Moving the draft to Monday pulls implementation forward enough that the
end-of-September launch is reachable. It was not reachable on the original
"mid/end of next week" start. So the date change fixed the schedule.

**What it did not buy is slack.** There is one working day before the draft is
due and no room for a second approval round. Two consequences:

- **The draft has to be approvable in one pass.** That argues for showing the
  *sequence and the fork* at deliberately lower fidelity rather than three
  polished sections. The meeting itself framed Monday as "agreement on the Figma
  direction first", so structure is the deliverable and pixels are not.
- **The blocking answers are needed before Monday, not on Monday.** Typography
  especially. If GTM wants a different typeface, every heading in the draft
  changes, and finding that out on Tuesday wastes the only buffer there is.

### 2. Almost none of this needs writing

The meeting recorded the page as missing a problem-awareness section. The
content is not missing. It is written, live, and sitting on the sub-pages:

- `/companies` carries **"We know the struggle"** with three named pain points
  (finding talent is slow and expensive, training from scratch is not an option,
  skilled trades are hard to find for specialist roles), then
  **"Let's change the game"** as the turn.
- `/job-seekers` carries **"We get it."** (the search feels overwhelming, is
  college the only route) and **"Here's the reality..."** as the turn.

So the homepage problem section is a **promotion and compression job**, not a
copywriting job. Both sides already have a problem statement and a reframe in
the client's own voice. That is the difference between a two-day draft and a
two-week one.

### 3. Pricing is not blocked

The single worst finding in the UX audit was no pricing on the homepage, called
a major conversion barrier. But `/companies` already publishes the full model:

| Action | Price |
|---|---|
| Post a job | Free |
| Invite a matched job seeker to apply | $25 per invitation |
| Unlock a Candidate (entry level) | $99 |
| Unlock a Skilled Applicant (prior trade experience) | $199 |
| Unlock an Expert Applicant (plumbing, electrical, HVAC) | $399 |

Usually pricing on a homepage is blocked waiting on a business decision. Here
the numbers are already public. Surfacing them is a design decision you can make
this week, and the skill-based tiering is a genuinely differentiated thing to
show. Confirm with Brian that the numbers are still current, then use them.

---

## What is on the site today

| Page | Sections, in order |
|---|---|
| **Home** | Rotating hero ("Find the best projects / employees / careers in your area") with one CTA "Start your search" · profanity banner · company value props (Save money, Get real applicants, Grow your business) · How it works, company side only · worker value props (No experience required, Paid training, Privacy) · Jobs on our platform · "Why we built GoFindBuild" stats |
| **/companies** | Hero · We know the struggle · Let's change the game · **Pricing** · Find your next project · Why GoFindBuild |
| **/job-seekers** | Hero · We get it. · Here's the reality... · What we'll do for you · Ready to build a bright future? |

**The real structural problem.** All three pages half-serve both audiences.
The homepage tries to sell to companies and workers in alternating blocks, and
the sub-pages repeat the job properly. Nothing forks cleanly. That is why the
page does not convert, more than any individual section being absent.

Note also: "How it works" exists for companies and has no worker equivalent
anywhere. Workers get benefits but never a three-step path.

---

## Proposed homepage structure

Following the two-sided pattern the Wellfound reference validates: one shared
promise, an immediate fork, then a dedicated run for each side, then shared
proof, then FAQ.

| # | Section | Job it does | Where the content comes from |
|---|---|---|---|
| 1 | Hero, single promise | One sentence on what GoFindBuild is. Kills the rotating text. | New, one line. Audit already suggests "the construction job platform built for the trades" |
| 2 | **Audience fork, two cards** | The whole two-sided requirement, solved in one component. "Hire skilled trades" / "Find work". Two CTAs, visibly different destinations. | New component, existing labels |
| 3 | Proof strip | Logos or a live count. Sits high, like the reference does. | **Blocked, needs Brian** |
| 4 | Problem, both sides | Problem awareness the meeting asked for | Compress `/companies` "We know the struggle" + `/job-seekers` "We get it." |
| 5 | Solution / how it works, company | Three steps | Exists on Home |
| 6 | Solution / how it works, worker | Three steps, parity with companies | **Write new, worker side has none** |
| 7 | Pricing | Removes the biggest objection | Exists on `/companies`, lift it |
| 8 | Live jobs | Marketplace liquidity as proof | Exists on Home |
| 9 | Stats, reframed | Problem scale, outward facing | Exists on Home, see note below |
| 10 | Testimonials | Trust. Alternate company and worker quotes. | **Blocked, needs Brian** |
| 11 | FAQ, both ICPs | Objection handling + SEO surface | Seeds below |
| 12 | Final CTA, split again | Mirrors section 2 so both paths close | New |

**On the stats:** they are currently last, under the heading "Why we built
GoFindBuild", which frames them as company backstory. The same four numbers
reframed outward ("94% of construction businesses cannot fill roles") become the
problem section. Same asset, moved and re-headed. Do not write new ones.

---

## The five targets, turned into work

### 1. Polish the designs
The audits already prescribe this. Do not re-derive it. The three critical items:

- **Typography.** Audit calls it Critical: no hierarchy, all weights read the
  same. Fix is a 4-level ladder (H1, H2, H3, body) with real weight contrast,
  plus a separate mobile scale capped at 2 lines per heading. Desktop 40 to 64px
  must not carry to mobile unchanged.
- **CTAs.** Also Critical: at least four different button styles for the same
  action. Collapse to exactly two variants, Primary and Secondary, same label
  for the same action everywhere. Drop the mixed angled and pill shapes.
- **Hero image.** This is the meeting's "get it out of the standalone
  container" item, and the audit is more specific than the meeting was:
  - Mobile hero is a **contrast failure**, white text straight on the photo with
    no scrim. Rated Critical. Add a gradient overlay, or move the headline to a
    solid panel below the image, which is the safer mobile answer.
  - Cropping cuts subjects at joints (excavator arm at the frame edge, workers
    cut at the waist). Write a short art-direction rule: 20% breathing room,
    never crop at a joint, leave the left 35% clear for text.
  - **Asset ceiling, checked 19 Sep.** The hero file is only **1024 x 768** on
    the CDN, and that is the master, not a crop. Requesting it at 2500w still
    returns 1024. So the bad cropping is not a design mistake, it is a too-small
    4:3 source forced into a wide band. This is the one real constraint on the
    hero's visual direction, and it sits in tension with the meeting's ask to
    take the hero out of a standalone container. Resolution options are in the
    hero note below.

**Hero treatment, given a 1024px source.** Three ways out, in order of preference:
1. **Masked shape that bleeds off one edge.** "Not in a standalone container"
   does not have to mean full bleed. An image masked into a shape that runs off
   the right edge and overlaps the type block reads as integrated, needs far less
   pixel width than a full-bleed band, and works at 1024. Best answer available
   without new photography.
2. **Full bleed with a heavy gradient or duotone.** A 1.4x upscale to 1440 is
   borderline, and treatment hides softness. Also fixes the mobile contrast
   failure at the same time.
3. **Solid panel below the image**, which the mobile audit recommends outright.
   Safest and cheapest, but the most contained, so it argues against what the
   meeting asked for.

Pick 1 for the Monday draft, and note the photography request in the annotation
so the direction is legible as a constraint rather than a choice.

### 2. Landing page structure
Build the table above. The order is the deliverable, so get agreement on the
sequence before polishing any single section.

### 3. FAQs
Seeds below. Send as a list for Brian to strike, not as finished copy. Faster to
react to 16 questions than to a blank page.

### 4. Category pages
See the IA recommendation below. The important move is to build **one template
per intent, not twelve pages.**

### 5. First Figma draft
Follow the file's existing conventions, they are in `Design/Figma/00_FIGMA-WORK-LOG.md`: each round is
its own section on the Presentation page, never edit a prior round in place,
annotation text light because the section background is dark grey.

---

## The three days

Working Sat 19, Sun 20, Mon 21. Structure first, then fidelity where it pays.

**Saturday, decide the page.** Lay out all 12 sections as stacked labelled blocks
on a new Presentation section. No styling. The output is the sequence, which is
the thing actually being approved. Pull the problem copy across from
`/companies` and `/job-seekers` while laying out, since it already exists.

**Sunday, make the argument visible.** Hero and the audience fork to high
fidelity. These two carry the whole two-sided case and the entire first
impression, so if only two things are finished, these are they. Then drop in the
pricing block with the real numbers off `/companies`, and apply the 4-level type
ladder and the two CTA variants across every block, including the low fidelity
ones, so the hierarchy fix reads even where the section is grey.

**Monday, close it.** Problem section to proper layout. Annotation frames above
each screen explaining what each section is doing and where its content came
from, which is what turns a layout into something approvable in one pass. Then
the placeholders, labelled honestly.

**Grey and labelled on Monday**, because each one waits on someone else:
testimonials, logo wall or count, FAQ copy, worker how-it-works, trade pages.
A box reading "Testimonials, 3 employer + 3 worker, awaiting quotes from Brian"
still gets the sequence approved, and it makes the dependency visible to the
client rather than looking like an omission.

**File conventions**, from `Design/Figma/00_FIGMA-WORK-LOG.md`: new top-level section on the Presentation
page, never edit a prior round in place, annotation text light because the
section background is dark grey. Font is Inter throughout the canvas furniture.

## Proposed cut for launch

**P0, ships for launch.** All of it is re-sequencing or a known fix, so none of
it waits on anyone else.

1. Hero rework, rotating text gone, single promise
2. Audience fork cards, the two-sided requirement
3. Problem section, compressed from the two sub-pages
4. Pricing lifted from `/companies`
5. Typography ladder and the two CTA variants
6. Hero image overlay and crop rule
7. Two content bugs that are live right now, both trivial:
   - the stats section reads **"023 HBI Labor Market Report"**, missing the 2
   - the banner still reads **"designed to get sh** done!"**. The UX audit
     flagged this as a brand and trust risk in May and it is still there. Worth
     raising directly rather than quietly fixing, since it may be a deliberate
     voice choice by a 20-year construction veteran. Ask, do not assume.

**P1, straight after launch.** Each one waits on someone else.

| Item | Waiting on |
|---|---|
| Testimonials | Brian, real quotes from employers and workers |
| Logo wall or user count | Brian, permission and real numbers |
| FAQ final copy | Brian's review of the seeds |
| Trade category pages | GTM's trade list and keyword targets |
| Worker-side how it works | Brian, does a worker three-step path exist |
| Favicon, footer utility and legal links | Audit items, small, no design risk |

---

## FAQ seeds

Written against the actual model, not generic. Send for Brian to strike.

**Companies**
1. What does it cost to hire through GoFindBuild?
2. How does paying per applicant work, and what if I do not want to interview anyone I am sent?
3. How is this different from a recruiter, or from posting on a general job board?
4. How quickly will I start seeing applicants?
5. Are workers screened, and can I see certifications before I unlock someone?
6. Which trades can I hire for?
7. Can I find subcontractors and crews, or only individual employees?
8. Is there a contract or a minimum commitment?

**Workers and job seekers**
1. Does it cost me anything to use GoFindBuild?
2. Do I need a resume, a degree, or previous experience?
3. Who can see my personal and contact details, and when?
4. How does the paid training work?
5. What kinds of jobs and trades are on the platform?
6. How do I know a company posting a job is legitimate?
7. How long until I hear back after applying?
8. What certifications help me get hired faster, and can I add them later?

Two of these, company #1 and worker #1, are the highest-value answers on the
page. Cost is the first objection on both sides, and the current site answers it
for companies only, and only if you find the sub-page.

---

## Trade category pages: the IA recommendation

**A single page per trade will not work,** because "hire plumbers" and "plumbing
jobs" are two different intents with two different conversions. One page serving
both converts neither.

Recommendation, two intents, two URLs, cross-linked:

```
/hire/plumbers      company intent   CTA: post a job
/jobs/plumbers      worker intent    CTA: create a profile
```

- **Sitemap position.** Both sit under the existing audience split, so they
  inherit the right navigation. `/hire/*` under Companies, `/jobs/*` under Job
  Seekers.
- **Discoverability.** A "Browse by trade" block in the footer covering both
  columns, plus a trades index at `/hire` and `/jobs`, plus contextual links
  from the two homepage audience sections. Footer alone is not enough, and the
  audit already flags the footer as minimal.
- **Design system.** Build **two templates**, one per intent, driven by fields
  (trade name, hero photo, pain points, typical pay range, sample jobs). GTM
  then adds trades without design involvement. If this ships as hand-built
  pages, you will be hand-building trade pages for the next year.
- **Pricing tie-in.** The $99 / $199 / $399 tiers map onto trades directly.
  Plumbing, electrical and HVAC are the named Expert tier. A trade page that
  states the tier up front is doing real conversion work.

---

## Reuse the audits, do not redo them

`Audit/` (one checklist: `Audit/Audit list.md`) holds 46 findings across desktop (19), mobile (16) and UX (11).
Most of the meeting's asks are already written up there with a prescribed fix
and a severity. Working from the audit instead of from scratch is the main
reason a draft can still land against a broken schedule.

Two file notes, because the names mislead:

- **Latest audit is `GoFindBuild_Design_Audit_Final_v2 (1).xlsx`**, 26 May
  16:45, 23KB. The one without the `(1)` is older and smaller despite the
  cleaner name.
- `GoFindBuild_Design_Audit (1).xlsx` is byte for byte identical to
  `GoFindBuild_Design_Audit.xlsx`. Say the word and I will delete the copy.

Also worth knowing: the mobile audit references sections named "We know the
struggle", "Let's change the game" and "What we'll do for you", which means it
covered the sub-pages, not just the homepage. The audit is broader than it looks.

---

## Open items, split by owner

**Platform note, checked 19 Sep.** The current site runs on **Squarespace**. The
plan is to implement in **HubSpot**. That is a migration, not a restyle, and a
one week implementation estimate reads differently in that light. Flagged on
Harpreet's list alongside the scope question.

### Harpreet to raise, client and GTM side

These are management conversations, not design ones. Sent as a list in
`03_BLOCKERS_for-Harpreet.md`.

| # | Item | Why it is his | Blocks |
|---|---|---|---|
| 1 | GTM typography feedback: what was it exactly? | GTM relationship | Resolved for now by keeping the existing system, but a late change reworks the design system too |
| 2 | Do real testimonials exist? 3 employer + 3 worker | Brian owns the customers | Post-launch section, grey Monday |
| 3 | Are $25 / $99 / $199 / $399 still current? | Commercial | Pricing block ships with them either way, marked unverified |
| 4 | Is the banner profanity deliberate brand voice? | Client's voice, not ours to change | A live brand risk flagged in May |
| 5 | Which trades first, and keyword targets? | GTM owns the list | Trade page templates |
| 6 | Is a worker-side three-step path defined? | Product knowledge sits with Brian and Jeff | Worker how-it-works section |
| 7 | **Is the marketing site + HubSpot build in scope?** | Commercial, squarely his | Nothing design-side, but a week of implementation is about to go in |

Item 7 is the one to raise regardless of how the draft lands.
`Project Context/Project-Scope.txt` is six phases, every one about the platform and
product: audit, UX strategy, wireframing, validation, UI design, testing. A
marketing website and a HubSpot build are not in that document.

### Shubham to decide, design side

Resolved and no longer open:

- Section sequence and the fork pattern. Decided, table above.
- Type ladder and CTA variants. Decided, existing system plus the audit's
  4-level ladder, exactly 2 CTA variants.
- Hero image treatment. Decided, gradient overlay or a solid panel below the
  image, plus the 20% breathing room and no-crop-at-joints rule.
- Which sections ship grey. Decided, the five listed above.
- Trade page IA. Recommended, two intents and two URLs, built as two templates.
  Needs Harpreet to get the trade list before it can be built.

### Housekeeping

`GoFindBuild_Design_Audit (1).xlsx` is byte for byte identical to
`GoFindBuild_Design_Audit.xlsx`. Awaiting a yes before deleting the copy.
