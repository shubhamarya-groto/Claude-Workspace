// use_figma script: builds "Hero photo options" board on Presentation page (493:1016). See Design/Assets/AI-HERO-PHOTOS_I-20_I-21.md
const page = await figma.getNodeByIdAsync("493:1016");
await figma.setCurrentPageAsync(page);
if (page.children.find(n => n.name.startsWith("Hero photo options"))) return { error: "board exists" };
await Promise.all([
  figma.loadFontAsync({ family: "Instrument Sans", style: "SemiBold" }),
  figma.loadFontAsync({ family: "Inter", style: "Regular" }),
  figma.loadFontAsync({ family: "Inter", style: "Semi Bold" })]);
const V = id => figma.variables.getVariableByIdAsync(id);
const [vBrand, vMuted, vBorder, vOrange] = await Promise.all([V("VariableID:783:162"), V("VariableID:783:169"), V("VariableID:783:179"), V("VariableID:783:163")]);
const paint = v => figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 0, g: 0, b: 0 } }, "color", v);
const txt = (chars, family, style, size, v, w) => { const t = figma.createText(); t.fontName = { family, style }; t.characters = chars; t.fontSize = size; t.fills = [paint(v)]; if (w) { t.resize(w, t.height); t.textAutoResize = "HEIGHT"; } return t; };
const section = figma.createSection();
section.name = "Hero photo options · I-20 Company / I-21 Job Seeker";
section.x = 27800; section.y = 1343;
const board = figma.createAutoLayout("VERTICAL", { name: "Board", itemSpacing: 64, paddingTop: 96, paddingBottom: 96, paddingLeft: 96, paddingRight: 96 });
board.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
section.appendChild(board);
const head = figma.createAutoLayout("VERTICAL", { name: "Header", itemSpacing: 16 }); head.fills = [];
board.appendChild(head);
head.appendChild(txt("Hero photo options", "Instrument Sans", "SemiBold", 48, vBrand));
head.appendChild(txt("AI-generated, 23 Oct 2026, in the style of the Plumbing page photo Brian referenced (21 Oct). Brief: tradespeople mid-task on a real jobsite, not looking at the camera, workwear, less clean and polished. Pick one for the Company hero (I-20) and one for the Job Seeker hero (I-21). Comment with the code, e.g. \"C2 + J1\".", "Inter", "Regular", 20, vMuted, 3792));
const options = {
  "Company hero · I-20 · crews (employer view)": [
    ["C1", "Framing crew", "Three carpenters framing a house: nail gun, carrying a stud, checking a level. Overcast daylight."],
    ["C2", "HVAC crew", "Two HVAC technicians fitting metal ductwork in an unfinished commercial ceiling. Window light."],
    ["C3", "Electrical crew", "Two electricians pulling wire through metal studs, one on a ladder, one at the spool."]],
  "Job Seeker hero · I-21 · one tradesperson": [
    ["J1", "Carpenter", "Cutting a board with a circular saw on sawhorses, sawdust flying, house frame behind. Morning sun."],
    ["J2", "Plumber", "Soldering copper pipe in an unfinished basement, kneeling, small torch flame, work lamp."],
    ["J3", "Electrician", "Wiring an outlet box in an exposed stud wall, wire strippers, cable along the studs."]]
};
const slotIds = {};
for (const [rowTitle, items] of Object.entries(options)) {
  const row = figma.createAutoLayout("VERTICAL", { name: rowTitle, itemSpacing: 24 }); row.fills = [];
  board.appendChild(row);
  row.appendChild(txt(rowTitle, "Inter", "Semi Bold", 24, vBrand));
  const cards = figma.createAutoLayout("HORIZONTAL", { name: "Options", itemSpacing: 96 }); cards.fills = [];
  row.appendChild(cards);
  for (const [code, trade, brief] of items) {
    const card = figma.createAutoLayout("VERTICAL", { name: `${code} · ${trade}`, itemSpacing: 16 }); card.fills = [];
    cards.appendChild(card);
    const slot = figma.createFrame();
    slot.name = `${code} · photo (paste image here)`;
    slot.resize(1200, 800); slot.cornerRadius = 16;
    slot.fills = [{ type: "SOLID", color: { r: 0.937, g: 0.945, b: 0.957 } }];
    slot.strokes = [paint(vBorder)]; slot.strokeWeight = 1;
    card.appendChild(slot); slotIds[code] = slot.id;
    const capRow = figma.createAutoLayout("HORIZONTAL", { name: "Caption", itemSpacing: 12 }); capRow.fills = []; capRow.counterAxisAlignItems = "CENTER";
    card.appendChild(capRow);
    capRow.appendChild(txt(code, "Inter", "Semi Bold", 22, vOrange));
    capRow.appendChild(txt(trade, "Inter", "Semi Bold", 22, vBrand));
    card.appendChild(txt(brief, "Inter", "Regular", 18, vMuted, 1200));
  }
}
section.resizeWithoutConstraints(board.width, board.height);
return { sectionId: section.id, boardId: board.id, slotIds, size: [board.width, board.height] };
