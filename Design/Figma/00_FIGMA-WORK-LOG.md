# Figma work log · GoFindBuild

Figma only: what's in the file, what each round did, what's next. Add a dated line to the
progress log every time Figma work moves. Plans that feed Figma live beside this file:
`01_STRUCTURE_Marketing-Homepage.md` and `02_HIFI-PLAN.md`.

## The file

**GofindBuild Website Redesign** · key `aC59gtTG9nh2hwUraPnCXj`
https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign

| Page | Node | What's on it |
|---|---|---|
| Marketing website | `1027:3073` | Homepage rounds R1, R2, R3 |
| Presentation | `493:1016` | Client-facing rounds, Hi Fi flow, Flow A hi-fi |
| Design System | `790:11512` | "Built Bold" components and documentation |
| Icon | `786:158` | Lucide set |
| Changes Based on Review | `432:1243` | Early wireframe explorations |
| Wireframe | `115:599` | Mission Control dashboard wireframe (plugin in `Source files/`) |

`Source files/GofindBuild Website Redesign.fig` is a 20 Jun export, far older than the live file.
Always work in the live file.

**Second file, same name, found 22 Sep:** key `eulu7Yq3gH7gaezVZbn0bi`, same pages and node IDs as
`aC59` (R1–R3, Flow A, the design system), so one is a copy of the other. Every note above and this
log point to `aC59`; Shubham's 22 Sep links pointed to `eulu7`. **22 Sep: Shubham directed the Job
Seeker page build to `eulu7`** — that resolves question 16 from
`Read me/03_BLOCKERS_for-Harpreet.md` for this task, but not which file is the working one going
forward. Ask before writing to either file until that's settled.

## Homepage rounds

| Round | Section | Position | Date | What it is | Status |
|---|---|---|---|---|---|
| R1 | `1032:3` | x 0 | 19 Sep | Structure: 12 bands and a notes rail, from Brian's mockup | Superseded |
| R2 | `1061:134` | x 2560 | 21 Sep | R1 with the issues-log changes applied | Superseded, kept for comparison |
| **R3** | **`1075:228`** | **x 5120** | 21 Sep | **Hi-fi, each band rebuilt from its HubSpot Elevate preset, restyled to the design system and the Hi Fi flows. One note per band with the preset, modules and changes** | Current hi-fi |
| **R4** | **`1151:651`** | **x 7680** | 23 Sep | **Module map: R3 with every band marked with the HubSpot module that renders it, checked against the live demo. Blue = Elevate preset, orange = custom module, grey = HubSpot default. One note per band with its module stack** | **Current for the build handoff** |

R3 inside: page frame `1075:359`, notes rail `1075:681`, description `1075:229`.
R4 inside: page frame `1151:652`, notes rail `1157:745`, description `1155:745`.

**The live HubSpot page, rebuilt in Figma (23 Sep):** section `1160:745` "2026-09-23 · HubSpot live page · /demo · rebuilt in Figma" at **x 10240, y 0** (2176 × 7280). Page frame `1160:750` is 247469662.hs-sites-na2.com/demo exactly as it renders at 1440 wide: 15 sections, the live colours and type sizes, the real images (hero screenshot, red backgrounds, SNACKZO logo, Elevate stock photos) uploaded into the file. Rail `1160:751` names the module behind each section and what is wrong with it. Use it to redline the live page against R3.
What the live page is built from: `Design/HubSpot/Home/03_COMPONENT-INVENTORY_Live-Demo.md`.
How R3 maps to HubSpot: `Design/HubSpot/Home/01_R3_HubSpot-Elevate-Mapping.md`.

## Job Seeker marketing page (file `eulu7Yq3gH7gaezVZbn0bi`, built 22 Sep)

New page **Marketing page · Job Seeker** (`3021:319`), placed right after Marketing website, holding
one dated section: **`2026-09-22 · Job Seeker Page · Hi-Fi`** (`3021:320`). Built from
`Design/Figma/03_CONTEXT_Job-Seeker-and-Company-Pages.md`, that file's final plan. Section holds:

| Part | Node | What's there |
|---|---|---|
| Description | `3021:321` | Title, one-line summary, what changed from the plan |
| Page frame | `3021:322` | 11 bands, 00–10, auto-layout so it hugs its own height (5497 tall) |
| Notes rail | `3067:3` | One note per band, aligned to that band's y, same convention as R3 |
| Header — states | `3047:152` | The header's other 6 states, beside the page |
| Phone frames · 375 | `3058:282` | Header, jobs, how it works, FAQ, sticky CTA |

