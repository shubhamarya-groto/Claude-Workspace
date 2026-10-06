# Home page · Code vs Template

Read 6 Oct 2026 from the Figma file itself (`aC59gtTG9nh2hwUraPnCXj`, frame **Home Page** `1259:9027`),
checking each band's real layer type and main component. Layer names were not trusted on their own.

Goes with `04_FINAL-DESIGN_Home-Page.md`, which has sizes, copy and band order.

## The two groups

| Group | Meaning | How it's built | Who controls the look |
|---|---|---|---|
| **Template** | Picked from HubSpot's "Add to page" panel (Elevate section, module or global) and dropped in | Drag in, type the content, set editor options (background image, item count) | **Theme settings**, once for the whole site, plus small child-theme CSS where noted |
| **Code** | No template in the panel can produce it | Custom module (HTML/CSS/fields), built to match Figma | The module code and the Figma file |

## Band by band

| # | Band | Node | Group | From the template panel / what to code |
|---|---|---|---|---|
| 00 | Top Nav | `1259:9028` | **Template** | Elevate **Site header** (global). Figma: DS Top Nav instance |
| 01 | Hero + fork | `1259:9031` | **Code** | Custom module **GFB Hero** (already exists, `code/gbf-module/`) |
| 02 | Trust bar | `1259:9048` | **Template** | Elevate **Card** ×3 (icon + one line), CSS to keep them in one row with the 28px check badge |
| – | What you get | `1363:8560` | **Code** | Custom module. See note 1 |
| 08 | Testimonials | `1259:9068` | **Template** | Elevate **TestimonialSlider** (Heading + slider) |
| – | Pricing | `1259:9084` | **Template** | Elevate section **`pricing`**. Figma: real instance; changes are text, band fill, one hidden element |
| 03 | Problem + stats | `1355:8192` | **Template** | Elevate section **`metrics`**. See note 2 |
| – | FAQ | `1259:9108` | **Template** | Elevate section **`faq-v2`**. Figma: real instance; text changes only |
| 10 | Final CTA | `1259:9109` | **Template** | Elevate **Card** variant 4 (H2, subhead, **Post a job** + **Find work**). See note 3 |
| 11 | Footer | `1259:9149` | **Template** | Global footer from **Logo**, **Rich text** (copyright), **Menu** (legal links), **Social follow** (Instagram, LinkedIn) |

**Count:** 8 Template · 2 Code (Hero, What you get).

## Notes

1. **What you get is Code.** It is named `Elevate / Section / Products / products-and-services-two-column`,
   but it is a plain frame, not an instance. The real preset is a heading plus three full-width feature
   rows (1440 × 607). The design is two 568-wide cards, each with a header strip and rule, then three
   features **laid over an image** (1440 × 770). Card and ImageAndText can't put a feature list on top of
   an image, so no template gets there. Also found:
   - Five of the six icon layers contain a different icon from their name: `Icon / briefcase` is
     **timer**, `contact` is **user-check**, `message-circle` is **messages-square**, `clock` is **pin**,
     `badge-dollar-sign` is **radar**. Only `file-check` matches. Build from the icons, not the names.
   - The Job Seekers image (`image 235`) is 563 tall in a 440 card, so it's cropped. Confirm the crop.
2. **Problem + stats stays Template, with two conditions.** Metrics covers the heading and the four stats
   (88% · $58k+ · 723,000 · 90%, overline `WHAT'S AT STAKE`). The background photo and the three vector
   illustration groups have to be **exported as one section background image** and set in the editor; the
   40 × 4 accent bar per stat and the two-tone problem statement are CSS. If the illustrations must sit at
   fixed positions across screen sizes, this moves to Code.
3. **Final CTA.** The wave background (`Frame 174`) is drawn vectors: export it as an image and set it as
   the section background in the editor. Blur and white border on the card are CSS.
4. **Footer.** Two legal text layers both say "Privacy" (open in `04`).

## Changes this makes to `04_FINAL-DESIGN_Home-Page.md`

- "What you get" is Code, not an Elevate preset.
- Bands 03 and 10 are now read (above).
- Build note 2 there ("Hero is the only custom code") no longer holds: **What you get** is code too.
