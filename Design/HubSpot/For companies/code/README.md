# Company page · code

Built 9 Oct 2026 from `../02_FINAL-DESIGN_Company-Page.md` and Figma **Company · Hi-Fi** (`1259:8932`).
The page reuses the Home modules wherever a band matches, and adds a module only where none does.

| # | Band | Module | From |
|---|---|---|---|
| 00 | Top nav | `gfb_top_nav` | Home, unchanged. Companies gets the orange underline from the page path |
| 01 | Hero, company variant | `gfb_hero_v2` | Home, **two new optional fields** (`checks`, `glow`), see `../../Home/code/gfb-hero/README.md` |
| 02 | Workers near you | `gfb_match_cards` | **New**, `gfb-match-cards/` |
| – | Look first (products list) | `gfb_checklist` | **New**, `gfb-checklist/` |
| 05 | Search → worker match | `gfb_search_match` | **New**, `gfb-search-match/` (static illustration) |
| – | Features | `gfb_features` | **New**, `gfb-features/` |
| – | FAQ | `gfb_faq` | Home, **one new field** (`background`: grey here) |
| 09 | Final CTA | `gfb_final_cta` | Home, unchanged |
| 11 | Footer | `gfb_footer` | Home, unchanged |

Orange buttons keep the Home modules' white label (decided 7 Oct, I-01).

## Files

| File | What |
|---|---|
| `page.json` | The page: module order and the field values that differ from each module's defaults (the Company copy) |
| `build_page.py` | Writes the template and the preview from `page.json`. Run `python3 build_page.py` (needs Jinja2); `--embed` puts the photo inside the preview file |
| `templates/gfb-companies.html` | HubSpot page template **GFB Companies**: the GFB Home canvas, fonts and motion, with this page's modules in the drag-and-drop area |
| `preview/gfb-companies-preview.html` | Static preview rendered from the modules' own `module.html` and `module.css`. Open in a browser |
| `gfb-*/` | The four new modules: `fields.json`, `module.html`, `module.css`, `README.md` |

Don't edit the template or the preview by hand: change `page.json` or a module, then rebuild.

## To get it into HubSpot

Nothing here has been pushed to the portal yet.

1. Push the **GFB Hero v2** and **GFB FAQ** changes through the connector (they're shared with Home; the new
   fields default to off/white, so the Home page doesn't change).
2. Create the four new modules through the connector, at `custom/content-mcp/modules/gfb_match_cards`,
   `gfb_checklist`, `gfb_search_match`, `gfb_features` (CSS inlined in the HTML, as for the Home modules).
3. Create the template from `templates/gfb-companies.html`, then a page on it (slug `/companies`).
4. Upload the hero photo in the Hero's Photo field.

## Still open

- **Hero photo:** Figma shows two men in hard hats with plans; the only photo in the repo is the welders.
- **Copy** is the Figma copy and still placeholder for the publish pass: feature lines ("One line of supporting
  detail."), FAQ answers 2 and 3, the claims (88%, 90 seconds, posting is free, no placement fee), the match
  count and profile scores. FAQ structured data is off until the answers are real.
- **Links:** Hire workers and Post a job go to `app.gofindbuild.com/signup`; the Send job buttons have none.
