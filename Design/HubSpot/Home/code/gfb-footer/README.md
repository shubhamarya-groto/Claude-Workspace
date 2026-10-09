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
