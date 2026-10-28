# GFB Hero (`/custom/content-mcp/modules/gfb_hero_v2`)

The source of truth is the module in HubSpot, edited through the connector. This folder mirrors it.
- `module.live.html`: the full module source as last pushed, with the CSS inlined in a `<style>` block (23 Oct 2026).
- `fields.json`: the field schema as last pushed.
- The older split files (`module.html`, `module.css`, README with the Design Manager steps) are on branch `claude/sleepy-knuth-n7r6zh`, last changed 14 Oct.

## 23 Oct 2026: rich text headline
- New first field **Headline** (`headline_rich`, rich text). Each paragraph (press Enter) is one line of the H1. **Bold words turn orange** (the brand accent), so editors control line breaks and highlights without matching strings.
- `headline` and `highlight` are kept as a **legacy fallback**: the module uses them only when the rich text field is empty. The new field's default is empty on purpose, so existing pages didn't change when the module updated.
- Content set in the drafts: Job Seeker "Local trade jobs. / **Better pay.** / **Less searching.**", Company "Build your workforce. / **Not your recruiting bill.**", Home "A better way to build your **workforce**".
- Pages using the module: GFB Home (staging) `223806550529`, GFB Companies (staging) `223986607632`, GFB Job Seekers (staging) `224337738564`.

## Spacing field (28 Oct)

New `spacing` choice: **Standard** (96 top and bottom, min height 717; Companies, Job Seekers) or **Compact**
(80 top, 20 bottom, height from content; desktop only). Home uses Compact, matching Figma `1259:9031`
(`01 · Hero + fork`, padding 80 / 20). Tablet and phone layouts are unchanged.
