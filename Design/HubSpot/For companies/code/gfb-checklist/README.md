# GFB Checklist

Company "Look first" band, Figma `1355:7459` (the design's Elevate `products-and-services-list`). Built 9 Oct 2026 for the Company page. Figma copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks, like the Home modules |

**Not in HubSpot yet.** Create it through the connector at `custom/content-mcp/modules/gfb_checklist`, CSS inlined in the HTML.

## Look

Heading and body in 5 of 12 columns, a ruled list of 1 to 8 points in 7 of 12. Each point has a 28px icon badge in What You Get's Companies colours (`#FDEDDF`, orange icon).

Stacks to one column below 1024px.

## Fields

| Field | Type | Default |
|---|---|---|
| `heading` | Text | Look first, reach out when you're ready |
| `intro` | Text | Browsing costs nothing. You pay only when you want to talk. |
| `items` | Repeater, 1 to 8 (`icon`, `item_text`) |  |
| `background` | Choice: White / Light grey | white |