**Desktop bands**, in order: 00 Top Nav (DS Top Nav, Job Seekers marked active) · 01 Header (A2's
populated hero, `867:924`, not A1's own hero which is empty here; Brian's copy; button contrast
fixed) · 02 Jobs pay-first (Job Match Card `891:189` ×2) · 03 Problem → reality (built from
scratch, R3's own band is empty; live-site copy + the 723,000 stat, "023" typo fixed to "2023") ·
04 How it works (R3's worker column, `1075:453`, Brian's 3 steps) · 05 You choose who sees you,
P1 (new Job Seeker card, Private concept, waits on question 2) · 06 Proof (R3's worker testimonial
card, `1075:513`, Matthew B. verbatim) · 07 FAQ (R3's shell, `1075:586`, the plan's 7 questions) ·
08 Browse jobs by trade, P1 (promoted out of the footer source, `1075:656`) · 09 Final CTA (built
from scratch, light background) · 10 Footer (R3's footer, `1075:628`, trade columns removed).

**Client comments applied (Brian and David, via screenshots Shubham sent 22 Sep):** band 09 uses a
light background, not dark — Brian, on the homepage final CTA, "not a fan of the dark color...
prefer very subtle"; band 10 drops the Hire-by-trade / Jobs-by-trade columns — Brian, "we can
likely ditch these categories at the bottom of the page." Brian separately confirmed the preview
cards belong on the dedicated pages, not the homepage, which matches band 02 and Jeff's note
already in the plan.

**Header states**, beside the page frame: 1 default (= band 01) · 2 trade picker open (`867:988`
tiles, reset to neutral, footer line repurposed to A1's old "Free to join" text) · 3 typing,
filtered list (simplified, 3 example matches) · 4 trades selected (cloned fresh from `867:924`,
ZIP fixed to Indianapolis) · 5 ZIP not recognised (warning added under the field) · 6 button
inactive (`Active=False` variant) · 7 phone, see below.

**Phone, 375 wide:** header (state 7 — stacked fields, full-width button, popular trades as a
scrolling row), jobs (cards stack), how it works, FAQ, and a sticky CTA bar. Not built responsive:
03 problem, 06 proof, 08 browse-by-trade, 09 final CTA, 10 footer — same selective-mobile approach
R3 used on the homepage.

**New, not yet in the design system:** Job Seeker card (Private variant only; Public variant is
the Company page's job) and the phone sticky CTA bar.

**Open, from the plan, unchanged:** all 16 questions in `Read me/03_BLOCKERS_for-Harpreet.md`
still need Brian's or Jeff's answer, including which Figma file is the working one (question 16).

## Marketing pages in `aC59` (the row at y 9548)

Shubham moved the page work into `aC59` and laid the pages out in one row on **Marketing website**
(`1027:3073`). This is where the sub-pages now live, so `aC59` is the working file in practice.

| Frame | Node | X | Size |
|---|---|---|---|
| Home Page | `1186:3338` | 12664 | 1440 x 5947 |
| Job Seeker · Hi-Fi | `1186:4790` | 14485 | 1440 x 4911 |
| **Company · Hi-Fi** | **`1193:5591`** | **16365** | **1440 x 4911** |
| Company · changes made (notes card) | `1202:1180` | 17885 | 600 x 1314 |
| **About Us · Hi-Fi** | **`1205:1587`** | **18565** | 1440 x 4496 |
| About Us · changes made (notes card) | `1210:1551` | 20085 | 600 x 1058 |

Bands inside Company · Hi-Fi, in page order: 00 Top Nav `1193:5592` · 01 Header `1193:5595` ·
02 Workers near you `1193:5630` · 05 Look first, reach out `1193:5637` · 08 Proof `1193:5645` ·
03 Problem and how it works `1193:5661` · 10 FAQ `1193:5703` · 09 Final CTA `1193:5720` ·
11 Footer `1193:5758`.

About Us · Hi-Fi is the same skeleton again: 00 `1205:1588` · 01 `1205:1591` · 02 Two sides, one network `1205:1626` · 05 **hidden** `1205:1633` · 08 Proof, Matthew B. `1205:1641` · 03 Why we built it `1205:1657` · 10 FAQ `1205:1699` · 09 Final CTA `1205:1716` · 11 Footer `1205:1754`. The frame hugs its content, so the hidden band leaves no gap.

## Other work in the file

- **Hi Fi flow** `823:4275` (Presentation): "B · Image Based Layout" `823:4122` (homepage hero
  variant), welcome with trade and zip capture, trade picker (open, typing, selected), auth email,
  verify code. Two colour variants of each.
- **Flow A Hi-Fi** `867:833` (Presentation, 27 Aug): eight screens. A1 to A4 onboarding, A5 to A8
  the logged-in app. Check these against Audit list sections B to D.
- **Moodboard** `83:597`: Bright, Middle ground, Minimal. Middle ground chosen on 22 Jun.

## Design system (page `790:11512`)

**Components:** Top Nav `790:11423` · Button `787:10782` (Type Default / Primary / Text; label
property `Button Label#787:0`) · Chip `790:11387` (Primary / Neutral / Glass × Subtle) · Job Match
Card `891:189` · Profile Checklist Item `890:179`.

**Variable collections:** Color Tokens `772:2` · Structural tokens `773:8` (spacing, border-radius,
stroke-width) · Typography Tokens `775:2` · Color Mode `783:158` (semantic).

**Text styles (22):** Display 3xl to 7xl in Instrument Sans; Heading, Body and UI in Inter.

**Not in the system yet:** input / form field, hero, stat block, step card, testimonial card,
FAQ row, pricing card, footer.

**Known defect:** `primary/default` `#f16c0e` with a white label is 3.05:1 and fails AA at 16px
(I-01). If the label goes navy (5.09:1), `primary/hover` must go lighter, `#F4811F`, or it drops
to 4.36:1 (I-18).

## Reusable images already in the file

| Image | Hash | Use it like this |
|---|---|---|
| Brian's welder photo | `0f3204cbdc4e881f693ec5150d5dcf4ae1064acb` | Hero, in the folder-tab shape |
| Dark streak (welcome hero) | `24e04aac4e9edcc141c8c691be94060f7b6265fa` | Portrait: paint rotation 90 and a ~55% black overlay |
| Orange waves (auth screen) | `c8f2df68b92bbaf13d7adf9cebc3d296852d3325` | Portrait: paint rotation 270 |
| Warm glow (verify screen) | `06a603ab8b692635add8ce54f82851479e4d7fac` | Avoid in wide bands: crops to bright orange, captions fail contrast |
| B's site photo | `b22cf2b6a04450b2cba34a4369dbca009d7b385e` | Construction workers |

## Conventions

- New work goes in a new top-level Section named `YYYY-MM-DD · …`. Never edit a previous round.
- Annotation text stays light (white, 78% grey) on the dark grey section background.
- One note per band in the notes rail, aligned to its band.
- "Created by Claude" on sections Claude builds.
- When adding work, report the file, page and X / Y position.
- Everything binds to variables and text styles. No hex values, no manual font sizes.

## Progress log

- **22 Jun** · Moodboard review. Middle ground recommended.
- **27 Aug** · Profile Checklist Item and Job Match Card components; Flow A hi-fi, eight screens.
- **19 Sep** · R1 homepage structure.
- **21 Sep** · R2: issues-log changes applied.
- **21 Sep** · R3 hi-fi on HubSpot Elevate presets. Welder photo uploaded; B's stat pill, folder-tab
  photo, frosted card and check badges cloned in; band 03 on the dark streak; band 10 on the
  orange waves with a frosted card; how-it-works steps aligned (I-17 fixed); band 06 heading
  proposed. Frosted card moved from Satoshi and SF Pro to Inter; "Verifed", "Autin, TX" and
  "6yrs" fixed.
- **22 Sep** · Live HubSpot demo checked against R3. Results in `Design/HubSpot/Home/02_SITE_Changes-Needed-Home-Page.md`.
- **23 Sep** · Live demo read module by module: 32 modules, 26 Elevate presets, 5 HubSpot default, 1 custom (GFB Hero). Found that every section sits inside the theme's **global header partial** while the page's own content area is empty. R4 module map built from R3 on the Marketing website page: every band marked with the module that renders it, layers renamed to match, one note per band. The live page was then rebuilt in Figma as its own section (`1160:745`, x 10240), section by section, with its real images.
- **22 Sep** · Job Seeker marketing page built hi-fi, in file `eulu7Yq3gH7gaezVZbn0bi`: 11 desktop
  bands, 7 header states, phone frames (header, jobs, steps, FAQ, sticky CTA), a notes rail, and
  Brian's and David's comments on the homepage folded in where they applied. Details above.

- **25 Sep** · **Company page built**, desktop, in `aC59` at `1193:5591`. Shubham had duplicated
  Job Seeker · Hi-Fi into the Company slot; every band was converted in place, section order and
  layout untouched. Nav active state moved to Companies (its loose hex now bound to
  `blue/navy-780-brand`); header carries Brian's company copy and "See who's available"; bands 02
  and 05 refilled as worker profiles; Elevate's sample testimonial replaced with the Brothers
  Insulation quote, its stock images greyed and the slider chrome hidden; band 03 carries the live
  /companies pains, Brian's three hiring steps and the 88% employer stat; FAQ swapped to five
  company questions; final CTA is "Post your first jobs free." Changes card at `1202:1180`.
  Not added: the cost comparison band, which waits on pricing (I-12).

- **25 Sep** · **About Us page built**, desktop, `1205:1587`, cloned from the Company page so the
  three pages share one skeleton. No active nav item (About is a footer link). The trade and ZIP
  search is replaced by a two-button fork, Post a job and Find work, since a search bar has no job
  on this page. Band 02 now shows one worker card beside one job card, captioned by whose view each
  is, which also answers I-07. Band 05 hidden. Band 08 carries the worker quote, Matthew B., since
  the Company page carries the employer one. Band 03 is Brian's problem line verbatim, three
  principles in place of three steps, and 723,000 with its real citation. Changes card at
  `1210:1551`. Only two lines on the page are Brian's approved words; the rest needs his read.

- **25 Sep** · **HubSpot Elevate kit built** on its own page, `1215:3`. Read from the theme's own
  source rather than the editor UI: 6 layouts, 20 modules, 47 section presets catalogued. All 26
  layouts and modules built at Elevate's 1200 container width, bound to Built Bold variables and
  text styles, then turned into components named `Elevate / Layout / …` and `Elevate / Module / …`.
  SiteHeader and Button reuse the DS components instead of duplicating them. Spec:
  `Design/HubSpot/00_ELEVATE-KIT.md`. Sections and dark variants not built.

- **25 Sep** · **All 46 Elevate section presets built** on a second page, **HubSpot Elevate
  sections** (`1226:3`), each as a component `Elevate / Section / <category> / <preset>`. Built from
  the theme source, so every one carries the column split, light or dark treatment and module list
  the preset actually declares. Six columns by category: Hero 6, CTA 4 + FAQ 4, Pricing 3 + Social
  proof 6, Products 10, Team 5 + Events 1, Forms 3 + Media 4. Count corrected: the theme ships
  **46** sections, not 47. The 47th entry was the `schemas` folder.

- **25 Sep** · **Iteration 1 reviewed** (section `1233:5037`: Home, Job Seeker, Company, About Us,
  desktop and mobile). Every band captured and judged. Findings in `05_REVIEW_Iteration-1.md`:
  5 stop-ship items (Elevate placeholder quotes and FAQ still on Home, "Reccomended" misspelled,
  an internal [Copy] note rendered as page copy, two mobile menus stuck open in two different
  designs), 5 off-brand calls (purple Elevate illustrations, gear watermarks, peach gradients,
  green money, full-orange mobile heroes that swallow their own CTA), 5 dated patterns, 12 craft
  defects and a rebuild list for About Us, which is currently two product bands wearing an About
  headline.

- **25 Sep** · **Iteration 2 built** (`1238:2407`, x 44090), the same eight screens with **21 sections
  replaced by Elevate kit components**, 2 removed as duplicates and 1 added. Rule for the round: no
  edits inside a band, only whole-section swaps, which is how it will be assembled in HubSpot.
  Ratings before and after: Home 4 to 7.5, Job Seeker 6 to 8, Company 6.5 to 8, About Us 4 to 8.
  Mobile barely moved (4.4 to 4.9 average) because **the kit has no mobile sections**, which is now
  the biggest gap in the system. Home's page frame was a grid layout, which is how its band order
  drifted; converted to vertical. Detail in `06_ITERATION-2_Section-swaps.md`.

## Next in Figma

- [ ] Job Seeker page: settle which Figma file is the working one (question 16), then either
  redo the build in `aC59` or make `eulu7` the record everyone points to.
- [ ] Job Seeker page: state 3 (typing) is a simplified 3-item example, not pulled from a real
  151-trade list; band 08's trade grid could read more like a browsable grid than footer links.
- [ ] Job Seeker page: annotate for HubSpot the way R3 is (Elevate preset per band), once the
  file question above is settled.
- [ ] Settle the button treatment in the design system itself: label colour and hover (I-01, I-18). Fork buttons follow (I-02).
- [ ] Band 06: build the Job Seeker preview card as a component; give both cards the same number of actions (I-07).
- [ ] Band 08: match the heading to the tiers once pricing is decided (I-12, I-21).
- [ ] Mobile frames for R3: hero and fork, preview cards, how it works, testimonials (see `02_HIFI-PLAN.md`).
- [ ] Missing design system components, the input field first (the sub-page search widgets need it).
- [x] Company page: desktop built 25 Sep (`1193:5591`). Plan: `04_CONTEXT_Company-Page.md`.
- [ ] Company page: phone frames at 375, the header's states, and the cost comparison band once
  pricing lands (I-12).
- [ ] Job Seeker card as a real component, Public and Private variants. Both sub-pages borrow the
  Job Match Card today, so worker profiles carry a company icon.
- [ ] About Us: Brian to read the copy, decide whether About joins the top nav (I-14), and supply
  a photo of himself for the "built by someone who has done the work" block.
- [ ] **Elevate kit: mobile sections at 393.** Iteration 2 proved this is the blocker: the two
  mobile heroes are still full-bleed orange with an orange-on-orange primary button.
- [ ] Elevate kit: add dark (`section_variant_4`) variants of the modules. The section presets show
  the dark treatment already.
- [ ] Check the About Us page against the `about-us` and `about-us-one-column` presets before it is
  built in HubSpot.
- [ ] Build the input component (I-13). The three form presets are the argument for it.
- [ ] Hi Fi B still has Satoshi, SF Pro and the typos (I-19, I-20).
- [ ] Dashboard: review Flow A against Audit list sections B to D.

## Gotchas that have already cost time

1. **Section backgrounds are dark grey (~#616161), so annotation text must be light.** Title
   `#FFFFFF`, body 78% grey, accent bar blue `rgb(0.18, 0.35, 0.78)`. Dark text disappears.
2. **Some Lucide icons are empty shells that render blank:** circle, filter, zap, wrench,
   bookmark, dot, message-square, message-circle. Check the component has a child first.
3. **The Primary Button's arrow disc defaults to white.** Override it to `primary/hover`
   `783:164` or the arrow disappears.
4. **Exposing a nested instance wipes its variant override.** Re-apply the variant after exposing.
5. Section children use **local** coordinates, relative to the section.
6. Screens are white 1440-wide frames. Annotation frames sit *above* each screen, never inside.

## Source files

- `GofindBuild Website Redesign.fig`: 20 Jun export, outdated.
- `Go Find Build-User Flows.jam` and `.pdf`: the FigJam user flows.
- `GoFindBuild-Marketing-Site-All-Pages.html`: Brian's 11 Sep mockup, three pages, his approved
  copy. The brief that came with it is in `Project Context/2026-09-11_Brian-Mockup-Brief.md`.
- `gofindbuild-wireframe-plugin.js`: a Figma plugin script (paste into `code.js`, run from
  Plugins > Development) that draws the Mission Control dashboard wireframe on the Wireframe page.
  It predates the design system and uses its own hex colours: a layout skeleton, not a colour source.

## 9 Oct 2026 · Pricing component redesigned (client screenshot)

- **Component** `Elevate / Section / Pricing / pricing` (`1231:129`, page *HubSpot Elevate sections*) rebuilt to the
  client's screenshot: heading "Start free. Pay only when you connect.", intro, orange line, and three cards
  (Introductory Offer · Free; Starter · $0/month with a $49 / $149 / $349 rate table; Pro · $249/month, dark, Best value
  badge). Equal-height cards (Starter hugs, the others fill), note box + button pinned to the bottom. New layers are
  bound to the file's tokens (Typography, Color Tokens, Color Mode, spacing, radius). Height 657 → 1073.
- **Instances:** the Marketing Website Home Page copy (`1259:9084`) was fixed at 657 high; set to hug. It keeps its
  `#F8F9FA` band fill. The Iteration 2 (`1241:3327`) and Presentation (`1259:5386`) copies grew automatically.
- **Nearby frames:** each Home Page is a vertical auto-layout stack, so the bands below Pricing moved down on their own.
  The three *Mobile Home Page* frames under them (`1259:9277`, `1260:3259`, `1259:5579`) were moved down 416 px to keep
  their original gaps. No section needed resizing.
- Code counterpart: `Design/HubSpot/Home/code/gfb-pricing/` (same content, 9 Oct).
