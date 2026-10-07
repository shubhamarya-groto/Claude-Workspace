# GFB Pricing

Home pricing band. Figma: Home Page `1259:9027` → `1259:9084` (an instance of `Elevate / Section / Pricing / pricing`).
Read 7 Oct 2026. Classified as Template; built as a custom module on request, styled to the Figma frame.

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
| `heading` | Text | "Simple pricing" |
| `plans` | Repeater, 1 to 4 | One card per plan |
| ↳ `tier` | Text | Small label above the price ("Growth", "Enterprise") |
| ↳ `price` | Text | Large, e.g. "$149/mo", "Custom" |
| ↳ `featured` | Toggle | Dark card (Elevate card variant 4) |
| ↳ `features` | Text, repeating 0 to 20 | One line each, orange dot |
| ↳ `button_label` | Text | Empty hides the button |
| ↳ `button_link` | Link | |

## Equal heights

All cards in a row are one grid row with `align-items: stretch`, so every card takes the tallest
card's height. The button has `margin-top: auto`, so it sits at the bottom of each card and the
buttons line up even when one plan lists fewer features. On phones (≤900px) the cards stack and
each one hugs its own content.

## From Figma

Band `#F8F9FA`, 96px padding, 1200 container, heading Instrument Sans SemiBold 48 / 1.1, 32px gap.
Cards 384 wide, 24 apart, radius 20, padding 28, gap 14, white with `#D9DBDE` 1px border; featured
`#16243D`. Tier Inter Medium 13; price Instrument Sans SemiBold 48; features Inter 14 / 1.5
`#525C70` (featured `#D9DEE5`), 6px dot `#F16C0E` (featured `#FFBA6B`). Button full width, pill,
46px, `#F16C0E`, label Inter Medium 13. Figma's label is navy `#16243D`; changed to **white** on 7 Oct
(team decision; about 3:1 contrast, I-01). Hover `#EA580C`.

## Notes for the copy pass (not changed here)

- **Growth card's button says "Cancel any time"** in Figma; the other two say "Get started". Looks like
  the feature line was pasted into the button.
- **Two cards are both "Enterprise / Custom"** with different feature lists. Pricing model is still open (I-12).
- The Growth card's last feature ("Priority support") sits lower in Figma because its row is 56px tall;
  treated as a spacing slip, so all lines here use the same 14px gap.
- Tier label on white cards uses `#BB5B09` instead of Figma's `#F16C0E`: orange text at 13px is 3.2:1,
  below the 4.5:1 minimum.
