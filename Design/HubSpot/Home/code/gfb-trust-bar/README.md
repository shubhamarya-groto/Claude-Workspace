# GFB Trust bar

Home band 02. Figma: Home Page `1259:9027` → `1259:9048` (`M1 · Elevate · Card ×3`). Read 7 Oct 2026.
Exact Figma copy as defaults. Built as code on request; three Elevate Cards stay the fallback.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (check icon inlined, Figma's `check_small` path) |
| `module.css` | Styles |
| `demo.html` | Static demo |

## Fields

| Field | Type | Notes |
|---|---|---|
| `items` | Repeater, 1 to 6 | `item_text`: Direct employer connections · No recruiter middlemen · 150+ trade categories |
| `alignment` | Choice | Left (as in Figma) or Centre |

## From Figma

White band, padding 0 / 96 / 64 / 96 (it sits right under the hero, so no top padding). Items 32 apart.
Badge 28 × 28, radius 6, `#FFBA6B` at 20%, check `#B86117`. Text Inter Medium 15 / 1.5 `#16243D`, 10 from the
badge. Built: band 1440 × 92 and items at x 96 / 372 / 611, the same as Figma.

Responsive: 24px sides on tablets (lines up with the hero), one item per line on phones. The list has an
accessible name ("Why GoFindBuild"); the badges are hidden from screen readers.
