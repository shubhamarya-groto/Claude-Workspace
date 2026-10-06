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
| `Design/Figma/Source files/` | `GoFindBuild-Marketing-Site-All-Pages.html` (Brian's 11 Sep mockup, 3 pages, his approved copy) · `Go Find Build-User Flows.pdf` / `.jam` (FigJam user flow incl. first-time experience, job seeker, company, project owner and trade partner paths) · `GofindBuild Website Redesign.fig` (20 Jun export, outdated; work in the live Figma file) · `gofindbuild-wireframe-plugin.js` (draws the Mission Control dashboard wireframe; predates the design system) |
| `Design/HubSpot/00_ELEVATE-KIT.md` | What the HubSpot Elevate theme ships (6 layouts, 20 modules, 46 sections), how it maps to the Figma kit, and why one theme setting fixes the button contrast everywhere |
| `Design/HubSpot/For companies/00_PLAN_Redesign-and-Build.md` | Company page build plan: steps 0–5, blockers B1–B3, decisions D1–D5, HubSpot band→Elevate preset map, QA checklist, week plan to Wed 30 Sep |
| `Design/HubSpot/For companies/01_CURRENT-PAGE_Teardown.md` | Teardown of the live Squarespace /companies page: what to keep, 15 measured defects, copy that survives |
| `Design/HubSpot/Home/01_R3_HubSpot-Elevate-Mapping.md` | How homepage R3 maps band by band to Elevate presets, with [Theme]/[Editor]/[CSS]/[Module]/[Copy] tags and the theme defaults that change |
| `Design/HubSpot/Home/02_SITE_Changes-Needed-Home-Page.md` | Live demo fix list H-01 to H-24 (the `H-xx` references in the audit list) |
| `Design/HubSpot/Home/03_COMPONENT-INVENTORY_Live-Demo.md` | What the live demo is built from (32 modules, 1 custom) and the global-header problem |
| `Design/HubSpot/Home/code/gfb-home-test.html` | HubSpot page template for the homepage test: nav, hero, trust bar, empty drag-and-drop area, design tokens as CSS variables |
| `Design/HubSpot/Home/code/gbf-module/` | The custom GFB Hero module (`module.html`, `module.css`). The hero photo URL is a placeholder (`PASTE-THE-FILE-MANAGER-URL-HERE`) |
| `Project Context/UX-Review-7-1.md` | Brian's review of the dashboard designs (1 Jul), converted from the .docx |

## Source notes

- Dashboard audit versions: `Final_v2` and `Final_v2_1` hold the same 39 issues. `Grouped_By_Severity` is a regrouped copy that drops issue 1. `_1` / `_2` / `GoFindBuild_Design_Audit.xlsx` are earlier versions or the marketing-site audit.
- `UX_Review_-_7_1.docx` was uploaded twice (byte-identical), one copy kept.

## Still missing

- **Read me/**: README, next actions, issues log, blockers, FAQ seeds
- **Project Context/**: Brian's brief as received, scope, meeting notes
- **Mobile Audit.csv and UX Audit.csv** (marketing site conversion, 11 items). The Mobile data is covered by the xlsx; the UX Audit has no other copy.
- **Read me/** files the Figma docs cite: `02_ISSUES-LOG.md` (I-01…I-22), `03_BLOCKERS_for-Harpreet.md` (questions 1–27), `01_NEXT-ACTIONS`, `04_FAQ-SEEDS_sub-pages.md`
- `Project Context/2026-09-11_Brian-Mockup-Brief.md` and `2026-09-15_Meeting-Notes.md`
- **Design/HubSpot/For workers/** (Home and For companies are in)
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
