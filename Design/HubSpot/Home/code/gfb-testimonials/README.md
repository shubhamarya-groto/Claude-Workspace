# GFB Testimonials

Home band 08. Figma: Home Page `1259:9027` → `1259:9068`. Read 7 Oct 2026.

Classified as **Template** in `../../05_SECTION-SPLIT_Code-vs-Template.md` (Elevate TestimonialSlider).
Built as a custom module on request, so its look follows the GoFindBuild design instead of Elevate's
slider styling. The Elevate slider remains the fallback.

| File | What |
|---|---|
| `fields.json` | Heading + repeater of 1 to 10 testimonials (default 5, Figma's placeholder copy) |
| `module.html` | HubL; carousel with ARIA roles, buttons, dashes |
| `module.css` | Styles; reads Elevate theme variables with GoFindBuild fallbacks |
| `module.js` | Arrows, dashes, keyboard. Without it the slides still swipe/scroll |
| `demo.html` | Static demo with the default content; open in any browser |

## Fields

| Field | Type | Notes |
|---|---|---|
| `heading` | Text | "What our members say" |
| `slides` | Repeater, 1 to 10 | One per testimonial; arrows and dashes hide when there is only one |
| ↳ `quote` | Text | |
| ↳ `name` | Text | |
| ↳ `role` | Text | Role or trade |
| ↳ `photo` | Image | Large photo, 322 × 300. Leave empty for a quote-only slide |
| ↳ `avatar` | Image | 80px round headshot; a person icon if empty |
| ↳ `link_label` | Text | "Read case study"; the link only shows when both label and link are set |
| ↳ `link` | Link | |

## Changes from Figma

- Figma still has Elevate's stock styling. Heading now uses the theme H2 font (Instrument Sans) and
  navy `#16243D` instead of Inter and `#09152B`.
- Link and arrow colour `#F6B26B` is about 1.9:1 on white, below the 4.5:1 minimum. Uses orange/500
  `#BB5B09` instead (the colour R3 chose for tags). Active dash uses brand orange `#F16C0E`.
- No autoplay (it moves content people are reading). Phones swipe; arrows hide below 768px.
- Copy is still placeholder: real quotes, names, photos and permission come at the publish pass.
