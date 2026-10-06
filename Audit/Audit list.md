# Audit list · GoFindBuild

Every audit in `Source files/`, compiled into one checklist on 22 Sep 2026.
**Tick an item the moment it's cleared.** Keep ticked items in the list: the ticks are the record.

## How to use it

- **Tick only when the fix is live** on the site or shipped in the product. Designed isn't cleared.
- Each item carries a status for today:
  - **In R3**: the Figma hi-fi already solves it (`Design/Figma`). Tick once it's live.
  - **Old site only**: that part of the old Squarespace site doesn't exist in the new design. Tick once the new site replaces the old one.
  - **Open**: nothing solves it yet.
- `H-xx` points to the live-page check in `Design/HubSpot/Home/02_SITE_Changes-Needed-Home-Page.md`.
- Severity comes from the source audit. Where two audits rated the same point differently, the higher rating is kept. "Not rated" means the source gave none.
- Sources are shown in `code`: `D` Desktop, `M` Mobile, `U` UX (marketing site), `#` dashboard spreadsheet row, `R` responsive PDF row, `T` other-tabs PDF row, `BR` Brian's review.

## Summary

| Section | Items | Critical | Today |
|---|---|---|---|
| A · Marketing site | 30 | 7 | 17 in R3 · 5 old site only · 8 open |
| B · Employer dashboard, main screens | 42 | 14 | all open |
| C · Dashboard, other tabs | 50 | 2 | all open |
| D · Brian's review of the dashboard designs | 28 | not rated | all open |

**Before ticking anything in B, C or D:** the Figma file has newer logged-in screens (Flow A Hi-Fi,
`867:833`, screens A5 to A8). Check each item against those first.

## Sources merged

| File | Scope | Items | Note |
|---|---|---|---|
| Audit Go find Build X Groto - Desktop Audit.csv | Marketing site, desktop | 19 | `GoFindBuild_Design_Audit.xlsx` and its `(1)` copy hold the same 19 |
| Audit Go find Build X Groto - Mobile Audit.csv | Marketing site, phone | 16 | `GoFindBuild_Mobile_Design_Audit.xlsx` holds the same 16 |
| Audit Go find Build X Groto - UX Audit.csv | Marketing site, conversion | 11 | no severity column |
| GoFindBuild_Design_Audit_Final_v2 (1).xlsx | Employer dashboard | 39 | latest of four versions. `(2)`, `Final_v2` and `Grouped_By_Severity` are earlier or regrouped copies. Rows 7 and 12 are the same issue |
| Dashboard(Responsive) Audit.pdf | Employer dashboard | 30 | visual version of the spreadsheet. 4 items it adds are B-39 to B-42 |
| Dashboard audit other Tabs.pdf | Profile, projects, hiring, support, settings | 50 | |
| UX Review - 7_1.docx | Brian's review, 1 Jul | 28 notes | two identical copies |

---

## A · Marketing site

From the May audits of the old Squarespace site, checked against R3 and the live HubSpot demo.

### Critical

- [ ] **A-01 · Critical · The hero doesn't say what GoFindBuild is.** Rotating words, three audiences at once, one vague CTA. → One-sentence promise, split CTAs for hiring and for work.
  `U1` · **In R3**, live on the demo · the fork buttons link nowhere yet (H-15)
- [ ] **A-02 · Critical · Hero text unreadable on phones.** White headline straight on the photo, no scrim. → Keep the headline off the photo, or add a gradient.
  `M2` · **In R3**, live on the demo · tick after a check on a real phone
- [ ] **A-03 · Critical · No type hierarchy.** Every weight looks the same; mobile headings wrap to three lines. → Four-level scale, separate mobile scale, headings at most two lines.
  `D1` `M5` · **In R3** · live: only the H1 uses the display face (H-10); the phone H1 wraps to five lines
- [ ] **A-04 · Critical · CTA buttons inconsistent and narrow on phones.** Four or more styles for one action; mobile buttons 55 to 70% wide. → Exactly two variants, the same label per action, full-width and 48px tall on phones.
  `D3` `M3` · **In R3** · live: two different oranges, 2.03:1 contrast (H-09); phone buttons aren't full width
