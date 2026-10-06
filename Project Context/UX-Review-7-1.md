# UX Review – 7/1 (Brian's feedback & meeting notes)

_Converted from `Source-UX_Review_-_7_1.docx`. The upload `UX_Review_-_7_1_1.docx` was byte-identical, so only one copy is kept._

Core fields for matches

1.  Location (we use distance from zip code. Openroute can return coordinates from zip code or city, state)

2.  Trade categories (there are 151 of them - maybe there’s a way to make a few categories for general searching?) Typeahead with pills, first 3 characters should be enough

Job Seeker Onboarding - Welcome

1.  Don’t know that we have numbers we want to advertise (yet)

2.  For Companies hiring near you, would have to try to get geolocation from browser

Almost there

1.  GFB should rank fields by importance

2.  Would need a well-defined formula for a profile score (at some point, add AI interview to profile score criteria)

Dashboard

1.  Not sure what “AI” job matches is

OHSA - what to show if nothing selected

Brian

- what do we think about profile completion leading to “unlock”

- Maybe GFB could communicate with users via “Messages” function

- This all assumes user has opted in

1.  Eliminate job post match email - would like to just make this same notification as company match email (eliminates the double email, which is likely going to be most common) JK: Maybe combine to a single email with jobs then companies, do not list companies that have jobs listed

2.  Eliminate "find me opportunities" - consolidate all matches on dashboard like design shows and allow company to contact any matches they want and send job invitation for free (eliminate double charge) JK: To clarify, then: 1. No more opt-in, 2. Send jobs is free - only risk of that is company just spamming the users with jobs

3.  Explore using AI to detect any and all forms of bypassing our paywall (companies typing a phone number using digits, typing out numbers, trying to re-direct via email, etc. when using typing boxes JK: We have a ticket for this already - won’t be difficult

4.  During quizzes, allow copy/paste but indicate job seeker likely cheated, also ask what other methods would somebody try (typing quickly initially but then deleting and typing, scanning online during grading to see what Google AI summary indicates and determine similarities, etc. and indicate likely cheating

5.  We talked about it but want to expand or elaborate on what type of questions we can ask non-skilled job seekers to sniff out red flags (how many jobs have you had in the past 2 years (frequent job turnover), etc. - (Ask AI what the most common employer red flags are for employees and build questions around those)

6.  Want to discuss specs for implementing quizzing for companies to strengthen their profile and validate their core service trade categories and also implement reputation building with ratings (Communication/reliability/quality of work/cost) not sure legally if I need to require comments but initially I'm thinking no since that requires a online tit for tat police force. - To discuss with UX team \[this is also a virality play - requesting your crews and subcontractors to join GFB to help your company reputation build

7.  Allow companies to ask their own questions as part of their job post and see answers before unlock - ? (ASK UX) - AI cheating with phone or other attempted contact outside GFB has to be bulletproof for this

UX/UI FEEDBACK:

1.  On dashboards - I like the to-do list and I've seen this before with construction software I've used particularly when they have had multiple training videos

2.  At the top of dashboards, I think this is where we nest the profile score and experience score (add this) since complete your profile is right there - is this redundant if we have the to-do list and can add any blank questions there, quizzes, etc. I like having photo separate but maybe we can consolidate the list some, especially when it comes to profile questions left un-answered

3.  I like the "Overview" items (profile views, job matches, Applications)

4.  I do not understand the "what you'll unlock" section, not sure we need the "no job matches yet - finish profile" section - maybe this can be direct click to job postings or they scroll here?

5.  I like the concept of the "recommended for you" section but maybe we are too early for this since we have not linked to any training yet - OR we add in local training places, career centers, local initiatives, etc.

6.  Not sure what the +Create is for at the top right of the dashboard

7.  Calendar is not needed yet, I like the "my applications" and "actions Required" sections

8.  I like the "your profile is live" page - boosting your score should be front and center - if we guide them right to apply to jobs their profile will be shit - we should also throw them a notification or alert if they apply to a job and their profile score is below "X" and basically let them know they will not find a job being lazy...in a nice way. I do like the data displayed, but I also fear it will not be ideal while we are still early

9.  I need to review the marketing site he worked on, but the first design tile is targeted only to job seekers - how do they get here from the marketing site?

10. I do like the code verification to access, especially faster via mobile and could minimize spam

11. If we convert to "Almost there" and take the fast process to onboard - need to confirm bare minimums but I'm thinking (name, phone - text notifications?, zip code - location, are they 18, trade categories, all questions on "your trade" - after these present the profile score page and to-do list OR present the long form profile giving them the choice to bypass it (go to dashboard) and we may have some that willingly spend the time to finish it all (some have)

Low exp / General Laborer - set off questions
