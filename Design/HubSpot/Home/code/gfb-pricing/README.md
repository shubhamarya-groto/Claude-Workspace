# GFB Pricing

Home pricing band. Figma component `1231:129`. **Redesigned 9 Oct 2026 from a supplied screenshot**, then edited in Figma
(note moved under the button, no grey box; sizes on the file's type tokens) ("Start free. Pay only when you connect."),
replacing the earlier Figma `1259:9084` layout (three plain plan cards). Copy below is from the screenshot.

> **Live in HubSpot (9 Oct 2026):** module `custom/content-mcp/modules/gfb_pricing` updated through the connector to this
> design (GoFindBuild 47303551), and the GFB Home (staging) page's Pricing module (`main-module-4`) set to the new
> content. Update it through the connector, not the Design Manager.

| File | What |
|---|---|
| `fields.json` | Heading + 1 to 4 plans; defaults are the exact Figma copy |
| `module.html` | HubL |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks |
| `demo.html` | Static demo with the Figma copy |
| `demo-data.json` | The three plans as data |

## Fields

| Field | Type | Notes |
|---|---|---|
| `heading` | Text | "Start free. Pay only when you connect." |
| `intro` | Text (multi-line) | The paragraph under the heading |
| `accent_line` | Text | Orange line: "Workers can enjoy access to our hiring network for free." Empty hides it |
| `plans` | Repeater, 1 to 4 | One card each; all cards share the tallest card's height |
| ↳ `card_style` | Choice | `highlight` (orange border, green ticks), `light` (grey border, orange ticks), `dark` (navy, peach ticks) |
| ↳ `badge` | Text | Optional pill on the top edge ("Best value") |
| ↳ `tier` | Text | Small caps label ("Included with every account") |
| ↳ `plan_name` | Text | "Introductory Offer", "Starter", "Pro" |
| ↳ `price` / `price_suffix` | Text | "$249" + "/ month" |
| ↳ `description` | Text | One or two lines under the price |
| ↳ `rates_label` + `rates` | Text + repeater 0 to 6 | Rate table (`rate_name`, `rate_detail`, `rate_price`, `rate_unit`). Starter only by default |
| ↳ `features` | Repeater 0 to 10 | `highlight` (bold part, optional) + `text` |
| ↳ `note` | Text | Optional small centred line **under** the button (two-line slot, so buttons stay level) |
| ↳ `button_label` / `button_link` / `button_style` | Text / Link / Choice | Orange or outline. Links are empty: set them in the editor |

## Defaults (from the screenshot)

| Card | Style | Price | Button |
|---|---|---|---|
| Included with every account · **Introductory Offer** | highlight | Free | Start free trial (orange) |
| Starter · Pay as you go · **Starter** | light | $0 / month + rates $49 / $149 / $349 per connection | Continue with Starter (outline) |
| Pro · Unlimited hiring · **Pro** (badge Best value) | dark | $249 / month | Go Pro (orange) |

## Notes

- Colours use the site's tokens (navy `#16243D`, orange `#F16C0E`), not the slightly different navy and orange in
  the screenshot, so the band matches the rest of the page. Small orange labels use `#BB5B09` and the orange intro
  line `#E0580B` for contrast; white button labels on orange stay as decided 7 Oct (I-01).
- Rate details end in "..." as in the screenshot; longer text is also cut with an ellipsis on one line.
- Equal heights: grid rows stretch; the button and the note under it sit at the bottom (`margin-top: auto`), so buttons line up.
  On tablets and phones the cards stack and hug their content.
- Prices and plan rules are copy; they still go through the pricing decision (I-12) before launch.
