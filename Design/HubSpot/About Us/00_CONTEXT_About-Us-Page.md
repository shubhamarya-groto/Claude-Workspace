# About Us page · context and final design

Context and build reference for the About Us page. 14 Oct 2026. Same format as the Home and Company docs.

- **Figma:** frame **About Us · Hi-Fi** `1259:9158`, 1440 × 2956, file `aC59gtTG9nh2hwUraPnCXj`, at x 6454, y 519 (the slot after Home, Company and Job Seeker in the final row).
- **Found by node-ID pattern, not from a link.** The About Us frame was not linked in the chat. It sits next to the other final frames and matches the row layout, but **confirm this is the final About Us design.**
- **Read from:** node structure and a full-page screenshot. Colors, fonts and spacing values were not read.
- **Rule for this build:** staging only; copy is placeholder until final publishing (`../00_BUILD-PLAN_Staging.md`).

## Purpose and status

- About Us was **not in Brian's mockup** (his three pages were Home, For companies, For workers) and is not a launch-critical page. It was added in Figma on 25 Sep, cloned from the Company page skeleton, and rebuilt since.
- It answers "who is behind this and why should I trust it", for companies who buy from a handshake and for workers who have never heard of the product.
- **Copy status:** the work log says only two lines on the 25 Sep version were Brian's approved words and the rest needed his read. Nothing in the files shows he has approved the final copy. Treat all of it as placeholder until the publish pass.
- The older version (25 Sep, node `1205:1587`) had a two-button fork header, a worker card beside a job card, a Matthew B. quote, a "why we built it" band with the 723,000 stat, and an FAQ. **The final design drops all of those.**

## Bands

| # | Band | Node | Size | Built from in HubSpot |
|---|---|---|---|---|
| 00 | Top Nav | `1259:9159` | 1440 × 96 | Elevate Site header. **About Us** is the active link (underline at x 516). The Companies underline layer is hidden |
| 01 | Header | `1259:9163` | 1440 × 425 | Centered banner: H1, subhead, two buttons. Not named as a module in Figma. Most likely Elevate `hero-banner-centered` (inference, check) |
| – | About us | `1259:9189` | 1440 × 330 | Elevate section `Team / about-us` |
| – | Three alternating rows | `1259:9190` | 1440 × 1280 | Image and text rows, alternating sides, each with a button. Most likely Elevate `multi-row-alternating` (inference, check) |
| 09 | Final CTA | `1259:9228` | 1440 × 562 | Elevate CTA (content read from screenshot below) |
| 11 | Footer | `1368:10322` | 1440 × 263 | Elevate footer |

**No custom modules are needed on this page.** There is no GFB Hero, no Job Match Card and no Search → match band.

## Band details (read from the screenshot)

### Nav
Logo, **Companies · Job Seekers · About Us**, Login, Get Started. The nav no longer has Pricing. About Us is now a top-level link, which settles the earlier question of whether About joins the nav (I-14).

### 01 · Header
- H1: "The connection between them is broken."
- Subhead: "The workers are out there. The opportunities are out there. GoFindBuild was built by a 20 year construction veteran to connect them directly, with no recruiter in the middle."
- Two buttons: **Post a job** (orange) and **Find work** (dark), 156 and 155 wide, 48 tall, centered.
- Background: a soft blue glow on white, not the dark photo used on the other pages. There is a large `image 230` layer (1440 × 1152) in the frame, below the visible header; it is probably the glow asset (check).
- Leftovers: a hidden search bar and a hidden "Popular trades" row (the old Job Seeker header). **Do not build them.**

### About us (Elevate `about-us`)
Eyebrow "ABOUT US", heading "Built by someone who has done the work", body on the right: "Brian spent twenty years in construction before writing a line of this. GoFindBuild is built in Indianapolis and works across central Indiana, for the firms and the trades that never found each other on a job board."

### Three alternating rows
Container 1200 at x 120. Each row is 320 tall, with a 576 × 320 image and 576 wide text, 48px between the columns:
1. Image left, text right: **Twenty years on site**: "Brian watched good crews go unfilled while good workers went unfound. The same week, every week, on both sides of the same fence." **Learn More →**
2. Text left, image right: **Hiring never got easier**: "Job boards returned resumes with no licence check. Agencies took a cut of every hour worked. Small firms had neither the time nor the budget for either." **Learn More →**
3. Image left, text right: **So we built the connection**: "One profile for workers. One post for companies. Nobody in the middle taking a cut of anyone's hours." **Learn More →**

