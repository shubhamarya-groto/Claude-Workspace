# gfb_hero_signup (Plumbing landing page header)

Custom module `/custom/content-mcp/modules/gfb_hero_signup`, created 23 Oct 2026 from Figma `1528:10672`
("GFB / Section / Hero + sign-up form", Components · Plumbing · Hi-Fi). Placed on LP-20261007-INDY-EmployerSignup-Plumbing-STAGING
(`223867638545`) as `dnd_area-module-5`, row 0. It replaces the old 6/6 row (linked image, `indy_…_hero`, eyebrow rich text,
company-name rich text, `@hubspot/form`), which was removed.

- **Layout:** grey band (#F6F7F8). Left (674): rounded photo, orange eyebrow, H1 (rich text, bold words orange), body, 3 stat cards, note. Right (478): white card with the company name, the HubSpot form and a full-width orange Submit, plus a "Claim your profile" corner ribbon.
- **Company name:** the card title shows the company property `fcklmarketing_company_name` when HubSpot knows it (toggle), otherwise "Indianapolis Plumbing Businesses".
- **Form:** same form as before, `8750fff0-3492-4d53-8187-2a7682bc2320`. The response is now an **inline thank-you message**. The old setting redirected to `http://www.google.com`, a placeholder already flagged in the landing pages context doc.
- **Anchor:** the card keeps `id="employer-signup-form"`, so the final CTA's "Claim your free company profile" link still scrolls to it.
- **Copy:** stat lines follow Figma ("Connect with talent in Indianapolis", "You choose who you want to interview"), and the H1 is "Connect your plumbing business with / **Indianapolis Talent**".
- **Checked locally:** a Playwright render of the module CSS with standard HubSpot form markup came out 955 px tall at 1440 (Figma is 954) and stacks cleanly at 390. The live render wasn't seen; hs-sites.com is blocked from the container.
- Files: `module.css`, `module.html` (HubL), `fields.json`, `module.live.html` (as pushed).
