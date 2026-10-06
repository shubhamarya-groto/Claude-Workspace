# Go Find Build

Master context for the GoFindBuild project (Groto working with the GoFindBuild team). Written after reading every uploaded file and cross-checking them. Start here, then follow the links.

---

## 1. What this is

**GoFindBuild** (gofindbuild.com) is a two-sided **construction labour marketplace**.

- **Companies** post trade jobs, get matched to workers, invite them, and pay to unlock contact details. They can also post projects and find trade partners (live, free, empty).
- **Workers** (skilled trades and labourers, many entry level, non-technical, phone-first) build one profile, get matched, and hear from employers. Free for workers.
- **State in mid-2026:** about 250 job seekers (30–40 a month, all from Google Ads), few paying companies. Brian: "nothing has worked for companies", they come from in-person networking. The app is a built Vue product; the public site is Squarespace.
- **The engagement:** Groto (UX) audits and redesigns. Scope file lists 6 phases (audit done, then UX strategy, wireframes, validation, UI, testing). The marketing site and HubSpot build are **not in that scope file** (blockers item 7).

**People:** Brian (client, founder, writes the copy) · Jeff (developer, onboarding, fractional) · Harpreet (Groto, manager/client lead) · Shubham (Groto, designer) · GTM team (typography, trade pages).

**Visual direction:** "Middle ground" (chosen 22 Jun): clean neutral base, purposeful orange. Design system **Built Bold**: Instrument Sans (display), Inter (everything else), navy `#16243D`, orange `#F16C0E`.

---

## 2. Timeline (what the files show)

| Date | Event | Where |
|---|---|---|
| 27 Apr | Intro call: audit first, hours-per-week engagement | `Project Context/Meeting-1.txt` |
| 14 May | Product walkthrough, pricing mechanics, acquisition reality | `Meeting-2.txt` |
| 22 Jun | Priorities: profiles, onboarding, dashboard; moodboard "Middle ground" chosen | `Meeting-3.txt` |
| 1–2 Jul | Brian's review of dashboard designs; action items | `UX-Review-7-1.md`, `Meeting-5.txt` |
| 11 Sep | Brian's marketing mockup and brief | `2026-09-11_Brian-Mockup-Brief.md` |
| 15 Sep | Decision: marketing site first, then product; launch end of Sep | `2026-09-15_Meeting-Notes.md` |
| 19–21 Sep | Homepage R1 → R3 in Figma | `Design/Figma/00_FIGMA-WORK-LOG.md` |
| 21–23 Sep | Live HubSpot demo built and checked | `Design/HubSpot/Home/` |
| 22–25 Sep | Job Seeker, Company, About Us pages; Elevate kit; Iteration 1 review, Iteration 2 | Figma docs 03–06 |
| ~30 Sep | Target launch | `Read me/01_NEXT-ACTIONS…`, `Company/00_PLAN…` |

**Latest dated entry in the files is 25 Sep.** Update, 6 Oct: the page designs are done and the HubSpot build starts now, on staging, with copy changes ignored until final publishing. See `Design/HubSpot/00_BUILD-PLAN_Staging.md`.

---

## 3. How the files connect

```
Meetings 1,2,3,5 ─┐
Project-Scope     ├─► Brian's UX review 1 Jul ──► Audit list section D
Brian's brief 11 Sep ─► Brian's mockup HTML ──┐
15 Sep meeting ───────────────────────────────┤
                                              ▼
Audits (desktop 19, mobile 16, UX 11) ─► Audit list A ─► Figma homepage R1→R3→R4 ─► HubSpot demo (Home)
Dashboard audits (xlsx 39 + PDFs 30/50) ─► Audit list B, C        │                      │
                                                                  ▼                      ▼
                          Job Seeker / Company / About Us pages (Figma)   H-01…H-24 fix list, module inventory
                                                                  │
                                    Iteration 1 review ─► Iteration 2 (Elevate kit swaps) ─► HubSpot build plan
```

| Layer | Files | Role |
|---|---|---|
| **Why** | `Project Context/` | What Brian wants, what was decided, what the product does |
| **What's wrong** | `Audit/` (esp. `Audit list.md`) | 150 checkable items, A marketing (30), B dashboard (42), C other tabs (50), D Brian's review (28) |
| **What to build** | `Design/Figma/` | Plans 01–04, work log, review, iteration notes |
| **How to ship it** | `Design/HubSpot/` | Elevate kit spec, R3 mapping, live-demo fix list (H-01…24), hero module code, Company page build plan |
| **Status** | `Read me/` | Next actions (old), issues log (I-01…17), blockers, FAQ seeds |
| **Assets** | `Design/Assets/` | The welder hero photo; `In Use/` empty |

