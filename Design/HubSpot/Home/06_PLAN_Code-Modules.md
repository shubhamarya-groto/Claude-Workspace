# Home page · plan for the two Code modules

Written 6 Oct 2026. Covers the two bands that no template can produce (`05_SECTION-SPLIT_Code-vs-Template.md`):
**01 · Hero + fork** and **What you get**. Goal: built in code, but placed and edited in the HubSpot page
editor like any template module, with no developer needed to change copy, images, links or item counts.

## Sources

`developers.hubspot.com` is blocked from this session's network, so the plan is built from HubSpot's own
public code and the docs' search summaries:

- **Elevate theme source**, `github.com/HubSpot/cms-elevate-theme-public` (cloned 6 Oct): theme.json,
  templates, sections, and the CSS variables its theme settings produce.
- **HubSpot CMS boilerplate**, `github.com/HubSpot/cms-theme-boilerplate`: the official example of
  classic modules (`meta.json`, `fields.json`, `module.html`, `require_css` + `scope_css`, repeaters).
- **HubSpot CLI** on npm, `@hubspot/cli` **8.15.0** (latest on 6 Oct).
- Docs pages, read through search summaries: Coding custom modules (`/docs/reference/cms/modules/files`),
  Module and theme fields (`/docs/cms/reference/fields/module-theme-fields`), Child themes
  (`/docs/cms/start-building/building-blocks/themes/child-themes`), Default themes, CMS CLI commands
  (`/docs/developer-tooling/local-development/hubspot-cli/commands/cms-commands`), page editor best
  practices (`/docs/cms/best-practices/content-editing/page-editor`), HubL standard tags.

Before building, open those docs pages in a normal browser and confirm the points marked **(verify)**.

## Five facts the plan rests on

1. **Elevate's own modules are React, inside a project-based theme.** Elevate doesn't show in the Design
   Manager, and its modules can't be edited there. Adding a module *to* Elevate means forking the theme.
   We don't. We add **our own classic HubL modules** next to it.
2. **Elevate's templates are open drag-and-drop areas.** `home.hubl.html` is one `dnd_area "dnd_area"`.
   Any module with `host_template_types: ["PAGE"]` and `is_available_for_new_content: true` shows up in the
   editor's **Add → Modules** panel and drops into those areas, next to Elevate's modules. That is how the
   current GFB Hero (module id `398585349876`) already sits on the demo page.
3. **A module is editable only through its `fields.json`.** Anything written straight into `module.html`
   is frozen. The current GFB Hero is all hard-coded (headline, both cards, buttons, links set to `#`,
   photo URL placeholder), so **an editor can change nothing in it today**. That's the main fix.
4. **Elevate's theme settings come out as CSS variables** (`--hsElevate--…`), set on every page. A custom
   module that reads them changes when the theme settings change, just like Elevate's modules. Examples
   from the source: `--hsElevate--h1__font`, `--hsElevate--h1__fontSize`, `--hsElevate--body__font`,
   `--hsElevate--button--primary__backgroundColor`, `--hsElevate--button--primary__textColor`,
   `--hsElevate--button--primary__borderRadius`, `--hsElevate--card--variant1__borderColor`,
   `--hsElevate--card--variant1__borderRadius`, `--hsElevate--spacing--24`.
   Elevate's button *classes* are CSS-module hashed (`styles['hs-elevate-button']`), so we can't reuse
   them; we reuse the **variables**.
5. **CLI 8 moved CMS commands under `hs cms`.** It's `hs cms module create`, `hs cms upload`,
   `hs cms watch`. The old `hs upload` / `hs watch` no longer work.

## Decision: where the modules live

**A child theme of Elevate, "GoFindBuild", in this repo, uploaded with the CLI.**

