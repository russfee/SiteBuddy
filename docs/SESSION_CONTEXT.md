# Session Context

## Session updates
- 2026-01-22: Updated AGENTS.md paths to use docs/* and remove ProjectTemplate references. Current status: paths cleaned. Next steps: none.

## What this repo is
- One sentence: what this project does.

Example Q/A:
Q: What is this repo?
A: A Chrome extension that batch-fills Drupal edit forms from a CSV.

## Current goal
- The most important thing to do next.

Example Q/A:
Q: What’s the goal for this session?
A: Add support for XLSX import and fix notification styling.

## Where to look first
- 3–5 files/folders that matter most.

Example Q/A:
Q: What files should I check first?
A: manifest.json, lib/data-manager.js, lib/form-filler.js, content/content.js, config/form-templates.json.

## Known issues / risks
- Bullet list of sharp edges or unresolved problems.

Example Q/A:
Q: Any known issues?
A: XLSX import doesn’t work; CSV parsing fails on embedded newlines.

## How to validate
- Minimal steps to verify changes.

Example Q/A:
Q: How do we validate?
A: Reload the extension, import a sample CSV, open a /node/*/edit page, click “Fill Form,” confirm fields update.
