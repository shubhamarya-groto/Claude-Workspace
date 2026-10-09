# GFB Search Match

Company band 05, Figma `1362:2627` (replaces the hidden testimonial). Built 9 Oct 2026 for the Company page. Figma copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks, like the Home modules |

**Not in HubSpot yet.** Create it through the connector at `custom/content-mcp/modules/gfb_search_match`, CSS inlined in the HTML.

## Look

Copy (508) beside a static illustration (620): search bar with trade and location, a connector with the match pill, and a Private worker card (profile score, skills with 4-step level bars, location, seeking, two buttons).

It is a picture, not a working search: the illustration has one description for screen readers (`visual_label`) and its buttons are not links. On phones the search bar wraps to two rows.

## Fields

| Field | Type | Default |
|---|---|---|
| `eyebrow` | Text | How matching works |
| `heading` | Textarea | Search your trade. / See who's ready to work. |
| `intro` | Text | Enter the trade you need and your ZIP code. Matched workers show their skills, experience level and distance up front, so you're reviewing people, not resumes. |
| `visual_label` | Text | Example: a search for Journeyman Electrician near 46204 Indianapolis finds 4 matching workers, including a private profile with a 96% profile score. |
| `trade_label` | Text | Trade |
| `trade` | Text | Journeyman Electrician |
| `near_label` | Text | Near |
| `near` | Text | 46204 · Indianapolis |
| `match_text` | Text | 4 workers match your trade near 46204 |
| `profile_title` | Text | Private Profile |
| `private` | Boolean | True |
| `profile_role` | Text | Journeyman |
| `score` | Text | 96% |
| `score_label` | Text | Profile score |
| `skills_label` | Text | Looking for |
| `level_label` | Text | Experience |
| `skills` | Repeater, 0 to 4 (`skill`, `tone`, `level`, `level_text`) |  |
| `location` | Text | Indianapolis, IN |
| `distance` | Text | 4.1 mi from 46204 |
| `seeking` | Text | Seeking Full-time |
| `primary_text` | Text | Send job |
| `secondary_text` | Text | View profile |
| `background` | Choice: Light grey / White | grey |
