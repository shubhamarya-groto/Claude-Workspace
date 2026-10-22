# gfb_vision ("Our Vision" band)

Custom module `/custom/content-mcp/modules/gfb_vision`, created in the portal on 22 Oct 2026 for I-24.
It sits on GFB Home (staging) `223806550529` as `main-module-11`, between the final CTA and the footer.

- Fields: `heading` (text), `body_copy` (rich text), `closing` (text, shown bold). `body` is a reserved name in HubSpot.
- Layout: light grey band (#F8F9FB), one centred 760px column, a short orange rule, an H2, Brian's paragraph, then his last sentence as a bold closing line. No buttons, so it doesn't compete with the CTA above it.
- Copy is Brian's, word for word, from his Figma comment on 21 Oct.
- Styles: `module.css` (inline in the module HTML). Previews: `preview-1440.png`, `preview-390.png` (local mock with stand-ins for the CTA and footer).
- Figma: added 22 Oct as `10b · Our Vision` (`1569:3096`) inside Home Page `1259:9027` (page Presentation), between `10 · Final CTA` and the footer. It's auto-layout, bound to file variables (primary orange rule, foreground/brand, muted/foreground, spacing 20/24/5/6, radius sm) and the text styles Body/Body lg and Heading/Heading lg. The heading is Instrument Sans SemiBold 32 (no matching style in the file). The background is #F8F9FB, the same raw value as the What you get band.
