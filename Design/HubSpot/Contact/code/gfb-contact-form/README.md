# GFB Contact form

HubSpot custom module `/custom/content-mcp/modules/gfb_contact_form` (created 29 Oct 2026 through the connector;
CSS inlined in the HTML, so `module.live.html` is exactly what HubSpot holds). Placed on the Contact Us page
(`225830133851`, module `main-module-7`), replacing the theme header + `@hubspot/form` modules.

Inputs follow the design-system field **`GFB / Input field`** (Figma `1525:2812`, the field used on the Plumbing
sign-up hero): label Inter Medium 14/18 navy #16243D, 6px gap, 48px white box, 1px #D9D9D9, radius 8, 16px side
padding, Inter 16 (placeholder #525C70). Textareas 144px min. Submit: the GFB orange pill (48 high, hugs its label;
full width on phones). Content is centred at **max 800px**. Fields the form puts side by side (e.g. first / last name)
stay side by side, 16 apart; one per row under 768px.

| Field | Notes |
|---|---|
| `eyebrow` | Optional orange overline |
| `heading`, `heading_level` | "Contact Us", H1 by default |
| `intro` | Rich text under the heading |
| `form_field` | HubSpot form (default `a4872182…`), inline thank-you message (the old module redirected to google.com) |
| `notify_override`, `notify_emails` | Submission emails, comma-separated (brian@gofindbuild.com, as before) |
| `alignment` | Left / Centre |
| `background` | White / Light grey |
| `anchor_id` | Section id (`contact-form`) |

Files: `module.html`, `module.css`, `fields.json`, `module.live.html`.
