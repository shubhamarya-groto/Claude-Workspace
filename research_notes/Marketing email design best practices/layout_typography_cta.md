# Marketing / Lifecycle Email Design: Layout, Typography, Hierarchy, CTAs, Imagery

Research date: 2026-11-12. Context: GoFindBuild welcome emails (mobile-first tradespeople and contractors), built in HubSpot drag-and-drop.

**Method caveat (read first):** This session's network blocked direct page fetches from litmus.com, nngroup.com, caniemail.com and stylecampaign.com (DNS failure; those hosts have to be allowed in the session's network settings). The findings below come from web-search result summaries of those primary pages and of secondary sites that quote them. I could not read the full original pages, so treat exact percentages as "reported by the source, not independently re-read". Where a figure appears only on an aggregator, it is labelled that way.

---

## 1. Layout: content width, columns, responsive vs hybrid, and mobile share of opens

### Takeaway
Use a single-column layout in a fluid container capped at about 600px (the "hybrid" pattern). Assume most opens are on phones. Apple accounts for about 45–60% of tracked opens, but that share is inflated by Mail Privacy Protection (MPP). The device split most often attributed to Litmus is roughly 42% mobile, 41% webmail and 16% desktop.

### Cited Findings
- Litmus market-share data is built from more than 1 billion opens in Litmus Email Analytics; the latest dataset is July 2026. Apple Mail and Gmail together account for "nearly 90%" of opens. — [Litmus Email Client Market Share](https://www.litmus.com/email-client-market-share)
- February 2026 Litmus figures, as relayed by an aggregator: Apple 45.51%, Gmail 23.54%, Outlook 5.67%, Yahoo 2.06%. — [Demandsage summary of Litmus](https://www.demandsage.com/?p=9995)
- Another secondary summary of the July 2026 data gives Apple 62.26%, Gmail 27.03%, Outlook 5.83%. This conflicts with the February 2026 split, so treat the per-client numbers as unstable from month to month. — via search summary of the [Litmus market share page](https://www.litmus.com/email-client-market-share)
- Litmus warns that opens from users who opted into Apple MPP are unreliable for client detection, which inflates Apple's share. It also says Gmail is credited only when the email is opened in a Gmail client. — [Litmus blog: email client market share](https://www.litmus.com/blog/email-client-market-share)
- Device split attributed to Litmus on several aggregator pages: mobile 41.6%, webmail 40.6%, desktop 16.2%. The pages disagree on whether this is 2025 or 2026 data. Other aggregators claim "62% of opens on mobile" or "55% in 2025", but I could not trace either figure to a Litmus primary page. — [Mailmodo mobile email stats](https://www.mailmodo.com/guides/mobile-email-statistics); [emaillistvalidation.com benchmarks](https://emaillistvalidation.com/blog/mobile-vs-desktop-email-open-rate-benchmarks/)
- Responsive design starts from a fixed-width layout (typically 600px) and uses media queries to make it fluid on small screens. Hybrid ("spongy") design is fluid by default, uses `max-width` plus Outlook conditional comments to cap width at 600px, and adapts without media queries. — [Litmus: Understanding Responsive and Hybrid Email Design](https://www.litmus.com/blog/understanding-responsive-and-hybrid-email-design/); [Litmus: Scalable, Fluid or Responsive](https://www.litmus.com/blog/anatomy-mobile-email)
- Older adoption data (2017, Litmus and Salesforce): 77% of B2C brands had adopted mobile-friendly design, up from 56% a year earlier. Most of the gain came from "mobile-aware" and "responsive-aware" approaches, meaning simple single-column designs, rather than full responsive builds. — [Litmus: Responsive-Aware and Mobile-Aware Design See Gains](https://www.litmus.com/blog/responsive-aware-and-mobile-aware-design-see-gains-as-marketers-focus-on-production-cost)
- Vendors consistently recommend single-column layouts for mobile because multi-column layouts can break or stack awkwardly. — [Zoho ZeptoMail: responsive email](https://www.zoho.com/zeptomail/articles/responsive-email.html); [Mailgun welcome email guide](https://www.mailgun.com/blog/email/welcome-email/)

### Inferences
- Webmail (mostly Gmail) has about the same share as mobile, and Gmail strips a lot of CSS (see web fonts below). So the design must still work if media queries or `@font-face` fail. A single column that is fluid by default (hybrid) degrades most safely. HubSpot's drag-and-drop editor already outputs a 600px, stacking, responsive layout. The practical choice is to keep every section to one column and to avoid 2- or 3-column modules whose stacking order you do not control.
- For a mobile-first tradesperson audience, the real mobile share is likely above the blended 42%. Validate this in HubSpot's email analytics by device; HubSpot reports opens and clicks by device type.

### Gaps
- I could not read Litmus's State of Email or the current market-share page directly, so I have no confirmed 2025–2026 primary-source device split.
- I found no controlled experiment comparing 600px with 640px (or other) widths. The 600px convention rests on practitioner consensus and old desktop preview-pane constraints, not on a test.
- I found no current (2023+) data on the share of brands using hybrid versus responsive builds.

---

## 2. Typography: mobile font size, line height and length, web fonts, headings

### Takeaway
Set body text at 16px or larger. Older iOS versions auto-enlarged text below about 13–14px, which can break layouts, and current devices may not upscale at all. Apple Mail renders custom web fonts reliably; Gmail web strips them; Outlook support is inconsistent. A font like Inter therefore needs a robust system fallback stack, and the email should look right in the fallback.

### Cited Findings
- Style Campaign (Anna Yeaman, practitioner research) tested iOS devices. It found iOS appears to have had a minimum font size of about 14px at some point, and that 9px text on older iOS devices was auto-scaled to about 15pt while newer devices render it at 9px. It notes that 16px is the default in many browsers and 17px is the system body size on newer iPhones, and suggests these are intended as body-text sizes, not minimums. — [Style Campaign: Small text and accessibility in email](https://stylecampaign.com/blog/small-text-and-accessibility-in-email/)
- Disabling iOS auto-resizing requires `-webkit-text-size-adjust: none`, which works against accessibility. WCAG 2.1 has no stated minimum font size. — [Style Campaign](https://stylecampaign.com/blog/small-text-and-accessibility-in-email/)
- Users report that for most HTML emails, iOS Mail's text-size settings have no effect, so the designer's chosen size is what readers get. — [Apple Community thread](https://discussions.apple.com/thread/7667124); [AppleVis forum](https://applevis.com/forum/ios-ipados/text-size-mail-ios-101)
- `@font-face` support (caniemail): about 22% of tested clients have full support, about 29% when partial support is included. The partial cases are clients that accept it only via a `<link>` tag or only via a `<style>` tag. — [caniemail: @font-face](https://caniemail.com/features/css-at-font-face)
- Apple Mail renders custom fonts reliably. Gmail web strips `@font-face`, so the fallback always applies there. Gmail's iOS and Android apps have partial and inconsistent support. — [Scalero: Typography in email](https://scalero.io/company/blog/email-typography-what-renders-esp-limitations); [Buttondown: Can you use web fonts in email?](https://buttondown.com/blog/newsletter-custom-fonts)
- Outlook for Windows desktop does not support web fonts. Some versions fall back to Times New Roman unless `mso-font-alt` or a similar fix is used. Sources disagree on Outlook for Mac, Outlook.com and the mobile apps. — [Email on Acid: Best font for email](https://www.emailonacid.com/blog/article/email-development/best-font-for-email-everything-you-need-to-know-about-email-safe-fonts/); [Rémi Parmentier: mso-generic-font-family](https://medium.com/emails-hteumeuleu/today-i-learned-about-mso-generic-font-family-85b0e4703079)
- Every source recommends declaring web-safe fallbacks (Arial, Helvetica, Georgia and similar) in the font stack. — [Campaign Monitor: web fonts in email](https://www.campaignmonitor.com/dev-resources/will-it-work/webfonts/)

### Inferences
- A fallback stack in the shape `Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif` would follow from the support data above, because each named system font matches a platform where `@font-face` fails. I did not find a primary source that prescribes this exact stack. Note also that HubSpot's drag-and-drop editor limits font choice to its built-in list plus any custom fonts configured at account level.
- Gmail is the largest webmail client and strips web fonts, so a large share of readers will see the fallback. Brand-critical type, such as a logo or wordmark, should be an image with alt text, not a web font.
- Body text of 16px on mobile (and at least 14px everywhere) avoids iOS auto-resize artefacts and matches platform defaults.

### Gaps
- Line height (for example 1.4–1.6) and line length (about 50–75 characters): I found no email-specific primary research in this session. These are general typographic conventions, not email-tested findings.
- Heading sizes: I found no sourced data for email specifically.
- I could not confirm the commonly repeated "13px iOS minimum" figure. The best evidence (Style Campaign) points to about 14px on older iOS and no upscaling on newer devices.

---

## 3. Hierarchy and scannability: what NN/g says, email length, one message per email

### Takeaway
NN/g eye-tracking found that readers give a newsletter about 51 seconds after opening it, and fully read only 19% of newsletters. Scanning is the dominant behaviour, and NN/g judged scannability about 50% more important for newsletters than for websites. The email therefore needs a front-loaded, single-message structure. Note that this research is old (early-to-mid 2000s; the report is in its 6th edition) and has not been replicated with recent data.

### Cited Findings
- NN/g eye-tracking: average time spent on a newsletter after opening it was 51 seconds. — [NN/g: Email Newsletters: Surviving Inbox Congestion](https://www.nngroup.com/articles/email-newsletters-inbox-congestion/); [ClickZ: 51 Seconds to E-Newsletter Success](https://www.clickz.com/51-seconds-to-e-newsletter-success/58236/)
- Participants fully read 19% of newsletters; the predominant behaviour was scanning. — [Campaign Monitor quoting NN/g Alertbox, 2006](https://www.campaignmonitor.com/blog/email-marketing/email-usability-keeping-your-email-newsletters-short-and-sweet/); [Wylie Communications](https://wyliecomm.com/2022/08/skim-scan-read)
- Scannability is "about 50% more important for newsletters" than for websites. Users spent an additional 33 seconds on site content reached through newsletter links. — [Smart Insights summary of NN/g report](https://www.smartinsights.com/email-marketing/enewsletter-usability-5-subscriber-behaviours-to-consider/)
- NN/g's newsletter usability report (6th edition) contains 199 design guidelines. — [PRSA summary](https://prsay.prsa.org/2019/06/27/how-long-should-your-e-newsletter-be/)
- NN/g's Ecommerce UX Vol. 12 report on transactional email, confirmation messages and notifications contains 143 recommendations covering subject lines, sender details and message body. NN/g notes that users are likely to check email on a mobile device and that email now competes with push notifications. — [NN/g report: Transactional Email](https://www.nngroup.com/reports/ecommerce-transactional-email-confirmation-message/); [NN/g: State of transactional email](https://www.nngroup.com/articles/state-transactional-email/)
- NN/g's older guidance on newsletters: they are a supplement to a website, and their value depends on being quick to consume. — [NN/g: Email Newsletters: Increasing Usability](https://www.nngroup.com/articles/e-mail-newsletters-increasing-usability/)

### Inferences
- With about 51 seconds of attention, mostly spent scanning, a welcome email should put the single most important action and its benefit in the first screen. That is roughly the first 500–600px on a phone, including the preheader. Supporting detail follows in inverted-pyramid order. The "first 500–600px" figure is often attributed to Litmus, but I could not verify it.
- "One message per email" is consistent with both the scanning behaviour and the CTA evidence below. I found no controlled test of single-topic versus multi-topic emails.

### Gaps
- I found no recent (2020+) NN/g eye-tracking data specific to email on mobile, nor a confirmed F-pattern study for email. The F-pattern comes from NN/g web-page research, so applying it to email is an extrapolation.
- I found no rigorous evidence on optimal word count for lifecycle or welcome emails.

---

## 4. CTA design: one CTA or several, button types, placement, tap targets, copy

### Takeaway
Use HTML "bulletproof" live-text buttons, not image buttons. They survive image blocking and screen readers, and Campaign Monitor measured 28% more clicks for a button than for a text link. Size tap targets to at least 44×44: Apple's HIG specifies 44pt and WCAG 2.5.5 (AAA) specifies 44 CSS px, while WCAG 2.5.8 (AA) sets a 24px floor. The single-CTA evidence is suggestive but mixed. The best-supported pattern is one primary action, optionally repeated, with secondary links visually subordinate.

### Cited Findings
- Campaign Monitor: using a call-to-action button instead of a text link gave a 28% increase in click-throughs. The test compared buttons with text links, not image buttons with live-text buttons. — [Campaign Monitor: Why you should use buttons](https://www.campaignmonitor.com/blog/email-marketing/buttons-email-marketing-campaigns/)
- Litmus: image buttons "get lost" when images are turned off and are not accessible to screen-reader users. Bulletproof buttons are HTML/CSS live text, with VML fallbacks for Outlook where needed. — [Litmus: Guide to Bulletproof Buttons](https://www.litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design); tool: [buttons.cm](https://buttons.cm/)
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), level AA: targets must be at least 24×24 CSS px. Exceptions include targets with 24px spacing from neighbours and inline links in sentences. SC 2.5.5 Target Size (Enhanced), level AAA: 44×44 CSS px. Apple HIG: 44×44pt. Google Material: 48dp. — [GOV.UK WCAG primer 2.5.8](https://alphagov.github.io/wcag-primer/sc/2.5.8.html); [Smashing Magazine, July 2024](https://smashingmagazine.com/2024/07/getting-bottom-minimum-wcag-conformant-interactive-element-size/); [Silktide 2.5.8 guide](https://silktide.com/accessibility-guide/the-wcag-standard/2-5/input-modalities/2-5-8-target-size-minimum/)
- Single CTA: a Whirlpool case study is widely reported as producing a 42% click-through lift from cutting an email from four CTAs to one. This is secondary reporting; I did not see the primary source. — [BNP Media: How simpler emails drive higher click-to-open rates](https://www.bnpmedia.com/resources/articles/how-simpler-emails-drive-higher-click-to-open-rates/)
- Mixed evidence: James Wellbeloved tested one to three CTAs with Klaviyo. For new customers, a two-offer variant won by +0.15 points of click rate; for repeat customers the difference was +0.02 points. In a later reminder test, the single-CTA version won by +0.46 points. — [Klaviyo case study: James Wellbeloved](https://klaviyo.com/uk/customers/case-studies/james-wellbeloved-ab-testing)
- An Omnisend analysis of about 229 million emails, reported second-hand, found 2–3 CTAs performed best and 4 or more performed worse. I could not see the methodology. The often-quoted "371% more clicks with a single CTA" (attributed to WordStream/Campaign Monitor) could not be traced to a primary study. — [Databox: improve email CTR](https://databox.com/improve-your-email-click-through-rate)
- For comparison, on landing pages rather than email: Unbounce found single-CTA pages converted at 13.5% and pages with three or more CTAs at 10.5% (18,639 pages). — [Foundry CRO summary](https://foundrycro.com/blog/cta-button-conversion-rate-benchmarks-2026/)

### Inferences
- In HubSpot drag-and-drop, the native Button module renders a live-text, padded-table button, which is effectively bulletproof. Set button height to at least 44px (for example 16px text with about 14px vertical padding). On mobile, full-width buttons give the largest tap area for users wearing gloves or with dirty hands on site, which is a plausible concern for this audience but an inference.
- For a welcome email: one primary CTA above the fold (for example "Complete your profile" or "Post your first job"), optionally repeated at the end. Secondary actions should be text links. This is consistent with the Whirlpool and Wellbeloved results and with the Omnisend finding that 4 or more CTAs underperform.
- Button copy: use specific, verb-first wording that names the outcome. I found no rigorous email-specific test of button wording, so treat this as convention.

### Gaps
- No peer-reviewed study on single versus multiple CTAs in email.
- No primary data on whether above-the-fold CTA placement affects click rate in email.
- No primary test of button copy for lifecycle emails.

---

## 5. Images vs live text: blocking, image-to-text ratio, alt text, GIFs, hero images, UI screenshots

### Takeaway
Image blocking is now uncommon by default: Gmail, Apple Mail and Outlook.com load images, though some Outlook desktop configurations still block them. The 60/40 image-to-text rule is largely a myth. Email on Acid's test found no spam effect once an email has at least 500 characters of text, but image-only emails remain risky. Key messages and CTAs belong in live text, and every image needs meaningful alt text.

### Cited Findings
- Gmail and Outlook.com do not block images by default. Older Outlook desktop versions (2007–2016) show alt text only after a security prompt. Sources disagree on current Outlook for Windows defaults. — [Email on Acid: Mastering styled alt text](https://www.emailonacid.com/blog/article/email-development/mastering-alt-text-in-email/) (2016; client table likely dated); [Mailblaze: image blocking](https://www.mailblaze.com/thinking/image-blocking-in-email)
- Email on Acid advises against image-only emails because screen readers can only read alt text, and because such emails cause accessibility and deliverability problems. — [Email on Acid glossary: image blocking](https://www.emailonacid.com/glossary/image-blocking/)
- Email on Acid tested against 23 spam filters. Emails with 500 or more characters of text were not affected by text-to-image ratio. — [Email on Acid: Does text-to-image ratio affect deliverability?](https://www.emailonacid.com/blog/article/email-development/does_text_to_image_ratio_affect_deliverability/)
- Movable Ink calls "image-heavy emails hurt deliverability" a myth, provided the email has more than about 500 characters of text. — [Movable Ink: Truth behind image-to-text ratio](https://movableink.com/blog/the-truth-behind-image-to-text-ratio-in-email-campaigns)
- Counterpoint: SpamAssassin has rules that penalise low text-to-image area, which can matter more at smaller receivers. A very high image ratio is rarely the sole cause of spam placement. — [Suped (citing Email Geeks)](https://www.suped.com/knowledge/email-deliverability/content/does-a-high-image-to-text-ratio-affect-email-deliverability-and-spam-filtering)
- HubSpot's own tests: the version with an animated GIF had a 2.3% lower click-through rate, and the plain-text version got 42% more clicks overall once its higher open rate was included. A separate HTML-template versus plain test had a 21% lower click-through rate and 51% fewer total clicks for HTML. HubSpot also reported that click rate trended down as the number of images rose. — [HubSpot: Plain text vs HTML emails data](https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data)

### Inferences
- Treat hero images as optional decoration. Headline, value proposition and CTA should be live text so they render even if images fail and are read by screen readers.
- Screenshots of the GoFindBuild app UI will be scaled down to about 50–60% on a phone: a 600px design shown on a roughly 375px-wide screen is about 62%. Any text inside a screenshot will therefore be too small to read. Crop tightly to one UI element, or describe the step in live text and use the image only as a visual cue. This is derived from the width maths, not from a found study.
- Keep each welcome email above about 500 characters of live text to stay clear of image-ratio filter rules.

### Gaps
- No current (2024–2026) primary table of image-blocking defaults by client.
- No found study on how legible UI screenshots are inside emails.
- No rigorous current data on GIF performance beyond HubSpot's internal test (date unclear, probably about 2014–2016).

---

## 6. Plain-text-style vs designed HTML emails

### Takeaway
The available evidence (HubSpot's internal A/B tests and Parcel's welcome-flow test) leans toward plain or lightly designed emails getting more clicks or conversions. It is vendor-run, often not like-for-like, and not peer-reviewed. HubSpot itself cautions that results vary by audience.

### Cited Findings
- HubSpot: in every A/B test it ran, the simpler-designed email won, and emails with fewer HTML elements won with statistical significance. Its "plain-text" variants still used hyperlinks and tracking pixels. HubSpot cautions that subscribers may expect images and that results may not generalise. — [HubSpot: Plain text vs HTML emails data](https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data)
- Parcel (useparcel.com): a five-month split test of its welcome flow, text-based versus designed. The text-based variant converted better. The authors note the variants were "not apples to apples". A search snippet also showed CTRs of 6.55% (text) and 8.85% (designed), which seems to contradict the conversion result; I could not reconcile the two. — [Parcel: Onboarding results, text-based vs designed](https://parcel.io/blog/text-based-vs-designed-emails)
- Litmus ran its own HTML versus plain-text A/B test. I could not retrieve its results in this session. — [Litmus: A/B testing HTML vs plain text](https://www.litmus.com/blog/the-results-are-in-a-b-testing-html-vs-plain-text-emails)
- SitePoint's welcome test (image versus no image) was inconclusive: 118 versus 114 clicks. — [Conversion Sciences](https://conversionsciences.com/5-welcome-email-tests-turn-tryers-buyers/)
- Practitioner argument (Growth/Kogan): designed emails look like ads, while plain emails look like they come from a person and perform better for B2B and SaaS. This is opinion backed by anecdotal results. — [Greg Kogan: Don't design your emails](https://gkogan.co/dont-design-emails)

### Inferences
- For GoFindBuild, a hybrid approach is likely best: a lightly branded, single-column HTML email that reads like a letter, with a logo, a short headline, short paragraphs and one bulletproof button. This keeps tracking, accessibility and tap-friendly CTAs while capturing the "personal" advantage. Testing this against a plain founder-style version in HubSpot's A/B tool would settle it for this audience.

### Gaps
- No peer-reviewed or independent controlled study.
- No data specific to blue-collar or trades audiences.

---

## 7. Founder / personal "note" email conventions

### Takeaway
Many SaaS companies use plain-text-style emails, sent from a named person at a real reply-to address, for welcome and onboarding. The case for them is mostly anecdotal or vendor-reported; the only test data is the plain-text evidence in section 6.

### Cited Findings
- Userlist catalogues more than 20 SaaS companies that use "old school" plain-text emails for onboarding and founder notes. It reports their conventions: from a person's name, no header image, short paragraphs, a signature, often a question inviting a reply. — [Userlist: Why SaaS companies choose plain text emails](https://userlist.com/blog/saas-plain-text-emails/)
- Kogan argues plain emails get more replies and engagement because they resemble personal correspondence. — [gkogan.co](https://gkogan.co/dont-design-emails)

### Inferences
- In HubSpot, a founder note can be built with a single Rich Text module: no hero, left-aligned 16px text, a personal sender name, and a monitored reply-to. Use a text link or one small button. Asking a single reply question (for example "What trade are you in?") also generates engagement signals, which plausibly helps deliverability, though I found no source in this session to confirm that.

### Gaps
- No controlled data isolating "from a person" versus "from a brand" sender names in welcome emails. This was out of scope for this set of searches and may be covered by other researchers.
- Not covered due to tool limits: dark-mode rendering share and Gmail's 102KB clipping threshold. Both are relevant to HubSpot drag-and-drop output and worth a follow-up.
