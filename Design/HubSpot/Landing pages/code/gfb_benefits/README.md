# gfb_benefits · HubSpot custom module

Portal `47303551`, path `/custom/content-mcp/modules/gfb_benefits`. Created 16 Oct 2026 through the HubSpot content tools.
Built Bold version of the one-off `gofindbuild_plumbing_company_benefits`; the visual is `../gfb-company-benefits.html`.

**Fields:** `eyebrow` (text, optional) · `heading` (text, rendered as H2) · `intro` (richtext) · `cards` (group, 1–6: `icon` choice, `title` text, `text` richtext) · `background` (white | grey).

**Icon choices (Lucide, inline SVG):** file_plus, users, user_check, briefcase, search, map_pin, shield_check, message_circle.

**In use:** LP-20261007-INDY-EmployerSignup-Plumbing-STAGING (`223867638545`), module `dnd_area-module-3`, row 1 (after the hero, before pricing). Replaced `widget_1791407173044`. Content copied unchanged; the intro's inline `color: #525c70` span dropped (the module sets that colour). Icons: file_plus (Post an opportunity), users (Connect with matched job seekers), user_check (Choose who to interview).

The HubL and CSS live in the portal (Design Manager). The markup and CSS match `../gfb-company-benefits.html`, with HubL loops for the cards and an `{% if %}` chain for the icons.
