# Technical design constraints for marketing emails: accessibility, dark mode, email-client rendering

Context: GoFindBuild welcome emails built in HubSpot's drag-and-drop editor. Brand navy #16243D, orange #F16C0E, font Inter.

**Method note (read first):** In this session WebFetch could not reach any of the primary sources (emailmarkup.org, litmus.com, developers.google.com and others failed DNS, so the hosts appear to be outside the session's allowed network). Every finding below comes from WebSearch result summaries, which quote or paraphrase the indexed pages. Findings attributed to caniemail.com, Litmus or EMC are therefore **secondhand** unless marked otherwise. The contrast ratios for the brand colours were **calculated in this session** with the WCAG relative-luminance formula. They do not come from a source and can be checked with any WCAG contrast checker. Before relying on a per-client support claim, verify it on caniemail.com and in a Litmus or Email on Acid test.

## Accessibility: contrast, font size, semantic HTML, alt text, link text, colour-only meaning, failure rates

### Takeaway
Almost every marketing email fails automated accessibility checks. The 2026 Email Markup Consortium (EMC) report found serious or critical issues in 99.88% of 376,348 emails. The most common failures are mechanical and easy to fix: missing `lang`/`dir` and layout tables without `role="presentation"`. For GoFindBuild, the main brand risk is that **white text on orange #F16C0E is only 3.05:1**, which fails WCAG AA for normal-size text such as button labels. Navy on white (15.51:1) and navy on orange (5.09:1) both pass.

### Cited Findings
**Failure-rate data (EMC reports)**
- EMC 2026 report: 376,348 HTML emails sent between May 2025 and May 2026. 99.88% had serious or critical accessibility issues, and only 8 emails from 3 brands passed every check (about 0.002%). — [beSpacific summary of EMC 2026 report](https://www.bespacific.com/?p=125394); [Harvard TagTeam feed item, "Email Accessibility Report 2026"](https://tagteam.harvard.edu/hub_feeds/2087/feed_items/18322019)
- The most common 2026 issues were missing `dir` (97.41% of emails), missing body-level `lang` (95.66%), and layout tables not marked as presentation (84%). — [unspam.email, "Email Accessibility in 2026" (secondary, cites the EMC report)](https://unspam.email/articles/email-accessibility); [Stripo, "Email accessibility in production"](https://stripo.email/blog/email-accessibility-in-production-why-it-still-breaks-and-what-teams-can-do-about-it/)
- EMC 2025 report: 443,585 emails, 99.89% with serious or critical issues. Emails without serious or critical issues rose from 28 of 409,357 (2024) to about 488 of 443,585 (2025). The 2024 failure figure was 99.97%. — [CSS-Tricks mirror, "HTML Email Accessibility Report 2025"](https://thedigitalinsider.com/html-email-accessibility-report-2025); ["…it depends" newsletter, Email accessibility in 2025](https://itdependsnewsletter.beehiiv.com/p/email-accessibility-in-2025)
- Secondary write-ups say the EMC report stresses descriptive link text and alt text, a `<title>` tag, and a contrast ratio of at least 4.5:1. — [Resend, "6 tips for accessible emails"](https://resend.com/blog/6-tips-for-accessible-emails)
- Caveat: the numbers differ between summaries. The share that "passed all automated checks" is under 0.01%, while the share with "no serious/critical issues" is about 0.11% in 2025. These are different measures, so do not mix them.

**WCAG 2.2 thresholds** (standard text. The w3.org pages could not be fetched this session, so the URLs are given for verification.)
- SC 1.4.3 Contrast (Minimum), AA: 4.5:1 for normal text and 3:1 for large text. Large text is at least 18pt (about 24px) regular or at least 14pt (about 18.66px) bold. — [W3C Understanding SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); the 4.5:1 and 3:1 figures are also restated in [Resend](https://resend.com/blog/6-tips-for-accessible-emails)
- SC 1.4.11 Non-text Contrast, AA: UI component boundaries and meaningful graphics need 3:1 against adjacent colours. A button's outline or fill counts. — [W3C Understanding SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- SC 1.4.1 Use of Color: colour must not be the only way information is conveyed. For example, links in body copy should not be marked by colour alone, so underline them. — [W3C Understanding SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
- SC 2.4.4 Link Purpose (In Context): link text should describe its destination. Avoid "click here" and "read more". — [W3C Understanding SC 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)

**Brand-colour contrast (calculated in this session with the WCAG formula)**
| Foreground | Background | Ratio | Normal text (4.5:1) | Large text / UI (3:1) |
|---|---|---|---|---|
| Navy #16243D | White #FFFFFF | 15.51:1 | Pass | Pass |
| White #FFFFFF | Orange #F16C0E | 3.05:1 | **Fail** | Pass (barely) |
| Navy #16243D | Orange #F16C0E | 5.09:1 | Pass | Pass |
| Orange #F16C0E | White #FFFFFF | 3.05:1 | **Fail** (orange body text or links on white) | Pass |
| Orange #F16C0E | Navy #16243D | 5.09:1 | Pass | Pass |
| Orange #F16C0E | Dark-mode grey #121212 | 6.15:1 | Pass | Pass |
| Navy #16243D | Dark-mode grey #121212 | 1.21:1 | **Fail** (navy logo or text disappears in dark mode) | Fail |
| Navy #16243D | Black #000000 | 1.35:1 | **Fail** | Fail |

**Font size**
- WCAG sets no minimum font size, so the email figures below are conventions. — [Mailtrap, Email Accessibility Guide](https://mailtrap.io/blog/email-accessibility/)
- Adobe recommends at least 16px for body text. — [Adobe Experience League, "Design accessible content"](https://experienceleague.adobe.com/en/docs/campaign-web/v8/content/email-design/accessible-content)
- Ohio State's email guide asks for at least 14px on desktop and 16px on mobile. — [OSU Email Accessibility Guide](https://omc.osu.edu/communities/email-community/email-accessibility)

**Semantic HTML**
- `<html lang="en">`: screen readers use `lang` to choose pronunciation rules. — [Adobe Experience League](https://experienceleague.adobe.com/en/docs/campaign-web/v8/content/email-design/accessible-content); [Dotdigital, Email accessibility](https://support.dotdigital.com/en/articles/8199030-email-accessibility)
- Put `role="presentation"` on layout tables only. Data tables keep their table semantics. — [Adobe Experience League](https://experienceleague.adobe.com/en/docs/campaign-web/v8/content/email-design/accessible-content); [NSW Government email design system, accessibility for developers](https://email.digital.nsw.gov.au/development/accessibility-for-email-developers)
- Use real heading elements in a logical order (h1 for the title, h2 for sections, h3 for subsections), and never use headings just for visual styling. — [Dotdigital](https://support.dotdigital.com/en/articles/8199030-email-accessibility); [OSU guide](https://omc.osu.edu/communities/email-community/email-accessibility)
- Give meaningful images descriptive alt text and decorative images an empty `alt=""`. — [Resend](https://resend.com/blog/6-tips-for-accessible-emails)

### Inferences
- **Orange CTA buttons:** white label text on #F16C0E (3.05:1) fails AA at normal button-label sizes (14–16px). Options are (a) navy #16243D label on orange (5.09:1), (b) white label at 24px or more regular, or 18.66px or more bold (passes the large-text 3:1 by a margin of 0.05, which is fragile), or (c) a darker orange shade for text-bearing buttons. Option (a) keeps the brand colours and passes cleanly.
- Do not use orange for body text or inline links on white (3.05:1). Use navy for links, underlined to satisfy SC 1.4.1.
- HubSpot's drag-and-drop output controls the `<html>` wrapper and table markup. Whether its templates include `lang`, `dir` and `role="presentation"` was not verified in this session. Given the EMC data, assume they may not, and check by inspecting the sent HTML ("View as web page" or the source of a test send).
- Suggested baseline for welcome emails: 16px body text, line-height about 1.5, h1 around 24–28px, alt text on every image, descriptive CTA text ("Complete your GoFindBuild profile" rather than "Click here").

### Gaps
- The EMC report pages themselves (emailmarkup.org) could not be fetched. The 2026 per-issue percentages (97.41% / 95.66% / 84%) come from secondary write-ups. Contrast-failure and missing-alt percentages from the EMC data were not found.
- No authoritative source found on how screen readers (VoiceOver, TalkBack, NVDA, JAWS) behave in specific email clients, such as Gmail webmail wrapping content or Outlook adding its own roles. Mark Robbins' and Paul Airy's work on this could not be accessed.
- HubSpot's default `lang` and `role` output was not verified.

## Dark mode: client behaviour, `prefers-color-scheme` / `[data-ogsc]`, logo and colour implications, usage share

### Takeaway
Clients treat dark mode in three ways: no change, partial invert (only light backgrounds are darkened) and full invert. Reference charts disagree about Apple Mail and Gmail Android, so test in the real clients. Only some clients honour `@media (prefers-color-scheme: dark)`: Apple Mail does, Gmail generally does not, and Outlook exposes `[data-ogsc]`/`[data-ogsb]` hooks instead. For GoFindBuild, a navy-on-transparent logo (1.21:1 against a typical dark background) will effectively disappear. Orange holds up well on dark backgrounds (6.15:1).

### Cited Findings
- **Gmail iOS:** usually described as full invert. **Gmail Android:** disputed. Litmus's chart says partial invert, Email on Acid's says full invert. — [Litmus, Ultimate Guide to Dark Mode](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers); [Parcel, Guide to dark mode](https://parcel.io/guides/dark-mode)
- **Outlook.com and the Outlook apps for macOS, iOS and Android:** generally partial invert. **Classic Outlook / Office 365 on Windows and Windows Mail:** full invert. — [Litmus guide](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers); [Parcel](https://parcel.io/guides/dark-mode)
- **Apple Mail:** charts conflict. Some list it as "no change", meaning the email stays light unless it declares dark styles. Email on Acid lists it as full invert. Apple Mail is described as the most predictable client once dark-mode CSS is supplied. — [Parcel](https://parcel.io/guides/dark-mode); [Email on Acid, dark mode development challenges](https://www.emailonacid.com/blog/article/email-development/dark-mode-email-development-challenges/)
- **New Outlook for Windows:** described as partial inversion, "better than legacy". Outlook.com, new Outlook, Outlook mobile and the Gmail Android app reportedly leave elements that are already dark unchanged. — [DEV Community / mailpeek, "Complete guide to email client rendering differences in 2026"](https://dev.to/mailpeek/the-complete-guide-to-email-client-rendering-differences-in-2026-243f); [freeCodeCamp, Dark mode in HTML email (Patrik Krupař)](https://www.freecodecamp.org/news/dark-mode-in-html-email-everything-you-need-to-know/)
- **`prefers-color-scheme`:** per caniemail as cited secondhand, Apple Mail iOS supports it from iOS 13, and supports the `color-scheme` property from iOS 16.1 (root element only). Gmail webmail does not support it, and reports on Gmail Android conflict. Outlook.com support is disputed: one source says supported, another says it ignores the query and tags changed elements instead. — [freeCodeCamp](https://www.freecodecamp.org/news/dark-mode-in-html-email-everything-you-need-to-know/); [Courier, dark mode email design](https://www.courier.com/blog/dark-mode-email-design); [caniemail repo index](https://docsearch.algolia.com/mcp/docs/repo/hteumeuleu/caniemail)
- **`[data-ogsc]` / `[data-ogsb]`:** when Outlook converts a text colour it adds `data-ogsc` to the element, and when it converts a background it adds `data-ogsb`. These attribute selectors let you restyle elements in Outlook (web and apps) dark mode. Gmail ignores the media query and offers no equivalent hook. — [Litmus guide](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers); [Parcel](https://parcel.io/guides/dark-mode)
- **HubSpot:** the editor has a Dark mode preview toggle (Display options) and client-specific previews. HubSpot suggests a `prefers-color-scheme` media query to control dark-mode images and text, and notes that some clients support it only partially. The preview is an approximation. — [HubSpot KB, Optimize marketing emails for dark mode](https://knowledge.hubspot.com/marketing-email/optimize-marketing-emails-for-dark-mode)
- **Usage share:** no reliable 2024–2026 figure was found. Litmus (via Mailmodo) gives 34% of opens in dark mode as of August 2022. Email on Acid's tests put it at about 11.5%. Publicare's analysis gives 12% of opens (estimated range 10–25%). — [Mailmodo, Dark mode email statistics](https://www.mailmodo.com/guides/dark-mode-email-statistics/); [Publicare, How widespread is dark mode?](https://publicare.de/en/blog/how-widespread-dark-mode-is) (vendor sources, dated, not verified against the originals)

### Inferences
- **Logo:** navy #16243D on a transparent PNG reaches only 1.21–1.35:1 against dark backgrounds and will vanish in clients that darken the background but leave images alone (Apple Mail with dark styles, partial-invert clients). Mitigations: (a) add a thin white or light outline/glow ("stroke") around the navy logo in the PNG, (b) place the logo on a solid white or light rounded "chip" baked into the image, or (c) use a dark-mode logo swap in `prefers-color-scheme` for Apple Mail, combined with (a) or (b) for clients that ignore the media query.
- **Navy header bands:** an already-dark background (#16243D) is usually left alone by partial-invert clients. A full invert may lighten it, so test.
- **Orange CTA:** orange buttons survive dark mode visually (6.15:1 against near-black). A full invert may shift the hue, so check the CTA in Gmail iOS and classic Outlook Windows.
- **Text inside images** cannot be adapted by the client. Keep headings and CTAs as live text so clients can recolour them, and test images with transparency on both light and dark backgrounds.
- Because Gmail, the largest webmail client, offers no dark-mode hook, design the light version so that it degrades acceptably under inversion. Do not rely on dark-mode CSS.

### Gaps
- Litmus's current (2025–2026) dark-mode test chart could not be fetched, so per-client behaviour above is aggregated from guides that are often dated (some 2020–2022) and conflict on Apple Mail and Gmail Android.
- No current, methodologically sound share of recipients using dark mode was found.
- It is unclear whether HubSpot's drag-and-drop editor lets users add custom `<style>` blocks, such as a `prefers-color-scheme` block, without a coded template. The KB summary mentions the media query, but the exact editor mechanism (for example, a head-HTML field) was not confirmed.

## Rendering constraints: Gmail clipping, Outlook Word engine, iOS auto-scaling, web fonts, background images, border-radius, SVG, images, GIFs

### Takeaway
Keep HTML under about 102KB to avoid Gmail clipping. Assume classic Outlook for Windows (Word engine) drops `border-radius`, CSS background images, SVG, `@font-face` and GIF animation (only the first frame shows). Assume Inter will render only in Apple Mail, iOS Mail and some Outlook Mac/web clients, with Gmail falling back. Design every element so the fallback still looks acceptable.

### Cited Findings
- **Gmail clipping:** Gmail clips messages whose HTML exceeds about 102KB and shows "[Message clipped] View entire message". Clipping also cuts off the open-tracking pixel at the bottom. Images do not count toward the limit, only the HTML/code. Google does not document the threshold publicly; the figure comes from ESP documentation. — [SendGrid support, Message clipped](https://support.sendgrid.com/hc/en-us/articles/9298249378075--Message-clipped-Emails-Sent-to-Gmail-Inboxes); [Email on Acid, Gmail email clipping](https://www.emailonacid.com/blog/article/email-development/gmail-email-clipping/); [MXToolbox, email clipping](https://mxtoolbox.com/dmarc/email/email-clipping)
- Repeated test sends with the same subject thread together in Gmail and can trigger clipping, so vary subject lines when testing. — [Drip help, avoid Gmail clipping](https://help.drip.com/hc/en-us/articles/4424710412941-Avoid-Email-Clipping-In-Gmail)
- **Web fonts:** Apple Mail (macOS) and iOS Mail support `@font-face`. Gmail strips custom fonts, apart from its own Google Sans and Roboto. Classic Outlook 2007–2019 and 365 on Windows (Word engine) strip `@font-face` and can fall back to Times New Roman unless a fallback is declared. Outlook for Mac (WebKit) renders web fonts, and reports on Outlook web conflict. — [Scalero, Typography in email](https://scalero.io/company/blog/email-typography-what-renders-esp-limitations); [Courier, Fonts in email](https://www.courier.com/blog/fonts-in-email-what-works-what-breaks-and-how-to-fix-it); [Email on Acid, best email-safe fonts](https://www.emailonacid.com/blog/article/email-development/best-font-for-email-everything-you-need-to-know-about-email-safe-fonts/)
- Litmus data (February 2026, as cited) puts Apple Mail at about 51% of opens. — cited secondhand in the [Scalero typography piece](https://scalero.io/company/blog/email-typography-what-renders-esp-limitations) (open share is inflated by Apple Mail Privacy Protection, so it is not a reliable measure of actual reading)
- **border-radius:** ignored by classic Outlook for Windows because of the Word engine, which gives square corners. Newer Outlook web and mobile clients reportedly accept it. VML is the workaround for rounded buttons. — [Kontent.ai, rounded buttons in Outlook](https://kontent.ai/blog/emails-rounded-buttons-with-shadow-outlook); [Adobe Marketo community, Outlook rendering](https://experienceleaguecommunities.adobe.com/adobe-marketo-engage-general-27/outlook-rendering-question-184070)
- **Background images:** classic desktop Outlook does not support CSS `background-image` (VML is needed). Outlook 365 web and Outlook.com reportedly added CSS background support. — [Elastic Email, Outlook rendering issues](https://elasticemail.com/blog/transactional_email/email-rendering-issues-in-outlook-and-hacks-to-save-the-day/); [Rule.io, Outlook common issues](https://help.rule.io/en/articles/349467-outlook-common-issues)
- **SVG:** support is inconsistent. Classic Outlook for Windows displays neither inline SVG nor SVG in `<img src>`. Gmail support is limited or unclear. Use PNG fallbacks. — [AllSVGIcons, SVG in email (2026)](https://www.allsvgicons.com/blog/email-svg-icons/); [OnVoard glossary, SVG in email](https://onvoard.com/glossary/svg-in-email)
- **Animated GIFs:** classic Outlook 2007–2019 on Windows typically shows only the first frame. New Outlook for Windows uses web-based rendering and reportedly animates GIFs. Microsoft notes that if only the first frame plays, animations may be disabled in the user's settings. — [Microsoft Support, animated graphic doesn't work](https://support.microsoft.com/en-us/outlook/the-animated-graphic-in-my-e-mail-message-doesn-t-work); [Stripo, animated GIFs in Outlook](https://stripo.email/blog/animated-gifs-in-html-emails-in-ms-outlook)
- **iOS auto-scaling:** add `<meta name="x-apple-disable-message-reformatting">` and `<meta name="viewport" content="width=device-width, initial-scale=1">` to stop iOS Mail from rescaling the layout. The tag was suggested by Apple engineer James Magahern around iOS 10. The sources are dated (2016–2020). — [Litmus, 9 things about email in iOS 10](https://www.litmus.com/blog/9-things-you-need-to-know-about-email-in-ios-10); [Nebula Consulting, alignment issues on iPhone](https://nebulaconsulting.co.uk/insights/got-alignment-issues-on-iphone/)

### Inferences
- **Inter:** declare a stack such as `font-family: Inter, Arial, Helvetica, sans-serif`. Gmail and classic Outlook (a large share of B2B readers) will show Arial or Helvetica, so designs, line lengths and button widths must work in Arial. Never put critical text in an image just to keep Inter.
- **GIFs:** put the key message and CTA in frame 1. Classic Outlook shows only the first frame.
- **Buttons:** expect square corners in classic Outlook. HubSpot's button module output was not verified for VML.
- **Retina images:** the usual practice is to export at 2x the display width and constrain them with a `width` attribute (for example a 1200px export displayed at 600px). No 2022+ primary source was retrieved, so treat this as convention.
- **Image file size:** no authoritative per-client limit was found. The general guidance is to keep individual images small (often under about 200KB and hero GIFs under about 1MB) for load time. This is unsourced convention, so verify it before using it as a hard rule.

### Gaps
- caniemail.com could not be fetched, so all per-client feature support above is secondhand. Verify `@font-face`, `border-radius`, `background-image`, SVG and `prefers-color-scheme` there.
- The rumoured mobile Gmail clipping thresholds (about 20KB iOS, 75KB other) appear in only one source and are unverified.
- No current source confirms whether iOS 17/18 Mail still needs `x-apple-disable-message-reformatting`.
- No authoritative max-image-size or 2x-retina guidance from Google, Apple or Microsoft was found.

## HubSpot drag-and-drop editor: fonts, custom CSS, dark mode, mobile overrides, section styles

### Takeaway
HubSpot's drag-and-drop editor offers global text styles (paragraph, h1, h2, links), section-level desktop and mobile styling (Marketing Pro/Enterprise), hide-on-desktop/mobile, column stacking options, a dark-mode preview, and, since a 2026 beta, custom fonts from the brand kit with a mandatory fallback. Inter may therefore be usable through the brand-kit beta, but Gmail and Outlook recipients will see the fallback.

### Cited Findings
- The global Text styles settings cover font, size and colour for paragraph, h1 and h2, plus a link colour and style. Font changes made in individual modules override the global styles. — [HubSpot KB, Create marketing emails in the drag-and-drop editor](https://knowledge.hubspot.com/email/create-marketing-emails-in-the-drag-and-drop-email-editor); [Insidea, editing HubSpot email design](https://insidea.com/blog/hubspot/kb/how-to-edit-marketing-email-content-and-design) (third-party)
- **Custom fonts (beta, KB updated April 2026):** custom fonts are added through the brand kit, and each needs a chosen fallback font. Accounts in the "custom fonts in marketing email" beta see them under "Custom Fonts" in the font dropdown. Recipients whose clients support custom fonts see them, and everyone else sees the fallback. HubSpot advises choosing a fallback with similar x-height and weight and previewing across clients. — [HubSpot KB, Use custom fonts in marketing emails](https://knowledge.hubspot.com/marketing-email/use-custom-fonts-in-marketing-emails)
- Older community threads say custom fonts are not available in drag-and-drop emails, only a limited built-in set (Lato and Merriweather are listed as web fonts for the drag-and-drop editor). These threads predate the beta and are likely outdated. — [HubSpot KB, Use fonts in HubSpot](https://knowledge.hubspot.com/website-and-landing-pages/use-fonts-in-hubspot); [HubSpot Community, Custom fonts in Drag and Drop emails](https://community.hubspot.com/t/custom-fonts-in-drag-and-drop-emails/14319)
- **Section styling:** desktop and mobile styling can be set separately per section or for the whole email by turning off the "All devices" switch under Background or Spacing (Marketing Pro and Enterprise). — [HubSpot KB, Customize marketing email section styling](https://knowledge.hubspot.com/marketing-email/customize-marketing-email-section-styling); [HubSpot KB, Optimize marketing email for mobile devices](https://knowledge.hubspot.com/marketing-email/optimize-marketing-email-for-mobile-devices)
- **Mobile:** modules and sections can be hidden on desktop or mobile, and a Stacking setting controls column stacking (keep columns, or left on top of right). There is a "remove padding on mobile" option. Community posts report missing controls (no right-to-left stacking in older threads, and odd behaviour with 1x1 "hidden" images). — [HubSpot KB, Optimize marketing email for mobile devices](https://knowledge.hubspot.com/marketing-email/optimize-marketing-email-for-mobile-devices); [HubSpot Community, Mobile stacking order](https://community.hubspot.com/t5/CMS-Development/Mobile-Stacking-Order-in-Drag-and-Drop-Email-Template/m-p/250519)
- **Dark mode:** there is a Dark mode preview toggle under Display options, previews for specific clients, and guidance to use `prefers-color-scheme` (with a caveat about limited client support). — [HubSpot KB, Optimize marketing emails for dark mode](https://knowledge.hubspot.com/marketing-email/optimize-marketing-emails-for-dark-mode)
- Coded email templates (developer docs) allow full markup control, unlike drag-and-drop. — [HubSpot Developers, Email template markup](https://developers.hubspot.com/docs/cms/start-building/building-blocks/templates/email-template-markup)

### Inferences
- To use Inter, enrol in or check the custom-fonts beta and set Arial or Helvetica as the fallback (similar x-height). Otherwise use a built-in sans-serif and accept that Inter is not available.
- Dark-mode logo strategies that need CSS (image swaps) may require a coded template. In pure drag-and-drop, prefer a logo PNG with a stroke or a light background chip, which needs no code.
- Mobile-specific backgrounds and spacing need Marketing Pro or Enterprise, so confirm GoFindBuild's tier.

### Gaps
- HubSpot KB pages were not fetched in full. Exact menu labels, tier gating for hide-on-mobile and stacking, and whether drag-and-drop accepts a custom `<style>`/head HTML block were not confirmed.
- No HubSpot documentation was found on the accessibility of drag-and-drop output (`lang`, `role="presentation"`, heading tags in rich text), on the button module's Outlook/VML handling, or on how much HTML weight HubSpot's wrapper adds against the 102KB Gmail limit.
- The custom-fonts beta status (still beta or generally available as of November 2026) was not confirmed.