- [ ] **A-05 · Critical · The two landing pages look like two different sites.** → Shared hero template, card, icon set and section rhythm.
  `D2` · **Open** · applies to For companies and For workers, not designed yet
- [ ] **A-06 · Critical · Mobile menu has no context.** Bare full-screen overlay, no active page, no close label. → Drawer with logo, active page, a labelled close button and a dimmed backdrop.
  `M1` · **Open** · the live page uses Elevate's drawer: check its close button and active state
- [ ] **A-07 · Critical · Stats unreadable on phones.** One column, 3 to 4 line paragraphs, citations under each. → 2 × 2 grid, one-line captions, citations collapsed into one line.
  `M4` `D14` · **Open** · R3's captions still run two to three lines
- [ ] **A-08 · Not rated · No social proof.** No testimonials, company logos or real platform numbers. → Real quotes from both sides; logos and counts once permitted.
  `U3` · **In R3** (two real quotes) · live shows Elevate sample testimonials with stock photos (H-05)

### High

- [ ] **A-09 · High · Orange overused, and orange text fails contrast.** → Orange for CTAs and one or two accents; a darker orange for text.
  `D4` `M16` · **In R3** (orange/500 for small orange text) · live button contrast fails (H-09)
- [ ] **A-10 · High · Mixed icon styles.** Emoji, flat illustrations and photo circles together; pain-point emoji at 16px; oversized feature icons. → One icon set, sized to the text.
  `D6` `D15` `M10` `M13` · **In R3** (Lucide only) · live still shows Elevate sample illustrations (H-21)
- [ ] **A-11 · High · Hero photo crops subjects badly.** → Art direction: 20% breathing room, never crop at joints, text side left clear.
  `D7` · **In R3** (folder-tab welder photo) · live hero is a 2.8 MB screenshot (H-12)
- [ ] **A-12 · High · Pricing hidden, then flat.** No pricing on the homepage; tiers look identical; no tap affordance on phones. → Visible pricing, a highlighted recommended tier, a button per card.
  `U2` `D8` `M6` · **In R3**, soft until the pricing model is decided (I-12) · live: recommended tier not highlighted (H-22)
- [ ] **A-13 · High · Navigation gives no bearings.** No active or hover state; Login and Sign up look like plain links. → Active underline, hover state, filled Sign up button, clear For companies / For workers split.
  `D9` `U5` · **Open** · live nav is Elevate's default menu (H-18)
- [ ] **A-14 · High · Spacing has no rhythm.** Sections crammed, then far apart; mobile padding varies from 8 to 24px. → Spacing scale on an 8px grid, one mobile container.
  `D5` `M7` · **In R3** (spacing tokens) · check the live page
- [ ] **A-15 · High · Section photos float above text with no connection.** `M8` · **Old site only**
- [ ] **A-16 · High · Gear illustration looks broken on phones.** `M9` · **Old site only**

### Medium

- [ ] **A-17 · Medium · How it works is unnumbered and unconnected.** Only one of three steps is styled. → Numbered steps, a connector, the same treatment for every step.
  `D10` `M11` `U8` · **In R3** (numbered, one flow per audience) · live: numbered, but in dark sample cards (H-21)
- [ ] **A-18 · Medium · Too many backgrounds, including pure black.** Seven treatments per page. → Three backgrounds; navy or dark slate instead of black.
  `D11` `U10` · **In R3** · live band 03 is a red texture (H-20)
- [ ] **A-19 · Medium · Job card mockup is tilted and truncated.** → Flat card with a fixed anatomy.
  `D13` · **In R3** (Job Match Card) · live shows Elevate sample cards (H-04)
- [ ] **A-20 · Medium · Page too long on phones.** 12+ screens, no sticky CTA or back-to-top. → Sticky CTA after the hero, back-to-top button.
  `M12` · **Open** · the live phone page is 13,633px tall
- [ ] **A-21 · Medium · Decorative gear watermarks.** `D12` `M14` · **Old site only**
- [ ] **A-22 · Medium · Circular photo collage with meaningless lines.** `D16` · **Old site only**

### Low