**Cross-reference keys:** `A-/B-/C-/D-xx` Audit list items · `H-xx` live-demo fixes · `I-xx` design issues · `D1…D5, B1…B3` Company-plan decisions/blockers · numbered "questions" in plans 03/04 · `1075:228`-style Figma node IDs.

### Which file wins when they disagree

1. `Audit/Audit list.md`, `Design/Figma/00_FIGMA-WORK-LOG.md`, plans `03` and `04`, `Design/HubSpot/*` (newest, 22–25 Sep)
2. `Design/Figma/01_STRUCTURE…` (19 Sep v2): move 2 (preview cards on homepage) was **reversed** by Jeff's note in plan 03
3. `Read me/01_NEXT-ACTIONS…` (19 Sep): **partly superseded**; its pricing, testimonial, hero-photo and typo claims are wrong
4. `Read me/02_ISSUES-LOG.md`: current, but stops at I-17

---

## 4. The marketing site story

- **Brian's brief (11 Sep):** recreate his HTML mockup in Figma, optimise font/layout/journey, flag changes. Notes: integrate the welder photo, pricing diagram is a placeholder, make static cards less dull.
- **The audits** (May, old Squarespace site) found: no type hierarchy, two different landing-page looks, 4+ CTA styles, orange overuse and poor contrast, mixed icons, unreadable mobile hero, thin footer, no social proof.
- **What Figma R3/R4 did:** rebuilt on HubSpot Elevate presets, bound to Built Bold. R4 is the module map for the build.
- **The live demo** (HubSpot test portal 1 Meter House, `…hs-sites-na2.com/demo`): matches R3 in the hero, but still carries Elevate sample content, a stray SNACKZO logo, 16 dead links, a 2.8 MB hero screenshot, and failing button contrast (`H-01…H-24`).
- **Sub-pages:** Job Seeker (hi-fi, 11 bands, header states, phone frames), Company (desktop built 25 Sep), About Us (built, needs Brian's read). Same skeleton for all (A-05). Header is a search bar (trade + ZIP), with Jeff's note moving the preview cards onto the sub-pages.
- **Elevate kit:** 6 layouts, 20 modules, 46 sections built as Figma components. **Biggest gap: the kit has no mobile sections**, so mobile ratings barely moved (4.4 → 4.9).
- **Iteration ratings (before → after):** Home 4 → 7.5, Job Seeker 6 → 8, Company 6.5 → 8, About Us 4 → 8.

### The one fix that matters most

Every orange or blue button on Brian's mockup and on the live demo **fails WCAG AA** (2.63 / 3.28 / 2.03:1; the design system's `#F16C0E` with white is 3.05:1). **Orange fill with a navy `#16243D` label is 5.09:1** (hover `#F4811F`). In HubSpot this is **one theme setting** that fixes every button on every page (`00_ELEVATE-KIT.md`). The hero module code already does this.

---

## 5. The product / dashboard story

Brian's 1 Jul review and the 2 Jul meeting decided:
- Profile score **and** experience score sticky at the top, red/yellow/green; warn workers who apply with a red score.
- Remove "AI job matches" and "What you'll unlock"; calendar not needed; shrink the checklist to ≤5 items.
- Fast "Almost there" onboarding: name, email, ZIP, over 18, trade categories (phone later).
- New trade-category widget: typeahead after 3 characters, pills, 151 trades, popular trades, mobile-safe. Build as one component.
- Product ideas to design for: applicant expiry, coworker endorsements and referral credits (virality), AI quizzes, ratings, Spanish version, free job invitations, paywall-bypass detection.

Audit sections B and C (employer dashboard, other tabs) are **all open** and were written against older screens. The Figma file has **newer logged-in screens (Flow A Hi-Fi, `867:833`, A5–A8)**: check each item against those before ticking.

---

## 6. Decisions: made vs open

**Made**
- Marketing site first, product second (15 Sep).
- Keep Built Bold: Instrument Sans + Inter; middle-ground direction.
- Two CTA variants only; orange fill + navy label.
- Light (not dark) final-CTA band; drop trade columns from the footer (Brian/David).
- Preview cards go on the sub-pages, not the homepage (Jeff, Brian).
- New work goes in a dated Figma section; never edit a previous round.

