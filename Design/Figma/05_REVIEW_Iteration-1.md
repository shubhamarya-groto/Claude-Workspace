# Iteration 1 · design review

Reviewed 25 Sep 2026. Section **Iteration 1** (`1233:5037`) in `aC59gtTG9nh2hwUraPnCXj`, eight
screens: Home, Job Seeker, Company and About Us, each at 1440 and at 393.

Every finding gives the band, its node id, and where on the band to look. Judged as a senior
designer would judge it before it goes to a client: what looks dated, what fights the brand, what
Brian will push back on, and what is simply not what that kind of page is supposed to contain.

## How to read it

| Mark | Meaning |
|---|---|
| **STOP** | Do not show Brian until this is fixed. It reads as unfinished work |
| **A** | Off-brand or dated. Costs credibility even when nobody can name why |
| **B** | Craft defect. Visible to a designer, felt by everyone else |
| **C** | Worth doing, not urgent |

## Verdict by screen

| Screen | Node | Verdict |
|---|---|---|
| Home, desktop | `1233:3617` | **Weakest of the four.** Three bands still carry Elevate's demo content, the band order contradicts the agreed structure, and the one dark band is unreadable |
| Home, mobile | `1233:3835` | Hero is the best thing in the set. Navigation is stuck open |
| Job Seeker, desktop | `1233:2992` | Solid spine, two dated bands, one internal note left on the page |
| Job Seeker, mobile | `1233:3168` | Hero is a flat orange screen that loses its own CTA |
| Company, desktop | `1233:3302` | Cleanest desktop page. Same two dated bands as Job Seeker |
| Company, mobile | `1233:3478` | Same orange hero problem, plus navigation stuck open in a second, different style |
| About Us, desktop | `1233:4070` | **Wrong content for the page it claims to be.** See the section at the end |
| About Us, mobile | `1234:8181` | Built to a different spec from the other three. Broken card text |

---

## STOP · Do not show these to Brian

**S-01 · Home, testimonial band** `1233:3713`, centre of the band
The quote still reads **"Add a testimonial quote #1 here. Keep it concise and impactful to enhance
credibility with your business"**, attributed to "Customer name one", "Customer role one", with a
**stock photo of a man handing over a bag of groceries** and a "Read case study" link that goes
nowhere. Five slider dots for one quote. The same band on Job Seeker `1233:3046` has the identical
placeholder. Two real quotes already exist and are sitting unused.

**S-02 · Home, FAQ band** `1233:3809`, all five rows
Still Elevate's sample questions for a **digital marketing agency**: "What services does your
digital marketing agency offer?", "How can your digital marketing agency help my business grow?".
The curated GoFindBuild questions are written and are already live on the other three pages.

**S-03 · Home, pricing band** `1233:3729`, middle card, 48px heading
**"Reccomended" is misspelled.** It is also being used as the tier's name, so the middle column has
no name at all beside Basic and Enterprise, and it is not visually featured despite being the
recommended one.

**S-04 · Job Seeker** `1233:3038` **and Company** `1233:3348`, caption under the card stack
An internal note is rendered as page copy: "[Copy] exact visible fields pending Brian's
confirmation (question 2)." It is my annotation and it must come off the canvas.

**S-05 · Home mobile** `1233:3836` **and Company mobile** `1233:3479`, top of page
Both pages ship with the **mobile menu stuck open**, in **two different designs**: Home uses a text
"Menu" label with list rows and orange dashes, Company uses a circled hamburger with outlined pill
buttons. Job Seeker mobile `1233:3169` is correct and closed. About mobile `1234:8182` has an
**empty circle where the hamburger icon should be**.

---

## Off-brand · things that are not this brand

**A-01 · Home, the two dark cards** `1233:3686`, the illustration at the top of each card
This is the worst aesthetic offender in the set. Both cards carry **Elevate's stock purple
paper-plane and envelope illustration**, a soft 3D cartoon in violet, **used twice, side by side**,
on a brand that is navy, orange, photographic and blue-collar. It says "SaaS template" in a way no
amount of surrounding copy can undo. Replace with the numbered steps treatment R3 already had, or
with photography.

**A-02 · Home final CTA** `1233:3769` **and Job Seeker final CTA** `1233:3121`, background
**Decorative gear outlines are back**, on a pale peach to pink gradient. Gear watermarks are audit
item A-21 from the old Squarespace site, logged as "old site only". They have returned, and the
pastel gradient is not in the palette. It reads consumer and soft. Construction hiring is neither.

**A-03 · Job Seeker** `1233:3038`, **Company** `1233:3348`, whole band
The same peach gradient carries the privacy band on two pages. Three of the eight screens now have
a warm pastel band. Cumulatively the site is drifting from "clean neutral base with purposeful
orange" to "orange and peach everywhere".

**A-04 · Pay and score in green** · Job Seeker `1233:3031`, Company `1233:3341`, About `1233:4112`
**$23/HR, $32/HR and 92% are set in green.** Green is the design system's success colour, not a
brand accent. It reads like a trading app. Money and match quality should carry the brand's own
emphasis, not a semantic state colour.

