# Company page · code

Built 9 Oct 2026 from `../02_FINAL-DESIGN_Company-Page.md` and Figma **Company · Hi-Fi** (`1259:8932`).
The page reuses the Home modules wherever a band matches, and adds a module only where none does.

| # | Band | Module | From |
|---|---|---|---|
| 00 | Top nav | `gfb_top_nav` | Home, unchanged. Companies gets the orange underline from the page path |
| 01 | Hero, company variant | `gfb_hero_v2` | Home, **new optional fields** (`checks`, `glow`, `tone`), see `../../Home/code/gfb-hero/README.md` |
| 02 | Workers near you | `gfb_match_cards` | **New**, `gfb-match-cards/` (worker mode, large spacing) |
| – | Look first (products list) | `gfb_checklist` | **New**, `gfb-checklist/` |
| 05 | Search → match wrapper | `gfb_search_match` | **New**, `gfb-search-match/` (static illustration, copy offset 140) |
| 05 | Worker card | `gfb_worker_card` | **New** 14 Oct, `gfb-worker-card/`, split out of the wrapper |
| – | Features | `gfb_features` | **New**, `gfb-features/` |
| – | FAQ | `gfb_faq` | Home, **one new field** (`background`: grey here) |
| 09 | Final CTA | `gfb_final_cta` | Home, unchanged |
| 11 | Footer | `gfb_footer` | Home, unchanged |

Orange buttons keep the Home modules' white label (decided 7 Oct, I-01).

**Shared with the Job Seeker page** (`../../For workers/code/`, 14 Oct). The modules here are used by both pages;
the comparison and decisions are in `../../03_COMPONENT-COMPARISON_Company-vs-JobSeeker.md`. Spacing differences
between the two Figma frames are kept, through settings (`spacing`, `copy_offset`), not normalised.

## Files

| File | What |
|---|---|
| `page.json` | The page: module order and the field values that differ from each module's defaults (the Company copy) |
| `build_page.py` | Writes the template and the preview from a `page.json`. `python3 build_page.py` builds this page, `python3 build_page.py "../../For workers/code"` the Job Seeker page (needs Jinja2); `--embed` puts the photo inside the preview file |
| `templates/gfb-companies.html` | HubSpot page template **GFB Companies**: the GFB Home canvas, fonts and motion, with this page's modules in the drag-and-drop area |
| `preview/gfb-companies-preview.html` | Static preview rendered from the modules' own `module.html` and `module.css`. Open in a browser |
| `gfb-*/` | The new modules, shared with the Job Seeker page: `fields.json`, `module.html`, `module.css`, `README.md` |

Don't edit the template or the preview by hand: change `page.json` or a module, then rebuild.

## In HubSpot (9 Oct 2026)

Pushed through the connector to GoFindBuild (47303551). Update them through the connector, not the Design Manager.

| What | Where |
|---|---|
| Template **GFB Companies** | `custom/content-mcp/pages/gfb-companies.html`, template id `223986369108` |
| GFB Hero v2, GFB FAQ | Updated with the new fields (Home unchanged: they default off / white) |
| GFB Match Cards, GFB Checklist, GFB Search Match, GFB Features | Created at `custom/content-mcp/modules/gfb_match_cards`, `gfb_checklist`, `gfb_search_match`, `gfb_features` |

HubSpot reserves some field names (`name`, `body`, …), so Match Cards uses `worker` and the others `intro`.
Search Match also failed to save with a `textarea` heading, so its heading is two text fields.

**14 Oct:** modules updated for the Job Seeker page (see the table above). Search Match lost its card, so
**GFB Worker card** was inserted on the staging page right after it (module `main-module-10`). The GFB Companies
template in HubSpot was updated the same day to match `templates/gfb-companies.html` (worker card, settings,
and the hero photo URL), so a new page made from it comes out complete. Updated again the same day to the
Figma original photo (commit `acd99e6`).

**Staging page:** **GFB Companies (staging)**, slug `/companies-staging`, page id `223986607632`, **unpublished draft**.
Editor: https://app.hubspot.com/pages/47303551/editor/223986607632
Title "Hire skilled trades workers directly | GoFindBuild" and a meta description are set.

**Logo (14 Oct):** comes from the GFB Top Nav and GFB Footer code, so every page using them gets it:
the Logo image field if set, else the portal's brand logo (Settings > Branding), else the brand-kit file
`FullLogoColored-01.png` in HubSpot Files. The field is left empty on this page so it follows the brand logo.

**Hero photo (14 Oct): now the original source image from Figma, 1125 × 750,**
`Design/Assets/Testing assets/hero-companies-figma-1125x750.jpg` at commit `acd99e6`. Earlier note, 9 Oct: the Figma photo (`1363:8546`, two men in hard hats with plans), rendered from Figma
and cropped to the photo: `Design/Assets/Testing assets/hero-companies-figma-537x536.jpg`. The connector can't
upload to HubSpot Files, so the Photo field points at the file's raw GitHub URL, pinned to commit `8489296`.
**Before publishing:** upload the original photo to HubSpot Files and pick it in the Photo field instead. It is
only 537 px wide (Figma's render), so it is soft on high-density screens, and a GitHub URL is not a production host.

## Still open

- **Copy** is the Figma copy and still placeholder for the publish pass: feature lines ("One line of supporting
  detail."), FAQ answers 2 and 3, the claims (88%, 90 seconds, posting is free, no placement fee), the match
  count and profile scores. FAQ structured data is off until the answers are real.
- **Links:** Hire workers and Post a job go to `app.gofindbuild.com/signup`; the Send job buttons have none.
