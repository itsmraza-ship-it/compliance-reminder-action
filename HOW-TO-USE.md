# How to Use — Compliance Reminder Action

Six ways to use this repo. Pick the route that fits how you work.

## 1. As a Claude skill

1. Download `SKILL.md` from this repo.
2. Copy it into your Claude skills folder, or upload it where your Claude setup accepts skills.
3. Start a new conversation and ask a question in this domain: setting up compliance deadline reminders or asking when a state filing is due.
4. Claude will apply the guidance in `SKILL.md` — ask follow-ups in the same chat.

## 2. Inside Claude.ai

1. Open Claude.ai and create (or open) a Project.
2. Paste the contents of `SKILL.md` into the Project's custom instructions, or add it to the Project's knowledge.
3. Also add the repo's data/guide files (`action.yml`, `.github/workflows/example.yml`, `scripts/check.py`) to the Project knowledge for detail.
4. Chat inside the Project — every answer will be grounded in this material.

## 3. With the Epics Deals MCP server (live answers)

Instead of static files, connect the live Epics Deals MCP server:

- Endpoint: `https://epics-deals-mcp.epicsdeals.workers.dev/mcp`
- Add it as a custom connector / MCP server in your AI client, using that exact URL.
- Then ask the same questions — the server answers with live tool data rather than a snapshot of these files.

This route applies to all Epics Deals knowledge repos and is the best option when you want current answers.

## 4. As plain reference

1. Read `README.md` and the guides in this repo directly on GitHub.
2. Download any data files (`action.yml`, `.github/workflows/example.yml`, `scripts/check.py`) for your spreadsheet, docs, or filing prep.
3. Work through them in order — no AI tool required.

## 5. In other AI tools

1. Create a custom GPT (ChatGPT), a Gemini Gem, or a notebook in your tool of choice.
2. Upload `SKILL.md` plus the repo's data/guide files as knowledge.
3. Set the instruction: "Answer using only this uploaded material, and say so when something is not covered."
4. Ask questions in this domain: setting up compliance deadline reminders or asking when a state filing is due.

## 6. Fork it

1. Click **Fork** on GitHub to copy this repo to your own account.
2. Edit the files for your state, entity type, or clients.
3. This repo is MIT licensed — adapt it freely, keeping the license notice.

**For this repo, route 4 also means using the Action itself:** add the example workflow to your own repo with your `state`, `filing`, and `deadline-date`, ensure `issues: write` permission, and the Action opens a `compliance` issue inside your warning window.

---

epicsdeals.com — free tools by Epics Deals; US LLC formation from $130 + state fee.