**A-05 · Job Seeker mobile hero** `1233:3175` **and Company mobile hero** `1233:3496`, whole band
**The mobile heroes are full-bleed saturated orange** while their desktop counterparts are dark
navy with the streak. The same page looks like a different company on a phone. Three consequences:
white body copy on `#F16C0E` is about 3:1 and **fails AA**; the trade chips are orange on orange;
and worst, **the primary button is orange on orange**, so "See who's available" and "See my
matches" all but disappear at the exact moment the page asks for the click.

---

## Dated · patterns that age the work

**B-01 · Accordion rows** · Home `1233:3809`, Job Seeker `1233:3104`, Company `1233:3414`, About `1233:4185`
Every FAQ is a stack of **filled rounded boxes with borders**. That is the 2016 accordion. R3
specified no fill and a bottom rule only. The boxes also put a hairline between every question,
which doubles the visual noise.

**B-02 · The photo collage** · Job Seeker `1233:3062`, About `1233:4143`, right side of the band
Three stock photos, tilted, rounded, overlapping, scattered like polaroids. It is a 2014 treatment,
the photos are unrelated stock, and **the pile overlaps the 723,000 numeral**, cutting into the
digits. On the About page this collage sits directly beside "Built by someone who has done the
work", where the only correct image is Brian.

**B-03 · Home, the two dark cards** `1233:3686`, the steps inside each card
The three steps are set as a **default ordered list**, "1." "2." "3." with hanging indents. It
reads like a pasted Word document. The numbered navy discs used on Job Seeker `1233:3062` and
About `1233:4143` are the right treatment and already exist.

**B-04 · Home hero fork** `1233:3621`, the two cards under the subhead
Plain white boxes, thin grey border, square-ish. They carry the single most important decision on
the site and look like form fieldsets. Compare them with the confidence of the hero photo treatment
directly to their right.

**B-05 · Footer** `1233:3826` and the same band on all four pages
A single row: wordmark, copyright, three links. No navigation, no trades, no social, no contact,
263px tall with most of it empty. For a two-sided marketplace this is the thinnest part of the site
and it gives search nothing. Audit A-23 asked for three columns.

---

## Craft defects

**C-01 · Home, band order** `1233:3617`
**The problem band sits at y 4450, after the FAQ**, second to last. The 15 Sep meeting agreed hero,
problem, solutions, proof, FAQ. As built, the reader gets the pitch, the price and the FAQ before
being told what the problem is. Also two different bands are both numbered **10** in the layer
names, which is how this kind of mistake survives review.

**C-02 · Home, problem band** `1233:3659`, headline and overline
**No scrim on the background image.** The orange streak runs directly behind the type: the first
two headline lines are grey on bright orange, and the overline **"WHAT'S AT STAKE" is effectively
invisible** because it is centred on the brightest point of the image. R3 specified a 55% dark
overlay. This is audit A-02 reappearing.

**C-03 · Top nav, Home** `1233:3618`, nav row
**"Job Seekers" is marked as the active page on the Home page.** Copied from the Job Seeker page.
On Home nothing should be active.

**C-04 · Card heights** · Job Seeker `1233:3031`, About `1233:4112`, both card rows
Titles wrap to two lines in one card and one line in the other, so **the cards are different
heights and their buttons do not align**. Same defect on Company `1233:3341`.

**C-05 · About mobile** `1234:8243`, both cards
The worker card shows **"92%" labelled "Compensation"** (it is a profile score), and the meta line
is **truncated mid-value: "Seeking full-time · 5."**. Titles wrap to three and four lines. The card
anatomy does not survive 390px and needs a mobile variant.

**C-06 · Avatar glyph** · Company `1233:3341`, About `1233:4112`
Worker profiles use the **same building icon as company job cards**. A person is not a building.

**C-07 · About mobile artboard** `1234:8181`
Built at **390 wide** while the other three mobiles are 393, and its bands use a different naming
convention from every other screen. It was clearly produced separately and has not been brought
into line.

**C-08 · Leftover hidden band** · About `1233:4119`
"Look first, reach out when you're ready" is still in the file, hidden, at the same y as the
testimonial band. Delete it or it will resurface.

**C-09 · Copy consistency** · Home `1233:3621` and `1233:3659`
"Post jobs - see matches today free!" and "Free forever - find the best paying jobs!" use hyphens
where the sentence needs a comma, and **two exclamation marks in two adjacent cards** read louder
than the rest of the site. The stat caption still contains em dashes: "as hard—or harder—to fill".
Home `1233:3682` has the same hyphen problem, and **"Skills" is capitalised mid-sentence** in the
left dark card heading on `1233:3686`.

**C-10 · Pricing card copy** `1233:3729`
Capitalisation differs card to card: "1 active job posting" against "Unlimited Active Job Posting",
"Basic Candidate filtering", "Email Support". "Custom." carries a full stop the other prices do
not. "Verified licences" is British spelling; the rest of the site is American.

