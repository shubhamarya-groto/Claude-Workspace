# gfb_stats_dark · HubSpot custom module

Portal `47303551`, path `/custom/content-mcp/modules/gfb_stats_dark`. Created 16 Oct 2026. Visual: `../gfb-problem-stats.html`.

Dark version of the approved Home band "03 · Problem + stats" (Figma `1355:8192`, module `gfb_problem_stats`), with an optional **source** line per stat. Built as a separate module because `gfb_problem_stats` has no source field and its code could not be read, so changing it risked Home's band. Fold the two together later if wanted.

**Fields:** `overline` · `line_one` (white) · `line_two` (orange, optional) · `stats` (1–4: `number`, `caption`, `source`) · `background_image` (defaults to Home's band image, under a navy overlay). With both lines empty, the overline becomes the H2.

**In use:** LP-20261007-INDY-EmployerSignup-Plumbing-STAGING (`223867638545`), module `dnd_area-module-4`, where the hand-coded "Why we built GoFindBuild" rich text (`dnd_area-module-2`) was; row set to full width with no padding. Stats, captions and sources copied unchanged; the headline lines are Home's approved lines.
