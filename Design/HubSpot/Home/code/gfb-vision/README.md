# gfb_vision ("Our Vision" band)

Custom module `/custom/content-mcp/modules/gfb_vision`, created in the portal on 22 Oct 2026 for I-24.
**Page: About Us only** (Shubham, 22 Oct). It sits on GFB About Us (staging) `224339429033` as `main-module-7`, after the three alternating rows and before the final CTA, matching the Figma placement. It was briefly on the Home draft (`main-module-11`) and was removed there before it was ever published.

- Fields: `heading` (text), `body_copy` (rich text), `closing` (text, shown bold). `body` is a reserved name in HubSpot.
- Layout: light grey band (#F8F9FB), one centred 760px column, a short orange rule, an H2, Brian's paragraph, then his last sentence as a bold closing line. No buttons, so it doesn't compete with the CTA above it.
- Copy is Brian's, word for word, from his Figma comment on 21 Oct.
- Styles: `module.css` (inline in the module HTML). Previews: `preview-1440.png`, `preview-390.png` (local mock with stand-ins for the CTA and footer).
- Figma: `10b · Our Vision` (`1569:3096`), now inside **About Us · Hi-Fi** `1259:9158` (page Presentation), between the alternating rows and `09 · Final CTA`. It was built in Home Page first, then moved; Home Page is back to 5543 tall with no Our Vision layer. It's auto-layout, bound to file variables (primary orange rule, foreground/brand, muted/foreground, spacing 20/24/5/6, radius sm) and the text styles Body/Body lg and Heading/Heading lg. The heading is Instrument Sans SemiBold 32 (no matching style in the file). The background is #F8F9FB, the same raw value as the What you get band.