**Open, and who owns it**
| Question | Owner | Blocks |
|---|---|---|
| **Pricing model**: per-applicant ($25 invite, $99/$199/$399 unlock) vs flat monthly vs $49/$149/Custom (R3, unattributed). Three live in three places (I-12, I-21) | Brian | Pricing band, FAQ 1 and 6, hero chip; public `/companies` prices must come down when the new model ships |
| HubSpot portal, Squarespace → HubSpot move, domain | Harpreet, Brian, Jeff | Going live at all (B1, B2) |
| Which Figma file is the working one (`aC59…` vs same-named copy `eulu7…`) | Shubham, Harpreet | Work log says `aC59` in practice |
| Is skill verification live? Is messaging live? Same-day matches? Text alerts? | Brian, Jeff | Copy: "verified", "message directly", "matches the same day" |
| Nav labels and URLs (I-14) | Brian | Nav, URL, redirect from `/companies` |
| Testimonial permissions (Matthew B., Brothers Insulation) | Brian | Proof bands |
| What a private profile hides; open-to-work default | Brian, Jeff | Job Seeker band 05 |
| Phone number or human contact route on the Company page | Brian | Header, CTA |
| Trade list and keywords | GTM | Trade pages (`/hire/{trade}`, `/jobs/{trade}`) |

---

## 7. Contradictions and gaps found while connecting the files

