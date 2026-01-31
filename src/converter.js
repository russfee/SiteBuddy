import TurndownService from 'turndown';
import { load } from 'cheerio';

/**
 * Converts HTML to markdown
 * @param {string} html - The HTML content to convert
 * @returns {string} - The markdown content
 */
export function convertToMarkdown(html) {
  // Load HTML with Cheerio to clean it up
  const $ = load(html);

  // Remove script and style tags
  $('script, style, noscript').remove();

  // Get the main content (prefer article, main, or body)
  let content = $('article').html() || $('main').html() || $('body').html();

  if (!content) {
    content = html;
  }

  // Initialize Turndown service
  const turndownService = new TurndownService({
    headingStyle: 'atx',
    codeBlockStyle: 'fenced',
    bulletListMarker: '-',
  });

  // Convert to markdown
  const markdown = turndownService.turndown(content);

  return markdown;
}
