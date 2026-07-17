# Marvin Deployment Brief: Trades & Construction Audience Page

**Date:** 17 July 2026

**Final URL:** `https://reviewly.com.au/who-reviewly-is-for/trades-and-construction/`

**Status:** Approved to build as a WordPress draft. **Do not publish until Claude completes the final preview check.**

## 1. Purpose and audience

This is an audience page under **Who Reviewly Is (and isn't) For**, not a service page. It is written for established trades and construction businesses operating multiple sites, locations, branches or crews. The H1 remains broad for search intent, while the supporting copy makes the multi-site fit boundary clear.

Do not reposition the page for sole traders or add generic local-marketing language.

## 2. Required proof rule

Jones Plumbing Plus must not appear anywhere on this page. Jones is supplier and building-merchant proof and belongs only on the Trade Suppliers & Building Merchants page.

The completed HTML contains no Jones reference, client proof card, Visibility Score, Share of Voice figure, average-position result or named competitor comparison. The replacement section is **How we'd approach a multi-site trades business**. It describes Reviewly's approach honestly and makes no result claim.

Do not add a client, number or research statistic. A research figure may be added only when the genuine source, date and sample size are verified. A client proof card may be added only when a consented multi-site trades or construction result exists.

## 3. WordPress content block

Use:

`industry-pages/trades-and-construction.html`

Copy the `<div class="page-content-block">` and all content inside it into the WordPress page. Do not add separate `<html>`, `<head>` or `<body>` tags. WordPress supplies the global navigation and footer. The included CSS is scoped to the content block and uses Brand Bible V6 colours: Primary Blue `#004AAD` and Accent Teal `#34D1BC`.

## 4. Hub-and-spoke URL structure

| Page | Final URL |
|---|---|
| Who Reviewly Is For hub | `/who-reviewly-is-for/` |
| Trades & Construction | `/who-reviewly-is-for/trades-and-construction/` |
| Trade Suppliers & Building Merchants | `/who-reviewly-is-for/trade-suppliers/` |
| Multi-Location & Franchise | `/who-reviewly-is-for/multi-location/` |

The live hub must link to each audience page. Each audience page must link back to the hub. The Trades page already contains links to the hub, Trade Suppliers and Multi-Location at their final URLs.

At the time of this brief, `/who-reviewly-is-for/` returned HTTP 200. The three child URLs and the old `/trades-and-construction/` path returned HTTP 404. Do not publish the Trades page while its required child-page links still resolve to 404. If `/trades-and-construction/` is created, published or indexed before the final URL launches, add a permanent 301 redirect from it to `/who-reviewly-is-for/trades-and-construction/`. Do not create the old path merely to redirect it.

## 5. Metadata and schema

| Field | Approved value |
|---|---|
| SEO title | `AI Visibility for Trades & Construction \| Reviewly` |
| Meta description | `GEO for established Australian trades and construction businesses operating multiple sites or crews. Build consistent trust signals across every location.` |
| Canonical | `https://reviewly.com.au/who-reviewly-is-for/trades-and-construction/` |

The HTML contains commented Article and FAQPage JSON-LD. Extract both `<script type="application/ld+json">` blocks and add them through the SEO plugin or page-head controls. The FAQ schema contains four questions and must exactly match the four visible FAQs. Confirm that the author, Tanya Somerton, and publisher, Reviewly, connect to their site-wide Person and Organization entities.

## 6. Related-link restriction

Do not add `/best-geo-agencies-australia/` to this page. The Reviewly-authored ranking requires a separate impartiality and Australian Consumer Law review before it can be treated as a cleared related resource.

## 7. Draft preview gate

Build the page as a draft and provide the preview URL for Claude's final check. The preview must confirm:

| Check | Required outcome |
|---|---|
| Audience | Established multi-site trades and construction operators are clearly addressed |
| Proof | No Jones Plumbing Plus, borrowed figure, client result or invented research statistic |
| FAQs | Four visible questions exactly match four FAQPage schema entries |
| Canonical | Final nested URL is used in metadata and Article schema |
| Cluster links | Hub, Trade Suppliers and Multi-Location links use the approved final URLs |
| Link health | No required internal link resolves to 404 at publication time |
| Brand | Visibility Architecture Partner, REVIEW Method® and Brand Bible V6 colours remain intact |

Publication is not authorised until this preview review is complete.

## 8. Post-approval publication checklist

After final approval, publish the page, add it to the XML sitemap, submit the final canonical URL in Google Search Console, validate the Article and FAQPage schema, confirm mobile and desktop rendering, and notify Tanya after the indexing request. Any deployment-side source changes must also be pushed to GitHub.
