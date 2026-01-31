#!/usr/bin/env python3
"""
Website Content Extraction and Mapping Tool

Fetches HTML from URLs, extracts structured content with IDs and hierarchy,
and outputs clean markdown suitable for content migration planning.
"""

import sys
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re


def fetch_html(url):
    """Fetch HTML content from a URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None


def extract_content_structure(html, url):
    """
    Extract structured content from HTML, preserving hierarchy and IDs.
    Returns a dict with metadata and structured content elements.
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove script, style, and nav elements
    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()
    
    # Extract page title
    title = soup.find('title')
    page_title = title.get_text().strip() if title else urlparse(url).path
    
    # Extract meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '').strip() if meta_desc else ''
    
    content_elements = []
    
    # Find main content area (common selectors)
    main_content = (
        soup.find('main') or 
        soup.find('div', class_=re.compile(r'content|main', re.I)) or
        soup.find('article') or
        soup.body
    )
    
    if not main_content:
        main_content = soup
    
    # Extract structured elements
    for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'div', 'section']):
        # Skip empty elements
        text = element.get_text(separator=' ', strip=True)
        if not text:
            continue
        
        # Get element details
        tag_name = element.name
        element_id = element.get('id', '')
        element_class = ' '.join(element.get('class', []))
        
        # For headings, capture directly
        if tag_name.startswith('h'):
            content_elements.append({
                'type': 'heading',
                'level': int(tag_name[1]),
                'text': text,
                'id': element_id,
                'class': element_class
            })
        
        # For lists, capture items
        elif tag_name in ['ul', 'ol']:
            items = [li.get_text(strip=True) for li in element.find_all('li', recursive=False)]
            if items:
                content_elements.append({
                    'type': 'list',
                    'list_type': tag_name,
                    'items': items,
                    'id': element_id,
                    'class': element_class
                })
        
        # For paragraphs, only capture direct paragraphs (not nested)
        elif tag_name == 'p' and not element.find_parent(['li', 'blockquote']):
            content_elements.append({
                'type': 'paragraph',
                'text': text,
                'id': element_id,
                'class': element_class
            })
        
        # For sections/divs with IDs or specific classes, capture as containers
        elif tag_name in ['section', 'div'] and (element_id or 'hero' in element_class.lower() or 'feature' in element_class.lower()):
            # Only capture if it has meaningful ID or class
            child_text = element.get_text(separator=' ', strip=True)
            if child_text and len(child_text) > 20:  # Minimum content threshold
                content_elements.append({
                    'type': 'section',
                    'text': child_text[:500],  # Truncate long sections
                    'id': element_id,
                    'class': element_class
                })
    
    return {
        'url': url,
        'title': page_title,
        'description': description,
        'elements': content_elements
    }


def structure_to_markdown(structure):
    """Convert extracted structure to markdown format."""
    lines = []
    
    lines.append(f"# Page: {structure['title']}\n")
    lines.append(f"**Source URL:** {structure['url']}\n")
    
    if structure['description']:
        lines.append(f"**Meta Description:** {structure['description']}\n")
    
    lines.append("\n---\n\n## Content Structure\n")
    
    for elem in structure['elements']:
        # Add ID/class annotation if present
        annotation = []
        if elem.get('id'):
            annotation.append(f"id=\"{elem['id']}\"")
        if elem.get('class'):
            annotation.append(f"class=\"{elem['class']}\"")
        
        annotation_str = f" `[{', '.join(annotation)}]`" if annotation else ""
        
        if elem['type'] == 'heading':
            level = '#' * (elem['level'] + 1)  # Offset by 1 since we used # for page title
            lines.append(f"{level} {elem['text']}{annotation_str}\n")
        
        elif elem['type'] == 'paragraph':
            lines.append(f"{elem['text']}{annotation_str}\n")
        
        elif elem['type'] == 'list':
            list_marker = '-' if elem['list_type'] == 'ul' else '1.'
            lines.append(f"\n**List**{annotation_str}:")
            for item in elem['items']:
                lines.append(f"{list_marker} {item}")
            lines.append("")
        
        elif elem['type'] == 'section':
            lines.append(f"\n**Section**{annotation_str}:")
            lines.append(f"{elem['text']}...\n")
    
    return '\n'.join(lines)


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python extract_and_map.py <url> [--json]")
        print("  --json: Output as JSON instead of markdown")
        sys.exit(1)
    
    url = sys.argv[1]
    output_json = '--json' in sys.argv
    
    # Fetch and parse
    html = fetch_html(url)
    if not html:
        sys.exit(1)
    
    structure = extract_content_structure(html, url)
    
    # Output
    if output_json:
        print(json.dumps(structure, indent=2))
    else:
        print(structure_to_markdown(structure))


if __name__ == '__main__':
    main()
