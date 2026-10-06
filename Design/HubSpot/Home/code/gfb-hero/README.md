# GFB Hero · set up in the Design Manager


> **Live in HubSpot (6 Oct 2026):** created through the HubSpot connector as **GFB Hero v2**, path `custom/content-mcp/modules/gfb_hero_v2` in the GoFindBuild account (47303551), with every field below and the code from this folder (CSS inlined in the HTML). The hand-built `GFB Hero` (3 fields) can be deleted once v2 is on the page. Claude can update v2 through the connector; edit it there rather than in the Design Manager so the two don't drift.

Module **GFB Hero** (Design Manager, content types Site pages + Landing pages, Local).
Figma: Home Page `1259:9027` → band `1259:9031`. Copy and colours read from Figma on 6 Oct 2026.

`fields.json` in this folder is the same field list as JSON, for the CLI or for creating the module through the HubSpot connector.

Do the steps in this order: **fields first**, then paste the code. The code reads the fields by
their **HubL variable names**, so those names must match the table exactly.

## 1 · Module label

Right panel → **Label**: `GFB Hero`.
**Inline help text** (optional): `Homepage hero: headline, two audience cards and the photo.`

## 2 · Fields

Right panel → **Fields** → **Add field**. For each field: pick the type, type the label, then check the
**HubL variable name** under it (HubSpot fills it in from the label; change it if it differs).
Then set the default.

| # | Type | Label | HubL variable name | Default |
|---|---|---|---|---|
| 1 | Text | Headline | `headline` | `Where construction businesses and workers meet` |
| 2 | Text | Highlighted words | `highlight` | `and workers meet` |
| 3 | Text | Subhead | `subhead` | `We automatically match talented job seekers directly to the construction businesses that need them.` |
| 4 | **Group** | Card one | `card_one` | (fields 4a to 4e go inside it) |
| 4a | Text | Title | `title` | `I'm hiring` |
| 4b | Text | Line | `text` | `Post jobs - see matches today free!` |
| 4c | Text | Button label | `button_label` | `Hire workers` |
| 4d | Link | Button link | `button_link` | The Company page URL, once it exists |
| 4e | Choice | Button style | `button_style` | Options below, default **Orange** |
| 5 | **Group** | Card two | `card_two` | (fields 5a to 5e go inside it) |
| 5a | Text | Title | `title` | `I'm looking for work` |
| 5b | Text | Line | `text` | `Free forever - find the best paying jobs!` |
| 5c | Text | Button label | `button_label` | `Find jobs` |
| 5d | Link | Button link | `button_link` | The Job Seeker page URL, once it exists |
| 5e | Choice | Button style | `button_style` | Options below, default **Dark** |
| 6 | Image | Photo | `photo` | `hero-welder-1400x799.jpg` from Files, alt text `Two welders at work, sparks flying` |
| 7 | Choice | Photo focus | `photo_position` | Options below, default **Center** |

**Groups:** add the Group field first, then add the five fields **inside** it. Don't turn on
"Repeater" for these groups: there are exactly two cards, each with its own copy.

**Choice options** (each option has a *label* the editor sees and a *value* the code reads; the value
must be exactly as written):

| Field | Label → value |
|---|---|
| Button style | Orange → `primary` · Dark → `dark` |
| Photo focus | Center → `center` · Left → `left` · Right → `right` · Top → `top` |

**Help text worth adding** (each field has a help text box):
- Highlighted words: `Must match words in the headline exactly. They turn orange.`
- Photo: `Wide photo, at least 1200 px. The folder-tab shape is applied automatically.`

Leave **Style Fields** empty. Colours and fonts come from the theme settings.

## 3 · Paste the code

- `module.html` box ← all of `module.html` in this folder
- `module.css` box ← all of `module.css` in this folder
- `module.js` box: leave empty

Check the status bar at the bottom says **No errors found**, then click **Preview** to check, then
**Publish changes**.

## 4 · Place it

Page editor → **Add** → **Modules** → search `GFB Hero` → drag to the top of the page, in its own
full-width section. Every field above shows in the left panel when you click the hero.

## Things to know

- **The primary (orange) button follows the theme.** It reads Elevate's primary button settings, so until
  the theme-settings pass is done (build plan 0.2) it shows Elevate's stock colour, not orange. That's
  expected; the pass fixes it here and on every other button at once.
- **Headline font** comes from the theme's H1 font, so it shows Instrument Sans once the theme pass sets
  it. Size (68px on desktop, smaller on phones) is set here.
- **Button label colour:** Figma draws white on orange; the plan is a navy label (I-01, contrast). The
  code follows whatever the theme sets.
- **Changed from the old hard-coded module:** the orange highlight is now "and workers meet", as in Figma
  (was only "and"); card titles are 18px (were 16); the photo has Figma's folder-tab shape (was a
  rounded rectangle); the photo is a real image with alt text, not a CSS background; no Google Fonts link.
- If a **GFB Hero already exists** in the portal (the old one on the demo page), replace it on the page
  with this one, then delete the old module so editors only see one.
