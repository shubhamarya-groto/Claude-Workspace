# Home page · which sections are HubSpot components and which are Figma designs

Read 6 Oct 2026 from the Figma file itself (`aC59gtTG9nh2hwUraPnCXj`, frame **Home Page** `1259:9027`),
checking each band's real layer type and main component. Layer names were not trusted on their own.
Two names are wrong: "What you get" is named as an Elevate section but is a plain frame, and the
trust bar items are named "Elevate · Card" but are drawn by hand.

Goes with `04_FINAL-DESIGN_Home-Page.md`, which has sizes, copy and band order.

## The rule

| Kind | In Figma | In HubSpot | Who controls the look |
|---|---|---|---|
| **A · Component** | An instance of an `Elevate / …` kit component (or the DS Top Nav, which is the kit's SiteHeader) | Drop the matching Elevate preset or module and type the content in | **Theme settings**, once for the whole site. Don't restyle per page |
| **B · Elevate stand-in** | Drawn by hand, but copies an Elevate module's look and layout | Use the Elevate module. Treat it like A; the drawing is only a placeholder | Theme settings |
| **C · Figma design** | Designed in Figma, no kit component, or a kit component detached and redesigned | Custom module or child-theme CSS. The preset alone can't produce it | **Code** (module HTML/CSS) and the Figma file |

A and B: change how they look in theme settings, and the change reaches every page.
C: each one is its own piece of work, and has to be checked against Figma pixel by pixel.

## Band by band

| # | Band | Node | Figma layer type | Kind | Build it as |
|---|---|---|---|---|---|
| 00 | Top Nav | `1259:9028` | Instance of DS **Top Nav** (= kit SiteHeader) | **A** | Elevate Site header, global |
| 01 | Hero + fork | `1259:9031` | Plain frames, `M1 · Custom · GFB Hero`; only the two buttons are DS Button instances | **C** | Custom module **GFB Hero** (already exists) |
| 02 | Trust bar | `1259:9048` | Plain frames named `M1 · Elevate · Card ×3`; no instances | **B, check** | Elevate module, see note 1 |
| – | What you get | `1363:8560` | **Frame**, not an instance. Started from `products-and-services-two-column` and redesigned | **C** | Custom module or preset + heavy CSS, see note 2 |
| 08 | Testimonials | `1259:9068` | Rectangles and text copying the Elevate slider, sample content | **B** | Elevate **TestimonialSlider** |
| – | Pricing | `1259:9084` | **Instance** of `Elevate / Section / Pricing / pricing` | **A** | Elevate `pricing` preset |
| 03 | Problem + stats | `1355:8192` | Plain frames, background image, vector illustrations | **C** | Custom, see note 3 |
| – | FAQ | `1259:9108` | **Instance** of `Elevate / Section / FAQ / faq-v2` | **A** | Elevate `faq-v2` preset |
| 10 | Final CTA | `1259:9109` | Frame: hand-drawn vector background + a card frame named `Elevate · Card (variant 4) + custom CSS`; DS Button instances | **C (mixed)** | Elevate Card variant 4 on a section with a background image, plus CSS, see note 4 |
| 11 | Footer | `1259:9149` | Plain frames; Instagram and LinkedIn icon instances | **C, maps to globals** | Global footer: Logo, Rich text, Menu, Social follow, styled with CSS |

**Count:** 3 real components (Top Nav, Pricing, FAQ) · 2 Elevate stand-ins (Trust bar, Testimonials) ·
5 Figma designs (Hero, What you get, Problem + stats, Final CTA, Footer).

## What's overridden on the three real components

Checked from each instance's overrides list.

- **Top Nav:** no band-level changes.
- **Pricing:** text in every card, the band fill, and one element hidden (`1228:24`). All of these are
  editor or theme settings in HubSpot. Nothing needs code.
- **FAQ:** two text layers only.

## Notes on the C and B bands

1. **Trust bar.** The R3 plan mapped this to **FeatureList**; the layer names now say **Card ×3**. Neither
   gives three inline check + label items out of the box. Card adds padding and a border, FeatureList
   stacks. Pick one module and add the small CSS rule from R3 (one row, 28px check badge).
2. **What you get.** The real preset is a heading plus three full-width feature rows (1440 × 607). The
   design is two 568-wide cards, each with a header strip, a rule, an image and three features (1440 × 770).
   The preset can't do that layout. Also found:
   - The six icon layers are named after one icon but contain another: `Icon / briefcase` is **timer**,
     `contact` is **user-check**, `message-circle` is **messages-square**, `clock` is **pin**,
     `badge-dollar-sign` is **radar**. Only `file-check` matches. Build from the icons, not the names,
     and correct the list in `04_FINAL-DESIGN_Home-Page.md`.
   - The Job Seekers card image (`image 235`) is 563 tall inside a 440 card, so it is being clipped.
     Confirm the crop.
3. **Problem + stats.** Not a Metrics preset any more. It has a background image (`image 231`), three
   vector illustration groups, a two-line problem statement, a `WHAT'S AT STAKE` overline and four stats
   with a 40 × 4 accent bar each. The stats row alone could be Elevate **Metrics** with CSS for the bar;
   the illustrations and background need custom work. Copy: 88% · $58k+ · 723,000 · 90%.
4. **Final CTA.** The card is the Elevate part (Card variant 4: H2, subhead, two buttons **Post a job** and
   **Find work**). The background is drawn vector shapes (`Frame 174`), so export it as an image and set
   it as the section background in the editor. Blur and border on the card are CSS (R3).
5. **Footer.** Lives in the global footer, not on the page. Logo, copyright as Rich text, legal links as
   Menu, Instagram and LinkedIn as Social follow. Two legal text layers both say "Privacy" (open in `04`).

## Changes this makes to `04_FINAL-DESIGN_Home-Page.md`

- "What you get" is not a preset build. It moves from "Elevate preset" to custom work.
- Bands 03 and 10 are now read (above).
- Build note 2 there ("Hero is the only custom code") no longer holds. **What you get** and **Problem +
  stats** need custom work too, and the Final CTA and Footer need CSS.
