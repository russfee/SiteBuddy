# Session Context

## Session updates
- 2026-01-31: Bootstrapped SiteBuddy project. Created initial Node.js CLI structure for web-to-markdown conversion. Current status: initial setup. Next steps: implement core scraping and markdown conversion.
- 2026-01-31: Updated the "Home - Buddy Update" page content in the WordPress CSV export to match the content plan (headlines, sections, lists, CTAs, testimonial, pricing, stats, and contact placeholders).
- 2026-01-31: Created a renamed full export and a single-row CSV for "Home - Buddy Update" to avoid import confusion.
- 2026-01-31: Documented the WP All Export/Import workflow and troubleshooting steps in `docs/ImportExportSkill.md`.

## What this repo is
A Node.js CLI tool that reads websites and converts them to markdown files.

## Current goal
Migrate and refine website content in the WordPress export to match the new content plan.

## Where to look first
- package.json - project dependencies and scripts
- src/index.js - main CLI entry point
- src/scraper.js - web scraping logic
- src/converter.js - HTML to markdown conversion
- README.md - usage instructions

## Known issues / risks
- Need to handle different website structures and edge cases
- May need to handle JavaScript-rendered content (consider Puppeteer if needed)
- Rate limiting and robots.txt compliance
- WordPress imports must match on slug (IDs differ across installs) to avoid duplicate pages

## How to validate
Re-import the CSV with WP All Import using slug matching and verify the "Home - Buddy Update" page renders with updated copy.
