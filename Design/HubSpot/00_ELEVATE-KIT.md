# HubSpot Elevate kit · what the theme actually ships

Read 25 Sep 2026 from the theme's own source, `github.com/HubSpot/cms-elevate-theme-public`
(`src/theme/elevate`). This is what the "Add to page" panel offers in the portal: the panel shows
the same set, the source gives the fields behind each one.

**Three tabs, three levels.** Layouts are empty column skeletons. Modules are the 20 building
blocks. Sections are 46 ready-made arrangements of those modules. Build the modules and you can
make any section.

---

## Layouts (6)

Column splits, nothing else: **1 · 2 · 3 · 1/3 : 2/3 · 2/3 : 1/3 · 4**.

## Modules (20)

| Module | Repeats | Its own options |
|---|---|---|
| **Accordion** | 1 to 20 rows, 3 by default | Icon chevron or plus · size small/medium/large · card style |
| **Anchor** | | Invisible jump target |
| **BlogListing** | | Card style, heading |
| **Button** | 1 to 2 buttons | Style, size, gap, alignment, optional icon left or right |
| **Card** | 1 to 4 cards | Image or icon · heading · rich text · buttons |
| **CountdownTimer** | | Filled or no fill |
| **FeatureList** | 1 to 20 features, **8 by default** | Heading, section style |
| **Heading** | | Heading level h1 to h6, heading style, alignment, section style |
| **ImageAndText** | | Image left or right · heading · rich text · buttons |
| **List** | 1 to 20 items, 4 by default | Section style |
| **MediaAndSummary** | | Card style |
| **Menu** | | Link style primary or secondary |
| **Metrics** | 1 to 4 metrics | Heading style, section style |
| **PricingCard** | 1 to 4 cards, each 1 to 20 features (5 by default) | Heading, buttons |
| **RecentBlogPosts** | | Heading |
| **RichText** | | Section style |
| **SiteHeader** | | Logo, menu, buttons. Global |
| **SocialFollow** | 1 to 10 links, 5 by default | |
| **SocialShare** | | Facebook, X, LinkedIn, Pinterest, email |
| **TestimonialSlider** | 1 to 20 quotes, 3 by default | |

## The four style systems every module draws from

These are shared, so they are the variants worth having in Figma.

| System | Options | Notes |
|---|---|---|
| **Section style** | `section_variant_1`, `2`, `3` (light), `4` (**dark**) | Sets the text colour context. This is how Elevate alternates light and dark bands |
| **Button style** | primary · secondary · tertiary · accent, in small · medium · large | 12 combinations. Our DS Button covers primary, secondary and tertiary |
| **Heading style** | display_1 · display_2 · h1 to h6 | Eight steps. Separate from the semantic heading level |
| **Card style** | variants set in theme settings (`group_elements.group_cards.card_variant_1`…) | Variant 4 is the dark filled card we use for the featured pricing tier |
| **Link style** | primary_links · secondary_links | |

## Sections (46)

Ready-made arrangements. Useful as a menu of what can be dropped in without any build:

about-us · about-us-one-column · call-to-action · call-to-action-centered ·
call-to-action-two-column · two-column-call-to-action · contact · countdown · faq · faq-v2 ·
faq-v2-dark · faq-two-column · features · form-two-column · gallery · gallery-simple ·
heading-with-three-cards · hero-banner · hero-banner-centered · hero-banner-centered-dark ·
hero-banner-two-column · hero-banner-two-column-text · hero-video-two-column · logo-gallery ·
metrics · metrics-centered · multi-row · multi-row-alternating · newsletter · one-column-image ·
pricing · pricing-dark · pricing-four-column · products-and-services ·
products-and-services-list · products-and-services-two-column ·
products-and-services-three-column · products-and-services-three-column-dark ·
products-and-services-video-list · recent-blog-posts · team-members · team-members-dark ·
team-members-two-column · testimonial · testimonial-cards · video

**Worth noting: there is an `about-us` section preset.** The About Us page built on 25 Sep does not
use it, and should be checked against it before the HubSpot build.

---

## How this maps to the Figma kit

Built 25 Sep 2026 on a new page, **HubSpot Elevate kit** (`1215:3`), in `aC59gtTG9nh2hwUraPnCXj`.
Styled to Built Bold rather than Elevate's stock purple and Inter, because the point is to assemble
GoFindBuild demos. Everything is bound to the design system's variables and text styles.

**All 26 are real components**, named so they group in the assets panel:
`Elevate / Layout / …` (6) and `Elevate / Module / …` (20). Drag an instance, fill it in.

Where the design system already has the component, the kit reuses it instead of drawing a second
one: **SiteHeader** is the DS Top Nav `790:11423`, **Button** is the DS Button `787:10782`.

| On the page | Where |
|---|---|
| Layouts, 6 | x 0 |
| Heading, RichText, Button, Anchor, List | x 1520 |
| Card, Metrics, Accordion | x 3040 |
| FeatureList, ImageAndText, MediaAndSummary | x 4560 |
| PricingCard, TestimonialSlider, Menu | x 6080 |
| SiteHeader, BlogListing, RecentBlogPosts | x 7600 |
| SocialFollow, SocialShare, CountdownTimer | x 9120 |

Each module sits at Elevate's real **1200 container width**, with its name and its actual field
options written above it, and at its real default item count: FeatureList shows eight features,
Accordion three rows, TestimonialSlider three quotes, List four items.

## Sections in Figma

Built 25 Sep 2026 on the page **HubSpot Elevate sections** (`1226:3`), same file. **All 46**, each
as a component named `Elevate / Section / <category> / <preset>`, so the assets panel groups them
the way the "Add to page" panel does.

Each is a real **1440 band** with the 1200 container inside it, built at the column split the theme
declares, and carrying the preset's own light or dark treatment. Six columns on the canvas:

| Column | x | What |
|---|---|---|
| Hero, 6 | 0 | |
| Call to action 4, FAQ 4 | 1600 | |
| Pricing 3, Social proof 6 | 3200 | |
| Products and services, 10 | 4800 | |
| Team and about 5, Events 1 | 6400 | |
| Forms 3, Media 4 | 8000 | |

**Every section is assembled the way HubSpot assembles it**, so a page built from these in Figma
maps one to one onto a page built from the presets in the editor.

## Not built yet

- **Dark variants of the modules.** Every module has a section style, and `section_variant_4` is
  the dark one. The module kit is light only, though the dark section presets show what it looks
  like.
- **Button variants.** Elevate has 4 styles x 3 sizes. The kit shows primary and secondary at
  medium; the DS Button covers the rest.
- **An input component.** The form presets draw their fields. The design system still has no input
  component (I-13), and these three presets are the argument for building it.

## The answer to "can our button be the default everywhere"

Yes, and it needs no code. Every module that draws a button imports the same `ButtonStyle` field
from the theme's shared field library: four styles by three sizes. What each style **looks like**
is defined once in **theme settings**, so setting ours as `primary` changes every button in every
module and every section at once, including the ones inside Card, PricingCard, ImageAndText,
SiteHeader and all the hero and CTA presets.

Two caveats. The **variant stays an editor's choice** per module, so if you want to stop someone
picking badly, lock the field in a child theme. And **replacing the Button component itself** means
forking the theme, which costs you clean upgrades and buys nothing the setting does not.

The same is true of `HeadingStyle`, `CardStyle`, `LinkStyle` and `SectionStyle`. Which is also the
real shape of the I-01 fix: navy label on orange is **one theme setting**, and it corrects every
button on every page at once.
