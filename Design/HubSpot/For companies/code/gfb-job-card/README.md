# GFB Job card

Band 05 card, Job Seeker page. Figma `1354:9913` (440 × 294). Built 14 Oct 2026, per
`../../../03_COMPONENT-COMPARISON_Company-vs-JobSeeker.md`. Job Seeker copy as defaults.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL (Lucide icons inlined) |
| `module.css` | Styles; Elevate theme variables with Figma fallbacks |

HubSpot: `custom/content-mcp/modules/gfb_job_card`, CSS inlined in the HTML.

## Use

Place it **directly after GFB Search Match**, same background. It uses the wrapper's grid and sits in the
right-hand column under the connector. A job post as a worker sees it: company tile with two letters, job
title and company, heart (orange filled when `saved`), pay with an orange job-type pill, location with the
distance in orange, "Posted today", Apply now and View.

A static picture: hidden from screen readers (the wrapper's `visual_label` describes it), buttons are not links.

## Fields

| Field | Type | Default |
|---|---|---|
| `logo_text` | Text | AC |
| `job_title` | Text | Journeyman Electrician |
| `company` | Text | Apex Construction |
| `saved` | Boolean | True |
| `pay` | Text | $38/HR |
| `job_type` | Text | Full-time |
| `location` | Text | Indianapolis, IN |
| `distance` | Text | 3.2 mi from 46204 |
| `posted` | Text | Posted today |
| `primary_text` | Text | Apply now |
| `secondary_text` | Text | View |
| `background` | Choice: Light grey / White | grey |
