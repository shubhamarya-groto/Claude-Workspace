# Job Seeker page · code

Built 14 Oct 2026 from Figma **Job Seeker · Hi-Fi** (`1259:8837`) and
`../../03_COMPONENT-COMPARISON_Company-vs-JobSeeker.md`. **No module of its own:** every band reuses a Home or
Company module with different content. Band 05 uses the shared wrapper plus the Job card.

| # | Band | Module | Settings that differ from Company |
|---|---|---|---|
| 00 | Top nav | `gfb_top_nav` | Job Seekers gets the orange underline from the page path |
| 01 | Hero | `gfb_hero_v2` | "I'm looking for work" card, dark Find jobs button, 3 checks, `tone` **Blue** (blue glow, grey badges, navy tick) |
| 02 | Jobs, pay first | `gfb_match_cards` | `mode` **Job** (pay in green, "Compensation", Apply), `spacing` **Small** (32 px) |
| – | You choose who sees you | `gfb_checklist` | 5 items, new icons briefcase, person, power |
| 05 | Search → match wrapper | `gfb_search_match` | Job copy, "3 jobs match your trade near 46204", `copy_offset` **112** |
| 05 | Job card | `gfb_job_card` | **New** shared module (`../../For companies/code/gfb-job-card/`) |
| – | Features | `gfb_features` | For workers copy, new icon ID card |
| – | FAQ | `gfb_faq` | Worker questions, grey |
| 09 | Final CTA | `gfb_final_cta` | "Your next opportunity could find you", Create my free profile |
| 11 | Footer | `gfb_footer` | Same |

The modules live in `../../Home/code/` and `../../For companies/code/`. Change them there: both pages update.

## Files

| File | What |
|---|---|
| `page.json` | Module order and this page's field values |
| `templates/gfb-job-seekers.html` | HubSpot template **GFB Job Seekers**, generated |
| `preview/gfb-job-seekers-preview.html` | Static preview, generated. Open in a browser |

Rebuild from `../../For companies/code/`: `python3 build_page.py "../../For workers/code"`. Don't edit the
template or the preview by hand.

## In HubSpot (14 Oct 2026)

| What | Where |
|---|---|
| Template **GFB Job Seekers** | `custom/content-mcp/pages/gfb-job-seekers.html`, template id `224341904975` |
| Modules | All pushed: Hero (tone), Match Cards (mode, spacing), Checklist and Features (new icons), Search Match (wrapper only, copy offset), and the new **GFB Worker card** and **GFB Job card** (`custom/content-mcp/modules/gfb_worker_card`, `gfb_job_card`) |
| Staging page | Not created yet: waiting for a go-ahead on the name **GFB Job Seekers (staging)** and slug `/job-seekers-staging` |

The hero photo URL is written into the template (raw GitHub file pinned to commit `ee16f27`), so a page made
from it has the photo straight away.

The wrapper module keeps its band above the card band (`.dnd-section:has(.gfb-sm)`), so the copy that runs
beside the card is not covered while the template's reveal animation moves the bands.

## Hero photo

Figma `1363:8425` (two smiling workers in overalls holding up hard hats), rendered from Figma and cropped to the
photo: `Design/Assets/Testing assets/hero-job-seekers-figma-537x536.jpg`. The empty tab corner is filled flat; the
module's folder-tab shape covers it. Same caveat as the Company page: 537 px wide, hosted from GitHub until the
original is uploaded to HubSpot Files.

## Still open

- **Copy** is the Figma copy and partly placeholder: feature lines ("One line of supporting detail."), FAQ
  answers, "723,000 hires needed a year", the example jobs and pay. FAQ structured data is off.
- **Links:** Find jobs and Create my free profile go to `app.gofindbuild.com/signup`; Apply buttons have none.
- **Nav underline:** the Job Seekers link points at `/job-seekers`, so the underline shows on the live slug,
  not on the staging slug.
