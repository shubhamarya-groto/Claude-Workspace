# Homepage R3 · built from HubSpot Elevate presets

Built 21 Sep 2026. Figma file **GofindBuild Website Redesign**, page **Marketing website**
(`1027:3073`), section **2026-09-21 · Marketing Site R3 · Homepage Hi-Fi · HubSpot Elevate
presets** (`1075:228`), at **x 5120, y 0**, 2176 × 7359. Round 2 (`1061:134`) is untouched at
x 2560.

R3 is a copy of R2, rebuilt band by band from Elevate's preset sections, then restyled to the
Built Bold design system and to the look of the Hi Fi flows (`823:4275`: hero variant B, the
welcome and trade picker screens, the auth screens). Brian's copy and R2's band order are
unchanged. Each band's note in the Figma rail carries the detail below.

Elevate's section and module names come from HubSpot's public source for the theme
(`github.com/HubSpot/cms-elevate-theme-public`), and its defaults from the theme's own settings
file, so every "from" value below is what HubSpot ships, not a guess.

---

## How to read the tags

| Tag | Meaning | Who and what |
|---|---|---|
| **[Theme]** | An Elevate theme setting | No code. Changed once in Edit theme settings |
| **[Editor]** | Page editor or global content | No code. Background images, menus, logo, card counts |
| **[CSS]** | A few lines of custom CSS in a child theme | Developer, small |
| **[Module]** | A custom module to build | Developer, the real work |
| **[Copy]** | Wording for Brian to approve | Brian |

---

## Band by band

| # | Band | Elevate preset | Modules | Look from Hi Fi |
|---|---|---|---|---|
| 00 | Top Nav | Site header (global) | SiteHeader | Unchanged DS Top Nav |
| 01 | Hero + fork | Hero banner, two column | Heading, RichText, Card ×2 with Buttons, linked_image replaced | B: stat pill, folder-tab photo, frosted card, orange + dark buttons |
| 02 | Trust bar | Features | FeatureList | B: orange check badges |
| 03 | Problem + stats | Metrics, centered | Heading, Metrics | Welcome screen's dark streak |
| 04–05 | How it works | Features, image column swapped for a second FeatureList | Heading, RichText, FeatureList ×2 | Soft card surfaces |
| 06 | Preview cards | **None.** Shell: Products and services, two column | 2 custom modules | Company-card treatment |
| 07 | Testimonials | Testimonial cards | Card ×2 (Elevate ships 3) | Orange voice tags |
| 08 | Pricing (soft) | Pricing | PricingCard ×3 | Unchanged from R2 |
| 09 | FAQ | FAQ v2, lighter | Heading, Accordion | Unchanged from R2 |
| 10 | Final CTA | Call to action, centered | Card | Auth screen's orange waves + frosted card |
| 11 | Footer | Site footer (global) | Menu ×3, logo | Unchanged from R2 |

### 00 · Top Nav
- [Editor] Logo as an image, so the Source Serif 4 wordmark renders exactly.
- [Editor] Menu: Companies · Job Seekers · Pricing, plus Login.
- [Theme] Header CTA uses the Primary button, fill `#F16C0E`. Pill is already Elevate's default.
- [Theme] Primary hover: Elevate's purple `#6854E8` → `#EA580C`, or `#F4811F` if the label goes navy (I-01).

### 01 · Hero + fork
- [Theme] H1: Elevate Inter 57 / 500 → Instrument Sans Medium 68 (Display 4xl).
- [Theme] Base colours: `#09152B` text and `#4F38E0` purple accent → navy `#16243D`, orange `#F16C0E`.
- [Theme] Secondary button: Elevate is outline-only → filled near-black `#0A1612` (Find jobs).
- [Theme] Tag, for the stat pill: `#E5F0FF` / `#063E95` blue → `#FDEDDF` with orange text.
- [CSS] Arrow disc inside buttons. Not in Elevate's Button module.
- [CSS] Orange accent on "and workers meet", a colour class inside the RichText.
- [Module] Hero visual: folder-tab photo mask plus frosted card. linked_image can't do either.
- Photo is Brian's welder shot, uploaded. The frosted card's rows now read Indianapolis, IN.

### 02 · Trust bar
- [Module setting] FeatureList icon: a check in a 28px orange-tinted square.
- [CSS] Three items in one row, if FeatureList stacks them.
- [Theme] Text: Inter Medium 15.
- [Editor] White background, so it reads as the foot of the hero. R2 had a grey strip.

### 03 · Problem + stats
- [Theme] Dark section 1: `#09152B` → black-brand, text white, captions white 64%.
- [Editor] Section background image: the welcome screen's dark streak, 55% dark overlay.
- [Theme] Metric numbers in Instrument Sans.
- [Theme] Dark-section accent → orange/280 `#FFBA6B` for WHAT'S AT STAKE.
- [CSS] 40 × 4 orange rule above each number.
- [CSS] Two-tone problem statement.

