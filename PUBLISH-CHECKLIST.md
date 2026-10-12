# Publish Checklist — `compliance-reminder-action`

SAMPLE — kept ready locally. **Nothing ships without Muhammad's explicit yes.**

## Before going live

- [ ] Muhammad reviews and approves the repo (content + tone + CTA).
- [ ] Syntax-check the composite action YAML (`action.yml`) and test the workflow on a scratch repo — confirm the reminder issue opens and updates correctly.
- [ ] Verify `scripts/check.py` exit codes behave as documented.
- [ ] Copy the brand monogram to `assets/epics-deals-ed-monogram.png` and reference it in the README.
- [ ] Create the repo under the EpicsDeals GitHub org (or chosen account) as `compliance-reminder-action`.
- [ ] Update the README example `uses:` line to the published tag (e.g. `epicsdeals/compliance-reminder-action@v1`) and tag the release.
- [ ] Add repo description, topics (`github-actions`, `compliance`, `us-llc`, `reminders`), and website link (https://epicsdeals.com).
- [ ] Compliance sweep: no BOI-mandatory claims, no old pricing ($149/$150/$127), no guaranteed bank/Stripe approval language.
