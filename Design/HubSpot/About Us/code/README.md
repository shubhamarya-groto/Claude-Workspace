# About Us page · code

Built 14 Oct 2026 from `../00_CONTEXT_About-Us-Page.md` and Figma **About Us · Hi-Fi** (`1259:9158`). Existing GFB
modules with About Us content, plus **one new module** for the three alternating rows.

| # | Band | Module | What it took |
|---|---|---|---|
| 00 | Top nav | `gfb_top_nav` | Nothing. About Us gets the orange underline from the page path |
| 01 | Header | `gfb_final_cta` | Same heading, subhead and Post a job / Find work buttons as the closing CTA. **New `layout` choice, Banner**: no card or gradient, heading is the H1, blue glow behind |
| – | About us | `gfb_features` | **New optional `aside` field**: with no features, eyebrow and heading sit left and this paragraph right |
| – | Three alternating rows | `gfb_alt_rows` | **New module**, `gfb-alt-rows/` |
| 09 | Final CTA | `gfb_final_cta` | About Us copy. It is 562 tall here only because the heading wraps to two lines; same padding as the other pages |
| 11 | Footer | `gfb_footer` | Nothing. Terms and conditions · Privacy policy · About Us are already its links |

The Home, Company and Job Seeker pages are unchanged: the new choices default to the old look (`layout` Card,
`aside` empty).

## Files

| File | What |
|---|---|
| `page.json` | Module order and this page's field values |
| `templates/gfb-about-us.html` | HubSpot template **GFB About Us**, generated |
| `preview/gfb-about-us-preview.html` | Static preview, generated. Open in a browser |
| `gfb-alt-rows/` | The new module |

Rebuild from `../../For companies/code/`: `python3 build_page.py "../../About Us/code"`.

## In HubSpot (14 Oct 2026)

| What | Where |
|---|---|
| Template **GFB About Us** | `custom/content-mcp/pages/gfb-about-us.html`, template id `224342599979` |
| GFB Final CTA, GFB Features | Updated with `layout` and `aside` (other pages unchanged: they default to Card / empty) |
| **GFB Alternating Rows** | Created at `custom/content-mcp/modules/gfb_alt_rows` |
| Staging page | Not created yet: waiting for a go-ahead on **GFB About Us (staging)**, slug `/about-us-staging` |

The Company and Job Seeker templates in this repo also gained `.gfb-alt__row` in the reveal list when rebuilt; the
HubSpot copies were not re-pushed for that (they have no rows, so nothing changes on those pages).

## Not built (as the context doc says)

The hidden search bar and "Popular trades" row left in the header layer: not built.

## Open (from the context doc, not fixed here)

- Confirm `1259:9158` is the final About Us design (found by node pattern).
- Copy is placeholder until Brian reads it; "licence" (UK) in row 2; claims to confirm.
- Row photos are placeholders; "Learn More" has no destination.
- The Final CTA's gears and peach gradient were flagged off-brand in Iteration 1 (A-21).
