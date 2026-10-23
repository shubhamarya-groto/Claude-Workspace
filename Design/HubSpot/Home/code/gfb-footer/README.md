# GFB Footer

Home band 11. Figma: Home Page `1259:9027` → `1259:9149` (`11 · Footer + browse by trade`; there are no
trade columns in the final design). Read 7 Oct 2026. Exact Figma copy as defaults. Built as code on request;
the Elevate global footer (Logo, Rich text, Menu, Social follow) stays the fallback.

> **Live in HubSpot (7 Oct 2026):** created through the connector as **GFB Footer**, path `custom/content-mcp/modules/gfb_footer` (GoFindBuild 47303551). CSS inlined in the HTML. Update it through the connector, not the Design Manager.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy and GoFindBuild links |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks |
| `demo.html` | Static demo |

## Fields

| Field | Type | Notes |
|---|---|---|
| `brand_text` | Text | "GoFindBuild", Source Serif 4 SemiBold 24 (loaded by the module when no logo image is set) |
| `logo_image` | Image | Optional; replaces the logo text (shown 33px tall) |
| `brand_link` | Link | `/` |
| `copyright` | Text | "© 2026 GoFindBuild. All rights reserved." Update the year each January |
| `legal_links` | Repeater, 0 to 6 | `link_text` + `link` |
| `socials` | Repeater, 0 to 6 | `network` (Instagram, LinkedIn, Facebook, X, YouTube, TikTok) + `profile_url`. Opens in a new tab |

## Links set by default

| Item | Link | Source |
|---|---|---|
| Terms and conditions | `/gofindbuild-terms-and-conditions` | Published in the GoFindBuild portal (`04_FINAL-DESIGN` build note 6) |
| Privacy policy | `/gofindbuild-privacy-policy` | Same |
| About Us | `/about-us` | **Not confirmed.** Check the About Us page's slug and pick it in the link field |
| Instagram | `https://www.instagram.com/gofindbuild` | Current site's footer |
| LinkedIn | `https://www.linkedin.com/company/gofindbuild` | Current site's footer |

Facebook is left out, as in Figma (the old site had it). Fixes H-16 (social icons pointing at network home pages).

## From Figma

White band, 1px `#D9D9D9` top rule, padding 96 all round. Row: brand block left, actions right, both on
the bottom line. Logo `#16243D`, 16 above the copyright (Inter 14 / 1.5 `#525C70`). Links Inter 14 / 1.5
`#16243D`, 20 apart; 20 to the socials. Social buttons 40 × 40, white, 1px `#D9D9D9` ring, radius 20,
24px icon `#111111`, 20 apart. Built size: 1440 × 262 (Figma 263); actions at x 888 (Figma 887), 456 wide.

## Notes

- Icons are Lucide outlines (Figma uses the Lucide `instagram` and `linkedin` components).
- Hover: links underline in `#BB5B09`; social buttons get a navy ring and a light fill.
- Tablet and phone: brand, links and socials stack, left aligned.
- In Figma the About Us layer is named "Privacy" (the "two Privacy layers" note in `04`); its text is About Us.
- To use it on every page, place it in the site footer (global partial) rather than on each page.

## Logo (14 Oct 2026)

The logo comes from code, so every page gets it without setting a field: the Logo image field if set, else the portal's brand logo (`brand_settings.primaryLogo`, Settings > Branding), else the brand-kit file `FullLogoColored-01.png` in HubSpot Files. Change the brand logo in Settings and every page follows. The text logo is the last fallback.

## Staging and live addresses (14 Oct)

The module code holds one list, **SITE ADDRESSES** (`gfb_pages`, top of `module.html`), pairing each page's live
address with its staging copy: `/` → `/home-staging`, `/companies` → `/companies-staging`, `/job-seekers` →
`/job-seekers-staging`, `/about-us` → `/about-us-staging`. The link fields keep the **live** addresses.

- On a staging page (the address being viewed is in the staging column), links to those pages go to the staging
  copies, so reviewers stay on staging.
- On any other page, the live site included, links stay as typed. **Nothing needs changing at launch**: publish
  the pages at their live addresses and the links follow.
- The nav link for the page being viewed gets the orange underline (`aria-current="page"`), on staging and live.
- Add a row when a new page gets a staging copy (Login / Sign up later). GFB Top Nav and GFB Footer each carry the
  list: change both.

## Landing-page fixes (23 Oct)

- **Staging links on any staging page:** a page counts as staging when its address is in SITE ADDRESSES
  **or contains `-staging`** (e.g. `/indy-plumbing-company-signup-staging`), so the footer's About Us link there
  goes to `/about-us-staging` instead of the live `/about-us` (404 until launch).
- **Full bleed in a boxed container:** the Elevate landing-page footer partial is boxed and padded. The footer now
  breaks out to the full viewport width and zeroes the padding, margins and top rule of the wrappers around it
  (never a wrapper that holds `main`). `html { overflow-x: clip }` stops the 100vw band adding a sideways scroll.
- `module.live.html` is exactly what was sent to HubSpot (module.html + module.css inlined).