- [ ] **A-23 · Low · Footer has no legal or utility links.** → Three columns: platform, support, legal.
  `D17` `U7` · **In R3** (legal links plus trade columns) · live Privacy and Legal links are empty (H-15)
- [ ] **A-24 · Low · Footer tap targets under 44px.** → 44 × 44px touch area around each icon.
  `M15` · **Open** · check the live footer icons
- [ ] **A-25 · Low · Logo lockup kerning.** → Tight, unified wordmark.
  `D18` · **In R3** (Source Serif 4 wordmark) · live logo is a screenshot (H-13)
- [ ] **A-26 · Low · Section copy too long, no room under headings.** → Subtitles at most two lines, 16px under the heading.
  `D19` · **In R3** · check the live page

### Not rated

- [ ] **A-27 · Not rated · Profanity in the CTA banner.** `U4` · **Old site only** · not in Brian's copy
- [ ] **A-28 · Not rated · Stats typos ("023") and inconsistent citations.** `U6` · **In R3** · Brian's copy fixes both
- [ ] **A-29 · Not rated · No favicon.** → Export the logomark at 32 and 192px, plus an apple-touch-icon.
  `U9` · **Open** · none is set on the live page
- [ ] **A-30 · Not rated · No way to stay in touch for visitors not ready to sign up.** → Job-alert email capture or a lead magnet.
  `U11` · **Open** · not in R3, needs a decision

---

## B · Employer dashboard, main screens

All **Open**. Screens: dashboard, Add New Skill modal, sidebar, mobile drawer.

### Critical

- [ ] **B-01 · Critical · Empty dashboard gives no onboarding.** Raw 0 counters and red error alerts. → Numbered setup checklist, progress bar, info icons, a success state. `#1` `R1`
- [ ] **B-02 · Critical · Add New Skill: the dropdown spills outside the modal.** → Grow the modal or expand the list inline. `#2` `R2`
- [ ] **B-03 · Critical · The dropdown shows four trades with no scroll cue.** → Scrollbar and a fade at the bottom. `#3` `R3`
- [ ] **B-04 · Critical · Confirm and Cancel are hidden behind the open dropdown.** → Sticky footer, plus "Done selecting" in the dropdown. `#4` `R4`
- [ ] **B-05 · Critical · KPI cards show 0 in heavy black.** → Muted 0, a nudge line ("Post a job to get applications"), distinct icon banners. `#5` `R5`
- [ ] **B-06 · Critical · The action button in the dropdown is cut off.** → Fully visible, labelled "Clear all". `#6` `R6`
- [ ] **B-07 · Critical · The sidebar stays expanded at 768px.** → Collapse to an icon rail at tablet width. `#7` `#12`
- [ ] **B-08 · Critical · Desktop-only layout.** → Define desktop and mobile breakpoints. `#8`
- [ ] **B-09 · Critical · No notifications anywhere.** → Bell with an unread badge, an alert tray, toasts. `#9` `R7`
- [ ] **B-10 · Critical · The account menu is hidden at the bottom of the sidebar.** → Avatar and account dropdown at the top right. `#10`
- [ ] **B-11 · Critical · KPI cards turn into huge blocks on phones.** → Compact horizontal cards, icons at most 48px. `#11` `R8`
- [ ] **B-12 · Critical · The mobile drawer has no close button or backdrop.** → Close (X) in the header, dimmed backdrop. `#13` `R9`
- [ ] **B-13 · Critical · The trade categories section breaks on phones.** The edit icon floats loose. → Title on top, full-width "Edit categories" button. `#14` `R10`
- [ ] **B-14 · Critical · Skill tags become full-width blocks on phones.** → Inline tags that fit their text. `#15`

### Major / Medium

