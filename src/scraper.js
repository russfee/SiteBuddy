import axios from 'axios';

/**
 * Fetches HTML content from a given URL
 * @param {string} url - The URL to scrape
 * @returns {Promise<string>} - The HTML content
 */
export async function scrapeWebsite(url) {
  try {
    const response = await axios.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; SiteBuddy/1.0; +https://github.com/russfee/sitebuddy)',
      },
      timeout: 10000, // 10 second timeout
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      throw new Error(`Failed to fetch ${url}: ${error.response.status} ${error.response.statusText}`);
    } else if (error.request) {
      throw new Error(`Failed to fetch ${url}: No response received`);
    } else {
      throw new Error(`Failed to fetch ${url}: ${error.message}`);
    }
  }
}
