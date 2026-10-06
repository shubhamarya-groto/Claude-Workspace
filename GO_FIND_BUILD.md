# Go Find Build

Groto project: a trades hiring platform (employers find skilled workers; workers find jobs). This repo holds the project context and audits.

> Status: audits and Brian's review are in. Project brief, scope, Figma and HubSpot material have not been uploaded yet.

## What's in the repo

| Path | What it is |
|---|---|
| `Audit/Audit list.md` | **Master checklist.** Every audit merged into 4 sections: A marketing site (30), B employer dashboard (42), C other dashboard tabs (50), D Brian's review (28). Tick items when fixed. |
| `Audit/Desktop-Audit.md`, `Audit/Mobile-Audit.md` | Marketing-site audits, converted to tables (19 + 16 issues) |
| `Audit/Dashboard-Design-Audit.md` | Employer dashboard audit, Final v2 (39 issues: 15 Critical, 16 Major, 8 Minor) |
| `Audit/Dashboard-audits-raw.md` | Raw text from the two dashboard PDFs (column order scrambled; use the PDFs) |
| `Audit/Source files/` | All originals: 2 PDFs, 1 CSV, 9 XLSX versions |
| `Project Context/UX-Review-7-1.md` | Brian's review of the dashboard designs (1 Jul), converted from the .docx |

## Source notes

- Dashboard audit versions: `Final_v2` and `Final_v2_1` hold the same 39 issues. `Grouped_By_Severity` is a regrouped copy that drops issue 1. `_1` / `_2` / `GoFindBuild_Design_Audit.xlsx` are earlier versions or the marketing-site audit.
- `UX_Review_-_7_1.docx` was uploaded twice (byte-identical), one copy kept.

## Still missing

- **Read me/**: README, next actions, issues log, blockers, FAQ seeds
- **Project Context/**: Brian's brief as received, scope, meeting notes
- **Mobile Audit.csv and UX Audit.csv** (marketing site conversion, 11 items). The Mobile data is covered by the xlsx; the UX Audit has no other copy.
- **Design/Figma/**: work log, plans, file links (the audit list mentions R3 hi-fi and Flow A screens A5–A8, node `867:833`)
- **Design/HubSpot/**: Home, For companies, For workers, including `02_SITE_Changes-Needed-Home-Page.md` (the `H-xx` references in the audit list)
- **Design/Assets/**
- Dashboard PDF screenshots are not text-extractable; keep the PDFs as the reference.

## To decide before starting

- Pricing model (blocks A-12)
- Scope of the profile score formula and unlocks (D-18, D-20)
- Whether the dashboard audits (B, C) still apply to the newer logged-in Figma screens
