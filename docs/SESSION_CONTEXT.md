# Session Context

## Session updates
- 2026-01-31: Bootstrapped SiteBuddy project. Created initial Node.js CLI structure for web-to-markdown conversion. Current status: initial setup. Next steps: implement core scraping and markdown conversion.

## What this repo is
A Node.js CLI tool that reads websites and converts them to markdown files.

## Current goal
Set up initial project structure with basic web scraping and markdown conversion functionality.

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

## How to validate
Run `node src/index.js <url>` and verify markdown file is created with correct content.
