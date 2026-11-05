# GoFindBuild Onboarding Audit, 5 Nov 2026: screen index

Live audit of the staging app (`staging-app.gofindbuild.com`). We created two test accounts and ran each one through onboarding and the main tasks:

- **Company:** "Groto-testing Private Limited", user Shubham Arya (sidebar: Dashboard, Messages, Company Profile, Trade Partners, Find employees)
- **Job Seeker:** "Shubham Job Seeker" (sidebar: Dashboard, Messages, Profile, Find Jobs, My Jobs)

**Figma file:** `aC59gtTG9nh2hwUraPnCXj` (GofindBuild-Website-Redesign), page **Audit-5th nov** (`1719:3107`)

| Section | Node | Link | Screens |
|---|---|---|---|
| Company Flow | `1722:3` | [open](https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign?node-id=1722-3) | C-01…C-82 |
| Job Seeker Flow | `1722:92` | [open](https://www.figma.com/design/aC59gtTG9nh2hwUraPnCXj/GofindBuild-Website-Redesign?node-id=1722-92) | J-01…J-35 |
| Reference (old "Section 1") | `1720:3227` | **missing from page, see note** | R-01, R-02 |

Each screenshot layer is renamed `<code> · <original screenshot name>` (example: `C-05 · Screenshot 2026-11-04 at 7.34.56 PM 1`). A code label sits above each screenshot, so you can search the code in Figma to find it.
Error states are marked **⚠**.

## Canvas layout (updated 5 Nov)
- The Job Seeker Flow section now sits directly **below** the Company Flow section.
- Each **phase** (A–E) is one row. Its screens run **left to right** in the order you go through the flow.
- Each **unique screen** is a column with a name label on top. Other states of the same screen (typing, dropdown open, error, modal) are **stacked under it**.

| Phase | Columns, left → right (stacked states in brackets) |
|---|---|
| C-A Auth & Signup | Role select [C-01, C-03] · Login [C-02] · Company onboarding Step 1 [C-04…C-15] · Create profile [C-16, C-17] · Registration successful [C-18] · Confirm account [C-19…C-23] · Dashboard first load [C-24, C-25] |
| C-B Dashboard & Post a Job | Dashboard [C-26] · Job Postings empty [C-27] · Post a job form [C-28…C-40] · Job detail [C-41, C-42] · Job Postings active [C-43] |
| C-C Profile Edit Wizard | Company Profile page [C-45] · Step 1 Contact [C-44, C-46, C-52, C-53] · Step 2 Business [C-47] · Step 3 Services [C-48, C-54, C-59] · Step 4 Credentials [C-49, C-50, C-55] · Step 5 Additional [C-51, C-56, C-57, C-58, C-60, C-61, C-62] |
| C-D Search Projects | Search Projects [C-67] · Project detail [C-63, C-66, C-68] · Other company profile [C-64, C-65] |
| C-E Applicants & Messaging | Dashboard [C-73, C-75] · Job Postings [C-74] · Job detail Applicants [C-69] · Candidate profile, match [C-70…C-72] · Candidate profile, applicant (unlock, message) [C-76…C-81] · Messages [C-82] |
| J-A Signup | Landing [J-01] · Create profile [J-02] · Registration successful [J-03] · Trade & location [J-04, J-05] |
| J-B Dashboard & Find Jobs | Dashboard [J-06] · Find Jobs [J-07, J-08, J-11] · Job detail [J-09, J-10] · Profile [J-12, J-13] · My Jobs [J-14, J-15] |
| J-C Apply | Job detail [J-16, J-17] · Find Jobs [J-18] |
| J-D Profile Wizard | Step 1 Basic info [J-19…J-22] · Step 2 Experience & Certs [J-23…J-27] · Completed profile [J-28…J-30] |
| J-E Messaging | Find Jobs [J-31] · Messages [J-32…J-35] |

To see when a screen was captured, check the original screenshot name in its layer (for example `Screenshot 2026-11-05 at 12.08.44 PM`).

---

## Company Flow (`1722:3`)

### A · Auth and company signup
| Code | Node | Screen and context |
|---|---|---|
| C-01 | 1720:3108 | Role select: "Create your free profile", Job Seeker / Company cards |
| C-02 | 1720:3109 | Login: "Welcome back" (harpreet@letsgroto.com) |
| C-03 | 1720:3110 | Role select again (Company path) |
| C-04 | 1720:3111 | Company step 1 "Skilled trades workers, ready to hire": empty (company name, trades, zip) |
| C-05 | 1720:3112 | Step 1: company name entered |
| C-06 | 1720:3113 | Step 1: General Contractor chip selected |
| C-07 | 1720:3114 | Step 1: "Browse by trade" dropdown open (151 trades) |
| C-08 | 1720:3115 | Step 1: dropdown, Close button hover |
| C-09 | 1720:3116 | Step 1: selecting Acoustical & Decorative Ceilings |
| C-10 | 1720:3117 | Step 1: typeahead "ele", 2 matches (Electrical, Elevators) |
| C-11 | 1720:3118 | Step 1: 3 trades, dropdown open |
| C-12 | 1720:3119 | Step 1: same, scrolled |
| C-13 | 1720:3120 | Step 1: trades done, zip present, Continue disabled |
| C-14 | 1720:3121 | Step 1: valid zip, Continue enabled |
| C-15 | 1720:3122 | Step 1: partial zip, Continue disabled |
| C-16 | 1720:3123 | Create profile: first/last/email empty, Google sign-in |
| C-17 | 1720:3124 | Create profile: filled |
| C-18 | 1720:3125 | Registration successful: "check your email" + Enter confirmation code |
| C-19 | 1720:3126 | Confirm Account: 6-digit code + new password, rules list |
| C-20 | 1720:3127 | Confirm: typing confirm password |
| C-21 | 1720:3128 | Confirm: both passwords visible |
| C-22 | 1720:3129 | Confirm: focus state |
| C-23 | 1720:3130 | Confirm: new-password focus |
| C-24 | 1720:3131 | ⚠ First dashboard load: browser save-password prompt + 2× "Invalid or expired code" toasts |
| C-25 | 1720:3132 | ⚠ Dashboard: Success Center, stats, Employee Matching; toast still shown |

### B · Dashboard and post a job
| Code | Node | Screen and context |
|---|---|---|
| C-26 | 1720:3189 | Dashboard: 0 applications, "No Jobs Posted" |
| C-27 | 1720:3190 | Job Postings: empty state "No active jobs" |
| C-28 | 1720:3191 | Post a job form: title, description, trades, zip, type, compensation, benefits |
| C-29 | 1720:3192 | Rich-text description editing |
| C-30 | 1720:3193 | Rich text: highlight formatting |
| C-31 | 1720:3194 | Rich text: strikethrough |
| C-32 | 1720:3195 | Rich text: Heading 1 (formatting gets loud) |
| C-33 | 1720:3196 | Trade picker open (4 trades) |
| C-34 | 1720:3197 | Zip entered, Internship selected |
| C-35 | 1720:3198 | Benefits multi-select dropdown |
| C-36 | 1720:3199 | Why Work Here + experience / paid-training questions |
| C-37 | 1720:3200 | Publish CTA visible |
| C-38 | 1720:3201 | Answers set, Cancel / Publish |
| C-39 | 1720:3202 | ⚠ Zip validation error "Please enter a valid ZIP code" (10-digit zip accepted until submit) |
| C-40 | 1720:3203 | Fixing zip: browser autofill overlay |
| C-41 | 1720:3204 | Job detail (company view): Construction Test Job, Edit |
| C-42 | 1720:3205 | Job detail scrolled: rich-text styling carried into the published view |
| C-43 | 1720:3206 | Job Postings: active job card, Actions menu (View candidates, Edit, Copy, Inactivate, Delete) |

### C · Company Profile edit wizard
5 steps: Contact info → Business info → Services → Credentials → Additional info
| Code | Node | Screen and context |
|---|---|---|
| C-44 | 1720:3208 | Step 1 Contact Information: filled |
| C-45 | 1720:3209 | Company Profile page: Business Information all "Not specified" |
| C-46 | 1720:3210 | Step 1: Contact info re-filled |
| C-47 | 1720:3211 | Step 2 Business info: radius, employees, volume, payment terms, union, designations |
| C-48 | 1720:3212 | Step 3 Services: material vendor, trade categories |
| C-49 | 1720:3213 | Step 4 Credentials: project types, EMR, OSHA, license, insurance, affiliations dropdown |
| C-50 | 1720:3214 | Step 4: affiliations dropdown + description |
| C-51 | 1720:3215 | Step 5 Additional info: logo, showcase photos, referral |
| C-52 | 1720:3216 | Retry: Step 1 address lines empty again (data not kept) |
| C-53 | 1720:3217 | Step 1 re-filled (Missouri / LETSGROTO.COM) |
| C-54 | 1720:3218 | Step 3: trades empty again |
| C-55 | 1720:3219 | Step 4 Credentials |
| C-56 | 1720:3220 | Step 5: referral typing |
| C-57 | 1720:3221 | Step 5: Submit |
| C-58 | 1720:3222 | ⚠ Submit fails: "We couldn't update your profile." |
| C-59 | 1720:3223 | Step 3: Ceramic/Stone Tile trade only |
| C-60 | 1720:3224 | ⚠ Submit fails again |
| C-61 | 1720:3225 | Step 5 with files attached: Submit |
| C-62 | 1720:3226 | ⚠ Submit fails with files: profile never saves |

### D · Search projects and trade partners
| Code | Node | Screen and context |
|---|---|---|
| C-63 | 1720:3134 | Project detail: "Huge Plumbing Project" (Keller Software), Connect |
| C-64 | 1720:3135 | Keller Software company profile (Business Information) |
| C-65 | 1720:3136 | Keller profile: operational details, affiliations, designations |
| C-66 | 1720:3137 | Project: "Your connection was successful" toast |
| C-67 | 1720:3138 | Search Projects list (zip 46204), "Connected" tag |
| C-68 | 1720:3139 | Project "asdfasf": connection successful |

### E · Applicants, unlock and messaging
| Code | Node | Screen and context |
|---|---|---|
| C-69 | 1720:3170 | Job detail, Applicants tab: Jobseeker 5aec, View / Decline |
| C-70 | 1720:3171 | Jobseeker 6785 profile (match): Send Job, masked contact |
| C-71 | 1720:3172 | Jobseeker 6785: experience, certs, Looking For |
| C-72 | 1720:3173 | Jobseeker 6785: trade skills, work history |
| C-73 | 1720:3174 | Dashboard: 4 applications, Activities table (New Applicant) |
| C-74 | 1720:3175 | Job Postings: job with 1 view / 1 applicant |
| C-75 | 1720:3176 | Dashboard (repeat) |
| C-76 | 1720:3177 | Jobseeker 6aec profile: "Unlock free (3 left)" |
| C-77 | 1720:3178 | Jobseeker 6aec: trade skills, background |
| C-78 | 1720:3179 | "Use a free unlock?" confirm modal |
| C-79 | 1720:3180 | Unlocked: Shubham Job Seeker with phone/email visible |
| C-80 | 1720:3181 | New Message modal: empty (Send disabled) |
| C-81 | 1720:3182 | New Message: typed, Send enabled |
| C-82 | 1720:3188 | Messages: reply received from job seeker, "1 unread" badge |

---

## Job Seeker Flow (`1722:92`)

### A · Job seeker signup
| Code | Node | Screen and context |
|---|---|---|
| J-01 | 1720:3140 | Landing "Real trade work, right where you live": trades + zip, "See jobs near me" |
| J-02 | 1720:3141 | Create profile: empty |
| J-03 | 1720:3142 | Registration successful |
| J-04 | 1720:3143 | "Your trade & location": empty, Continue to dashboard |
| J-05 | 1720:3144 | ⚠ "We couldn't save your profile. Please try again." |

### B · Dashboard, find jobs, save and My Jobs
| Code | Node | Screen and context |
|---|---|---|
| J-06 | 1720:3145 | Dashboard: Complete Your Profile checklist (7 sections), Job Matching toggle |
| J-07 | 1720:3146 | Find Jobs: "No matching jobs available" (97206) |
| J-08 | 1720:3147 | Find Jobs: result card (zip 12345), View / Save Job |
| J-09 | 1720:3148 | Job detail: Construction Test Job, Apply |
| J-10 | 1720:3149 | Job detail scrolled: Why Work Here, Messages box |
| J-11 | 1720:3150 | Find Jobs: card shows "Saved" |
| J-12 | 1720:3151 | Profile view: mostly "not provided" |
| J-13 | 1720:3152 | Profile scrolled: Professional Summary, Background |
| J-14 | 1720:3153 | My Jobs, Activity: empty |
| J-15 | 1720:3154 | My Jobs, Saved Jobs (1): View / Remove |

### C · Apply to job
| Code | Node | Screen and context |
|---|---|---|
| J-16 | 1720:3155 | Job detail (saved star): Apply |
| J-17 | 1720:3156 | Apply success modal: "Back to Search" |
| J-18 | 1720:3157 | Find Jobs: no matches with 3 trades selected |

### D · Profile edit wizard and completed profile
3 steps: Basic info → Experience & Certifications → Work history
| Code | Node | Screen and context |
|---|---|---|
| J-19 | 1720:3158 | Step 1 Basic Information: personal & contact |
| J-20 | 1720:3159 | Step 1: Eligibility & Background yes/no questions |
| J-21 | 1720:3160 | Step 1: veteran, education, trades, licenses & transport |
| J-22 | 1720:3161 | Step 1: contact fields (SMS consent) |
| J-23 | 1720:3162 | Step 2 Experience & Certifications: CDL, CCS, OSHA, rich-text extras |
| J-24 | 1720:3163 | Step 2 Preferences: position type, management experience multi-select |
| J-25 | 1720:3164 | Step 2: hands-on experience, per-trade years + level slider |
| J-26 | 1720:3165 | Step 2: sliders (Journeyman / Master) |
| J-27 | 1720:3166 | Step 2: Awnings experience, Next |
| J-28 | 1720:3167 | Completed profile view: Profile Information |
| J-29 | 1720:3168 | Completed profile: Professional Summary, certs |
| J-30 | 1720:3169 | Completed profile: trade skills, background |

### E · Messaging with the company
| Code | Node | Screen and context |
|---|---|---|
| J-31 | 1720:3183 | Find Jobs: Messages "1 unread" badge |
| J-32 | 1720:3184 | Messages: list + "Select a conversation" |
| J-33 | 1720:3185 | Conversation open: "Hi Are you good in testing?" |
| J-34 | 1720:3186 | Typing reply |
| J-35 | 1720:3187 | Reply sent |

---

## Reference (not tied to one role)
| Code | Node | Screen and context |
|---|---|---|
| R-01 | 1720:3133 | ⚠ Signup "This email address is not allowed" + chat window (Nov 4, 11:25 AM) |
| R-02 | 1720:3207 | Client test brief: Brian's message listing what to test (onboarding, job posts, apply, messaging, unlocks, AI quizzes) |

> **Note (5 Nov):** After the regroup, the old "Section 1" (`1720:3227`) holding R-01 and R-02 is no longer on the page, and neither node can be found. It was probably deleted from the canvas. To restore it, undo in Figma or check version history.

## Early flags for the audit (from screen review, not yet verified)
- Company: the profile wizard never saves (C-58, C-60, C-62), and fields are wiped between attempts (C-52, C-54).
- Company: "Invalid or expired code" toast shows on first dashboard load, even though confirmation worked (C-24, C-25).
- Job Seeker: "We couldn't save your profile" during the trade and location step (J-05).
- Job post: rich-text formatting (H1, highlight, strikethrough) carries into the public job view without limits (C-32, C-42, J-09).
- Zip field accepts 10 digits and only fails on submit (C-39).
- Find Jobs empty state depends on the zip; a seeker in 97206 sees nothing while the job is in LA (J-07, J-18).

---

## Figma annotations (in progress)
Each annotated screen is wrapped in a frame that keeps its `C-xx · …` name. Inside the frame:
- **Red rectangle with a numbered badge** around the problem area
- **Yellow sticky** to the right with #, severity (High / Medium / Low), category, title, what's wrong, and **Fix →**
- **Dashed red connector** from the rectangle to the sticky

### Company A · Auth & Signup (pilot, 13 issues)
| # | Screen | Sev | Issue |
|---|---|---|---|
| 1 | C-01 | Med | Role cards don't read as choices (no hover/selected state, 12px copy) |
| 2 | C-02 | Low | Google sign-in button doesn't match the design system |
| 3 | C-04 | Med | No logo, step or progress on step 1 |
| 4 | C-04 | High | Placeholders ("Acme Electric LLC", "46204") look like real values |
| 5 | C-07 | Low | "Search 100+ trades" vs "151 trades total" |
| 6 | C-07 | Med | Close and Done do the same job, and the panel covers zip and Continue |
| 7 | C-13 | High | Continue stays disabled with no reason given |
| 8 | C-16 | Med | Account step loses company/role context and switches style |
| 9 | C-16 | Low | Google button doesn't match the Sign Up button |
| 10 | C-18 | Med | "Registration successful" while signup isn't finished; no email shown, no resend |
| 11 | C-19 | Med | Password rules are a static list; duplicate labels; code and password on one screen |
| 12 | C-24 | High | False "Invalid or expired code" toasts (×2) after successful verification |
| 13 | C-24 | Med | Onboarding to-dos styled as red errors |

---

## Tech-glitch audit (T-01…T-22)
These were found by cross-checking each screenshot's timestamp: what was entered at time X, and how it shows up later.
On the canvas each glitch is a **red-stroke rectangle** with a `T-xx` badge, plus a **pink sticky** with **Issue Type** and **Issue**, linked by a dashed red line. Blockers carry a dark **SEVERITY: HIGH · BLOCKER** pill.

### 🚫 HIGH: the company can't edit its profile (blocker)
The whole 5-step Edit Profile wizard is unusable. Every Submit fails with the same generic error and no field-level reason, so the user can't correct their mistake. Clicking outside the long modal closes it with no warning and throws away everything typed.

| # | Screen | Issue Type | Issue |
|---|---|---|---|
| T-07 | C-52 | Data loss **(HIGH)** | On reopening at 12:43 PM, address, phone and website are empty, though entered at 12:29 and 12:31 PM |
| T-08 | C-58 | Save failure **(HIGH)** | 12:45 PM Submit: "We couldn't update your profile." All steps show ✓, profile still "Not specified" |
| T-20 | C-60 | Save failure **(HIGH)** | 12:45:46 PM retry fails, with no reason given, so nothing can be fixed |
| T-21 | C-62 | Save failure **(HIGH)** | 12:47 PM with logo and photos attached, still fails. "Profile missing" nag can't be cleared |
| T-22 | C-52 | Interaction / data loss **(HIGH)** | Clicking outside the modal closes the 5-step form with no "Discard changes?" warning, and all input is lost |

### Other glitches
| # | Screen | Issue Type | Issue |
|---|---|---|---|
| T-01 | C-26 | Data inconsistency | "2 Total Matches" with no job posted (also at C-24 and C-73) |
| T-02 | C-40 | Validation | Zip error stays after a valid 12345 is entered |
| T-03 | C-41 | Wrong data | Job location "Los Angeles, CA", but zip was 12345 (NY) and company is in Indianapolis |
| T-04 | C-41 | Validation | Compensation "1234567890-98765" accepted (min > max, no currency) |
| T-05 | C-43 | Wrong data | "/hours" appended in the list; the form has no unit field |
| T-06 | C-45 | Missing data | Profile header contact icon has no name or phone after Contact info was filled |
| T-09 | C-68 | Validation / format | Project start date "Thu Dec 22 3222", in raw JS date format |
| T-10 | C-73 | Data inconsistency | Dashboard shows 4 applications and 2 matches; the job has 1 applicant and 0 matches |
| T-11 | C-79 | Needs verification | Phone (213) 456-7890 shown, but the seeker never entered a phone |
| T-12 | C-82 | State not updated | "1 unread" stays while the conversation is open |
| T-13 | J-04 | Data loss | The 4 landing-page trades are dropped on the trade & location step |
| T-14 | J-05 | Save failure | "We couldn't save your profile", then the user lands on the dashboard anyway |
| T-15 | J-06 | Wrong data | Matching trades (Appliance, Asphalt, Basement Waterproofing) were never selected |
| T-16 | J-06 | Data inconsistency | Personal & Contact 83% complete after a failed save, with no phone |
| T-17 | J-12 | Wrong data | Location 97206, but the last submitted zip was 97602 |
| T-18 | J-08 | Search logic | Zip 12345 (NY) search returns an LA job; search runs with no trade |
| T-19 | J-33 | Wrong identity | Company message shows a personal name and worker avatar, not the company |

---

## UI-inconsistency audit (U-01…U-30)
On the canvas: an **amber rectangle with a light yellow highlight**, a `U-xx` badge, and a **yellow sticky** with **Issue Type** and **Issue**.
**Reference states:**
- **Input:** C-08 (`1720:3115`) has the correct orange focus state.
- **Primary button:** the orange "Done" (rectangular is acceptable) is the brand primary, as on the website.

### 1. "TRADES" label inside the input (the field already has a label above it)
U-02 C-08 · U-10 J-04 · U-13 C-33 · U-18 C-48 · U-22 J-08 · U-26 J-21

### 2. Two helper texts on one field
U-03 C-04 ("Pick all that apply…" + "Pick at least one trade to keep going.") · U-10 J-04 · U-19 C-48 · U-22 J-08 (shown on a search filter that doesn't need it)

### 3. Primary button is blue instead of orange (breaks the component)
U-04 C-02 Log in · U-06 C-16 Sign Up · U-07 C-18 Enter confirmation code · U-08 C-19 Continue · U-09 J-05 Continue to dashboard · U-12 C-27 Post a job · U-16 C-38 Publish (Cancel also blue filled) · U-17 C-41 Edit · U-20 C-48 Next · U-23 J-08 Search / View / Save · U-24 J-09 Apply · U-28 J-21 Next · U-29 C-76 Unlock · U-30 C-81 Send

### 4. Other component inconsistencies
| # | Screen | Issue Type | Issue |
|---|---|---|---|
| U-05 | C-17 | Input focus & label | Blue focus border, and a floating label vs labels above the field on step 1 |
| U-11 | C-26 | Chip component | Selected trades are blue chips on the dashboard but orange chips in the pickers |
| U-13 | C-33 | 3 label styles | Floating label, label above, and label inside, all on one form |
| U-14 | C-33 | Copy | "150 trades total" vs "151" at signup |
| U-15 | C-33 | Layering | Trade panel overlaps the next field ("Add benefits" shows through) |
| U-21 | C-67 | Different picker | Search Projects uses a native dropdown instead of the chip multi-select |
| U-25 | J-21 | Double label | "Last Completed Education *" plus a floating "Select Education Level *" |
| U-27 | J-21 | Duplicate field | "Are you at least 18?" asked a second time (already answered in J-20) |
| U-30 | C-81 | 4th input style | Plain label above with a blue focus border in the New Message modal |
