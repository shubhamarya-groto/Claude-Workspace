# For companies · the page we're replacing

Read live on 23 Sep 2026 at 1024 desktop and 375 phone: **gofindbuild.com/companies**, Squarespace.
Contrast ratios and sizes below are measured off the rendered page, not estimated.

This is the redesign context: what the page is today, what it does well enough that losing it would
be a step back, what dies, and where each surviving piece lands in the new page. The new page's
plan is `Design/Figma/04_CONTEXT_Company-Page.md`.

---

## The page in one paragraph

Seven content bands between a fixed header and a footer. 4,180px tall at 1024 wide, **7,326px on a
phone, about nine screens**. It introduces the product, names three pains, publishes the whole
price list, offers a free projects feature, and closes with a paragraph about the company. It is
honest and complete, and it is completely quiet: **there are twelve links on the page and six of
them go to the same generic sign-up.** Nothing on it asks a company to post a job.

## What it gets right, and the redesign must not lose

1. **"Built by a 20 year construction veteran."** The only credibility line anywhere on the site,
   and the exact answer to "why should I trust another hiring tool". Brian's mockup has no line
   about who built this. Carry it over.
2. **The price list is the most complete thing GoFindBuild has published.** Post a job free, $25 to
   invite, $99 / $199 / $399 to unlock by skill level, each with a plain-English reason. Whatever
   the new model is, this page proves the audience will read detail if it is written like this.
3. **The three pain points are in the customer's words,** not marketing language: hiring is slow and
   expensive · training from scratch usually isn't an option · skilled trades are hard to find.
4. **"Find your next project, free"** is the only public sign that the trade-partner side exists.
5. **It is light.** About 70 requests, and on a warm cache well under 200 KB with a one second
   load. The new HubSpot demo makes 82 requests and its hero image alone is 2.8 MB. The old page is
   currently the faster of the two. Don't regress that on launch day.

---

## Band by band

| # | Band | What's on it now | Verdict | Where it goes |
|---|---|---|---|---|
| 00 | **Header**, fixed, 66px | Logo, Companies, Job Seekers, Login (outline), Sign up (filled). No Home link, no pricing link, no active state | Rebuild | New nav, active state on For companies (A-13) |
| 01 | **Hero** | Navy panel, headline 72px Teko in four lines with "with" alone on line three, "GoFindBuild" in orange, a stock portrait bleeding off the right edge, and a skewed orange and blue banner reading "Let me in! / Create your free profile", both lines at the same 32px | **Kill the layout.** Keep nothing but the audience | New band 01: Brian's headline, the trade and ZIP bar, one button |
| 02 | **We know the struggle** | H3, the veteran line, then three navy cards with emoji-style icons (hourglass, tools, diamond) carrying the three pain points | **Keep the copy, kill the cards** | New band 03, left column. Veteran line moves near the proof |
| 03 | **Let's change the game** | H3 and a paragraph: there are talented candidates, matching shouldn't be a headache, general laborers to master electricians | **Compress to two lines** | New band 03, right column |
| 04 | **Pricing** | H3, then three rows (Post a job · Free, Invite job seekers · $25 per invitation, Unlock applicants) and three tier cards, CANDIDATE $99 · SKILLED APPLICANT $199 · EXPERT APPLICANT $399 | **Depends entirely on I-12.** This is the public source of the old model | New band 05, as Brian's comparison. Numbers only once pricing lands |
| 05 | **Find your next project** | Light blue panel, gear illustration, free crews and subcontractors copy | **Shrink** | One FAQ answer (seed H7), question 22 |
| 06 | **Why GoFindBuild?** | Navy band, a paragraph about competitive edge, a Sign up button, a four-photo collage with orange corner brackets | **Replace** | Proof (band 06) and the final CTA (band 09) do this job properly |
| 07 | **Footer** | "© 2025 GoFindBuild", logo, LinkedIn and Facebook icons | Rebuild | New footer, with legal links |

---

## What is measurably broken

