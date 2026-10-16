# GFB team landing pages · context for bringing them into the approved design

16 Oct 2026. The GFB team built new landing pages in the GoFindBuild HubSpot portal and asked us to check them and bring them into the last approved design. This file is the context for that work: what the new pages are, what the approved build is, and where the two differ. Read from the portal through the HubSpot connector (module structure and field values). Not read: rendered screenshots, the live CSS of the one-off modules.

## The portal

- **GoFindBuild**, portal `47303551`, theme `@hubspot/elevate`. Preview domain `47303551.hs-sites.com`.
- This is the real GFB portal, not the 1 Meter House test portal (`247469662`) that `../00_BUILD-PLAN_Staging.md` names. The approved build now lives here too.

## The approved build (the reference)

Four website pages, built from the final Figma frames (section `1259:8836` on the Presentation page of `aC59gtTG9nh2hwUraPnCXj`) as **17 `gfb_*` custom modules** (`/custom/content-mcp/modules/gfb_*`).

| Page | Content ID | URL | Modules, in order |
|---|---|---|---|
| GFB Home (staging) | `223806550529` | `/home-staging` | not read here |
| GFB Companies (staging) | `223986607632` | `/companies-staging` | top_nav · hero_v2 · match_cards · checklist · search_match · **worker_card** · features · faq · final_cta · footer |
| GFB Job Seekers (staging) | `224337738564` | `/job-seekers-staging` | top_nav · hero_v2 · match_cards · checklist · search_match · **job_card** · features · faq · final_cta · footer |
| GFB About Us (staging) | `224339429033` | `/about-us-staging` | not read here |

**The `gfb_*` module set** (this is the approved kit in HubSpot): `gfb_top_nav`, `gfb_hero_v2`, `gfb_trust_bar`, `gfb_what_you_get`, `gfb_match_cards`, `gfb_checklist`, `gfb_search_match`, `gfb_worker_card`, `gfb_job_card`, `gfb_features`, `gfb_problem_stats`, `gfb_testimonials`, `gfb_pricing`, `gfb_faq`, `gfb_alt_rows`, `gfb_final_cta`, `gfb_footer`. There is also an older `/GFB Hero` (3 fields) from the first demo, which `gfb_hero_v2` replaces.

The approved pages run on a single `main` section with no Elevate header or footer partials. Every band is a `gfb_*` module.

## The new GFB team pages

All are **landing pages** on the Elevate `lp-header` / `footer` partials, built mostly from **one-off modules** (`gofindbuild_*`, `indy_skilled_trades_signup_20260929_*`) plus HubSpot defaults and hand-coded rich text.

| Page | Content ID | URL | Audience |
|---|---|---|---|
| LP-20261007-INDY-EmployerSignup-**Plumbing**-STAGING | `223867638545` | `/indy-plumbing-company-signup-staging` | Plumbing companies, Indianapolis |
| LP-20261007-INDY-EmployerSignup-**HVAC**-STAGING | `224521894575` | `/indy-hvac-company-signup-staging` | HVAC companies, Indianapolis |
| LP-20261006-**PS-JobSeekerSignup**-STAGING | `223769972131` | `/in-ps-jobseeker-signup-staging` | Paid-search job seekers |
| LP-20260930-PaidSearch-GoogleAds-JobSeeker-IN | `223273632560` | `/en/gofindbuild-find-local-construction-and-trade-job` | Google Ads job seekers (older, 30 Sep) |
| Signup Preview: Development / Staging / Employer-Staging | `223266017870` / `223632122124` / `223844483457` | `/signup-preview…` | Form previews; **not read** |
| Terms and Conditions / Privacy Policy | `223273637948` / `223273639762` | `/gofindbuild-terms-…`, `/gofindbuild-privacy-policy` | Legal; the footer links to these |

The list comes from content analytics since 1 Sep, so a page with no views would not appear. Ask the GFB team if any are missing.

### Band order per page

**Plumbing** (the most migrated: someone has already started swapping in `gfb_*` modules)
| Row | Module | Notes |
|---|---|---|
| 0 left | `indy_…_hero` + `@hubspot/linked_image` | Eyebrow, H, body, 3 stats ("Plumbing / Local / Your choice"), AI-generated photo |
| 0 right | rich text `{{ company.fcklmarketing_company_name }}` + rich text eyebrow + `@hubspot/form` | Personalised company name; eyebrow is inline Arial `#f57c00` |
| 1 | `gofindbuild_plumbing_company_benefits` | Heading, body, 3 cards |
| 2 | **`gfb_pricing`** | Free / Starter $0 + $49/$149/$349 per connection / Pro $249 a month |
| 3 | **`gfb_faq`** | **Placeholder answers** ("Write the answer here. Keep it short.") |
| 4 | `indy_…_faq` | A second FAQ, real answers. **Two FAQs on one page** |
| 5 | `@hubspot/rich_text` | Hand-coded "Why we built GoFindBuild" stats (94%, 723,000, $55k+, 90%) in inline styles |
| 6 | **`gfb_final_cta`** | Card layout, `show_gears: true` |
| footer | **`gfb_footer`** | Matches the approved footer |

**HVAC** (cloned from Plumbing *before* the `gfb_faq` / `gfb_final_cta` swaps)
Same rows 0–2, then `indy_…_faq` (row 3), hand-coded stats (row 4), `gofindbuild_gear_cta_editable_link` (row 5), `gfb_footer`.

**PS Job Seeker signup**
Row 0: `indy_…_hero` + image, beside the eyebrow and form · 1 `gofindbuild_paid_search_matching_example` · 2 `gofindbuild_privacy_centered_three_up` · 3 `indy_…_faq` · 4 `gofindbuild_gear_cta_editable_link` · footer `gfb_footer`.

