# Marvin Deployment Brief: Trades & Construction Industry Page

**Date:** 17 July 2026
**Target URL:** `reviewly.com.au/trades-and-construction/`
**Status:** Approved for immediate deployment.

## 1. Page Content
The complete HTML content block is located at:
`/home/ubuntu/reviewly-case-studies/industry-pages/trades-and-construction.html`

**Deployment Instructions:**
- Do NOT copy any `<html>`, `<head>`, or `<body>` tags.
- Copy ONLY the `<div class="page-content-block">` and its contents into the WordPress editor/builder.
- The WordPress theme will automatically supply the global header (navigation) and footer.
- The CSS `<style>` block included inside the div is scoped specifically to this content block and uses the confirmed V6 brand colours (Primary Blue `#004AAD`, Accent Teal `#34D1BC`).

## 2. Meta Data & Schema
You must inject the following into the page `<head>` using the SEO plugin (e.g., Yoast/RankMath) or header scripts tool:

**Title:** `AI Visibility for Trades & Construction in Australia | Reviewly`
**Meta Description:** `How Australian trades and construction businesses become understood, trusted, and recommended by AI systems. The definitive GEO framework for contractors.`

**JSON-LD Schema:**
The HTML file contains commented-out `<script type="application/ld+json">` blocks for both `Article` and `FAQPage` schema. You must extract these blocks and inject them into the page header. Ensure the `author` (Tanya Somerton) and `publisher` (Reviewly) nodes are correctly linked to the site's main Organization schema.

## 3. Global CSS Check
While deploying this page, please verify that the global WordPress theme CSS has been updated to use the new Accent Teal (`#34D1BC`) instead of the retired blue (`#2C75E4`), as requested in the CMO board update from 15 July 2026.

## 4. Post-Deployment
Once the page is live:
1. Verify the URL renders correctly on mobile and desktop.
2. Confirm the FAQ schema validates in the Google Rich Results Test.
3. Submit the URL to Google Search Console for immediate indexing.
4. Add the URL to the XML sitemap.
