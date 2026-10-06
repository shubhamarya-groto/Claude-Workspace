# HubSpot build plan

Written 6 Oct 2026, from the existing docs. Status as given: **designs for the GoFindBuild pages are done; the HubSpot build starts now.** No new meetings or context.

## Ground rules

1. **Build in the GoFindBuild HubSpot account** (`47303551`, "GoFindBuild"). This is the working account. Pages stay unpublished drafts until final publishing. The earlier sandbox (`247469662`) is not used for the build.
2. **Copy is placeholder until final publishing.** Use the copy in the Figma pages and the plans as it stands. Do not stop to change wording, verify claims ("verified", "same-day", "messaging") or resolve `[Copy]` notes. Log wording questions in one list and settle them at the publish pass.
3. **Structure, tokens, accessibility and links are not copy.** Those still get done now: button contrast, fonts, heading levels, alt text, page titles, dead links, image weight.
4. **Whole-section assembly only**, as in Iteration 2: Elevate presets and kit components, no one-off edits inside a band.
5. Everything else in the repo stays as the source of truth: `Design/Figma/00_FIGMA-WORK-LOG.md` (nodes), `Design/HubSpot/Home/01_R3_HubSpot-Elevate-Mapping.md` (tags and theme defaults), `Design/HubSpot/00_ELEVATE-KIT.md` (what Elevate ships).

## Build order

### Step 0 · Fix the foundation (before any page)

| # | Task | Source |
|---|---|---|
| 0.1 | **Move the homepage out of the theme's global header partial** into the page's own content area. Until then a second page would render the whole homepage above it | `Home/03_COMPONENT-INVENTORY_Live-Demo.md` |
| 0.2 | **Theme settings pass, once:** primary button `#F16C0E` with navy `#16243D` label, hover `#F4811F`; H1/H2/H3 to Instrument Sans (H2 = 48px); base colours, card variants, tag colours per the defaults table | `Home/01_R3…` "Elevate defaults that change", `H-09`, `H-10` |
| 0.3 | Page-level basics: language en-US, real title and meta description, favicon, logo as a proper file with alt text | `H-13`, `H-17`, `A-29` |
| 0.4 | Files: upload `Design/Assets/Testing assets/hero-welder-1400x799.jpg` to HubSpot Files; replace the 2.8 MB Cloudinary screenshot | `H-12` |
| 0.5 | Put `Design/HubSpot/Home/code/gfb-hero/` into the portal as the **GFB Hero** module (steps in its `README.md`); pick the photo in the module's image field; load fonts once, from the theme, not per module | `Home/code/` |

### Step 1 · Shared pieces (build once, every page reuses)

| # | Piece | Type | Notes |
|---|---|---|---|
| 1.1 | Site header, active state per page | Elevate Site header | Menu: Companies · Job Seekers · Pricing (label still open, I-14; placeholder is fine) |
| 1.2 | Footer, legal links, no trade columns | Elevate footer | Fixes the empty Privacy/Legal links (`H-15`) |
| 1.3 | **Search bar** (trade typeahead after 3 characters, ZIP, button) | **Custom module** | Same bar on Job Seeker and Company headers. If dev time is short: two buttons instead (no fake search fields) |
| 1.4 | **Job Match Card** and **Job Seeker card** (Public/Private) | **Custom modules**, static fields | Static examples now; live data later |
| 1.5 | Sticky CTA bar for phones | CSS + small module | "See my matches" / "Post a job" |
| 1.6 | Comparison block (agency vs GoFindBuild) | Elevate Pricing, two columns | Price line is a slot; build without numbers |

### Step 2 · Pages, in this order

| Order | Page | Figma frame | Why this order |
|---|---|---|---|
| 1 | **Home** | R3 `1075:228` / R4 module map `1151:651` / `Home Page` `1186:3338` | Already half-built on the demo; fix and finish |
| 2 | **Job Seeker** (HubSpot folder `For workers/`) | `Job Seeker · Hi-Fi` `1186:4790` | The paid-ads landing page; most traffic |
| 3 | **Company** (`For companies/`) | `Company · Hi-Fi` `1193:5591` | Reuses the Job Seeker skeleton |
| 4 | **About Us** | `About Us · Hi-Fi` `1205:1587` | Smallest; check against the Elevate `about-us` presets |

Per-page band to preset mapping: Home `Home/01_R3…`; Company `For companies/00_PLAN…` step 4 table; Job Seeker follows the same bands (00 nav, 01 header, 02 jobs, 03 problem, 04 steps, 05 private card, 06 proof, 07 FAQ, 08 browse by trade, 09 final CTA, 10 footer).

### Step 3 · Mobile

The Elevate kit has **no mobile sections** (Iteration 2 finding). Build mobile in CSS on the child theme, to the 375/393 frames: hero stacks, headings at most two lines, buttons full width at 48px, drawer menu with close button, sticky CTA. Check the two stuck-open mobile menus from Iteration 1 are gone.

## Cut order if time tightens

Pricing/comparison band → browse by trade → problem band → phone frames below the fold. Never cut the jobs/workers band; it is the only thing that shows the product.

## Pre-publish QA checklist

- [ ] One H1 per page, it is the headline; stat blocks are not H2s (`H-24`)
- [ ] Every button and every header line at 4.5:1 or better
- [ ] No dead links (`#`, empty, trailing spaces, `utm_source=null`); fork buttons go to the right pages (`H-15`)
- [ ] Alt text on every image; hero under about 300 KB; no upscaled photos
- [ ] No Elevate sample content left (SNACKZO logo, "Customer name one", agency FAQ, "E" logo, purple illustrations)
- [ ] Layout checked at 1440, 1280, 768, 393/375; no sideways scroll
- [ ] No sticky or global-partial leakage between pages
- [ ] Page weight and request count no worse than the Squarespace page it replaces
- [ ] Old `/companies` and `/job-seekers` URLs redirect at launch, they do not 404

## Held for the final publishing pass

Copy and claims, pricing numbers and model (I-12), testimonial permissions, nav labels (I-14), the trade list, a phone/booking route on the Company page, domain and redirects (Squarespace to HubSpot), and whether the project's scope covers this build.

## Not available from this session

There is no HubSpot connector in this session, so nothing here can be created in the portal by Claude. What can be done in the repo: module and template code (`module.html`, `module.css`, `fields.json`, page templates), CSS for the child theme, and checklists. Upload to the portal through the Design Manager or the HubSpot CLI.