### 04–05 · How it works
- [CSS] Soft card behind each column: blue/0, radius border-radius/3xl, padding spacing/10.
- [CSS] Numbered navy discs instead of FeatureList icons, or upload 1 · 2 · 3 as icon images.
- [CSS] Equal header heights, so step 1 sits beside step 1. **Fixes I-17.**
- [Theme] H2 in Instrument Sans (Display 3xl 48).

### 06 · Preview cards
- [Module] Job Seeker preview card and Job Match Card, both as custom modules with fields.
  Static examples: live results need a connection to the GoFindBuild app.
- [Copy] Captions say whose view each card is (I-07): What companies see · What workers see.
- **[Copy] PROPOSED, not Brian's:** heading "Every match works both ways." and subhead
  "What a company sees, and what a worker sees." Brian wrote no heading for this band.

### 07 · Testimonials
- [Editor] Three cards → two.
- [Theme] Card variant 1: fill blue/0, border `#D9D9D9` instead of `#D3DAE4`, radius 24.
- [Theme] Voice tags: Elevate grey `#647390`, 12 / 800 → orange/500 `#BB5B09` (4.55:1, AA).
- [Editor] Avatars stay placeholders until Brian supplies them.

### 08 · Pricing (soft)
- [Theme] Featured card = Card variant 4: `#18233B` → navy `#16243D`.
- [Theme] Prices in Instrument Sans.
- [Module setting] PricingCard ships with a button per card. R2 has none: add CTAs or switch them off.

### 09 · FAQ
- [Theme] Accordion rows: filled rounded card → no fill, bottom border only.
- [Theme] Questions in Inter Medium 15.
- [Module setting] Chevron: Lucide chevron-down.

### 10 · Final CTA
- [Editor] Section background image: the auth screen's orange waves, 20% dark overlay.
- [Theme] Card variant 4 → translucent dark with a white 16% border.
- [CSS] Background blur on the card.
- [Theme] Secondary button in dark sections: filled near-black + 1.5px white border.
- [Theme] Heading white, subhead white 64%.

### 11 · Footer
- [Editor] Two new Menu modules for `/hire/{trade}` and `/jobs/{trade}`.
- [Theme] Links navy, underline on hover.
- Later: drive the trade lists from HubDB, so GTM adds a trade by adding a row.

---

## Elevate defaults that change

From the theme's settings file. These are the theme-settings pass, done once.

| Setting | Elevate default | GoFindBuild |
|---|---|---|
| H1 | Inter 57 / 500 | Instrument Sans Medium 68 |
| H2 | Inter 43 / 600 | Instrument Sans SemiBold 48 |
| Body | Inter 18 | Inter 16 to 18, unchanged family |
| Base colour 2 (light surface) | `#F7F9FC` | `#F6F7F9` |
| Base colour 3 (text) | `#09152B` | `#16243D` |
| Accent 1 | `#F4F2FF` | `#FDEDDF` |
| Accent 3 | `#4F38E0` purple | `#F16C0E` orange |
| Primary button hover | `#6854E8` | `#EA580C`, or `#F4811F` with a navy label |
| Secondary button | outline, 2px | filled `#0A1612` |
| Card border | `#D3DAE4` | `#D9D9D9` |
| Card variant 4 fill | `#18233B` | `#16243D` |
| Tag | `#E5F0FF` / `#063E95` | `#FDEDDF` / orange |
| Caption | `#647390`, 12 / 800 | orange/500 `#BB5B09` where used as a tag |
| Form placeholder | `#7D8CA5` | `#525C70`, for the sub-pages' search fields |

**What it takes, in one line each:** one theme-settings pass; a handful of page-editor settings;
roughly eight small CSS rules; **three custom modules** (hero visual, Job Seeker card, Job Match
Card). The modules are the part that decides the one-week estimate.

---

## Found while building

1. **Hi Fi B's frosted card uses Satoshi and SF Pro.** Neither is in the design system, and SF Pro
   is Apple's system font, which can't be licensed as a web font. Fixed in R3 (now Inter). B
   itself still has them.
2. **Typos in B:** "Verifed" four times, "Autin, TX", "6yrs". Fixed in the R3 copies, still in B.
3. **The warm-glow image doesn't survive a wide band.** It's portrait, so filling a 1440-wide band
   crops to its bright orange middle and pushes white captions below AA. Band 03 uses the dark
   streak instead.
4. **Hover colour with the I-01 fix.** With a navy label on orange, the DS's darker hover `#EA580C`
   drops the label to 4.36:1. The hover has to go lighter: `#F4811F` holds 5.9:1.
5. **I-09 withdrawn.** Brian's mockup does put "and workers meet" in orange. R2 was right.

## Still open

I-01 orange label contrast · I-02 fork labels differ from the final CTA · I-03 testimonial order ·
I-07 preview cards' action counts · I-12 pricing model · I-14 nav labels · band 08 heading
describes the agency comparison, not the tiers · PricingCard buttons · band 06 proposed copy.
