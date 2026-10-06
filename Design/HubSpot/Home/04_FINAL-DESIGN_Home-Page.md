# Home page · final design (build reference)

Confirmed as the final homepage design on 6 Oct 2026.

- **Figma:** https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign?node-id=1259-9027
- **File:** GofindBuild Website Redesign, key `aC59gtTG9nh2hwUraPnCXj`, frame **Home Page** `1259:9027`, 1440 × 5127, at x 553, y 512
- **Read from:** Figma node structure only (names, sizes, positions). Colors, fonts and spacing values were not read: the Figma tool limit was hit. Take those from the design system and the existing HubSpot theme notes.
- **Component vs Figma-designed split:** `05_SECTION-SPLIT_Component-vs-Figma.md` (read 6 Oct; corrects the "What you get" row and build note 2 below, and covers bands 03 and 10).
- **Rule for this build:** staging only; copy is placeholder until final publishing (`../00_BUILD-PLAN_Staging.md`).

## Bands

Layer names in Figma carry the module for each band, in the same `M1 · Custom / Elevate` style as R4.

| # | Band | Node | Size | Built from in HubSpot |
|---|---|---|---|---|
| 00 | Top Nav | `1259:9028` | 1440 × 96 | Elevate Site header (DS Top Nav) |
| 01 | Hero + fork | `1259:9031` | 1440 × 717 | **Custom module GFB Hero** (code in `code/gbf-module/`) |
| 02 | Trust bar | `1259:9048` | 1440 × 92 | Elevate **Card ×3** |
| – | What you get | `1363:8560` | 1440 × 770 | Elevate section `products-and-services-two-column` |
| 08 | Testimonials | `1259:9068` | 1440 × 826 | Elevate Testimonial slider (**still sample content**) |
| – | Pricing | `1259:9084` | 1440 × 657 | Elevate section `pricing` |
| 03 | Problem + stats | `1355:8192` | 1440 × 663 | Elevate Metrics (per R3 mapping); frame content not read |
| – | FAQ | `1259:9108` | 1440 × 507 | Elevate section `faq-v2` |
| 10 | Final CTA | `1259:9109` | 1440 × 536 | Elevate CTA (per R3 mapping); frame content not read |
| 11 | Footer + browse by trade | `1259:9149` | 1440 × 263 | Elevate footer |

Order on the page: 00 → 01 → 02 → What you get → 08 → Pricing → 03 → FAQ → 10 → 11.

## Band details

### 01 · Hero + fork
- **Copy column** (`1259:9032`, 672 wide, at x 96): H1 (672 × 234, multi-line), subhead (672 × 58), then the **audience fork** (672 × 168) with two cards of 328 × 168 and a 16px gap.
  - Card 1 "I'm hiring": title, one line, button **Hire workers** (177 × 48).
  - Card 2 "I'm looking for work": title, one line, button **Find jobs** (150 × 48).
  - Card padding 25px.
- **Visual** (`1259:9044`, 504 × 557, at x 816): the welder photo as a **boolean-operation shape** (559 × 557), not a plain rectangle. The shape runs off the right side. The current module CSS uses a left-rounded rectangle, so check it against the Figma shape and adjust.
- Use `Design/Assets/Testing assets/hero-welder-1400x799.jpg` (312 KB), uploaded to HubSpot Files. Replace the `PASTE-THE-FILE-MANAGER-URL-HERE` placeholder in the module.
- Button style: orange fill, navy label (per the theme settings pass).

### 02 · Trust bar
Three items at x 96 / 372 / 611, each a 28px check badge + one text line: Direct employer connections · No recruiter middlemen · 150+ trade categories. One row, 28px tall.

### What you get (two columns)
Container 1200 at x 120, 96px top padding. Heading "What you get". Two cards of 568 wide with a 64px gap:
- **For Companies:** header with rule, image, three features (icon in a 28px badge, title, one-line description): Post a job in 90 seconds · Review matched workers, not resumes · Message them directly.
- **For Job Seekers:** header with rule, three features: Pick your trades and your location · See job details before you apply · Let employers come to you.
- Icons: Lucide (briefcase, contact, message-circle, clock, file-check, badge-dollar-sign).

### 08 · Testimonials, Pricing, FAQ
All three are Elevate instances or sample sections. The testimonial band still shows stock photo, "Add a testimonial quote #1", "Customer name one" and a slider. Pricing is the Elevate `pricing` preset. FAQ is `faq-v2`.

### 11 · Footer
Logo (Source Serif 4 SemiBold) + copyright on the left. On the right: legal links (three text layers) and two social buttons, **Instagram** and **LinkedIn**, 40 × 40 each. The Facebook link from the old site is gone.

## What changed from the earlier plans

| Earlier plan | In the final design |
|---|---|
| Preview cards band on the homepage (R3 band 06) | **Removed** (moved to the sub-pages, per Jeff's note) |
| Two how-it-works flows (R3 bands 04–05) | Replaced by the two-column **What you get** band |
| Problem + stats near the top (structure v2, move 1) | **Moved lower**, after pricing. Confirm this is deliberate |
| Pricing band cut-first, soft (I-12) | Still present as the Elevate preset |
| Footer with trade columns | No trade columns (Brian's comment) |
| Facebook, LinkedIn, Instagram in footer | Instagram and LinkedIn only |

## Build notes for HubSpot

1. Use whole presets and kit sections, no one-off edits inside a band (Iteration 2 rule).
2. Hero is the only custom code. Everything else is an Elevate preset with content typed in.
3. Put the page in its own content area, not the global header partial (`03_COMPONENT-INVENTORY_Live-Demo.md`).
4. Button style, fonts and colors come from the theme settings pass (`01_R3_HubSpot-Elevate-Mapping.md`, `H-09`, `H-10`).
5. Mobile is CSS on the child theme. The kit has no mobile sections, and this Figma node has no phone frames.
6. Footer legal links can point to the Terms and Privacy pages already published in the GoFindBuild portal (`/gofindbuild-terms-and-conditions`, `/gofindbuild-privacy-policy`).

## Held for the publish pass (copy, not structure)

- Testimonial band: replace Elevate sample quote, name, role and photos.
- Footer: two text layers are both labelled "Privacy"; confirm the three legal links.
- Pricing numbers and model (I-12).
- Problem + stats and Final CTA copy (frames not read here).
- Nav labels (I-14), claims such as "verified", and the 90-second promise.

## Not read, check in Figma before building

- Colors, type styles and spacing values.
- Contents of bands 03 (Problem + stats) and 10 (Final CTA).
- Phone frames, if any exist for this homepage.
- Whether the sticky CTA bar and header states apply (those are on the Job Seeker and Company pages).
