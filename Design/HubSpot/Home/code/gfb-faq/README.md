# GFB FAQ

Home band FAQ. Figma: Home Page `1259:9027` → `1259:9108` (an Elevate `faq-v2` instance). Read 7 Oct 2026.
Exact Figma copy as defaults. Built as code on request, like Pricing and Problem + Stats; Elevate `faq-v2`
stays the fallback.

> **Live in HubSpot (7 Oct 2026):** created through the connector as **GFB FAQ**, path `custom/content-mcp/modules/gfb_faq` (GoFindBuild 47303551). CSS inlined in the HTML. Update it through the connector, not the Design Manager.

| File | What |
|---|---|
| `fields.json` | Fields with the Figma copy |
| `module.html` | HubL: `<details>` accordion + optional FAQPage JSON-LD |
| `module.css` | Styles; reads Elevate theme variables with Figma fallbacks |
| `demo.html` | Static demo |

## Fields

| Field | Type | Notes |
|---|---|---|
| `heading` | Text | "Frequently asked questions" |
| `items` | Repeater, 1 to 20 | `question` (text), `answer` (rich text), `open` (toggle: open on page load) |
| `one_at_a_time` | Toggle, on | Opening a question closes the open one (the `name` attribute on `<details>`) |
| `faq_schema` | Toggle, on | Adds FAQPage structured data from the questions and answers (answers as plain text) |

## From Figma

White band, padding 96 / 120, 1200 container, 32 under the heading. Heading Instrument Sans SemiBold 48 / 1.1,
−0.5px, `#16243D`, 900 wide. Row: question Inter SemiBold 18 / 1.4 `#16243D` + sign Inter Bold 24 `#525C70`
(16 gap); 12; answer Inter 16 / 1.6 `#525C70`; 12; 1px rule `#D9DBDE`; 20 to the next row.
Open row 82px, closed row 44px, the same as in the build.

## Notes

- **No JavaScript.** `<details>`/`<summary>` open and close natively, with keyboard and screen readers.
  The +/– sign is CSS. "One at a time" needs a current browser; older ones just let several stay open.
- **Answers missing in Figma.** Only question 1 has an answer, and it is placeholder text ("The answer sits
  under the question and stays short."). Questions 2 and 3 default to "Write the answer here. Keep it short."
  Fill in all three before publishing. The schema output repeats whatever is in the answers, so placeholders
  must not go live.
- **Layer names differ from the text.** `How is this different from a staffing agency?` shows
  "…or a job board?"; `Are licenses and certifications verified?` shows "Is GoFindBuild free for workers?".
  The build uses the visible text. Confirm which questions are wanted.
- Hover turns the question `#BB5B09`; answer links are `#BB5B09` (AA on white).
