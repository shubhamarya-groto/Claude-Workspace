# GFB Problem + Stats

Home band 03. Figma: Home Page `1259:9027` → `1355:8192`. Read 7 Oct 2026. Exact Figma copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (gear SVG inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks |
| `demo.html` | Static demo |
| `gear-path.txt` | The redrawn gear outline |

## Fields

| Field | Type | Notes |
|---|---|---|
| `line_one` | Text (multi-line) | "The workers are out there. / The opportunities are out there." Line breaks kept |
| `line_two` | Text | Orange line: "The connection between them is broken." |
| `overline` | Text | "What’s at stake" (shown in capitals) |
| `stats` | Repeater, 1 to 4 | `number` + `caption`; the orange bar is automatic |
| `background_image` | Image | Optional; replaces the built-in gradient |
| `show_gears` | Toggle | The two faint gear decorations |

## From Figma

Light band (not the dark band the R3 notes planned). Padding 128 / 96 / 112 / 96, 64px between statement
and stats. Statement Instrument Sans SemiBold 48 / 1.1, −0.5px: dark lines black at 64%, orange line
`#F97316`. Label Inter Medium 12, caps, `#16243D`. Stats 4 × 264 wide, 48 apart: 40 × 4 bar `#F16C0E`,
number Instrument Sans SemiBold 48 `#16243D`, caption Inter 14 / 1.5 black at 64%.

## Differences

- **Background:** Figma uses a 2000 × 3000 photo of a soft gradient (`image 231`), too large to export here.
  Rebuilt with CSS radial gradients (peach bottom-left, blue top-right, lilac bottom-right). Upload the
  real image to the Background image field for an exact match.
- **Gears:** Figma's two gear drawings (`Group 6`, `Group 7`) export as ~29,000 characters of path data.
  Redrawn as a simple 9-tooth gear at the same positions, sizes and faintness. Hidden on phones.
- Responsive: stats go 2 × 2 on tablets and one column on phones.

## Note for the copy pass

The orange line `#F97316` on the light background is about 2.8:1. Large text needs 3:1, so it sits just
under. A slightly deeper orange (`#EA580C`) would pass.
