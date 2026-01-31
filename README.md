# SiteBuddy

A Node.js CLI tool that reads websites and converts them to markdown files.

## Installation

```bash
npm install
```

## Usage

```bash
node src/index.js <url> [options]
```

### Examples

```bash
# Convert a website to markdown
node src/index.js https://example.com

# Specify output file
node src/index.js https://example.com -o output.md
```

## Options

- `-o, --output <file>` - Specify output file name (default: auto-generated from URL)
- `-h, --help` - Display help information

## How it works

1. Fetches the HTML content from the provided URL
2. Parses the HTML using Cheerio
3. Converts HTML to markdown using Turndown
4. Saves the result to a .md file

## Development

See [COMMANDS.md](docs/COMMANDS.md) for development commands.

## Project Structure

- `src/index.js` - CLI entry point
- `src/scraper.js` - Web scraping logic
- `src/converter.js` - HTML to markdown conversion
- `docs/` - Project documentation
- `.claude/skills/` - Claude Code skills

## Claude Skills

This project includes a **website-content-migration** skill for content migration workflows. The skill provides:

- Structured content extraction with hierarchy preservation
- Content mapping between old and new site templates
- Content rewriting and planning templates
- Python script for extracting page structure

To use the skill in Claude Code, it will be automatically available when working in this project.
