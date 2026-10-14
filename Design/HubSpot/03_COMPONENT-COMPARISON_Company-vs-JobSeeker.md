# Company vs Job Seeker · component comparison and build decisions

14 Oct 2026. Compares the final Company page (Figma `1259:8932`) with the final Job Seeker page (`1259:8837`), file `aC59gtTG9nh2hwUraPnCXj`. Read from node structure plus screenshots of the band 02 cards. Colors, fonts and spacing values were not read.

## Verdict

Almost every band is the **same component with content changed**. The only band that is not content-only is band 05, which is split into three components (decision below).

| Band | Company | Job Seeker | Same component? |
|---|---|---|---|
| 00 Nav | Underline under Companies (x 261, 87 wide) | Underline under Job Seekers (x 388, 97 wide) | Yes, active state only |
| 01 Hero | "I'm hiring" card, Hire workers (177 × 48), checks: Posting is free · No placement fee · You talk to the worker, not an agency | "I'm looking for work" card, Find jobs (150 × 48), checks: No resume needed · Build a profile in minutes · You choose who sees you | Yes, one **GFB Hero** module with fields for card title, line, button label, link and 3 checks |
| 02 Cards | "Workers near you": 2 Job Match Cards, worker content (name · trade, "Seeking full-time · 5.8 mi", profile score %, trade chip, **Send job**) | "Jobs, pay first": 2 Job Match Cards, job content (company · title, "Full-time · 5.8 mi", pay "$23/HR" with "Compensation", trade chip, **Apply**) | Yes, one **Job Match Card** with a worker mode and a job mode |
| List section | Elevate `products-and-services-list` | Same preset, same size (497) | Yes |
| 05 Search → match | See below | See below | **Three components** |
| Features | Elevate `features` (522) | Same | Yes |
| FAQ | Elevate `faq-v2` (507) | Same | Yes |
| 09 Final CTA | 513 | 513 | Yes |
| 11 Footer | Same layers, same two socials | Same | Yes |

Both pages also carry the same hidden Elevate testimonial instance and the same off-frame hero image layer (`image 229` / `image 230`, 1440 × 1152 at x 1738).

## Decision: band 05 is three components

Band 05 is the search → match band that replaces the testimonial. The wrapper is identical on both pages; the card inside is a different layout. Decision (from the team, 14 Oct): build it as **three components**, so either card can be changed later without touching the other or the wrapper.

| # | Component | Used on | What it contains |
|---|---|---|---|
| 1 | **Search → match wrapper** | Both pages | Copy block (eyebrow, heading, body) on the left; on the right the search bar (trade segment, ZIP segment, 52px search button), the connector with the match pill and live dot, and a **slot** for the card |
| 2 | **Job Seeker page card** (job post card) | Job Seeker page | Company logo tile, job title and company, heart, pay row with Full-time badge, location, "Posted today", **Apply now** (290 × 42) and **View** (88 × 45). Frame `1354:9913`, 440 × 294 |
| 3 | **Company page card** (worker preview card) | Company page | Private avatar with lock, level, 96% profile score, heart, "Looking for / Experience" skill rows with level bars and pills, location, "Seeking Full-time", **Send job** (260 × 42) and **View profile** (138 × 45). Frame `1362:9980`, 460 × 349 |

Wrapper details that differ only by content: match pill text ("3 jobs match your trade near 46204" vs "4 workers match your trade near…"), pill width (273 vs 297), and the copy block's vertical offset (y 112.5 vs 140, centered on the visual height). Search bar content is identical on both pages ("Journeyman Electrician", "46204 · Indianapolis").

## Decision: spacing is not corrected

Spacing differences between the two pages stay as drawn. They are logged as a **Figma issue** and are **not** to be fixed or normalized in HubSpot. Build each page's bands to match its own Figma frame. Where a shared component is used on both pages, expose spacing as an editable setting so each page can match its frame rather than forcing one value.

Differences found (for the record, nothing to change):

| Where | Company | Job Seeker |
|---|---|---|
| Band 02 gaps (heading → subhead → cards → note) | 64px | 32px |
| Band 02 height | 632 | 561 |
| Band 02 card row | Two cards, both 152 tall | First card 177 tall (title wraps to two lines), second 152 |
| Hero checks column | y 14, row 642 wide | y 0, row 568 wide |
| Band 05 height | 689 | 634 |
| Whole page | 4436 tall | 4310 tall |

## Custom modules needed (count)

1. **GFB Hero** (shared, with fields as above)
2. **Job Match Card** (worker mode and job mode)
3. **Search → match wrapper**
4. **Job Seeker page card**
5. **Company page card**

Everything else is an Elevate preset with content typed in. Nav only needs the active state per page.

## Not checked

- Whether the Elevate list, features, FAQ and Final CTA sections carry the same layout options on both pages (only sizes and preset names were compared).
- Phone frames: Job Seeker, Company, Home and About Us mobile frames exist in the older "Presentation" section of the Figma file. Not confirmed as final, not compared.
- Home page and About Us were not part of this comparison.
