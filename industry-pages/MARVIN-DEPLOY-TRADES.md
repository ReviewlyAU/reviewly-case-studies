# Marvin Deployment Brief: Trades & Construction Industry Page

**Date:** 17 July 2026

**Final URL:** `https://reviewly.com.au/trades-and-construction/`

**Status:** Approved to build as a WordPress draft. **Do not publish until Claude completes the final check on the preview.**

## 1. Required approved change

The page file already contains the approved replacement in **The result in the field** section:

> Across 90 tracked keywords in the Albury–Corowa market, Jones Plumbing Plus went from being outranked by the trades it supplies to outperforming national chains on local visibility (June 2026).

This replaces the named Reece and SP Plus comparison and removes the proprietary Visibility Score from the page. The lower proof card remains unchanged and may retain the consented **66.9% Share of Voice** and average-position movement from **25.5 to 18.1**.

## 2. WordPress content block

The complete implementation file is:

`industry-pages/trades-and-construction.html`

Copy the `<div class="page-content-block">` and all content inside it into the WordPress page. Do not add separate `<html>`, `<head>`, or `<body>` tags. The WordPress theme supplies the global navigation and footer. The included CSS is scoped to this content block and uses Brand Bible V6 colours: Primary Blue `#004AAD` and Accent Teal `#34D1BC`.

## 3. Final URL and internal links

Use `/trades-and-construction/` as the single canonical URL. Do not create `/services/trades-construction/` as a second page.

Update the Trade Suppliers page link from `/services/trades-construction/` to `/trades-and-construction/`. When the Multi-Location page is built, it must also link to `/trades-and-construction/`, and this page should receive a reciprocal link where contextually relevant.

The link to `/best-geo-agencies-australia/` has been removed from the related-resources block pending a separate impartiality and Australian Consumer Law review. Do not restore that link unless it is cleared in writing.

## 4. Metadata and schema

Add the following metadata through the SEO plugin or page-head controls:

| Field | Approved value |
|---|---|
| SEO title | `AI Visibility for Trades & Construction \| Reviewly` |
| Meta description | `GEO for Australian trades and construction businesses. Build the verified trust signals AI systems use when recommending contractors.` |
| Canonical | `https://reviewly.com.au/trades-and-construction/` |

The HTML file contains commented Article and FAQPage JSON-LD. Extract both `<script type="application/ld+json">` blocks and inject them into the page head. Confirm that the author, Tanya Somerton, and publisher, Reviewly, connect to the corresponding site-wide Person and Organization entities.

## 5. Draft and preview gate

Build the page as a **draft** and provide the preview URL for Claude's final check. Publication is not authorised before that check is complete. The preview review must confirm that the named competitor comparison is absent, the lower proof card retains the approved figures, all three visible FAQs match the FAQ schema, and all internal links resolve to their final destinations.

## 6. Post-approval publication checklist

After final preview approval, publish the page and complete the following checks:

| Check | Required outcome |
|---|---|
| Responsive rendering | Confirmed on mobile and desktop |
| Global colour system | Accent Teal `#34D1BC`; no retired `#2C75E4` in page or relevant theme rules |
| Structured data | Article and FAQPage schema valid; visible FAQ content matches schema |
| Internal links | No reference to `/services/trades-construction/`; all page links return successful responses |
| XML sitemap | Final canonical URL included |
| Google Search Console | Final URL submitted for indexing |
| Team notification | Tanya notified after publication and indexing request |
| Version control | Any deployment-side source changes pushed to GitHub |