1. **Meeting dates.** The 15 Sep notes say Meetings 1–5 are "all from early July". The transcripts are 27 Apr, 14 May, 22 Jun and 2 Jul. **Meeting 4 does not exist in the upload.**
2. **Question numbering collides.** The Job Seeker plan numbers its questions 1–16 and the Company plan 17–27. `Read me/03_BLOCKERS…` has 9 items with different numbering (its "1" is button colour; plan 03's "1" is nav label).
3. **Issues I-18 to I-22** are cited in the work log and plans but absent from `Read me/02_ISSUES-LOG.md` (stops at I-17).
4. **Pricing contradiction in copy:** Brian's hiring step 3 says contact goes straight to the worker with no cut, while the product charges $99–$399 to unlock contact. Suggested wording is in `04_CONTEXT_Company-Page.md`.
5. **Scope vs work:** the six-phase scope covers the product only, but the whole recent effort (marketing site, HubSpot build) sits outside it.
6. **Timeline:** the plan assumed launch Wed 30 Sep with one person doing three pages; the plan itself calls this the honest risk. No later status exists.
7. **Brian's mockup contradicts itself:** search says Journeyman Electrician; card says Welding; ZIPs are Dallas/Portland but cities say Indianapolis; two versions of the worker card (PDF 96% private vs HTML 92% public).
8. **Roles:** `Read me/00_README.md` calls Harpreet the manager; in Meeting 1 Harpreet pitches as the designer. Treat the README as correct.
9. **Dashboard audit versions:** `Final_v2` and `Final_v2_1` hold the same 39 issues; `Grouped_By_Severity` drops issue 1. The Audit list's 42 items = 39 + 4 from the responsive PDF − 1 duplicate (rows 7 and 12).
10. **Live-demo structural bug:** the whole homepage sits inside the theme's **global header partial**. Move it into the page's content area before publishing a second page, or the homepage will appear on top of every page.
11. **Claims the product can't back yet** (flagged across plans): "thousands of jobs", "verified" skills, "instant notifications" (email only), "3 open jobs", same-day matches.
12. **Two doc statuses to refresh:** the audit list "Today" column predates Iterations 1–2; `Read me/00_README.md` still says the Company page is "next".

---

## 8. What to do next (consolidated)

**Unblock**
1. Brian: pricing model, verification/messaging truth, nav labels, testimonial permission, canonical worker card.
2. Harpreet/Brian/Jeff: HubSpot portal and domain; settle the Figma file; confirm whether marketing/HubSpot work is in scope.

**Fix now (no decision needed)**
3. HubSpot theme: navy label on orange, lighter hover `#F4811F`; H2/H3 in Instrument Sans (`H-09`, `H-10`).
4. Live demo P0 list `H-01…H-08`: remove SNACKZO logo, add trust bar, replace Elevate sample content, fix typos ("Reccomended" etc.), remove the "E" logo.
5. Move the page out of the global header partial; replace the 2.8 MB hero screenshot with `Design/Assets/Testing assets/hero-welder-1400x799.jpg` (312 KB) via HubSpot Files; fix the hero module's `PASTE-THE-FILE-MANAGER-URL-HERE`.
6. Iteration 1 stop-ship items: Elevate placeholder quotes and FAQ on Home, internal `[Copy]` note rendered as copy, two stuck-open mobile menus.

**Design**
7. Build **Elevate mobile sections at 393** (the main blocker), the **input field component** (I-13), the **Job Seeker card** (Public/Private), and dark module variants.
8. Company page: phone frames, header states, empty-search state, cost-comparison band once pricing lands.
9. About Us: Brian reads the copy; check against Elevate `about-us` presets.
10. Dashboard: review Flow A against Audit list B–D, then update the audit list.

**Housekeeping**
11. Add I-18…I-22 to the issues log; reconcile question numbering; refresh the README status and audit list "Today" column; record whether launch happened.

---

## 9. Full file index

| Path | What it is |
|---|---|
| `Read me/00_README.md` | The project's own start-here: status, people, links, folder rules |
| `Read me/01_NEXT-ACTIONS_Marketing-Site.md` | 19 Sep plan (partly superseded) |
| `Read me/02_ISSUES-LOG.md` | Design issues I-01…I-17 |
| `Read me/03_BLOCKERS_for-Harpreet.md` | 9 open items for Harpreet |
| `Read me/04_FAQ-SEEDS_sub-pages.md` | 16 FAQ seeds: 7 on Home, 3+3 for sub-pages, 2 cut |
| `Audit/Audit list.md` | **Master checklist (150 items)** |
| `Audit/Desktop-Audit.md`, `Mobile-Audit.md` | Marketing-site audits as tables (19 + 16) |
| `Audit/Dashboard-Design-Audit.md` | Employer dashboard, Final v2 (39: 15 Critical, 16 Major, 8 Minor) |
| `Audit/Dashboard-audits-raw.md` | Rough text of the two dashboard PDFs (use the PDFs) |
| `Audit/Source files/` | 2 PDFs, 1 CSV, 7 XLSX originals |
| `Design/Figma/00_FIGMA-WORK-LOG.md` | File keys, node map, rounds R1–R4, built pages, DS, gotchas, next steps |
| `Design/Figma/01_STRUCTURE_Marketing-Homepage.md` | Homepage structure v2, four moves, contrast measurements |
| `Design/Figma/02_HIFI-PLAN.md` | Homepage hi-fi plan |
| `Design/Figma/03_CONTEXT_Job-Seeker-and-Company-Pages.md` | Job Seeker page final plan (questions 1–16) |
| `Design/Figma/04_CONTEXT_Company-Page.md` | Company page plan (questions 17–27) |
| `Design/Figma/05_REVIEW_Iteration-1.md` | Design review of four pages, STOP/A/B/C findings |
| `Design/Figma/06_ITERATION-2_Section-swaps.md` | 21 sections swapped for kit components, ratings |
| `Design/Figma/Source files/` | Brian's mockup HTML (bundled JS page), FigJam user flows (.jam/.pdf), old .fig export (20 Jun), dashboard wireframe plugin |
| `Design/HubSpot/00_BUILD-PLAN_Staging.md` | **Current plan:** build order, shared pieces, page order, mobile, staging QA, what is held for the publish pass |
| `Design/HubSpot/00_ELEVATE-KIT.md` | What Elevate ships; mapping to the Figma kit; button-default answer |
| `Design/HubSpot/Home/01_R3_HubSpot-Elevate-Mapping.md` | R3 bands → presets, with [Theme]/[Editor]/[CSS]/[Module]/[Copy] tags |
| `Design/HubSpot/Home/02_SITE_Changes-Needed-Home-Page.md` | Live-demo fix list H-01…H-24 |
| `Design/HubSpot/Home/03_COMPONENT-INVENTORY_Live-Demo.md` | 32 modules, 1 custom, global-header bug |
| `Design/HubSpot/Home/04_FINAL-DESIGN_Home-Page.md` | **Final homepage design** (Figma node `1259:9027`): bands, node IDs, module mapping, what changed from the plans |
| `Design/HubSpot/Home/code/` | `gfb-home-test.html` page template; `gbf-module/` GFB Hero module (`module.html`, `module.css`) |
| `Design/HubSpot/For companies/` | Build plan (steps 0–5, week plan) and teardown of the live `/companies` page |
| `Design/HubSpot/For workers/` | Empty (exists, nothing built) |
| `Design/Assets/Testing assets/hero-welder-1400x799.jpg` | The only real photo; `In Use/` is empty |
| `Project Context/` | Brian's brief, 15 Sep notes, Meetings 1/2/3/5, scope, UX review (docx + md) |

**Not provided:** Meeting 4; the Mobile Audit and UX Audit CSV originals (the UX Audit's 11 conversion items exist only inside the Audit list); `Design/HubSpot/For workers/` content; `Design/Assets/In Use/` content. Brian's mockup HTML, the `.jam` and the `.fig` could not be read as text (bundled or binary); their content is described through the docs that cite them.