| Option | For | Against |
|---|---|---|
| **Child theme (chosen)** | One place for both modules, the mobile CSS (build plan step 3) and the theme-settings overrides. Docs: modules built in a child theme aren't affected by the parent. Version-controlled in git | Pages must be created on the child theme **(verify on staging that the child theme lists Elevate's templates and sections)** |
| Loose modules in Design Manager (today's GFB Hero) | Already works; usable in any theme | Code edited in the browser, no git history; the mobile CSS has to live somewhere else anyway |

If the child-theme check fails, fall back to loose modules in a `GoFindBuild/` Design Manager
folder. The module code is identical either way; only the upload path changes.

## Repo layout

```
Design/HubSpot/code/gofindbuild-child/        ← uploaded as the child theme
├── theme.json                                 "extends": "@hubspot/elevate" (verify exact parent path)
├── child.css                                  mobile rules, small preset CSS from R3 (accent bars, trust-bar row)
└── modules/
    ├── gfb-hero.module/
    │   ├── meta.json
    │   ├── fields.json
    │   ├── module.html
    │   └── module.css
    └── gfb-what-you-get.module/
        ├── meta.json
        ├── fields.json
        ├── module.html
        └── module.css
```

**Update 6 Oct:** the GFB Hero is being built in the **Design Manager** for now (module `GFB Hero`, folder
in the portal, content types Site pages + Landing pages). Its paste-in code and field setup are in
`Home/code/gfb-hero/` (`README.md`, `module.html`, `module.css`). The field list there replaces the
hero field table below: the two fork cards are two fixed groups, not a repeater, because the Design
Manager can't give each repeater item its own default copy.

## Rules both modules follow

| Rule | How |
|---|---|
| Every visible word, image, link and count is a field | Nothing editable lives in `module.html` |
| Defaults = the Figma copy | `fields.json` `default` values, so a fresh drop already looks like the design |
| Inline editing where the docs allow it | `{% inline_text field="…" value="{{ module.… }}" %}` for one-line text, `{% inline_rich_text %}` for rich text: editors type on the page, not only in the sidebar |
| Repeaters, not fixed copies | `type: "group"` with `occurrence` (`min`, `max`, `default`, `sorting_label_field`) |
| Links are link fields | `type: "link"`, rendered with `href`, `open_in_new_tab` → `rel="noopener"`, `no_follow` → `rel="nofollow"` (the boilerplate button pattern) |
| Images are image fields | `type: "image"` gives the File Manager picker and a required alt text. Rendered as `<img>`, not a CSS background, so alt text and `loading` work |
| Look comes from theme settings | Colours, fonts, radii read `var(--hsElevate--…, <Figma fallback>)`. **No Google Fonts link in the module**; fonts load once, from the theme |
| Styles scoped | `{% require_css %}` + `{% scope_css %}` for any field-driven CSS; static CSS in `module.css` under a `.gfb-…` root class |
| Safe output | `|escape_attr` on attributes, `|escape_url` on URLs, `|sanitize_html` on rich text |
| Help text on fields | `help_text` on every field, so the editor sidebar explains it |
| Breakpoint | Elevate's mobile breakpoint is `max-width: 767px` (`theme.json`); use the same |

## Module 1 · GFB Hero

**Figma:** `1259:9031` (copy `1259:9032`, visual `1259:9044`). **Replaces** the hard-coded module on the demo.

`meta.json`: `label` "GFB Hero", `host_template_types` `["PAGE"]`, `is_available_for_new_content` true,
`global` false, `categories` `["body_content"]`, `icon`.

`fields.json`, Content tab:

| Field | Type | Notes / default |
|---|---|---|
| `headline` | text | "Where construction businesses and workers meet". Rendered as the page's **one H1** |
| `headline_highlight` | text | "and". The module wraps the first match in the orange accent span, so editors never touch HTML |
| `subhead` | text | Current lede |
| `fork_cards` | group, `occurrence` min 1, max 2, default 2, sorting label `title` | One card per audience |
| ↳ `title` | text | "I'm hiring" / "I'm looking for work". Rendered as H2 |
| ↳ `text` | text | One line |
| ↳ `button_label` | text | "Hire workers" / "Find jobs" |
| ↳ `button_link` | link | Company page / Job Seeker page. Fixes the `#` links (`H-15`) |
| ↳ `button_style` | choice: `primary` (orange), `dark` (navy) | Default primary / dark |
| `photo` | image | `hero-welder-1400x799.jpg` from File Manager; alt "Two welders at work, sparks flying" |

Style tab (`tab: "STYLE"`), kept small:

| Field | Type | Notes |
|---|---|---|
| `photo_position` | choice: center, left, right, top | `object-position` for different photos |

Rendering notes:
- The photo is an `<img>` with `loading="eager"` and `fetchpriority="high"` (it's the largest thing on the
  page), `width`/`height` from the field, `object-fit: cover`.
- The Figma visual is a **boolean-operation shape** (559 × 557, runs off the right edge), not a plain
  rounded rectangle. Export that shape's outline as an SVG once and apply it with CSS `mask-image`, so
  any photo an editor picks gets the same shape.
- Arrow disc in the buttons stays as an inline SVG, decorative (`aria-hidden`).
- Buttons read `--hsElevate--button--primary__…` variables, so the I-01 navy-on-orange fix in theme
  settings lands here too. The "dark" style keeps its own navy.

## Module 2 · GFB What You Get

**Figma:** `1363:8560`.

`meta.json`: same as the hero, `label` "GFB What You Get".

`fields.json`, Content tab:

| Field | Type | Notes / default |
|---|---|---|
| `heading` | text | "What you get". H2 |
| `columns` | group, `occurrence` min 1, max 2, default 2, sorting label `title` | One per audience |
| ↳ `title` | text | "For Companies" / "For Job Seekers" |
| ↳ `image` | image | The card image (`image 234` / `image 235`), with alt |
| ↳ `features` | group, `occurrence` min 1, max 4, default 3, sorting label `title` | |
| ↳↳ `icon` | choice | See below |
| ↳↳ `title` | text | e.g. "Post a job in 90 seconds" |
| ↳↳ `description` | text | One line |

Defaults for the six features are the Figma copy:
- **For Companies:** Post a job in 90 seconds · Review matched workers, not resumes · Message them directly.
- **For Job Seekers:** Pick your trades and your location · See job details before you apply · Let employers come to you.

**Icons.** HubSpot's `icon` field type draws from Font Awesome. The design uses **Lucide**. So the icon is
a `choice` field listing a fixed set of Lucide icons, and the module inlines the matching SVG. The set
starts with the six actually drawn in Figma (which don't match their layer names, see `05`): **timer,
user-check, messages-square, pin, file-check, radar**, plus a handful of spares (briefcase,
message-circle, clock, badge-dollar-sign, map-pin, shield-check). Adding an icon later is a one-line code
change. Rejected: an image field per icon (editors would upload SVGs, and the icon colour couldn't follow
the theme).

Layout notes:
- Two 568-wide cards with a 64px gap inside the 1200 container, at Figma's 96px top padding. One column
  under 767px.
- Each card: header strip with title and a 1px rule, then the features **laid over the image**. This
  overlay is why no Elevate template fits.
- The Job Seekers image is 563 tall in a 440 card (`05`, note 1). Build with `object-fit: cover` so any
  image fills the card; confirm the crop with design.

## How they're placed on the page

1. Upload the child theme (below) and create the Home page on it, **Home** template.
2. Clear the template's starter sections. Then, top to bottom, in the editor:
   **Add → Modules → GFB Hero** · Card ×3 (trust bar) · **Add → Modules → GFB What You Get** ·
   TestimonialSlider · `pricing` section · `metrics` section · `faq-v2` section · Card variant 4 (CTA).
   Header and footer are global and come with the template.
3. Each Code module goes in its **own full-width section**, so the section's background and spacing
   controls still work around it.
4. Optional, once both are right: in the editor, **save each of these two sections as a reusable section**
   (the page editor's "Save section" option, **verify** the name in the current UI). The Job Seeker and
   Company pages can then drop them from the Sections tab like a template.

This also does build-plan step **0.1**: the homepage goes into the page's own content area, not the
global header partial.

## Upload workflow

```
npm i -g @hubspot/cli              # 8.x
hs init                             # once, against the GoFindBuild account 47303551
hs cms upload Design/HubSpot/code/gofindbuild-child gofindbuild-child
hs cms watch  Design/HubSpot/code/gofindbuild-child gofindbuild-child   # while building
```

`hs cms upload` and `hs cms watch` push changes live straight away, so upload only modules that no published
page uses yet, or test changes on a copy of the module first. To start a module skeleton, `hs cms module create <name> <dest>` asks for the same
`meta.json` settings listed above.

## What editors can and can't change

| Can change in the editor, no code | Needs a developer |
|---|---|
| All headings, lines and button labels (inline or sidebar) | Card or band **layout** |
| Button links and target | A new icon not in the list |
| Hero photo, card images, alt text, photo position | The hero photo's **shape** |
| Number of fork cards (1 to 2), columns (1 to 2), features (1 to 4) and their order | |
| Colours, fonts, button style and radius, via **theme settings** (affects the whole site, same as Elevate) | |

## Build order

1. Child theme skeleton (`theme.json`, empty `child.css`). Upload. **Verify** that pages can
   use Elevate's templates and sections from the child theme.
2. GFB Hero: `fields.json` first, then `module.html` built on the fields, then `module.css` moved to
   `--hsElevate--` variables with the Figma values as fallbacks. Upload. Place it on the draft Home page, replacing the
   old one, and remove the Cloudinary screenshot (build plan 0.4).
3. GFB What You Get: same order.
4. Editor test: as a non-developer, change every field on both modules, add and remove repeater items,
   switch the photo, and confirm nothing breaks.
5. QA against the pre-publish checklist in `../00_BUILD-PLAN_Staging.md`: one H1 (the hero headline), alt
   text, no dead links, hero image under about 300 KB, 1440 / 1280 / 768 / 393 widths.

## Open items

- **(verify)** The exact `extends` value for Elevate in `theme.json`, and that a child of a project-based
  theme accepts classic HubL modules. The docs' "Default themes" page says to customise Elevate by
  creating a child theme; confirm in the CLI or Design Manager before writing more than the skeleton.
- **(verify)** That `inline_text` / `inline_rich_text` work for fields inside repeater groups. If not,
  those fields stay sidebar-only, which still works.
- The export of the hero photo's boolean shape as an SVG mask (design task).
- No HubSpot connector in this session: Claude can write and commit the code, but the upload and the
  page assembly run from a machine with the CLI and portal access.
