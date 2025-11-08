// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://dentistrygrowthpartners.com',
  output: 'static',
  build: {
    inlineStylesheets: 'never',
  },
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
      // Filter out backup and old files for clean sitemap
      filter: (page) => {
        const url = page.toLowerCase();
        return !url.includes('index-old') &&
               !url.includes('index-backup') &&
               !url.includes('index%20copy') &&
               !url.includes('-old') &&
               !url.includes('.backup') &&
               !url.includes('contact-old') &&
               !url.includes('aio-seo-old') &&
               !url.includes('multi-implant-marketing-old') &&
               !url.includes('website-design-management-old');
      },
    }),
  ],
});
