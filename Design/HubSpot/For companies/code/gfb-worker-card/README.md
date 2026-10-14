# GFB Worker card

Band 05 card, Company page. Figma `1362:9980` (460 × 349). Split out of GFB Search Match on 14 Oct 2026, per
`../../../03_COMPONENT-COMPARISON_Company-vs-JobSeeker.md`. Company copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields (moved unchanged from GFB Search Match) |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; Elevate theme variables with Figma fallbacks |

HubSpot: `custom/content-mcp/modules/gfb_worker_card`, CSS inlined in the HTML.

## Use

Place it **directly after GFB Search Match**, same background. It uses the wrapper's grid (1200 container,
508 | 620, gap 72) and sits in the right-hand column under the connector. A Private worker profile: avatar
with lock, role, green profile score, heart, "Looking for / Experience" skill rows with 4-step level bars and
pills, location with the distance in orange, seeking, Send job and View profile.

A static picture: hidden from screen readers (the wrapper's `visual_label` describes it), buttons are not links.

## Fields

`profile_title`, `show_lock`, `profile_role`, `score`, `score_label`, `skills_label`, `level_label`,
`skills` (repeater 0–4: `skill`, `tone`, `bars`, `level_text`), `location`, `distance`, `seeking`,
`primary_text`, `secondary_text`, `background`.
