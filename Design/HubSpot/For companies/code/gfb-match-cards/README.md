# GFB Match Cards

Company band 02, Figma `1259:8969`. Built 9 Oct 2026 for the Company page. Figma copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks, like the Home modules |

In HubSpot at `custom/content-mcp/modules/gfb_match_cards`, CSS inlined in the HTML.

**14 Oct: shared with the Job Seeker page** (`03_COMPONENT-COMPARISON_Company-vs-JobSeeker.md`). `mode` switches between worker cards (Company) and job cards (Job Seeker); `spacing` keeps each page's own Figma gaps (Company 64, Job Seeker 32) instead of normalising them. Cards keep their own height, so a title that wraps makes only that card taller, as in Figma.

## Look

Centred heading and subhead, 1 to 4 static Job Match Cards (two 550-wide cards, 24 apart, in an 1124 container) and a one-line note. Card: building icon tile, name and trade, meta line, green profile score, trade chip and a dark Send job pill (same fill as the Hero's dark button).

The cards are examples, typed in, not live data from the app. On phones the cards stack and the score moves under the name.

## Fields

| Field | Type | Default |
|---|---|---|
| `heading` | Text | See who's available before you post |
| `subhead` | Text | Every profile shows trades, experience and how far away they are. |
| `cards` | Repeater, 0 to 4 (`worker` = title, `meta`, `score` = green value, `trade`, `button_text`, `button_link`) |  |
| `score_label` | Text | Profile score (Job Seeker: Compensation) |
| `note` | Text | Get instant notifications of new matches and applicants |
| `mode` | Choice: Worker / Job | worker |
| `spacing` | Choice: Large 64 / Small 32 | large |
| `background` | Choice: Light grey / White | grey |