**Google Ads Job Seeker (30 Sep)**
`indy_…_hero`, `gofindbuild_rounded_hero_image`, `gofindbuild_gear_cta_editable_link`, `gofindbuild_signup_form_anchor`, `gofindbuild_paid_search_matching_example`, `gofindbuild_privacy_centered_three_up`, `gofindbuild_compact_about_trust`, form, `indy_…_faq`. Footer is **Elevate `social_follow` + rich text + dividers**, not `gfb_footer`.

## Gaps against the approved design

### Structure and components
| New-page piece | Approved equivalent | Gap |
|---|---|---|
| Elevate `lp-header` with a logo only (`img.src` null, inherits the theme logo) | `gfb_top_nav` | No nav. Possibly intended for paid LPs (no exits). **Decision needed** (below) |
| `indy_…_hero` + image + form in a 6/6 split | `gfb_hero_v2` | Approved hero has fork cards or checks and the cut-out welder photo, **no form**. There is no approved hero-with-form. **Decision needed** |
| `gofindbuild_plumbing_company_benefits` (3 cards) | `gfb_features` or `gfb_checklist` | One-off module |
| `gofindbuild_paid_search_matching_example` | `gfb_search_match` + `gfb_job_card` | One-off; the approved band 05 is the 3-component search → match |
| `gofindbuild_privacy_centered_three_up` | `gfb_checklist` / `gfb_features` | One-off |
| `gofindbuild_compact_about_trust` | `gfb_trust_bar` or `gfb_alt_rows` | One-off |
| Hand-coded stats rich text | `gfb_problem_stats` | Inline styles, Inter for the 48px numbers (approved display font is Instrument Sans), not editable as fields |
| `indy_…_faq` (4 fixed Q/A fields) | `gfb_faq` | One-off; Plumbing carries both |
| `gofindbuild_gear_cta_editable_link` | `gfb_final_cta` | One-off |
| Elevate social_follow footer (Google Ads page) | `gfb_footer` | Old footer |
| `gfb_pricing`, `gfb_faq`, `gfb_final_cta`, `gfb_footer` | same | Already approved modules |

### Tokens and accessibility
- **Primary button label is white** in these pages' theme settings (`primary_button.default_state.text_color #ffffff`, hover `#f4811f` with white). Approved: **navy `#16243D` label on orange** (5.09:1); white on orange fails AA (I-01, I-18). Check whether the approved staging pages override this inside the `gfb_*` modules, or whether the theme is still wrong for everything.
- Eyebrows use inline **Arial** and **`#f57c00`**, which are not Built Bold tokens (Inter, orange `#F16C0E`).
- Inline hex and font styles in rich text throughout (stats band, eyebrows). The approved rule is no one-off edits inside a band.
- Logo in the LP header has `alt: null`; the header logo is rendered as an `h1` (`heading_level: h1`), which competes with the page H1 (QA: one H1 per page, `H-24`).
- **Gear watermarks** on the final CTA (`show_gears: true` and the gear CTA module). Iteration 1 called gears off-brand (A-21), but the approved About Us CTA also uses them. Confirm the approved stance before changing.
- **AI-generated photos** (`AI-Generated Media/Images/…`, 1536 × 1024 PNG/WebP). The approved design uses the welder photo; image weight not checked against the ~300 KB QA limit.
- Leading `&nbsp;` runs used to indent text (eyebrow, company name). Breaks on mobile.

### Content bugs (copy is held for the publish pass, but these are factual errors)
- **HVAC page says "Plumbing"**: hero stat 1 value, benefits card 1 and 2 bodies ("plumbing role", "your plumbing business"), FAQ Q3 ("plumbing candidates").
- Plumbing `gfb_faq` has template placeholder answers and duplicates the real FAQ below it.
- `gfb_pricing` buttons have **empty links**, and the pricing model is still open (I-12). Prices here ($49/$149/$349, Pro $249) differ from both earlier sets ($99/$199/$399; $49/$149/Custom).
- Forms redirect to **`http://www.google.com`** after submit (all employer and job seeker forms).
- Footer "About Us" points to `/about-us`; the approved page is at `/about-us-staging`, so this works only after launch slugs are set.

### Not design, but flag before anything ships
- **The PS Job Seeker page posts every form submission to an ngrok tunnel** (`https://cb97-76-200-116-200.ngrok-free.app/api/hubspot/signup-invites`) from an inline `<script>` in a rich-text module. That sends job seekers' personal data to a temporary developer machine. Raise it with Jeff and the GFB team; do not carry it into the rebuilt page.

## Decisions needed before the rebuild

1. **Nav on paid landing pages:** use `gfb_top_nav` (approved) or keep a logo-only header (common for ad pages)?
2. **Hero with a form:** add a form variant to `gfb_hero_v2`, or put the form in its own band below an approved hero?
3. **Pricing on employer LPs:** keep `gfb_pricing` with these numbers, or remove until I-12 is settled?
4. **Gears on the final CTA:** keep (approved About Us has them) or drop (Iteration 1)?
5. **Stats band:** move to `gfb_problem_stats`, with sources kept?
6. Scope: these four pages only, or also the Signup Preview pages?

## Suggested approach

Clone each page and rebuild it on `gfb_*` modules band for band (the Plumbing page shows the GFB team already started this), keeping their copy as placeholder. Fix the theme's primary button label once, which fixes every page. Rebuild HVAC from the finished Plumbing page so the plumbing copy leaks don't come back. Run the staging QA checklist in `../00_BUILD-PLAN_Staging.md` on each.
