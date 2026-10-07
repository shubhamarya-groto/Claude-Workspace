# GFB Top Nav

Home band 00. Figma: Home Page `1259:9027` → `1259:9028` (DS `Top Nav` instance). Read 7 Oct 2026.
Exact Figma copy as defaults. Built as code on request; the Elevate Site header stays the fallback.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy and GoFindBuild links |
| `module.html` | HubL (Lucide `user`, menu and close icons inlined) |
| `module.css` | Styles |
| `demo.html` | Static demo (narrow the window to see the drawer) |

## Fields

| Field | Type | Default |
|---|---|---|
| `brand_text` / `logo_image` / `brand_link` | Text / Image / Link | "GoFindBuild" (Source Serif 4 SemiBold 22), no image, `/` |
| `nav_links` | Repeater, 0 to 6 (`link_text`, `link`) | Companies `/companies` · Job Seekers `/job-seekers` · About Us `/about-us` |
| `login_text` / `login_link` | Text / Link | "Login" → `https://app.gofindbuild.com/` |
| `cta_text` / `cta_link` | Text / Link | "Get Started" → `https://app.gofindbuild.com/signup` |
| `sticky` | Toggle, off | Keeps the bar at the top while scrolling |

Empty Login or button text hides that item. The link that matches the current page gets
`aria-current="page"` and an orange underline.

## Links to confirm

- `/companies`, `/job-seekers`, `/about-us`: those HubSpot pages aren't built yet. Pick the real pages in the
  link fields once they exist (the editor's page picker survives slug changes).
- Login → `app.gofindbuild.com/` and Get Started → `app.gofindbuild.com/signup` (the sign-up URL from the
  current site, without its `utm_source=null` tags). Confirm the login address.

## From Figma

1440 × 96, padding 24 / 96. Left: logo, 40 gap, three text buttons (Inter Medium 16 `#111111`, 48 tall, 40 apart).
Right, 28 apart: Login with a 20px user icon, and a 48px orange pill with a white label (Figma's Primary button
without the arrow disc). Built within a few px of Figma; the logo text renders slightly wider with the web font.

## Tablet and phone (not in Figma)

Figma has no phone frames, so this follows the build plan's mobile notes ("drawer menu with close button"):

- Below 1024px: links and Login move into a drawer; a round Menu button (48px) opens it and turns into a close (×).
  The Get Started button stays in the bar on tablets.
- Below 768px: Get Started moves into the drawer too, as a full-width 48px button.
- Built on `<details>`/`<summary>`: no JavaScript, works with the keyboard.

## Note

To use it on every page, put it in the page template's header (global) rather than on each page.