| # | Finding | Measured | Audit |
|---|---|---|---|
| 1 | **The page has no H1.** Zero H1, one H2, four H3, seven H4. The page title is an H2 | counted in the DOM | A-03 |
| 2 | **Every call to action fails AA.** Blue `#0095E2` with white text | **3.28:1**, AA needs 4.5:1 | Blocker 1 |
| 3 | The three price tier labels, blue on white | **3.06:1**, fails | A-09 |
| 4 | **No body webfont.** Body type resolves to generic `sans-serif`. Headings are Teko, some sub-heads are Inter, the mobile menu renders in the system font | computed style | A-03 |
| 5 | **The hero photo is upscaled and cropped.** Source is 1024 × 466, shown in a 1009 × 925 box on cover, so roughly half the frame is enlarged about 2× | natural vs rendered | A-11 |
| 6 | The headline wraps to **four lines** at desktop and four at 375, with an orphan | rendered | A-03 |
| 7 | **On a phone the first screen is a photo.** The stock portrait takes the top ~330px, the headline is cut by the fold, the CTA is below it | 375 × 812 | A-02 |
| 8 | **Nine phone screens, no sticky CTA, no back to top** | 7,326px | A-20 |
| 9 | **The mobile menu is a blank white screen with two links floating in the middle,** in the fallback font, no active page, no Home, no label on the close | opened at 375 | A-06 |
| 10 | Social icons are **28 × 28**, under the 44px target | rendered | A-24 |
| 11 | **Footer says © 2025** and carries no Terms or Privacy link | rendered | A-23 |
| 12 | **Empty meta description.** No og:image, no apple-touch-icon. Title uses Squarespace's em dash | head tags | A-29 |
| 13 | **Broken links.** Two sign-up URLs carry `utm_source=null&utm_medium=null&utm_campaign=null`, and one `href` ends in a space | `https://app.gofindbuild.com/signup ` | new |
| 14 | Every image except the logo has **empty alt text** | 6 images | new |
| 15 | **No phone number, no email, no contact link anywhere on the page** | 0 `tel:` or `mailto:` | new |

---

## The two faults that matter more than the list

**1. The page never asks for a job post.** "Post a job" appears once, as the first row of the price
list, where it is a price and not a button. Every action on the page is "Sign up", pointing at a
generic sign-up form that doesn't know whether the visitor is hiring or looking for work. The one
thing the business needs from this page, a posted job, is never requested. That is the single
biggest conversion defect here, above any contrast or type problem.

**2. It explains the product instead of showing it.** There is no worker card, no job card, no
proof, no FAQ, and no sign that anyone is on the platform. A company owner leaves knowing what
GoFindBuild claims and nothing about what it holds. Brian's own mockup fixes exactly this by
putting a worker card in the hero, and Jeff's note moves the cards onto this page.

---

## Copy that survives, verbatim

Worth keeping in one place, because the new page's plan assumes it exists.

| Piece | Copy |
|---|---|
| Credibility | "That's exactly why GoFindBuild was built by a 20 year construction veteran: to make finding skilled labor easier, faster, and more reliable." |
| Pain 1 | "Finding the right talent is time-consuming and expensive." |
| Pain 2 | "Training entry-level employees from scratch often isn't an option." |
| Pain 3 | "Skilled tradespeople are hard to come by, especially for specialized roles." |
| Turn | "There are talented candidates eager to work in the skilled trades, you just need a better way to connect with them." |
| Range | "Whether you're hiring general laborers or master electricians, GoFindBuild makes it easy to find who you need, when you need them." |
| Post a job | "Once you post a job, we immediately start finding the best matches from our network of talented job seekers who have the skills and experience that your job requires." |
| Invite | "$25 per invitation, you can connect with your ideal candidates and fill your positions faster." |
| Unlock | "When you find a promising applicant, you can unlock their contact information to schedule an interview. The cost to unlock an applicant is dependent upon the applicant's skills and experience." |
| Projects | "Need skilled crews for framing, carpentry, masonry, or other trades? Stop wasting time searching in the wrong places!" |

The turn line uses an em dash on the live page, shown here as a comma.

---

## Decisions this teardown forces

1. **What does `/companies` say on launch day?** It is the public source of the per-applicant
   prices. If the new page ships with Brian's flat-monthly comparison, these numbers have to come
   down at the same moment, or the two pages contradict each other in public (I-12).
2. **Does the URL stay `/companies`?** It sets the nav label question (I-14) and whether a redirect
   is needed. Whatever happens, the old URL must not 404: companies Brian met have this link.
3. **Keep the veteran line?** Brian's mockup has no "who built this". My recommendation is to keep
   it, because on a page selling to people who bought from a handshake, the founder is the product.
4. **Does "Find your next project" survive at all?** One FAQ answer is my recommendation
   (question 22). Deleting it silently removes the only public trace of the feature.
5. **Is there a human route?** No phone, no email, nothing. On a page whose entire acquisition
   channel is Brian in person, that is worth one decision (question 24).

---

## How this was read

Browser pane, 23 Sep 2026. Desktop at 1024 wide, phone emulated at 375 × 812. Heading sizes,
colours, contrast ratios, image dimensions, tap targets and link targets read from the rendered
page. Page weight measured with a warm cache, so treat it as approximate.

**Sources.** gofindbuild.com/companies · `Audit/Audit list.md` section A ·
`Read me/02_ISSUES-LOG.md` (I-12, I-14) · `Read me/03_BLOCKERS_for-Harpreet.md` (item 1, contrast) ·
`Design/Figma/04_CONTEXT_Company-Page.md` (the page that replaces this one).
