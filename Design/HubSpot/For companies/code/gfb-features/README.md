# GFB Features

Company features band, Figma `1259:8978` (the design's Elevate `features`). Built 9 Oct 2026 for the Company page. Figma copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks, like the Home modules |

**Not in HubSpot yet.** Create it through the connector at `custom/content-mcp/modules/gfb_features`, CSS inlined in the HTML.

## Look

Eyebrow, heading and body in 4 of 12 columns; a two-column grid of 1 to 8 features (icon badge, title, one line) in 8 of 12.

One column of features on phones.

## Fields

| Field | Type | Default |
|---|---|---|
| `eyebrow` | Text | For companies |
| `heading` | Text | Automatically get matched to the skills you need |
| `body` | Text | Tell us what you need and the matches come to you. |
| `items` | Repeater, 1 to 8 (`icon`, `title`, `description`) |  |
| `background` | Choice: White / Light grey | white |