- [ ] **B-15 · Major · Mixed icon styles in the sidebar.** → One icon library. `#16` `R14`
- [ ] **B-16 · Major · KPI icon containers differ in size.** → Identical containers. `#17`
- [ ] **B-17 · Major · Weak modal title and subtitle hierarchy.** → Title 18 / 600, subtitle 14 / 400 muted. `#18`
- [ ] **B-18 · Major · Selected pills use a full-saturation blue.** → Light tint with dark text. `#19`
- [ ] **B-19 · Major · Activities empty state: huge illustration, tiny text.** → 80px illustration, 16 / 500 headline. `#20`
- [ ] **B-20 · Major · The sidebar collapse button is hard to see.** → Hover state and a tooltip. `#21`
- [ ] **B-21 · Major · "+1" overflow hides selections.** → Tooltip listing the hidden items. `#22` `R17`
- [ ] **B-22 · Major · No global search.** → Search in the top bar, with a keyboard shortcut. `#23` `R18`
- [ ] **B-23 · Major · Identical "Take Action →" buttons.** → Labels that say what each does. `#24` `R19`
- [ ] **B-24 · Major · Logout sits in the main navigation.** → Move it to the account menu. `#25` `R20`
- [ ] **B-25 · Major · No focus rings.** Keyboard users can't see where they are. → Visible 2px focus ring on everything interactive. `#26` `R21`
- [ ] **B-26 · Major · The icon-only sidebar at 1024px has no labels.** → Tooltips, or expand on hover. `#27`
- [ ] **B-27 · Major · Long tags break the Add New Skill modal on phones.** → Truncate and wrap. `#28` `R22`
- [ ] **B-28 · Major · Success Center icons are top-heavy at 768px.** → Centre the icons. `#29` `R23`
- [ ] **B-29 · Major · "Messages" is missing its icon in the mobile drawer.** `#30` `R24`
- [ ] **B-30 · Major · The mobile top bar is logo and hamburger only.** → Add the avatar and bell. `#31` `R25`
- [ ] **B-31 · Medium · No top navigation bar or page header.** The audit's own summary calls this the single highest-leverage fix: it unlocks notifications, search, account access and logout placement. → Top bar with the page title and utility actions. `#33` `R11`
- [ ] **B-32 · Medium · Flat cards, no elevation system.** → A consistent shadow and elevation scale. `R12`
- [ ] **B-33 · Medium · The Success Center shows only errors, even when there's nothing to fix.** → Positive states and a completion state. `R13`
- [ ] **B-34 · Medium · Body, labels and metrics are too close in size.** → A clearer type scale. `R15`
- [ ] **B-35 · Medium · Red means both error and critical notification.** → Semantic colours for error, warning, info and success. `R16`

### Minor / Low

- [ ] **B-36 · Minor · A wrench icon beside the trade categories misleads.** → Neutral tag icon. `#32` `R26`
- [ ] **B-37 · Minor · The modal close button is 16px.** → 36px visual, 44px touch target. `#34`
- [ ] **B-38 · Minor · The Success Center card can't be dismissed.** → A success state once everything is done. `#35` `R28`
- [ ] **B-39 · Minor · Name and company are the same size in the sidebar footer.** → 14px name, 12px company at 60%. `#36`
- [ ] **B-40 · Minor · The dropdown search has no icon and a vague placeholder.** `#37` `R29`
- [ ] **B-41 · Minor · The collapse chevron points inconsistently.** `#38`
- [ ] **B-42 · Minor · Mobile cards touch the screen edges.** → 16 to 20px side padding. `#39` `R30`

---

## C · Dashboard, other tabs

All **Open**. Rated as the source rated them: two Critical, one not rated, the rest Medium.

### Across the platform

- [ ] **C-01 · Critical · Empty states are dead ends.** No explanation or next step. → Guided empty states with a clear action. `T1`
- [ ] **C-02 · Medium · Headers and page structure differ between sections.** → One page framework for every module. `T2`
- [ ] **C-03 · Not rated · Profile sections just say "Not specified".** → Say why it matters and add a CTA ("Add operational details"). `T3`

### Company profile and onboarding

