# GFB Search Match (Search → match wrapper)

Band 05 on both pages, Figma `1362:2627` (replaces the hidden testimonial). Built 9 Oct 2026 for the Company page; **split 14 Oct** into this wrapper plus two card modules, per `../../../03_COMPONENT-COMPARISON_Company-vs-JobSeeker.md`. Company copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks, like the Home modules |

In HubSpot at `custom/content-mcp/modules/gfb_search_match`, CSS inlined in the HTML.

## Look

Copy (508) beside a static illustration (620): search bar with trade and location and a connector with the match pill. **The card is the next module on the page**: GFB Worker card (`../gfb-worker-card/`, Company) or GFB Job card (`../gfb-job-card/`, Job Seeker). HubSpot modules can't hold other modules, so the card module uses the same grid and lines up under the connector; the band reads as one. Give both the same background.

`copy_offset` places the copy on desktop (Company 140, Job Seeker 112, measured from the top of the search bar as in Figma). The copy box has no height, so it runs down beside the card without pushing it down. On tablets and phones the copy sits above the search bar.

It is a picture, not a working search: the illustration has one description for screen readers (`visual_label`, which should describe the card too) and the card's buttons are not links. On phones the search bar wraps to two rows.

## Fields

| Field | Type | Default |
|---|---|---|
| `eyebrow` | Text | How matching works |
| `heading` | Text | Search your trade. |
| `heading_two` | Text | See who's ready to work. |
| `intro` | Text | Enter the trade you need and your ZIP code. Matched workers show their skills, experience level and distance up front, so you're reviewing people, not resumes. |
| `visual_label` | Text | Example: a search for Journeyman Electrician near 46204 Indianapolis finds 4 matching workers, including a private profile with a 96% profile score. |
| `trade_label` | Text | Trade |
| `trade` | Text | Journeyman Electrician |
| `near_label` | Text | Near |
| `near` | Text | 46204 · Indianapolis |
| `match_text` | Text | 4 workers match your trade near 46204 |
| `copy_offset` | Number (px) | 140 |
| `background` | Choice: Light grey / White | grey |
