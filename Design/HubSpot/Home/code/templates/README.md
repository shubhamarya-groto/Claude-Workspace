# GFB Home template + staging page

**Template:** `gfb-home.html`, created in HubSpot 7 Oct 2026 as `custom/content-mcp/pages/gfb-home.html`
(template id `223800719733`, GoFindBuild 47303551). Update it through the connector (UPDATE_CUSTOM_TEMPLATE),
using the template id.

A clean canvas: one drag-and-drop area (`main`), every section full width with zero padding, so each GFB
module controls its own background, width and spacing. Fonts (Instrument Sans, Inter, Source Serif 4) load
once in the head. Not an Elevate template, so `--hsElevate--…` variables are absent and the modules use their
Figma fallback values.

The template starts with the eight GFB modules in Figma order. Editors can reorder, remove or add modules
in the page editor.

**Staging page:** **GFB Home (staging)**, slug `/home-staging`, page id `223806550529`, **unpublished draft**.
Editor: https://app.hubspot.com/pages/47303551/editor/223806550529

| # | Band | Module |
|---|---|---|
| 0 | Top nav | `gfb_top_nav` (added 7 Oct) |
| 1 | Hero + fork | `gfb_hero_v2` |
| 1b | Trust bar | `gfb_trust_bar` (added 7 Oct) |
| 2 | What you get | `gfb_what_you_get` |
| 3 | Testimonials | `gfb_testimonials` |
| 4 | Pricing | `gfb_pricing` |
| 5 | Problem + stats | `gfb_problem_stats` |
| 6 | FAQ | `gfb_faq` |
| 7 | Final CTA | `gfb_final_cta` |
| 8 | Footer | `gfb_footer` |

## Not on the page yet

- **Hero photo:** empty (grey). Upload `Design/Assets/Testing assets/hero-welder-1400x799.jpg` to Files and
  pick it in the Hero's Photo field. Same for What You Get images and testimonial photos.
- **Button links:** Hero, Pricing and Final CTA buttons have no links yet.
- **FAQ answers** 2 and 3 are placeholders; the FAQ search data is on, so fill them before publishing.
- **About Us** footer link points to `/about-us`; confirm.

## Motion (live in the template, 7 Oct)

`gfb-motion.html` holds the section reveal and page intro; the same code is in `gfb-home.html`, updated in
HubSpot through the connector (template id `223800719733`). The template's starting layout now also includes
the Top Nav and Trust bar, so new pages built on it match the staging page. Inside the editor
`is_in_editor` sets `window.GFB_EDITOR`, which turns both effects off.

- **Reveal:** bands below the first screen fade in and rise 24px as they scroll into view (0.6s, ease-out);
  cards, stats, FAQ rows and trust items follow 80ms apart. The nav, hero and trust bar show at once.
  Testimonial slides are left alone because they already move.
- **Intro:** a gear beside the GoFindBuild logo, on white. The gear turns while its orange outline draws round
  it (1s); when the outline closes the gear fills orange (0.2s) and the page shows. Uses the same gear as
  Problem + Stats and Final CTA. Shows only if the page is still loading after 0.3s, once shown it always
  finishes the fill (about 1.25s), once per visit.
- **Off** for "reduce motion", inside the HubSpot editor (`window.GFB_EDITOR`, to be set from `is_in_editor`),
  and when JavaScript doesn't run: content is never left hidden.
- `window.GFB_FORCE_INTRO` is for the preview's "Replay intro" button only.
