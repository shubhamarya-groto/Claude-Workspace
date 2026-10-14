# GFB Alternating Rows

About Us band "three alternating rows", Figma `1259:9190` (About Us · Hi-Fi `1259:9158`). Built 14 Oct 2026. The
only module made from scratch for About Us: no existing GFB module has image-and-text rows that switch sides.

| File | What |
|---|---|
| `fields.json` | Fields, with the Figma copy and the three Figma images as defaults |
| `module.html` | HubL (Lucide arrow inlined) |
| `module.css` | Styles; Elevate theme variables with Figma fallbacks, like the other GFB modules |

HubSpot: `custom/content-mcp/modules/gfb_alt_rows`, CSS inlined in the HTML.

## Look

1200 container. Each row: a 576 × 320 image (radius 16) beside 576 of text, 48 apart, text centred against the
image; 64 between rows, 96 above and below. Title 24, body 16 muted, then a text link with an arrow. The image is on
the left in row 1 and switches sides each row (`first_image` flips that). On tablets and phones every row stacks,
image first.

## Fields

| Field | Type | Default |
|---|---|---|
| `rows` | Repeater, 1 to 6 (`image`, `title`, `text`, `link_text`, `link`) | The three Figma rows: Twenty years on site / Hiring never got easier / So we built the connection |
| `first_image` | Choice: Left / Right | Left |
| `background` | Choice: White / Light grey | White |

The link reads "Learn More: <title>" to screen readers, so three identical "Learn More" links stay distinct.

## Open

- Images are the Figma placeholders (layers named "photo of Brian on site, to come"), source and rights unknown.
  Hosted from GitHub (`Design/Assets/Testing assets/about-row-*.jpg`) until uploaded to HubSpot Files.
- "Learn More" has no destination in the design: the links are empty (`#`). Decide or hide (clear Link text).
