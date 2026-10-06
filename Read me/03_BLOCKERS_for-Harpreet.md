# What I need unblocked, GoFindBuild marketing site

For Harpreet. Rewritten 19 Sep 2026 after reading Brian's 11 Sep mockup brief.
Draft on track for Monday 21 Sep EOD.

**Four of the seven items on the previous version are now closed.** Brian's
mockup already answered them: the testimonials exist, the worker three-step
flow is written, the banner profanity is gone, and there is a usable hero photo.
What is left is sharper and mostly needs Brian rather than GTM.

---

## Decisions only Brian can make

**1. Button colour, and it is a real accessibility problem.**
Measured against WCAG on his own mockup:

- Orange `#F77F00` with white text, used on Get started, Hire workers, Post a
  job, See who's available: **2.63:1**. Fails AA and also fails AA-Large.
- Blue `#0095E2` with white text, used on Apply now, Send job, Create my free
  profile and every card action: **3.28:1**. Fails AA.
- Navy `#003049` with white text, used on Find jobs: **13.82:1**. Passes.

AA requires 4.5:1 for text this size. So every orange and every blue action on
the site fails, and the only compliant primary button is the navy one he already
designed.

The fix is not a rebrand. **Promote the navy button to primary everywhere and
keep orange for accents that carry no text** (wordmark, icons, progress dashes,
the hero accent word). Brian asked specifically that we "follow the best
guidelines proven to work best", so this is answering his question, not
second-guessing his taste.

Worth knowing: the same defect is in our design system, marginally less bad at
3.05:1. It needs fixing in both or they drift.

**2. Whose card is canonical?**
Brian has drawn a Job Post preview card. Our design system already has a Job
Match Card (`891:189`) doing the same job in a different visual language. Two
versions of one component is how a system dies early. I would merge them,
keeping his emphasis on pay and distance and the system's match percentage, but
he should agree the merged card is the one that gets built.

**3. What came out of the Tuesday pricing conversation?**
Brian flagged the pricing diagram as a placeholder for the 15 Sep discussion and
said it may be left out initially. Our notes from that meeting contain no
pricing decision. His mockup shows a flat-monthly model set against a staffing
agency's 18 to 25% markup, which is a different model from the per-applicant
pricing still live on the site. I need to know which is real before that band
gets built, or whether it is cut for launch.

**4. Navigation.**
His mockup uses Home / For companies / For workers. The design system nav uses
Companies / Job Seekers / Pricing. Small, but it sets the URL structure and the
trade pages hang off it, so better settled now.

---

## Still with GTM

**5. Which trades first, and keyword targets?**
For the category pages. My recommendation is two pages per trade rather than
one, because "hire plumbers" and "plumbing jobs" convert differently. Built as
two templates so GTM can add trades without coming back to design.

**6. The typography feedback.**
Lower priority now. I am building Monday on the design system, Instrument Sans
for display and Inter for body, which is a direct answer to Brian's ask to
"optimize the font". His mockup uses Open Sans. If GTM has a view, now is the
time.

---

## Scope, unchanged and still worth raising

**7. Is the marketing site and the HubSpot build inside the current engagement?**
`Project Context/Project-Scope.txt` is six phases, all about the platform and product. A
marketing website and a HubSpot implementation are not in it. Also: the current
site is on **Squarespace** and the plan is HubSpot, so this is a migration, not
a restyle, and a one week estimate reads differently in that light.
Implementation starts around 23 Sep, so better settled before that week than
after.

---

## Nice to have, not blocking

**8. More photography.** The welder shot is 1400 x 799, which is enough to work
with. Brian asked for photos elsewhere on the page too. Originals at 2400px on
the long edge would open that up.

**9. Testimonial permissions.** Two real quotes are in the mockup, from Matthew
B. and from Brothers Insulation & Construction. Confirm we can use the names and
locations publicly, and whether a photo or logo exists for either.

---

## Schedule

| | |
|---|---|
| First Figma draft | Mon 21 Sep EOD |
| Direction approved, best case | Tue 22 Sep |
| HubSpot implementation, ~1 week | Tue 23 Sep to Mon 29 / Tue 30 Sep |
| Launch target | end of September |

Only item 1 really needs answering before Monday, and I can draft both ways if
it is quicker to decide in the room.