- [ ] **C-04 · Medium · Five steps that feel like enterprise setup.** → Progressive disclosure, a completion indicator, a time estimate. `T4`
- [ ] **C-05 · Medium · The whole flow runs inside a modal.** → Full page or side panel. `T5`
- [ ] **C-06 · Medium · Nothing explains why the information matters.** → Value messaging and completion benefits along the way. `T6`
- [ ] **C-07 · Medium · No sign that progress is saved.** → Auto-save, drafts, resume later. `T7`
- [ ] **C-08 · Medium · Related details are scattered.** → Group into Company, Operations, Compliance, Certifications, Branding. `T8`
- [ ] **C-09 · Medium · Jargon goes unexplained: EMR, OSHA, Net 15, liability insurance.** → Helper text and examples. `T9`
- [ ] **C-10 · Medium · Chips, dropdowns and multi-selects pile up.** → Searchable autocomplete, grouped choices. `T10`
- [ ] **C-11 · Medium · It ends abruptly on uploads.** → Completion summary, profile strength, a success moment. `T11`
- [ ] **C-12 · Medium · It assumes one uninterrupted sitting.** → Smaller milestones, resumable progress. `T12`
- [ ] **C-13 · Medium · Large modals and horizontal selectors won't fit phones.** → Mobile-first stacked steps. `T13`
- [ ] **C-14 · Medium · No review step before submitting.** → Review and confirm, with a profile preview. `T14`

### Projects and finding trade partners

- [ ] **C-15 · Medium · Posting a project asks every decision at once.** → Stages: Basics, Scope and trades, Vendor preferences, Review. `T15`
- [ ] **C-16 · Medium · No guidance on what makes a good listing.** → Tips, examples, recommendations. `T16`
- [ ] **C-17 · Medium · No drafts or auto-save.** `T17`
- [ ] **C-18 · Medium · My Projects, Find Trade Partners and Search Projects feel like separate tools.** → One flow from posting to matching. `T18`
- [ ] **C-19 · Medium · Decisions aren't prioritised.** → Reveal advanced options only when needed. `T19`
- [ ] **C-20 · Medium · Filtering overload.** → Smart search, autocomplete, progressive filters. `T20`
- [ ] **C-21 · Medium · Discovery is entirely manual.** → Recommendations and matching. `T21`
- [ ] **C-22 · Medium · No quality check before publishing or searching.** → Completeness indicator, publish-readiness check. `T22`
- [ ] **C-23 · Medium · After publishing, no status or activity.** → Lifecycle states, activity summary, next steps. `T23`
- [ ] **C-24 · Medium · Weak or empty results are a dead end.** → Recovery suggestions. `T24`
- [ ] **C-25 · Medium · One flow for every role.** → Role-based flows. `T25`
- [ ] **C-26 · Medium · Won't scale as projects and vendors grow.** → Scalable search, saved preferences. `T26`
- [ ] **C-27 · Medium · Repeat users re-enter everything.** → Templates, saved searches, duplicate project. `T27`
- [ ] **C-28 · Medium · Context is lost when switching sections.** `T28`
- [ ] **C-29 · Medium · Filters and long forms are hard on phones.** `T29`

### Hiring and job posts

- [ ] **C-30 · Medium · Posting a job asks everything in one flow.** → Staged steps with guidance. `T30`
- [ ] **C-31 · Medium · No help writing a good job post.** → Templates, suggested defaults, quality checks. `T31`
- [ ] **C-32 · Medium · No drafts, templates or "duplicate job".** `T32`
- [ ] **C-33 · Medium · Posting, matching and applicants feel like separate modules.** → One hiring journey. `T33`
- [ ] **C-34 · Medium · One flow for every hiring type** (apprentice, part-time, urgent). → Adaptive flows. `T34`
- [ ] **C-35 · Medium · After publishing or with no matches, no next step.** → Hiring insights and recovery. `T35`
- [ ] **C-36 · Medium · Filters and state are lost when moving between hiring sections.** `T36`
- [ ] **C-37 · Medium · Long hiring flows are hard on phones.** `T37`
- [ ] **C-38 · Medium · "Why work here" has a full formatting toolbar.** → Remove tools a job post doesn't need. `T38`

### Support

- [ ] **C-39 · Medium · Support opens as a small modal.** → A support page: raise an issue, track it, view history. `T39`

### Settings and account

