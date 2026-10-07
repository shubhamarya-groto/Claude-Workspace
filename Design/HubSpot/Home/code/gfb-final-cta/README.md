# GFB Final CTA

Home band 10. Figma: Home Page `1259:9027` → `1259:9109` (`M1 · Elevate · Card (variant 4) + custom CSS`).
Read 7 Oct 2026. Exact Figma copy as defaults. Built as code on request; Elevate Card variant 4 plus a
section background stays the fallback.

> **Live in HubSpot (7 Oct 2026):** created through the connector as **GFB Final CTA**, path `custom/content-mcp/modules/gfb_final_cta` (GoFindBuild 47303551). CSS inlined in the HTML. Update it through the connector, not the Design Manager. The button text field is `button_text` because HubSpot reserves `label`.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (gear and arrow SVGs inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks |
| `demo.html` | Static demo |

## Fields

| Field | Type | Notes |
|---|---|---|
| `heading` | Text | "The right connection could change everything." |
| `subhead` | Text | "Find the people you need. Find the opportunity you deserve." |
| `buttons` | Repeater, 0 to 3 | `button_text`, `link`, `style` (Orange primary / Dark). Defaults: **Post a job** (orange), **Find work** (dark). Links are empty: set them in the editor |
| `background_image` | Image | Optional; replaces the built-in gradient |
| `show_gears` | Toggle | The four faint gear outlines |

## From Figma

Band 1440 × 536, padding 120 / 96. Card max 1163 wide, white 60%, 1px white 16% border, radius 24,
padding 56 / 64, 20 gap, glass effect (built as `backdrop-filter: blur(24px)`). Heading Instrument Sans
SemiBold 48 / 1.1, −0.5px, `#111111`; subhead Inter 18 / 1.6, black 64%. Buttons 48 tall, pill, 4px inset,
label Inter Medium 16 white with 16px sides, 40px arrow disc (white 8%), 16 apart, 32 under the subhead.
Dark button `#0A1612` with a 1.5px `#D9D9D9` ring. Built size: band 1440 × 535, card 1163 × 295.

## Differences

- **Background:** Figma stacks two photos (1152 × 2048 and 2000 × 1335) of a soft peach-to-pink gradient,
  too large to export here. Rebuilt with CSS gradients (cream left, pink right edge). Upload the real image
  to the Background image field for an exact match.
- **Gears:** Figma's gear outlines (`Frame 174`, two groups of boolean shapes) are redrawn with the same
  gear used in Problem + Stats, as orange outlines at the same centres and sizes (inner holes 104 and 73).
  The two small gears hide on phones.
- Responsive: the card narrows on tablets; on phones the buttons stack full width.

## Notes

- White label on orange `#F16C0E` is about 3:1 (decided 7 Oct, I-01). Hover goes to `#EA580C`.
- `04_FINAL-DESIGN` mentioned a **wave** background; the frame actually shows gear outlines.
