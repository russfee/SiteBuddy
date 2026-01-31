#!/usr/bin/env node

import { Command } from 'commander';
import { scrapeWebsite } from './scraper.js';
import { convertToMarkdown } from './converter.js';
import { writeFile } from 'fs/promises';
import { fileURLToPath } from 'url';
import path from 'path';

const program = new Command();

program
  .name('sitebuddy')
  .description('Convert websites to markdown files')
  .version('1.0.0')
  .argument('<url>', 'URL of the website to convert')
  .option('-o, --output <file>', 'Output file name')
  .action(async (url, options) => {
    try {
      console.log(`Fetching ${url}...`);

      // Scrape the website
      const html = await scrapeWebsite(url);

      console.log('Converting to markdown...');

      // Convert to markdown
      const markdown = convertToMarkdown(html);

      // Generate output filename if not provided
      let outputFile = options.output;
      if (!outputFile) {
        const urlObj = new URL(url);
        const hostname = urlObj.hostname.replace(/\./g, '-');
        const pathname = urlObj.pathname.replace(/\//g, '-').replace(/^-|-$/g, '') || 'index';
        outputFile = `${hostname}${pathname ? '-' + pathname : ''}.md`;
      }

      // Write to file
      await writeFile(outputFile, markdown, 'utf8');

      console.log(`✓ Saved to ${outputFile}`);
    } catch (error) {
      console.error('Error:', error.message);
      process.exit(1);
    }
  });

program.parse();