- [ ] **C-40 · Medium · Settings pages feel disconnected.** → One account area with setup progress. `T40`
- [ ] **C-41 · Medium · Empty billing, users and notification pages don't guide setup.** `T41`
- [ ] **C-42 · Medium · No roles or permissions for team members.** `T42`
- [ ] **C-43 · Medium · Risky actions have no safeguards** (delete user, change password, billing). → Confirmation, verification, undo. `T43`
- [ ] **C-44 · Medium · Security is just a password page.** → Security centre: two-factor sign-in, active sessions, password strength. `T44`
- [ ] **C-45 · Medium · Context is lost across admin tasks.** `T45`
- [ ] **C-46 · Medium · Notification settings are on/off only.** → By category, urgency and channel, with digests. `T46`
- [ ] **C-47 · Medium · Billing is payment entry and history only.** → Invoices, subscription, renewals. `T47`
- [ ] **C-48 · Medium · Success messages vanish with no next step or undo.** `T48`
- [ ] **C-49 · Medium · Settings are built for tiny teams.** → Multiple admins, department controls. `T49`
- [ ] **C-50 · Critical · The primary account can be deleted,** locking the company out. → Require ownership transfer to another verified admin first, with clear warnings. `T50`

---

## D · Brian's review of the new dashboard designs (1 Jul)

Brian's requests and open decisions, not audit findings. All **Open**.
`JK:` marks replies already in the document.

### Design changes Brian asked for

- [ ] **D-01** Put the profile score and experience score at the top of the dashboard, beside "Complete your profile". `BR`
- [ ] **D-02** Consider folding "Complete your profile" into the to-do list; keep the photo step separate. `BR`
- [ ] **D-03** Keep: the to-do list, Overview (profile views, job matches, applications), My applications, Actions required, code-verification login. `BR`
- [ ] **D-04** Rethink or remove "What you'll unlock": Brian doesn't follow it. `BR`
- [ ] **D-05** Rethink "No job matches yet, finish profile": link straight to job postings instead? `BR`
- [ ] **D-06** "Recommended for you" is too early without training links. Remove it, or fill it with local training centres and career initiatives. `BR`
- [ ] **D-07** Explain or remove "+Create" at the top right. `BR`
- [ ] **D-08** Remove the calendar for now. `BR`
- [ ] **D-09** "Your profile is live": put boosting the score front and centre, and gently warn workers who apply with a score below a threshold. `BR`
- [ ] **D-10** The first welcome screen targets job seekers only. Design how people get there from the marketing site. `BR`
- [ ] **D-11** Fast "Almost there" onboarding. Confirm the minimum fields (name, phone for text alerts, zip, over 18, trade categories, "your trade" questions), then show the profile score page and to-do list, or the long form with a skip. `BR`
- [ ] **D-12** Set-off questions for low-experience and general laborer profiles. `BR`
- [ ] **D-13** "Companies hiring near you" needs the browser's location. `BR`
- [ ] **D-14** 151 trade categories: typeahead with pills after three characters, maybe a few broad groups. Location comes from the zip code. `BR`
- [ ] **D-15** Don't advertise platform numbers on the welcome screen yet. `BR`

### Product and dev decisions from the same review

- [ ] **D-16** Define "AI job matches", or rename it. `BR`
- [ ] **D-17** Decide what the OSHA field shows when nothing is selected. `BR`
- [ ] **D-18** A defined formula for the profile score; later, an AI interview as one input. `BR`
- [ ] **D-19** Rank profile fields by importance. `BR`
- [ ] **D-20** Should completing the profile unlock anything? `BR`
- [ ] **D-21** Use Messages for platform-to-user communication (opted-in users only). `BR`
- [ ] **D-22** Merge the job-match and company-match emails into one: jobs first, skip companies already listed. `JK` agreed. `BR`
- [ ] **D-23** Remove "Find me opportunities": show all matches on the dashboard and make job invitations free. `JK`: no more opt-in; the risk is companies spamming workers. `BR`
- [ ] **D-24** AI detection of attempts to bypass the paywall (numbers typed out, email redirects). `JK`: ticket exists. `BR`
- [ ] **D-25** Quiz integrity: allow paste but flag likely cheating; list other cheating signals. `BR`
- [ ] **D-26** Red-flag screening questions for non-skilled job seekers, such as frequent job changes. `BR`
- [ ] **D-27** Company quizzes to validate trade categories, plus ratings (communication, reliability, quality, cost). Also a growth play: companies invite their crews. `BR`
- [ ] **D-28** Let companies add their own questions to a job post and see answers before unlock. Depends on bypass detection being airtight. `BR`
