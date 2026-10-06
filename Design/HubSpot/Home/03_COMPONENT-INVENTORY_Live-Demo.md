# What the live demo is actually built from

Page: **https://247469662.hs-sites-na2.com/demo**, read in the browser on 23 Sep 2026.

**32 modules in total: 26 Elevate theme presets, 5 HubSpot default modules, 1 custom-coded module.**
Only the hero is code. Everything else is a theme preset with content typed into it.

How each one was identified: every HubSpot module loads its own stylesheet, and the path says where
it comes from. Theme modules load from the Elevate theme bundle, HubSpot's own modules load from
HubSpot's shared portal, and a module built for this portal loads from this portal's own module
assets. The class names on the markup confirm it (`hs-elevate-…`, `hs-logo-grid`, `gfb-…`).

---

## 1. Custom-coded: one module

| Component | Where | Evidence |
|---|---|---|
| **GFB Hero** (headline, fork cards, both buttons, the photo) | Band 01 | Stylesheet `module_GFB_Hero.min.css` served from this portal's own module assets (module id `398585349876`), markup classes `gfb-hero__title`, `gfb-hero__lede`, `gfb-fork__card`, `gfb-btn--primary`, `gfb-btn--navy`, `gfb-hero__photo` |

Three things about it worth knowing:

- **The photo is a background image, not an image element.** It points at
  `res.cloudinary.com/rm6jyi4n/…/Screenshot_2026-09-21_at_4.54.35_PM.png`, **2,789 KB**, hosted
  outside HubSpot. The "Skilled workers nearby" card is baked into that screenshot, so its text is
  not real text on the page.
- **It loads its own fonts.** The module pulls Instrument Sans and Inter from Google Fonts itself,
  on top of the fonts the theme already loads.
- Everything else in the hero is real text and real buttons, so only the visual needs replacing.

---

## 2. Native Elevate theme modules: 26

| Band | What you see | Elevate module | Count |
|---|---|---|---|
| 00 | Nav: logo, menu, Get started, mobile menu | **Site header** | 1 |
| 03 | "About us" | **Rich text** | 1 |
| 03 | "Elevate Your Online Presence" | **Heading** | 1 |
| 03 | The paragraph under it | **Rich text** | 1 |
| 04 | The four stats (88%, $58k+, 723,000, 90%) | **Rich text**, one per stat | 4 |
| 05 | "Better opportunities. Better workers." | **Heading** | 1 |
| 05 | "One construction network." | **Heading** | 1 |
| 05 | "Finding the right worker…" | **Rich text** | 1 |
| 06 | How it works, the two dark columns | **Card**, variant 4, 2 cards in one module | 1 |
| 07 | "Every match works both ways." | **Heading** | 1 |
| 07 | "What company sees, and what a worker sees." | **Rich text** | 1 |
| 07 | The two preview cards (still Elevate's "Content Creation" samples) | **Card**, variant 1, 2 cards in one module | 1 |
| 08 | "What our members say" | **Heading** | 1 |
| 08 | The testimonial slider (still Elevate's sample quotes) | **Testimonial slider** | 1 |
| 09 | Pricing, three tiers ($49, $149, Custom) | **Pricing card**, 3 cards in one module | 1 |
| 10 | Jump target above the FAQ | **Anchor** | 1 |
| 10 | "Frequently asked questions" | **Heading** | 1 |
| 10 | The FAQ rows (still Elevate's marketing-agency questions) | **Accordion** | 1 |
| 11 | Jump target above the final CTA | **Anchor** | 1 |
| 11 | "The Right connection could change everything." | **Card**, variant 4, 1 card | 1 |
| 12 | Footer menu | **Menu** | 1 |
| 12 | Footer social icons | **Social follow** | 1 |
| 12 | Footer legal line | **Rich text** | 1 |

Counted by type: Rich text 9 · Heading 6 · Card 3 · Anchor 2 · Site header 1 · Testimonial slider 1 ·
Pricing card 1 · Accordion 1 · Menu 1 · Social follow 1.

---

## 3. Native HubSpot default modules: 5

These ship with HubSpot itself, not with the theme. They load from HubSpot's shared module portal.

| Band | What you see | Module |
|---|---|---|
| 02 | The stray SNACKZO logo strip under the hero | **Logo grid** |
| 12 | Footer logo | **Logo** |
| 12 | Two spacing blocks in the footer | **Spacer** ×2 |
| 12 | The footer's horizontal rule | **Divider** |

---

## 4. Two things found while checking

### The whole page is inside the global header

Every section, from the hero to the final CTA, sits inside
`@hubspot/elevate/templates/partials/header.hubl.html`, which is a **global** partial. The page's own
content area is empty:

```
<main id="main-content"><div class="hs-container-root" data-hs-grid-root-id="dnd_area"></div></main>
```

A global partial repeats on every page that uses it. As soon as a second page is published from this
theme, the entire homepage would appear at the top of it, above that page's own content. So this has
to be moved into the page's content area before the Job Seeker and Company pages are built, and it
also explains the SNACKZO logo and the Elevate sample sections: they are leftovers sitting in a
shared header, not on the page.

### What this means for the two new pages

Every band on the homepage is a theme preset with content typed in. The only code on the page is the
hero. For the Job Seeker page, the same holds true except for two components that no Elevate preset
covers:

| New component | Why a preset can't do it |
|---|---|
| **Search bar** (trade typeahead + ZIP + button) | The theme has no form-style module with a typeahead and no way to build a link out of two fields |
| **Job card** | The Card module can't carry pay, distance, posted date and a trade tag in that arrangement |

Everything else on the Job Seeker page maps to modules already proven on this page: Site header,
Heading, Rich text, Card, Testimonial slider, Accordion, Menu, Social follow, Logo, Divider, Spacer.

Also worth fixing while in there: each stat's orange rule is a stretched PNG (`Rectangle 6667419`,
29 × 3 shown at 59 × 6) inside a rich text module. A CSS border does that job at no weight.

---

Related: `02_SITE_Changes-Needed-Home-Page.md` (the fix list for this same page) and
`01_R3_HubSpot-Elevate-Mapping.md` (which preset each band was meant to use).
