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