**C-11 · Orange buttons, everywhere**
Every orange button still has a **white label, about 3:1, failing AA**: pricing `1233:3729` x3,
both final CTAs, both mobile heroes, the nav's Get Started. This is I-01 and it is one theme
setting, not a per-page fix.

**C-12 · Job Seeker FAQ, wrong audience first** `1233:3104`, row 1
The worker page opens its FAQ with **"What does it cost to hire through GoFindBuild?"**, a company
question, and follows it with "How does GoFindBuild match companies with skilled workers?". Two of
the five questions on the worker page are written for employers. The worker page should open with
"Is GoFindBuild free for workers?".

---

## Where Brian is likely to disagree

**D-01 · Pricing is on the page at all** `1233:3729`
Brian said the pricing diagram was a placeholder and might be dropped. The page now shows three
firm tiers at $49 and $149 that match neither the live site's per-applicant model nor his own
flat-monthly mockup. Expect a reaction. Either confirm the model or cut the band.

**D-02 · The problem band being last** `1233:3659`
He wrote the problem statement as the emotional hinge of the site. It currently arrives after the
price list.

**D-03 · His copy has been quietly reworded in places**
"Post a Job in 90 Sec" on `1233:3686` against his "Post a job in 90 seconds". Small, but he wrote
the copy and will notice.

**D-04 · Dark cards on the homepage** `1233:3686`
He said on the final CTA that he is "not a fan of the dark color, prefer very subtle". The two
largest cards on the homepage are now solid dark navy with purple artwork.

---

## About Us needs different content, not just better styling

This is the clearest structural miss in the set. The page is currently: header, two product cards,
a testimonial, three beliefs, FAQ, CTA, footer. **Two of its six bands are product bands borrowed
from the Company page**, so it reads as a product page wearing an About headline. Everything an
About page exists to do is missing.

What it has now:

| Band | Node | Judgment |
|---|---|---|
| Header | `1233:4074` | Keep. Brian's line is the right hook |
| Two sides, one network | `1233:4112` | **Move out.** Product content, and the two cards look identical so the point does not land |
| Testimonial | `1233:4127` | Keep, but a worker quote is the wrong proof on an About page |
| Why we built it | `1233:4143` | Keep the copy. Replace the stock collage |
| FAQ | `1233:4185` | Keep, shorten |
| Final CTA | `1233:4202` | Keep |

What is missing, in the order it should run:

1. **A face.** "Built by someone who has done the work" with a stock collage beside it is a promise
   with no proof. One photograph of Brian, on site, is worth the whole band. This is the single
   biggest change on the page.
2. **A place.** Nothing says where GoFindBuild operates. Indianapolis and central Indiana are all
   over the example data and never stated as fact. Local trust is most of the sell here.
3. **The origin, as a story with dates.** Twenty years in construction, what went wrong when hiring,
   when the product started, what exists today. A simple timeline band does more for credibility
   than any of the current product cards. Elevate ships `multi-row-alternating` for exactly this.
4. **Who is behind it.** Even three people. Elevate ships `team-members` and `team-members-two-column`.
   If the team is one person, say so plainly: that is a strength for a small contractor, not a gap.
5. **What we will not do.** The beliefs band is three numbered steps, which reads as a how-it-works.
   Values are stronger stated as commitments: no recruiters in the middle, free for workers always,
   skills over paperwork. Same words, different form, no numbers.
6. **A way to reach a person.** Elevate ships a `contact` preset. On a page about who you are,
   ending with a job-post button and no phone number is a missed hand.

Worth knowing before rebuilding: **Elevate ships `about-us` and `about-us-one-column` presets** that
were not used. Check them first.

---

## What is good, and should survive the next round

- **Home hero** `1233:3621` and **Home mobile hero** `1233:3856`. The folder-tab photo treatment is
  the best idea in the file, and the mobile stat pill is a strong opening line.
- **Job Seeker and Company dark headers** `1233:2996`, `1233:3306`. The streak with the search bar
  is confident and distinctive.
- **The three-step flow card** on `1233:3062` and `1233:4143`. Numbered navy discs, clear hierarchy,
  good rhythm. It is the pattern the homepage's dark cards should have used.
- **Company `02 Workers near you`** `1233:3341`. Showing the bench before asking for the post is the
  right strategic move and it reads well.
- **The band rhythm across the three sub-pages.** Home is the odd one out precisely because it does
  not follow it.

---

## Order to fix

1. The five **STOP** items. Half a day, and the deck stops looking unfinished.
2. **C-01** band order and **C-02** the missing scrim. These are structure and legibility.
3. **A-01** the purple illustrations and **A-05** the orange mobile heroes. Biggest brand wins.
4. **A-02, A-03** gears and peach. **B-01** accordions, **B-02** collage. The dated layer.
5. **C-11** the button contrast, once, in theme settings.
6. **About Us**, rebuilt to the content list above.

---

**How this was reviewed.** Every band captured from the Figma file at 1440 and 393 and judged
visually. Contrast calls are from the rendered colours. Structure and layer names read from the
file. Nothing here is inferred from the plans: it is what the screens actually show today.
