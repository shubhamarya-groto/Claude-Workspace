# AI hero photo options (I-20 Company, I-21 Job Seeker)

Generated 23 Oct 2026 in Magnific (Seedream 5 Pro, 2K, 3:2, 100 credits each, 600 total), in the style of the
Plumbing page photo Brian named as his reference. They're saved in the Magnific account's Personal project.
**Not reviewed yet:** this container can't load the image host (`pikaso.cdnpk.net`), so check each one by eye before showing the team.

## Round 2 (23 Oct): distinct people

Shubham's feedback on round 1: the people all look the same. Round 2 prompts describe every worker separately by age,
ethnicity, build and features, so each photo has different, ordinary-looking faces (600 credits). **Round 2 replaces round 1.**

| Code | Page | People | Open in Magnific |
|---|---|---|---|
| C1 | Company · framing crew | White man, late 50s, grey goatee, heavyset; Latino man, early 20s, backwards cap; Black man, mid 30s, short beard | https://www.magnific.com/app/creation/UPdAW1Iwny |
| C2 | Company · HVAC crew | Bald white man, mid 40s, ginger beard, on the ladder; Black woman, late 20s, braids, holding the duct | https://www.magnific.com/app/creation/N2vVdwk6D9 |
| C3 | Company · electrical crew | Latino man, late 50s, grey moustache, reading glasses, at the spool; lanky white man, early 20s, stubble, on the ladder | https://www.magnific.com/app/creation/gOpZnrYSXO |
| J1 | Job Seeker · carpenter | Black man, mid 40s, salt-and-pepper beard, broad build | https://www.magnific.com/app/creation/0e1vunRTfW |
| J2 | Job Seeker · plumber | Latino man, early 30s, moustache, tattooed forearms, stocky | https://www.magnific.com/app/creation/O68YVJiynm |
| J3 | Job Seeker · electrician | White woman, mid 30s, freckles, ponytail under a work cap | https://www.magnific.com/app/creation/N2vVdNg6D9 |

## Round 1 (superseded)

| Code | Page | Trade | Brief | Open in Magnific |
|---|---|---|---|---|
| C1 | Company | Framing crew | Three carpenters framing a house: nail gun, carrying a stud, checking a level. Overcast daylight | https://www.magnific.com/app/creation/SyeZx8jUb8 |
| C2 | Company | HVAC crew | Two HVAC technicians fitting metal ductwork in an unfinished commercial ceiling. Window light | https://www.magnific.com/app/creation/gOpRrIDSXO |
| C3 | Company | Electrical crew | Two electricians pulling wire through metal studs, one on a ladder, one at the spool | https://www.magnific.com/app/creation/gOpRrmeSXO |
| J1 | Job Seeker | Carpenter | Cutting a board with a circular saw on sawhorses, sawdust flying, house frame behind. Morning sun | https://www.magnific.com/app/creation/0e1hGwWTfW |
| J2 | Job Seeker | Plumber | Soldering copper pipe in an unfinished basement, kneeling, small torch flame, work lamp | https://www.magnific.com/app/creation/jUTN5tXLD0 |
| J3 | Job Seeker | Electrician | Wiring an outlet box in an exposed stud wall, wire strippers, cable along the studs | https://www.magnific.com/app/creation/EbismTmuuO |

Every prompt also said: candid documentary photo, absorbed in the work, not posing, not looking at the camera, realistic natural colours, no text, no logos.

## Getting them into Figma

Placing them on the Presentation page (`493:1016`) was blocked three ways on 23 Oct:
1. `upload_assets` refused: "You do not have permission to edit this file". The connector account is a **View** seat in the org that owns the file.
2. The image host `pikaso.cdnpk.net` is blocked by the environment's network policy, so the files can't be fetched here.
3. The Figma connector hit its seat's call limit.

`Design/Figma/scripts/hero-photo-options-board.js` builds the labelled board (six 1200 × 800 slots, C1 to J3, with captions) to the right of
the Marketing Website section. Run it with `use_figma` once the limit resets, then paste each image into its slot:
select the slot, then paste the image, or use Fill > Image.
