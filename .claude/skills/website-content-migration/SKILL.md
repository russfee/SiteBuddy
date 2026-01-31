---
name: website-content-migration
description: Website content migration and rewriting assistant. Use when the user requests help migrating content from an old/legacy website to a new template, asks for website content writing help, needs to map existing content to new layouts, or wants to analyze and rewrite website content for a new structure. Handles multiple pages, preserves content hierarchy, identifies content gaps, and generates detailed content plans with rewritten copy mapped to new template sections.
---

# Website Content Migration

## Overview

This skill helps migrate and rewrite content from legacy websites to new templates. It extracts structured content from existing URLs (preserving hierarchy, IDs, and semantic structure), analyzes new template layouts, and generates detailed content plans with rewritten copy mapped to specific template sections.

## Workflow

Follow this workflow when the user requests website content migration:

### Step 1: Extract Old Site Content

Use the `extract_and_map.py` script to fetch and parse content from the legacy website(s):

```bash
# For a single page
python3 scripts/extract_and_map.py "https://example.com/about" > old_about.md

# For multiple pages, process each URL
python3 scripts/extract_and_map.py "https://example.com" > old_home.md
python3 scripts/extract_and_map.py "https://example.com/services" > old_services.md
```

The script extracts:
- Page titles and meta descriptions
- Content hierarchy (headings, paragraphs, lists)
- Element IDs and CSS classes
- Semantic sections (hero, features, etc.)

**Output format:** Markdown with structure preserved and IDs/classes annotated

### Step 2: Analyze New Template Structure

Use the same script to analyze the new template/target layout:

```bash
python3 scripts/extract_and_map.py "https://newtemplate.example.com" > template_structure.md
```

Examine the template to identify:
- Available content sections and their IDs
- Content types expected in each area (hero text, feature cards, testimonials, etc.)
- Layout constraints (character limits, number of items, etc.)

### Step 3: Create Content Mapping and Plan

For each page being migrated, create a detailed content plan document that includes:

1. **Header Section:**
   - Old page title and URL
   - New page title and target URL
   - Brief migration notes

2. **Content Mapping Table:**
   - Map old content sections to new template areas
   - Flag content that doesn't fit the new structure
   - Identify gaps where new content is needed

3. **Rewritten Content by Section:**
   - For each template section, provide the actual rewritten content
   - Adapt tone, length, and style to fit the new design
   - Preserve key messages and SEO value
   - Include specific IDs/classes for implementation

4. **Orphaned Content:**
   - List any old content that doesn't map to new template
   - Suggest where it could go or if it should be discarded

5. **New Content Requirements:**
   - Specify any sections that need entirely new content
   - Provide suggestions or draft copy

### Step 4: Generate Output Files

Create one markdown content plan per page. Use the template at `assets/content-plan-template.md` as a starting point, which includes:

```markdown
# Content Plan: [Page Name]

**Old URL:** https://old-site.com/page
**New URL:** /new-page
**Migration Date:** [Date]

---

## Content Mapping

| Old Section | New Template Area | Status | Notes |
|-------------|-------------------|--------|-------|
| Hero headline | #hero-section | ✓ Mapped | Shortened to fit |
| About paragraph | #intro-text | ✓ Mapped | Rewritten for clarity |
| Services list | #features-grid | ✓ Mapped | Converted to cards |
| Contact info | — | ⚠ Orphaned | Move to footer? |
| — | #testimonials | ✗ New content needed | — |

---

## Rewritten Content

### Hero Section `[id="hero-section"]`

**Headline:** [Rewritten headline text]
**Subheading:** [Rewritten subheading]
**CTA Text:** [Button text]

### Intro Text `[id="intro-text"]`

[Full rewritten paragraph...]

### Features Grid `[id="features-grid"]`

**Feature 1:**
- Title: [Title]
- Description: [Description]
- Icon: [Suggested icon name]

**Feature 2:**
[...]

---

## Orphaned Content

The following content from the old site doesn't fit the new template:

- **Contact form details:** [Content] → Suggest moving to dedicated contact page
- **Old testimonials:** [Content] → Replace with new testimonials in new format

---

## New Content Requirements

### Testimonials Section `[id="testimonials"]`

Need 3 customer testimonials in this format:
- Quote (max 150 chars)
- Customer name
- Company/title
- Photo (to be sourced)

**Suggested draft:**
[Draft testimonial 1...]
```

### Step 5: Review and Iterate

Review each content plan with the user for:
- Accuracy of content mapping
- Quality of rewritten copy
- Completeness of new content
- Any missing sections or concerns

## Best Practices

- **Preserve SEO value:** Maintain important keywords and phrases from old content
- **Adapt tone:** Match the new brand voice while keeping core messages
- **Be specific:** Include exact IDs and classes for developer handoff
- **Flag uncertainties:** Mark any content mappings that need client confirmation
- **Think responsive:** Consider how content will work across devices
- **Include metadata:** Don't forget page titles, meta descriptions, and alt text

## Script Reference

### extract_and_map.py

Extracts structured content from a URL, preserving hierarchy and IDs.

**Usage:**
```bash
python3 scripts/extract_and_map.py <url> [--json]
```

**Output:** Markdown format by default, JSON with `--json` flag

**What it extracts:**
- Page title and meta description
- Headings (h1-h6) with hierarchy
- Paragraphs
- Lists (ul/ol)
- Sections with IDs or semantic classes (hero, features, etc.)
- Element IDs and CSS classes for all content

**Installation requirements:**
```bash
pip install requests beautifulsoup4 --break-system-packages
```

**Note:** This script requires network access to fetch URLs. In Claude.ai environments where network is disabled, Claude can still guide the user through the workflow using manually provided HTML content or by having the user enable network access in their settings.
