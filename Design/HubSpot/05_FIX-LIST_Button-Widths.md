# Button widths · fix list (fill container → hug content)

14 Oct 2026. Every button on the four staging pages measured in the static previews at **375** (phone), **768**
(tablet) and **1440** (desktop): actual width against its natural "hug" width.
All fixes are in shared module CSS, so each one fixes every page that uses the module.

**Status: items 1–5 fixed on 14 Oct 2026.** Module CSS updated in the repo and in HubSpot (`gfb_hero_v2`,
`gfb_final_cta`, `gfb_top_nav`, `gfb_worker_card`); module edits go live on published pages without a republish.
Re-measured at 375: Get Started 127, Hire workers 169, Find jobs 141, Post a job / Find work 155,
Create my free profile 247, Send job 167 + View profile 126 in one row. No horizontal scroll.

## Fixed (were stretched on phone, hug on desktop)

| # | Component (module, file) | Buttons | Pages | Phone 375 | Tablet 768 | Desktop 1440 | Rule causing it |
|---|---|---|---|---|---|---|---|
| 1 | **Hero** (`gfb_hero_v2`, `Home/code/gfb-hero/module.css` l.189) | Hire workers, Find jobs | Home, Companies, Job Seekers | **Fill** 277 (hug 141–169) | Hug | Hug | `@media (max-width:767px) .gfb .gfb-btn { width:100%; justify-content:space-between }` |
| 2 | **Final CTA, card layout** (`gfb_final_cta`, `Home/code/gfb-final-cta/module.css` l.136–137) | Post a job, Find work, Create my free profile | All four (closing band) | **Fill** 293 (hug 155–247) | Hug | Hug | `.gfb-cta__buttons { flex-direction:column; align-self:stretch }` + `.gfb-cta__btn { justify-content:space-between }` |
| 3 | **Final CTA, banner layout** (same rules) | Post a job, Find work | About Us header | **Fill** 295 (hug 155) | Hug | Hug | Same rules as #2 (banner shares them) |
| 4 | **Top nav drawer** (`gfb_top_nav`, `Home/code/gfb-top-nav/module.css` l.131) | Get Started (in the menu drawer) | All four | **Fill** 343 (hug 127) | **Fill** 720 | n/a (no drawer) | `.gfb-nav__cta--drawer { width:100% }` |
| 5 | **Worker card** (`gfb_worker_card`, `For companies/code/gfb-worker-card/module.css` l.80) | Send job, View profile | Companies (band 05) | **Both fill** 305, stacked (hug 103 / 126) | Send job 272 + View profile hug, one row | Same as tablet (as Figma) | `@media (max-width:767px) .gfb-wc__actions { grid-template-columns: minmax(0,1fr) }` stacks them |

**Fix applied for 1–4:** on phone the buttons keep their natural width (`max-width:100%`, drawer CTA `align-self:flex-start`,
Final CTA buttons `align-items:center`), stacked with the same gap, and let a button wrap only when its text is longer than
the screen. The arrow disc stays next to the label instead of being pushed to the far edge.
**Fix applied for 5:** keep the tablet/desktop row on phones (Send job flexible + View profile hug), as the Job card
already does, instead of stacking both full width.

## Checked, no change suggested

| Component | Buttons | Why it stays |
|---|---|---|
| Pricing (`gfb_pricing`, Home) | Start free trial, Continue with Starter, Go Pro | Full width of each plan card at every size (phone, tablet and desktop alike), so not a phone-only stretch. Not checked against Figma: confirm the plan cards are meant to have full-width buttons |
| Job card (`gfb_job_card`, Job Seekers band 05) | Apply now (fills), View (hugs) | Same on all sizes and matches Figma (Apply now 290 wide, View 88). Phone keeps one row |
| Match cards (`gfb_match_cards`) | Send job / Apply | Hug at every size |
| Top nav bar | Get Started | Hug; hidden on phone (shown in the drawer, see #4) |
| Alternating rows (About Us) | Learn More | Text link, hugs |
| Footer | Links and social buttons | Not stretched |

## How it was measured

The four page previews (Home rendered fresh from the current modules with their default Home content) opened in
Chromium at 375 / 768 / 1440, menu drawer opened, every button's width compared with the same button at
`width:auto`. A button counts as stretched when it is more than 24px wider than its content. HubSpot's live pages use
the same module CSS, so they behave the same; the HubSpot editor badge seen in the screenshots is not part of the page.
