# GFB Match Cards

Company band 02, Figma `1259:8969`. Built 9 Oct 2026 for the Company page. Figma copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks, like the Home modules |

**Not in HubSpot yet.** Create it through the connector at `custom/content-mcp/modules/gfb_match_cards`, CSS inlined in the HTML.

## Look

Centred heading and subhead, 1 to 4 static Job Match Cards (two 550-wide cards, 24 apart, in an 1124 container) and a one-line note. Card: building icon tile, name and trade, meta line, green profile score, trade chip and a dark Send job pill (same fill as the Hero's dark button).

The cards are examples, typed in, not live data from the app. On phones the cards stack and the score moves under the name.

## Fields

| Field | Type | Default |
|---|---|---|
| `heading` | Text | See who's available before you post |
| `subhead` | Text | Every profile shows trades, experience and how far away they are. |
| `cards` | Repeater, 0 to 4 (`name`, `meta`, `score`, `trade`, `button_text`, `button_link`) |  |
| `score_label` | Text | Profile score |
| `note` | Text | Get instant notifications of new matches and applicants |
| `background` | Choice: Light grey / White | grey |
