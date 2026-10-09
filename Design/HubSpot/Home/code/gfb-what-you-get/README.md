# GFB What You Get

Second Code module for the Home page (`../../05_SECTION-SPLIT_Code-vs-Template.md`).
Figma: Home Page `1259:9027` → band `1363:8560`. Styles read from Figma on 7 Oct 2026.

> **Live in HubSpot (7 Oct 2026):** created through the HubSpot connector as **GFB What You Get**, path `custom/content-mcp/modules/gfb_what_you_get` in the GoFindBuild account (47303551). Fields read back and match `fields.json`; CSS is inlined in the HTML. Update it through the connector, not the Design Manager, so the two don't drift.

| File | What |
|---|---|
| `fields.json` | Field schema with the Figma copy as defaults |
| `module.html` | HubL template (icons inlined as Lucide SVG) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks |
| `demo.html` | Static demo rendered from the defaults; open in any browser |

## Fields

| Field | Type | Notes |
|---|---|---|
| `heading` | Text | "Better opportunities. Better workers. One construction network." (the layer is named "What you get" in Figma; this is the actual heading) |
| `columns` | Repeater group, 1 to 2, default 2 | One card per audience |
| ↳ `title` | Text | For Companies / For Job Seekers |
| ↳ `accent` | Choice: `orange`, `blue` | Glow, icon badge and image tint. Companies orange, Job Seekers blue |
| ↳ `tone_image` | Toggle, off | **Fade and tint the image.** Off: the image shows exactly as uploaded (use the final Figma images). On: faded to 10% (orange) / 7% (blue), faded out towards the top and tinted with the accent (for an ordinary photo). Added 7 Oct |
| ↳ `image` | Image | Faint illustration behind the lower card. Figma uses a construction skyline (Companies) and worker silhouettes (Job Seekers); upload those to Files |
| ↳ `features` | Repeater group, 1 to 4, default 3 | |
| ↳↳ `icon` | Choice | timer, user-check, messages-square, pin, file-check, radar, briefcase, map-pin, shield-check, clock |
| ↳↳ `title` | Text | |
| ↳↳ `description` | Text | One line |

Repeaters are used here (unlike the hero) because each card's defaults are set as a list in `fields.json`, which the connector and CLI accept; in the Design Manager UI the same defaults would have to be typed per item.

## From Figma

- Band `#F8F9FA`, 96px top/bottom, 1200 container. Heading Instrument Sans SemiBold 48 / 1.1, −0.5px.
- Cards 568 wide, 64 apart, white, 1px black at 4%, radius 16, padding 24, gap 24.
  Glow: Companies `#F16C0E` 12% blur 24; Job Seekers `#3EB8FF` 17% blur 20.
- Card title Inter Bold 24, `#525C70`, 1px `#D9D9D9` rule under it.
- Icon badge 28, radius 8: Companies `#FDEDDF` with `#F16C0E` icon; Job Seekers `#E7EAEE` with `#4B74BE` icon.
- Feature title Inter SemiBold 18 / 1.4 `#16243D`; description Inter 14 / 1.5 `#525C70`.
- Icon layers in Figma are misnamed (e.g. "Icon / briefcase" is a timer); the icons above are the ones actually drawn.
