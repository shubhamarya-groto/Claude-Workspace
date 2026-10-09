# Company page · final design (build reference)

Final design for the For companies page, 9 Oct 2026. Same format as `../Home/04_FINAL-DESIGN_Home-Page.md`.

- **Figma:** https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign?node-id=1259-8932
- **File:** GofindBuild Website Redesign, key `aC59gtTG9nh2hwUraPnCXj`, frame **Company · Hi-Fi** `1259:8932`, 1440 × 4436, at x 2374, y 519
- **Read from:** Figma node structure only (names, sizes, positions, layer text where short). Colors, fonts and spacing values were not read. Take those from the design system and the theme settings notes.
- **Rule for this build:** staging only; copy is placeholder until final publishing (`../00_BUILD-PLAN_Staging.md`).
- **Earlier plans this supersedes:** `00_PLAN_Redesign-and-Build.md` (band list and step 4 preset table) and `Design/Figma/04_CONTEXT_Company-Page.md` (page structure). Those described the page before it was finished; where they disagree with this file, this file wins.

## Bands

| # | Band | Node | Size | Built from in HubSpot |
|---|---|---|---|---|
| 00 | Top Nav | `1259:8933` | 1440 × 96 | Elevate Site header; **Companies** marked active (2px underline, 87 wide, at x 261) |
| 01 | Hero + fork | `1363:8525` | 1440 × 717 | **Custom module GFB Hero**, company variant (see below) |
| 02 | Workers near you | `1259:8969` | 1440 × 632 | Elevate shell + **custom Job Match Card module ×2** (static) |
| – | Products and services list | `1355:7459` | 1440 × 497 | Elevate `products-and-services-list` |
| – | Testimonial | `1259:8977` | 1440 × 537 | Elevate `testimonial`. **Hidden in Figma** |
| 05 | Search → worker match (replaces testimonial) | `1362:2627` | 1440 × 689 | **New custom module** (static visual) |
| – | Features | `1259:8978` | 1440 × 522 | Elevate `features` |
| – | FAQ | `1259:8979` | 1440 × 507 | Elevate `faq-v2` |
| 09 | Final CTA | `1259:8980` | 1440 × 513 | Elevate CTA (per the R3 mapping); frame content not read |
| 11 | Footer + browse by trade | `1368:10286` | 1440 × 263 | Elevate footer |

Order on the page: 00 → 01 → 02 → products list → 05 → features → FAQ → 09 → 11. The hidden testimonial instance sits between the products list and band 05 and does not render.

## Band details

### 01 · Hero (company variant of the shared hero)
Same module name and layout as the homepage and Job Seeker hero (`M1 · Custom · GFB Hero — copy + fork` and `— visual`), so one module serves all pages.
- **Copy column** (672 wide at x 96): H1 (672 × 234), subhead (672 × 58), then a 642 × 168 row.
- **Only one fork card here:** "I'm hiring" (328 × 168) with the **Hire workers** button (177 × 48). There is no "I'm looking for work" card.
- **Next to it, a checks column** (282 wide): Posting is free · No placement fee · You talk to the worker, not an agency. Check badges are 28px, rows 56px apart.
- **Visual** (504 × 557): the welder photo in the same cut-out shape as the homepage. There is also a large image layer (`image 230`, 1440 × 1152) sitting at x 1738, outside the visible frame. Check in Figma whether it is meant to be the hero background.
- **No search bar in the header.** The Job Seeker plan used a trade + ZIP search here; the final company hero does not. The hero module needs a **company variant** (one fork card + checks) rather than a search module.

### 02 · Workers near you
Heading ("See who's available before you post"), a short subhead, two **Job Match Card** instances side by side (550 × 152, 24px gap, container 1124 at x 158), and a one-line note ("Get instant notifications of new matches and applicants").
- These are **Job Match Cards**, not Job Seeker cards. The plan (`04_CONTEXT_Company-Page.md`) called for three worker cards shown as a company sees them. Confirm this is intended; the worker card appears in band 05 instead.

### 05 · Search → worker match (replaces the testimonial)
Two columns inside a 1200 container (x 120):
- **Left, copy** (508 wide): eyebrow, heading, body.
- **Right, visual** (620 × 497), top to bottom:
  1. **Search bar** (620 × 64): TRADE segment ("Journeyman Electrician"), divider, NEAR segment ("46204 · Indianapolis"), round search button (52 × 52).
  2. **Connector** (297 × 84): vertical line, **match pill** with a live dot ("4 workers match your trade near…"), line, arrow.
  3. **Worker preview card** (460 × 349): private avatar, "Private Profile" with lock, "Journeyman", **96% profile score**, heart; "Looking for / Experience" with two rows (Electrical: Journeyman, Low voltage: Skilled) each with a four-bar level indicator and a level pill; Location row; "Seeking Full-time"; two actions, **Send job** (260 × 42) and **View profile** (138 × 45).
- This is an **illustration, not a working search.** Build it as one custom module with static content.
- It fixes the earlier card problems: the trade is consistent (search, chips and card all say electrical), the ZIP is Indianapolis, and the card is the **Private** variant, so no named worker with a headshot.

### Features, FAQ, Final CTA
Elevate `features` and `faq-v2` presets, and a Final CTA frame (513 tall) whose content was not read.

### 11 · Footer
Identical to the homepage: logo and copyright left; legal links and two social buttons (Instagram, LinkedIn, 40 × 40) right.

## What changed from the earlier Company plans

| Earlier plan | In the final design |
|---|---|
| Header with the trade + ZIP search bar, 8 header states, empty-search capture | **Dropped.** Hero is copy + one fork card + checks |
| Band 02 with three Job Seeker cards | Two **Job Match Cards**; the worker card moves to band 05 |
| Band 03 problem + 88% stat | **Not on this page** |
| Band 05 cost comparison (agency vs GoFindBuild), soft | **Not on this page**, so no pricing numbers needed for launch |
| Band 06 proof (Brothers Insulation) | Testimonial instance is **hidden**; band 05 replaces it. No customer quote on this page |
| Band 08 hire by trade | **Not on this page** |
| Sticky "Post a job" bar, phone frames | **Not in this node.** Check whether phone frames exist |
| 11 bands | **10 bands**, one of them a new custom visual |

## Build notes for HubSpot

1. **Reuse the GFB Hero module**, adding a company variant (second card replaced by a checks list). Same photo, same cut-out shape, same orange + navy-label button.
2. **Two new custom modules** (static): **Job Match Card** (shared with the Job Seeker page) and **Search → worker match** (search bar + match pill + worker preview card). The earlier "search bar" and "Job Seeker card" modules are not needed as separate, working components on this page.
3. Everything else is an Elevate preset with content typed in. Whole sections only, no one-off edits.
4. Active nav state: underline on **Companies**.
5. Mobile is CSS on the child theme; the kit has no mobile sections.
6. Footer legal links can point to the Terms and Privacy pages already in the portal.

## Held for the publish pass (copy, not structure)

- All headlines, subheads, card text, the match pill count ("4 workers…"), and the "Get instant notifications…" line.
- Claims: "Posting is free", "No placement fee", "You talk to the worker, not an agency", profile score, 96%.
- Pricing (not on this page), nav labels (I-14), a phone or booking route for Brian (not in the design).
- Footer: two layers both labelled "Privacy".
- The hidden testimonial: decide whether a customer quote returns before launch.

## Not read, check in Figma before building

- Colors, type styles, spacing values, and the real H1 and subhead text.
- Contents of the Final CTA band and the two Elevate sections (`products-and-services-list`, `features`).
- The off-frame hero image layer.
- Phone frames for this page, if any.
