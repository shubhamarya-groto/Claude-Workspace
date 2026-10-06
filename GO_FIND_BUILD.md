# Go Find Build

Groto project: a trades hiring platform (employers find skilled workers; workers find jobs). This repo holds the project context and audits.

> Status: audits, Brian's review and the Figma plans are in. Brian's brief, scope, Read me/ and HubSpot material are still to come.

## What's in the repo

| Path | What it is |
|---|---|
| `Audit/Audit list.md` | **Master checklist.** Every audit merged into 4 sections: A marketing site (30), B employer dashboard (42), C other dashboard tabs (50), D Brian's review (28). Tick items when fixed. |
| `Audit/Desktop-Audit.md`, `Audit/Mobile-Audit.md` | Marketing-site audits, converted to tables (19 + 16 issues) |
| `Audit/Dashboard-Design-Audit.md` | Employer dashboard audit, Final v2 (39 issues: 15 Critical, 16 Major, 8 Minor) |
| `Audit/Dashboard-audits-raw.md` | Raw text from the two dashboard PDFs (column order scrambled; use the PDFs) |
| `Audit/Source files/` | All originals: 2 PDFs, 1 CSV, 9 XLSX versions |
| `Design/Figma/00_FIGMA-WORK-LOG.md` | Figma file keys, page/node map, rounds R1–R4, built pages (Job Seeker, Company, About Us), design system, next steps, gotchas |
| `Design/Figma/01_STRUCTURE_Marketing-Homepage.md` | Homepage structure v2 from Brian's mockup: four recommended moves, button contrast measurements |
| `Design/Figma/02_HIFI-PLAN.md` | Hi-fi plan for the homepage (components first, phases) |
| `Design/Figma/03_CONTEXT_Job-Seeker-and-Company-Pages.md` | Job Seeker page final plan (bands, copy, open questions 1–16) |
| `Design/Figma/04_CONTEXT_Company-Page.md` | Company page plan (product reality, copy needing a yes, questions 17–27) |
| `Design/Figma/05_REVIEW_Iteration-1.md` | Design review of Home, Job Seeker, Company, About Us (desktop + mobile): STOP / A / B / C findings |
| `Design/Figma/06_ITERATION-2_Section-swaps.md` | Iteration 2: 21 sections swapped for Elevate kit components, before/after ratings |
| `Project Context/UX-Review-7-1.md` | Brian's review of the dashboard designs (1 Jul), converted from the .docx |

## Source notes

- Dashboard audit versions: `Final_v2` and `Final_v2_1` hold the same 39 issues. `Grouped_By_Severity` is a regrouped copy that drops issue 1. `_1` / `_2` / `GoFindBuild_Design_Audit.xlsx` are earlier versions or the marketing-site audit.
- `UX_Review_-_7_1.docx` was uploaded twice (byte-identical), one copy kept.

## Still missing

- **Read me/**: README, next actions, issues log, blockers, FAQ seeds
- **Project Context/**: Brian's brief as received, scope, meeting notes
- **Mobile Audit.csv and UX Audit.csv** (marketing site conversion, 11 items). The Mobile data is covered by the xlsx; the UX Audit has no other copy.
- **Design/Figma/Source files/**: Brian's mockup HTML (`GoFindBuild-Marketing-Site-All-Pages.html`), FigJam user flows, wireframe plugin, the old .fig export
- **Read me/** files the Figma docs cite: `02_ISSUES-LOG.md` (I-01…I-22), `03_BLOCKERS_for-Harpreet.md` (questions 1–27), `01_NEXT-ACTIONS`, `04_FAQ-SEEDS_sub-pages.md`
- `Project Context/2026-09-11_Brian-Mockup-Brief.md` and `2026-09-15_Meeting-Notes.md`
- **Design/HubSpot/**: Home, For companies, For workers, including `02_SITE_Changes-Needed-Home-Page.md` (the `H-xx` references in the audit list)
- **Design/Assets/**
- Dashboard PDF screenshots are not text-extractable; keep the PDFs as the reference.

## Figma at a glance

- Working file: **GofindBuild Website Redesign**, key `aC59gtTG9nh2hwUraPnCXj` (a same-named copy, `eulu7Yq3gH7gaezVZbn0bi`, also exists; the work log says `aC59` is the working file in practice).
- Built so far: homepage R1–R4, Job Seeker, Company and About Us hi-fi (desktop), HubSpot Elevate kit (46 sections), Iteration 1 review and Iteration 2.
- Biggest gaps: Elevate kit has no mobile sections; no input-field component; Company/Job Seeker phone frames; pricing model undecided.

## To decide before starting

- Pricing model (blocks A-12)
- Scope of the profile score formula and unlocks (D-18, D-20)
- Whether the dashboard audits (B, C) still apply to the newer logged-in Figma screens
