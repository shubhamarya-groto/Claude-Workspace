# GoFindBuild staging audit, 4–5 Nov 2026: flows checked and functional issues

**Figma:** the "Audit Summary — Flows checked & functional issues" section (`1745:3`), to the right of the Company Flow section on page **Audit-5th nov**: [open](https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign?node-id=1745-3). Each screen code in the Figma table links to its annotated frame.

This list covers **only problems that stop the system working correctly**: failures, data loss, wrong data, broken access or privacy rules, and invalid data that gets accepted. UI-consistency and UX polish items (U-xx and the yellow pilot notes) are left out on purpose. Those are in `00_SCREEN-INDEX.md`.

## Flows checked
**Company: "Groto-testing Private Limited"** (Shubham Arya), Nov 4, 7:33 PM → Nov 5, 3:14 PM, 82 screens
- A · Auth & signup: role select, login, company step 1, create account, email code, set password, first dashboard
- B · Post a job: dashboard, Job Postings, post form, publish, job detail, Actions
- C · Company profile edit: 5-step wizard, 3 submit attempts
- D · Search projects & trade partners: search, project detail, Connect, other company's profile
- E · Applicants, unlock & messaging: applicants, match profile, free unlock, message, reply

**Job Seeker: "Shubham Job Seeker"**, Nov 5, 1:06 PM → 3:14 PM, 35 screens
- A · Signup: landing (trades + zip), create account, registration, trade & location
- B · Dashboard, Find Jobs, job detail, save, Profile, My Jobs
- C · Apply to job
- D · Profile edit wizard and the completed profile
- E · Messaging with the company

**Not covered:** paid unlock / payment simulation, AI skills quizzes, multiple job seekers, mobile.

## P0 · Blockers (a core task can't be completed)
| # | Issue | What happens & impact | Screens · refs |
|---|---|---|---|
| 01 | Company profile can never be saved | Every Submit fails with a generic error and no field-level reason (3 attempts, with or without files). The profile stays "Not specified" and the "missing" reminder can never be cleared | C-58, C-60, C-62, C-45 · T-08, T-20, T-21, T-06 |
| 02 | Edit Profile modal throws away all input | Clicking outside closes the 5-step modal with no warning; fields are empty on reopening | C-52, C-44 · T-22, T-07 |
| 03 | Required question can't be answered | The duplicate "Are you at least 18? *" Yes/No buttons don't respond | J-21 · T-23 |
| 04 | Job seeker onboarding doesn't save correctly | "We couldn't save your profile", yet the user lands on the dashboard; landing-page trades are dropped | J-05, J-04 · T-14, T-13 |

## P1 · Broken (wrong data, broken logic, or access / privacy rules not enforced)
| # | Issue | What happens & impact | Screens · refs |
|---|---|---|---|
| 05 | Paywall bypass on match profiles | Match profile opens in full with no unlock gate; the applicant profile is gated | C-70, C-76 · T-24 |
| 06 | Privacy leak: work history before apply or unlock | Employer, dates and reason for leaving are visible, against the seeker form's promise | C-72, J-19 · T-27 |
| 07 | Wrong trades saved to the seeker profile | The saved set was never chosen, and it drives matching | J-06, J-12, C-76 · T-15 |
| 08 | Job location is wrong | Zip 12345 (NY), Indianapolis company → shown as "Los Angeles, CA" | C-41, J-08 · T-03 |
| 09 | Job search ignores location and the trade rule | A NY zip returns the LA job; search runs with no trade | J-08 · T-18 |
| 10 | Match and application counts wrong, never recalculated | 2 matches before any job; 4 applications vs 1; job shows 0 matches | C-24, C-26, C-73, C-74 · T-01, T-10, T-28 |
| 11 | False "Invalid or expired code" errors | Shown after successful verification | C-24 · UX #12 |
| 12 | Messages show the person, not the company | Sender shows as "Shubham Arya" with a worker avatar | J-33 · T-19 |
| 13 | Save (star) on the job page does nothing | Star doesn't respond; only reflects a save made from the search card | J-09, J-16 · T-32 |
| 14 | Search filters reset after viewing a job | Zip, trades and type revert on Back | J-31, J-08, J-18 · T-37 |
| 15 | Affiliation dropdown won't close | No close on blur or outside click | C-50 · T-31 |
| 16 | SMS checkbox silently disabled; phone shows no error | Looks clickable; nothing explains what blocks it | J-22 · T-33, T-34 |
| 17 | Experience level and years contradict, and go live | "< 1YR" + "Master" accepted and shown to employers | J-26, J-30, C-71 · T-29, T-30, T-26 |
| 18 | Seeker location inconsistent | Profile shows 97206; last zip submitted was 97602 | J-12, J-05 · T-17 |
| 19 | Phone shown that was never entered (to verify) | (213) 456-7890 on the unlocked profile | C-79, J-22 · T-11 |

## P2 · Bad data accepted (missing validation)
| # | Issue | What happens & impact | Screens · refs |
|---|---|---|---|
| 20 | City / state / zip not cross-checked; 4-digit zip | Indianapolis+Nevada+4620; Indianapoli+Missouri+46204; "Seattle, IN 46220" | C-44, C-53, C-70 · T-35, T-36, T-25 |
| 21 | Compensation accepts an absurd or inverted range | "1234567890-98765"; "/hours" appended | C-41, C-43 · T-04, T-05 |
| 22 | Project start date year 3222 | Raw JS date format | C-68 · T-09 |
| 23 | Zip error stays after a valid zip | — | C-40 · T-02 |
| 24 | Unread badge not cleared | — | C-82 · T-12 |
| 25 | Profile completion % wrong | 83% after a failed save | J-06 · T-16 |