Images shown: a worker in a hard hat reading plans on a construction site, two workers looking at a tablet, a handshake between a worker and a man in a suit. **The layers are named "photo of Brian on site, to come"**, so these are placeholders. They look like stock or generated images, so their source and rights are unknown (see issues).

### 09 · Final CTA
Peach-to-pink gradient with large outlined **gear watermarks** and a frosted card: "Find the people you need. Find the opportunity you deserve." / "Post a job, or build a free profile. Both take minutes." / **Post a job** and **Find work**. 562 tall (the Company and Job Seeker pages have 513).

### 11 · Footer
Logo and copyright on the left. On the right: **Terms and conditions · Privacy policy · About Us**, then Instagram and LinkedIn buttons. (This corrects an earlier note: the two text layers named "Privacy" are only layer names. The visible links are Terms and conditions, Privacy policy and About Us. The same footer layers appear on the Home, Company and Job Seeker pages.)

## What this page reuses from the other pages

| Piece | Same as other pages? |
|---|---|
| Nav (Elevate Site header) | Yes, with About Us active |
| Footer | Yes, identical layers |
| Final CTA | Same band and buttons, different height (562 vs 513) |
| Header | **No.** Centered banner, no search or fork card, so it is not the GFB Hero module |
| Everything between header and CTA | Unique to this page (Elevate presets only) |

## Build notes for HubSpot

1. Elevate presets only, whole sections, no custom code. This is the easiest page to build.
2. Upload the three row images to HubSpot Files with alt text, under about 300 KB each. Do not hot-link.
3. Footer links: **Terms and conditions** and **Privacy policy** can point to the pages already published in the GoFindBuild portal (`/gofindbuild-terms-and-conditions`, `/gofindbuild-privacy-policy`). **About Us** points to this page.
4. The "Learn More" buttons have no destination in the design. Decide where each goes, or remove them, before staging links are set (the live demo's dead-link problem is H-15).
5. Spacing is not corrected: build to this frame as drawn.
6. Mobile: CSS on the child theme. Mobile frames for About Us exist in the older Presentation section of the Figma file (two, `1259:6032` and `1259:6128`); not confirmed as final.

## Issues to log (do not fix now)

| Issue | Detail |
|---|---|
| **Final CTA looks off-brand against Iteration 1** | `05_REVIEW_Iteration-1.md` flagged gear watermarks and peach gradients as off-brand and dated (also A-21 in the audit list). The About Us CTA uses both. Check whether the same CTA band is on the other pages; only this one was seen here |
| **Placeholder photos** | Layers say "photo of Brian on site, to come". Real photos of Brian or the crews are still missing (I-15). Stock or generated faces next to a named founder is the problem H-05 raised for testimonials |
| **"Learn More" has no target** | Three buttons with no defined link |
| **Spelling** | Copy says "licence" (UK). The site is US; H-08 already changed "licences" to "licenses" on Home |
| **Claims to confirm** | "20 year construction veteran", "built in Indianapolis and works across central Indiana", "no recruiter in the middle", "agencies took a cut of every hour worked", "nobody in the middle taking a cut of anyone's hours". The last one sits against the $99–$399 unlock fee; suggested safer wording is in `Design/Figma/04_CONTEXT_Company-Page.md` ("no agency, no markup on their hours, no cut of their pay") |
| **Header glow image** | `image 230` (1440 × 1152) is outside the visible header. Check how the glow is actually produced |
| **CTA height** | 562 vs 513 on other pages (spacing, not corrected) |

## Missing from the page (earlier plan vs final)

No FAQ, no testimonial or proof band, no stats (the 723,000 line is gone), no team or Brian photo block, no cost comparison. If any of these were expected, they are not in this design.

## Held for the publish pass (copy, not structure)

All headings and body text above, the claims in the table, button labels, "Learn More" destinations, the three row photos, and whether Brian approves the page at all (the plan said Brian to read the About copy).

## Not read, check in Figma before building

- Colors, type styles, spacing values and the exact preset for the header and the rows (inferred above).
- Phone frames and whether they are final.
- Whether the Final CTA band content matches the other pages.
