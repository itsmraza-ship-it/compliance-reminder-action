# Compliance Reminder Action

A GitHub Action that watches your annual report and franchise tax deadlines — and opens a GitHub issue when one is getting close.

Miss a state deadline and you get penalties. Miss it long enough and the state can administratively dissolve your company. This action makes sure that doesn't happen quietly.

## How it works

On a schedule (e.g. every Monday morning), the action checks how many days remain until your deadline. If the deadline is within your warning window (default: 30 days), it opens a GitHub issue labeled `compliance` — or updates the existing one with a fresh countdown comment.

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `state` | yes | — | US state the filing is due in (e.g. `Wyoming`) |
| `filing` | no | `Annual report` | What is due (e.g. `Annual report`, `Franchise tax`) |
| `deadline-date` | yes | — | Deadline in `YYYY-MM-DD` format |
| `days-before` | no | `30` | Remind when this many days (or fewer) remain |
| `issue-label` | no | `compliance` | Label applied to the reminder issue |

## Setup

1. Copy this action into your repo, or reference it after publishing.
2. Add the example workflow at [.github/workflows/example.yml](.github/workflows/example.yml) and set your own `state`, `filing`, and `deadline-date`.
3. Make sure the workflow has `issues: write` permission (see the example).
4. Push. The workflow runs on its schedule and opens an issue when your deadline approaches.

Duplicate the job block in the example workflow for each deadline you want to track (annual report, franchise tax, registered agent renewal).

## Local helper

`scripts/check.py` computes the days remaining until a deadline — useful for a quick manual check:

```bash
python3 scripts/check.py --deadline-date 2027-04-01 --warn-days 30
```

## Example

```yaml
- name: Wyoming annual report reminder
  uses: ./  # or epicsdeals/compliance-reminder-action@v1 once published
  with:
    state: Wyoming
    filing: Annual report
    deadline-date: "2027-04-01"
    days-before: "45"
```

---

**Rather have compliance handled for you?** Epics Deals keeps non-resident founders compliant — annual reports, registered agent, and deadline tracking — and forms US LLCs for **$130 + state fee**.

- Website: https://epicsdeals.com
- WhatsApp: https://wa.link/x6klxo
- Email: info@epicsdeals.com

*Epics Deals — Compliance Team*
