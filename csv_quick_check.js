"use strict";
function parseCsv(text) {
  const rows = []; let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') { field += '"'; i += 1; }
      else if (ch === '"') quoted = false; else field += ch;
    } else if (ch === '"' && field === "") quoted = true;
    else if (ch === ",") { row.push(field); field = ""; }
    else if (ch === "\n") { row.push(field); rows.push(row); row = []; field = ""; }
    else if (ch !== "\r") field += ch;
  }
  if (field !== "" || row.length || (text && !text.endsWith("\n"))) { row.push(field); rows.push(row); }
  return {rows, unclosedQuote: quoted};
}
function inspectCsv(rows) {
  const width = rows.length ? rows[0].length : 0, data = rows.slice(1);
  let blanks = 0, uneven = 0, duplicates = 0; const seen = new Set();
  data.forEach((row) => {
    blanks += row.filter((cell) => cell.trim() === "").length;
    if (row.length !== width) uneven += 1;
    const key = JSON.stringify(row); if (seen.has(key)) duplicates += 1; else seen.add(key);
  });
  return {rows: data.length, columns: width, blanks, duplicates, uneven};
}
const fileInput = document.getElementById("csv-file"), clearButton = document.getElementById("clear-check");
const status = document.getElementById("privacy-note"), results = document.getElementById("results");
const summary = document.getElementById("summary"), findings = document.getElementById("findings");
function clearResult() {
  fileInput.value = ""; summary.replaceChildren(); findings.replaceChildren(); results.hidden = true;
  clearButton.disabled = true; status.textContent = "Nothing selected. Your file will not leave this browser.";
}
fileInput.addEventListener("change", async () => {
  const file = fileInput.files[0]; if (!file) { clearResult(); return; }
  status.textContent = `Checking ${file.name} locally…`;
  try {
    const bytes = await file.arrayBuffer(); let text, encodingWarning = false;
    try { text = new TextDecoder("utf-8", {fatal: true}).decode(bytes); }
    catch (_) { text = new TextDecoder("utf-8").decode(bytes); encodingWarning = true; }
    const parsed = parseCsv(text.replace(/^\uFEFF/, "")), report = inspectCsv(parsed.rows);
    const metrics = [["Data rows", report.rows], ["Header columns", report.columns], ["Blank cells", report.blanks], ["Exact duplicate rows", report.duplicates], ["Inconsistent-width rows", report.uneven]];
    summary.replaceChildren(...metrics.map(([label, value]) => { const box = document.createElement("div"), heading = document.createElement("h3"), p = document.createElement("p"); heading.textContent = label; p.textContent = String(value); box.append(heading, p); return box; }));
    const notes = []; if (!parsed.rows.length) notes.push("No rows were found.");
    if (parsed.unclosedQuote) notes.push("An unclosed quoted field was detected; counts may be unreliable.");
    if (encodingWarning) notes.push("Invalid UTF-8 byte sequences were replaced. Re-export as UTF-8 before relying on these counts.");
    if (!notes.length) notes.push("No parsing or UTF-8 decoding warning was detected. This does not prove the data is correct.");
    findings.replaceChildren(...notes.map((note) => { const li = document.createElement("li"); li.textContent = note; return li; }));
    results.hidden = false; clearButton.disabled = false; status.textContent = `Finished checking ${file.name} locally. No data was uploaded or stored.`; results.focus();
  } catch (_) { clearResult(); status.textContent = "This file could not be read. Nothing was uploaded."; }
});
clearButton.addEventListener("click", () => { clearResult(); fileInput.focus(); });
