# Changes needed on Home page · live site

Page: **https://247469662.hs-sites-na2.com/demo**, published 21 Sep 2026 in the HubSpot test
portal **1 Meter House** (free plan, Elevate theme).
Checked **22 Sep 2026** against the Figma hi-fi **R3** (`1075:228`, Marketing website page), at
1280 and 1440 wide on desktop and 375 on a phone.

**Priority:** P0 fix before anyone sees it · P1 theme settings pass · P2 speed and robustness ·
P3 links and basics · R3 design differences.
**Where:** [Editor] page or global content · [Theme] Edit theme settings · [CSS] child theme ·
[Module] custom module · [Files] HubSpot Files.

---

## What's working, keep it

- Hero matches R3 closely: headline with the orange accent, both fork cards, the welder photo in
  the folder-tab shape.
- Hero buttons pass contrast: Hire workers is navy on orange at **5.09:1**, Find jobs **15.5:1**.
- Only Inter and Instrument Sans load. No Satoshi or SF Pro.
- No layout shift while loading. No sideways scroll at any width. Phone menu works.
- "Better opportunities…" now stacks instead of sitting in two columns.

---

## P0 · Fix before anyone sees it

- [ ] **H-01 · Under the hero · [Editor]** A **SNACKZO** logo (another brand, `snackzo_logo.png`,
  alt text "logio") sits where the trust bar should be. Remove the logo gallery.
- [ ] **H-02 · Under the hero · [Editor]** Trust bar missing. Add the three check-badge items:
  Direct employer connections · No recruiter middlemen · 150+ trade categories.
- [ ] **H-03 · 03 Problem + stats · [Editor]** Elevate sample content: "About us / Elevate Your
  Online Presence" and Elevate's paragraph. Replace with Brian's problem statement: "The workers
  are out there. / The opportunities are out there. / The connection between them is broken."
- [ ] **H-04 · 06 Preview cards · [Module]** Two Elevate "Content Creation" sample cards. Replace
  with the Job Seeker preview card and the Job Match Card.
- [ ] **H-05 · 07 Testimonials · [Editor]** Elevate's sample slider: "Add a testimonial quote #1
  here", "Customer name one", "Read case study", stock photos. Replace with Brian's two quotes
  (Matthew B., Carpenter · Brothers Insulation & Construction). **Don't pair real customers'
  names with stock faces.**
- [ ] **H-06 · 09 FAQ · [Editor]** Elevate's "digital marketing agency" questions. Replace with the
  seven GoFindBuild questions from R3.
- [ ] **H-07 · 10 Final CTA · [Editor]** Elevate's "E" logo above the heading. Remove it.
- [ ] **H-08 · Typos · [Editor]**
  - [ ] 04–05: "Automatically get matched to the **S**kills you need**.**" → "…the skills you need"
  - [ ] 04–05: "Post a Job in 90 Sec" → "Post a job in 90 seconds" (Brian's copy)
  - [ ] 06: "What company sees" → "What **a** company sees"
  - [ ] 08: "Reccomended" → "Recommended"
  - [ ] 08: "Custom." → "Custom"
  - [ ] 08: "Verified licences and certificates" → "Verified licenses and certifications" (US)
  - [ ] 10: "The **R**ight connection" → "The right connection"

---

## P1 · Theme settings pass

- [ ] **H-09 · All buttons outside the hero · [Theme]** Fill `#FF9902` with `#F7F9FC` text is
  **2.03:1**, failing AA and AA-Large. Set the primary button to `#F16C0E` with a navy `#16243D`
  label, as the hero already is (5.09:1). Fixes nav Get started, pricing Get started ×2, Contact
  sales, final CTA Post a job in one change. If hover goes darker it drops below AA: use a
  lighter hover, `#F4811F` (I-18).
- [ ] **H-10 · All headings except the hero H1 · [Theme]** Still Elevate's default Inter at 57,
  43 and 32px. Set H2 and H3 to Instrument Sans (H2 = Display 3xl, 48px).
- [ ] **H-11 · 10 Final CTA · [Editor]** "Find work" button missing, so workers have no path at
  the end of the page. Add the secondary button.

---

## P2 · Speed and robustness

- [ ] **H-12 · 01 Hero visual · [Files] then [Module]** A **2,788 KB screenshot PNG** hosted on an
  outside Cloudinary account (`res.cloudinary.com/rm6jyi4n/…/Screenshot_2026-09-21_at_4.54.35_PM.png`).
  Heaviest file on the page by far; the largest element took about **5 s** on a fast connection.
  The frosted card's text is baked into the image: unreadable on a phone, invisible to screen
  readers and search. Breaks if that Cloudinary account changes.
  Short term: WebP around 200–300 KB, uploaded to HubSpot Files. Proper fix: the custom hero
  module with live text.
- [ ] **H-13 · Nav logo · [Editor]** The logo is a screenshot, alt text "Screenshot 2026-09-21 at
  4.53.48 PM". Use a proper logo file with alt text "GoFindBuild".
- [ ] **H-14 · 03 stat rules · [CSS]** The orange rules are 29 × 3 PNGs stretched to 59 × 6
  (blurry), alt text "Rectangle 6667419". Use a CSS border, or at least empty alt text.

---

## P3 · Links and basics

- [ ] **H-15 · Links · [Editor]** 16 dead links (`#`, empty or missing): Homepage (logo),
  Get started ×3, **Hire workers**, **Find jobs**, Read case study ×5, Contact sales, Post a job,
  Privacy Policy, Legal. The fork buttons should go to For companies and For workers.
- [ ] **H-16 · Footer · [Editor]** Social icons point to linkedin.com, facebook.com, twitter.com,
  instagram.com and tiktok.com home pages. Link GoFindBuild's accounts or remove them.
- [ ] **H-17 · Page settings · [Editor]** Title is "Demo", no meta description, language en-GB.
  Set a real title and description, language en-US.
- [ ] **H-18 · Nav · [Editor]** Elevate's default Home / Products / Pricing / Blog / Company.
  Set Companies · Job Seekers · Pricing (label choice still open, I-14).

---

## R3 design differences, seen in the same check

- [ ] **H-19 · 01 Hero** Stat pill missing: "723,000 worker hires needed every year →".
- [ ] **H-20 · 03 Problem + stats** Red texture background instead of R3's dark streak. Navy text
  on red is low contrast. "WHAT'S AT STAKE" overline missing.
- [ ] **H-21 · 04–05 How it works** Dark navy cards with Elevate's envelope illustrations, instead
  of R3's soft light cards with numbered navy discs.
- [ ] **H-22 · 08 Pricing** "Recommended" card isn't the navy featured card. Each card has a button;
  R3 has none (I-22).
- [ ] **H-23 · Phone** About 150px of empty space between the hero image and the next section.
- [ ] **H-24 · Headings** The four stats are H2 headings, and "Better opportunities. Better
  workers." / "One construction network." are still two H2s. One heading reads better for screen
  readers and search.

---

## How this was measured

- Contrast calculated from the rendered colours on the live page.
- Speed measured in the browser on a fast connection, not a throttled phone. Google PageSpeed was
  over its shared daily quota on 22 Sep. A real phone will be slower than the ~5 s above.
- 82 requests on load. Biggest file: the hero PNG at 2,788 KB, then two font files around 110 KB each.
- Visits and traffic weren't checked: the portal's analytics aren't connected here, and a test
  page published a day earlier has no meaningful traffic yet.
