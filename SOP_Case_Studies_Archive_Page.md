# SOP: Case Studies Archive Page - Top 1% Technical SEO Implementation

**File:** `case-studies-archive.html`
**Target URL:** `https://reviewly.com.au/case-studies/`
**Assigned to:** Marvin (WordPress Developer)
**Brand Bible:** V6 (May 2026)
**Last updated:** 30 May 2026

---

## Purpose of This Document

This SOP defines every step required to implement the case studies archive page at `reviewly.com.au/case-studies/` to Top 1% standard. It covers WordPress configuration, schema validation, image optimisation, internal linking, performance, and post-launch verification. Every step must be completed before the page is considered live.

Read this document in full before starting. Do not skip steps.

---

## Important: Stats Strip Design Decision

The hero stats strip on this page uses **evergreen values only**. No stat references a count of case studies or an average that will change as new case studies are added. This is intentional.

| Stat | Label | Why It Is Evergreen |
|---|---|---|
| 100% | GSC-Verified Results | True regardless of how many case studies exist |
| AI | Recommended in ChatGPT, Perplexity & Google | A capability claim, not a count |
| 5 days | Fastest #1 Ranking on Record | A record result, not an average |
| #1 | Primary Keyword for Every Client | Our standard, not a tally |

**Do not add a case study count to the stats strip.** When new case studies are published, the stats strip does not need updating. The only maintenance required is adding a new card to the grid (see Step 10).

---

## Brand Bible V6 Colour Reference

All colours on this page are taken directly from Brand Bible V6 (May 2026) Part 10 Visual Identity. Do not modify any colours when pasting into WordPress.

| Colour | Hex | Used For |
|---|---|---|
| Primary Blue | #004AAD | Primary accent, buttons, key highlights |
| Accent Blue | #2C75E4 | Gradient, hover states, section labels |
| Dark Charcoal | #1B1B1F | Page background |
| Light Grey | #F3F4F6 | Light section backgrounds |
| White | #FFFFFF | All body text and headings |
| Gradient | #004AAD to #2C75E4 | Hero heading highlight, CTA button |

Typography: Arial, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif. No Google Fonts. No external font requests.

---

## Pre-Implementation Checklist

Before touching WordPress, confirm the following are ready:

| Item | Status |
|---|---|
| HTML file downloaded from GitHub | [ ] |
| Google Search Console access confirmed | [ ] |
| Yoast SEO or Rank Math plugin active on the site | [ ] |

> **Note:** All images are pre-built and embedded directly in the HTML file as CDN URLs. No image uploads are required. Do not replace the image URLs.

---

## Step 1: WordPress Page Setup

### 1.1 Create the Page

Navigate to **Pages > Add New** in WordPress. Set the following:

| Field | Value |
|---|---|
| Page title | `Case Studies` |
| Slug / Permalink | `case-studies` |
| Parent page | None (top-level) |
| Page template | Full Width (no sidebar, no default header/footer) |
| Status | Draft (do not publish until all steps are complete) |

> **Important:** The slug must be exactly `case-studies` with no trailing characters. The final URL must resolve to `https://reviewly.com.au/case-studies/` with a trailing slash.

### 1.2 Paste the HTML Content

The HTML file (`case-studies-archive.html`) is a self-contained page with all styles inline. Paste the full HTML into the WordPress page editor using the **HTML / Code Editor** view (not the Visual/Block editor). Do not allow WordPress to strip or modify the `<style>` block or any `<script type="application/ld+json">` blocks.

If using Elementor or another page builder, use a **Custom HTML** widget to paste the full file content into a full-width section.

### 1.3 Disable Default WordPress Elements

The HTML file includes its own layout. Disable the following WordPress defaults for this page:

- Default page title (H1 is already in the HTML)
- Sidebar
- Default header (if the theme injects one above the content area)
- Default footer (if the theme injects one below the content area)

Most themes handle this via the Full Width page template. If the theme does not have a Full Width template, use a custom page template or a page builder full-width mode.

---

## Step 2: SEO Plugin Configuration (Yoast SEO or Rank Math)

### 2.1 Meta Title

Set the SEO title to exactly:

```
Client Results | Visibility Architecture Case Studies | Reviewly
```

Character count: 63 characters. Within the 580px pixel width Google allows.

### 2.2 Meta Description

Set the meta description to exactly:

```
Real outcomes from Australian businesses that partnered with Reviewly. See how entity-driven visibility architecture delivers measurable results in AI search, Google, and local discovery.
```

Character count: 189 characters.

### 2.3 Canonical URL

Set the canonical URL to:

```
https://reviewly.com.au/case-studies/
```

This must include the trailing slash. The canonical tag is already in the HTML file but must also be set in the SEO plugin to prevent WordPress from generating a conflicting canonical.

### 2.4 Open Graph Settings

In the Social / Open Graph section of the SEO plugin:

| Field | Value |
|---|---|
| OG Title | `Client Results \| Visibility Architecture Case Studies \| Reviewly` |
| OG Description | `Real outcomes from Australian businesses that partnered with Reviewly. See how entity-driven visibility architecture delivers measurable results in AI search, Google, and local discovery.` |
| OG Image | Upload the 1200x630px JPEG to Media Library and select it here |
| OG Image Alt | `Reviewly case studies - verified visibility architecture results for Australian businesses` |

### 2.5 Breadcrumb Configuration

If using Yoast SEO breadcrumbs, ensure the breadcrumb path for this page is:

```
Home > Case Studies
```

The BreadcrumbList schema is already embedded in the HTML file. If the plugin generates a conflicting BreadcrumbList, disable the plugin's schema output for this page only.

---

## Step 3: Schema Validation

The HTML file contains four JSON-LD schema blocks. Each must pass Google's Rich Results Test before the page goes live.

| Schema Type | Purpose | Validation URL |
|---|---|---|
| `CollectionPage` + `ItemList` | Tells Google this is an archive of case study pages | https://search.google.com/test/rich-results |
| `BreadcrumbList` | Enables breadcrumb display in SERPs | https://search.google.com/test/rich-results |
| `Organization` | Reinforces Reviewly's entity identity | https://validator.schema.org |
| `FAQPage` | Enables FAQ rich result in SERPs | https://search.google.com/test/rich-results |

### 3.1 How to Validate

1. Publish the page as **Private** (not public) in WordPress.
2. Copy the page URL.
3. Go to https://search.google.com/test/rich-results
4. Paste the URL and run the test.
5. Confirm all four schema types are detected with no errors (warnings are acceptable).
6. If errors appear, check that the SEO plugin has not injected conflicting schema blocks. Disable plugin schema for this page if needed.

### 3.2 Common Schema Conflicts to Watch For

WordPress SEO plugins (Yoast, Rank Math) automatically inject their own `WebPage`, `Organization`, and `BreadcrumbList` schema. This can cause duplicate or conflicting schema. To resolve:

- In **Yoast SEO**: Go to the page's Yoast settings panel and disable schema output for this specific page.
- In **Rank Math**: Go to the page's Rank Math settings > Schema tab and set Schema Type to "None".

The schema in the HTML file is the authoritative version. Plugin-generated schema must not conflict with it.

---

## Step 4: Images

All images are pre-built and embedded in the HTML file as CDN-hosted WebP URLs. No uploads, no compression, no Media Library work required.

| Image | Purpose | Status |
|---|---|---|
| OG / Social Share Image (1200x630px) | Displays when the page is shared on LinkedIn, Facebook, or via link preview | Pre-built, embedded in `og:image` and `twitter:image` meta tags |
| SOS Property Advocacy card thumbnail | Featured case study card image | Pre-built, embedded in `<img src>` |
| Paw4Paws Dog Grooming card thumbnail | Case study grid card image | Pre-built, embedded in `<img src>` |
| Bela Beauty College card thumbnail | Case study grid card image | Pre-built, embedded in `<img src>` |
| Financial Education Firm card thumbnail | Case study grid card image | Pre-built, embedded in `<img src>` |

> **Do not replace any image URLs.** The CDN URLs are permanent and tied to the Reviewly project lifecycle. Replacing them with WordPress Media Library URLs is unnecessary and would break the images if the WordPress uploads are ever moved or deleted.

---

## Step 5: Internal Linking

### 5.1 Links Already in the HTML File

The HTML file contains the following internal links. Verify each resolves correctly after the individual case study pages are installed:

| Link Text | Target URL | Action Required |
|---|---|---|
| "Read the Full Case Study" (SOS featured card) | `/case-studies/sos-property-advocacy/` | Verify after SOS URL fix |
| Paw4Paws card | `/case-studies/paw4paws-dog-grooming/` | Verify after Paw4Paws install |
| Bela Beauty College card | `/case-studies/bela-beauty-college/` | Verify after Bela install |
| Financial Education Firm card | `/case-studies/financial-education-share-of-voice/` | Verify after Financial Edu install |
| "Request a Visibility Audit" CTA | `/contact/` | Confirm this URL is correct on the live site |

### 5.2 Links TO This Page (From Other Pages)

After the archive page is live, add links to it from the following existing pages:

| Source Page | Anchor Text | Notes |
|---|---|---|
| Homepage | "See client results" or "View case studies" | Add to the social proof / results section |
| About page | "our client results" | Natural contextual link |
| Services / Visibility Architecture page | "documented client outcomes" | Contextual link in body copy |
| Navigation menu | "Results" or "Case Studies" | Add to main nav if not already present |
| Individual case study pages | "View all case studies" | Footer or navigation on each case study |

These inbound internal links are critical. Without them the archive page is an orphan and will not receive link equity from the rest of the site.

---

## Step 6: Core Web Vitals and Performance

### 6.1 Current Performance Baseline

The HTML file is already optimised with:
- All images using `loading="lazy"` (except above-the-fold hero)
- No external font requests (Arial/system-ui only, per Brand Bible V6)
- No JavaScript dependencies
- All CSS inline (no render-blocking external stylesheets)
- No jQuery or WordPress script dependencies required

### 6.2 Caching

Ensure the following caching rules apply:
- Page caching: enabled (WP Rocket, W3 Total Cache, or equivalent)
- Browser caching: enabled for static assets
- CDN: if Cloudflare is active on reviewly.com.au, ensure the page is cached at the edge

### 6.3 Target Core Web Vitals Scores

| Metric | Target | Tool |
|---|---|---|
| LCP (Largest Contentful Paint) | Under 2.5 seconds | PageSpeed Insights |
| CLS (Cumulative Layout Shift) | Under 0.1 | PageSpeed Insights |
| INP (Interaction to Next Paint) | Under 200ms | PageSpeed Insights |
| Mobile PageSpeed Score | 85+ | https://pagespeed.web.dev |
| Desktop PageSpeed Score | 95+ | https://pagespeed.web.dev |

Run PageSpeed Insights after the page goes live: https://pagespeed.web.dev/?url=https://reviewly.com.au/case-studies/

---

## Step 7: Heading Structure

Do not modify any heading levels when pasting into WordPress. The heading hierarchy is:

| Heading | Text | Level |
|---|---|---|
| H1 | "When AI Knows Your Business, Customers Choose You" | H1 |
| H2 | "The Fastest Path to #1" | H2 |
| H2 | "How a Brand New Business Ranked #1 for Its Top Keyword in 5 Days" | H2 |
| H2 | "Verified Outcomes Across Four Sectors" | H2 |
| H3 | Individual case study card titles | H3 |
| H2 | "What We Measure and Why It Matters" | H2 |
| H2 | "Frequently Asked Questions" | H2 |
| H2 | "Find Out Where Your Business Stands in AI Search" | H2 |

---

## Step 8: Post-Publication Verification Checklist

Complete every item after publishing. Do not mark the task as done until all items are ticked.

### Technical Checks

| Check | Tool | Expected Result |
|---|---|---|
| Page loads at correct URL | Browser | `https://reviewly.com.au/case-studies/` returns 200 |
| Canonical tag is correct | View Source | Points to `https://reviewly.com.au/case-studies/` |
| Meta title is correct | View Source | Matches exactly as specified in Step 2.1 |
| Meta description is correct | View Source | Matches exactly as specified in Step 2.2 |
| Robots meta is correct | View Source | `index, follow, max-snippet:-1, max-image-preview:large` |
| All 4 schema blocks validate | Rich Results Test | No errors |
| OG image loads correctly | Facebook Debugger | 1200x630px image displays in preview |
| Twitter Card renders | Twitter Card Validator | Summary large image with correct title and description |
| All internal links resolve | Click each card link | No 404 errors |
| Images load with correct alt text | View Source | All `<img>` tags have descriptive alt attributes |
| Mobile layout correct | Chrome DevTools | Cards stack to single column, text readable |

### SEO Submission

| Action | Tool |
|---|---|
| Submit URL for indexing | Google Search Console > URL Inspection > Request Indexing |
| Fetch and render | Google Search Console > URL Inspection |
| Check for crawl errors | Google Search Console > Coverage |
| Submit to Bing | Bing Webmaster Tools > URL Submission |

### Social Sharing Test

| Platform | Tool |
|---|---|
| Facebook / LinkedIn | https://developers.facebook.com/tools/debug/ |
| Twitter / X | https://cards-dev.twitter.com/validator |

---

## Step 9: Adding New Case Studies (Ongoing Maintenance)

Each time a new case study is published, update the archive page as follows. The stats strip does **not** need updating - it uses evergreen values by design.

**Checklist for each new case study added:**

1. Add a new card to the `cs-grid` section in the HTML file, following the same structure as the existing cards.
2. Update the `ItemList` in the `CollectionPage` schema to include the new case study as a `ListItem` with the correct position number.
3. Update the `numberOfItems` value in the schema to reflect the new total.
4. Re-validate all schema after updating (Rich Results Test).
5. Submit the updated archive URL to Google Search Console for re-indexing.
6. Push the updated HTML file to GitHub.

**Do not update the stats strip.** The four evergreen stats remain accurate regardless of how many case studies are published.

---

## Step 10: Backlog - WordPress Custom Post Type Build

When time permits, the archive page should be rebuilt as a proper WordPress custom post type. This is a one-time build that will auto-count published case studies and auto-calculate averages from custom fields, eliminating the need for any manual HTML edits when new case studies are added.

**Estimated build time:** 3 to 4 hours for an experienced WordPress developer.

**What it involves:**
- Register a `case-study` custom post type in WordPress
- Add custom fields (ACF or similar) for GSC metrics on each case study post
- Build a page template that queries and counts published case studies
- Wire the schema ItemList to pull dynamically from published posts

This is a backlog task, not a blocker for the current launch. The current HTML-based approach is fully functional and correct. The custom post type build is the long-term infrastructure upgrade.

---

## Technical SEO Audit Summary

| Element | In HTML File | Marvin Action Required |
|---|---|---|
| `<title>` tag | Yes | Set in SEO plugin to match |
| Meta description | Yes | Set in SEO plugin to match |
| Canonical URL | Yes | Set in SEO plugin to match |
| Robots meta | Yes | None |
| Open Graph tags (full set) | Yes | Upload OG image to Media Library, update src in HTML |
| OG image dimensions (width, height, type) | Yes | None |
| Twitter Card meta | Yes | None |
| CollectionPage + ItemList schema | Yes | Validate in Rich Results Test |
| BreadcrumbList schema | Yes | Validate in Rich Results Test |
| Organization schema | Yes | Validate in schema.org validator |
| FAQPage schema | Yes | Validate in Rich Results Test |
| Visible FAQ section | Yes | None (already in HTML) |
| H1 tag | Yes | Do not modify |
| H2-H4 hierarchy | Yes | Do not modify |
| Image alt text (all images) | Yes | None |
| `loading="lazy"` on below-fold images | Yes | None |
| Evergreen stats strip | Yes | Do not add a case study count |
| Internal links to case study pages | Yes | Verify all resolve after installs |
| Internal links FROM other pages TO archive | No | Add from homepage, about, services, nav |
| OG image file | Yes - CDN hosted | Do not replace the URL |
| Card thumbnail images (4) | Yes - CDN hosted | Do not replace the URLs |
| Image compression | Yes - WebP format | No action required |
| Page caching | No | Confirm WP Rocket or equivalent is active |
| GSC indexing submission | No | Submit after publishing |
| Bing Webmaster Tools submission | No | Submit after publishing |
| Facebook OG debugger test | No | Run after publishing |
| Rich Results Test validation | No | Run after publishing |
| DAN tracking pixel | Yes | None |

---

## Files Referenced in This SOP

All files are in the public GitHub repository: https://github.com/ReviewlyAU/reviewly-case-studies

| File | Description |
|---|---|
| `case-studies-archive.html` | The complete archive page HTML - paste into WordPress |
| `SOP_Case_Studies_Archive_Page.md` | This document |
| `SOP_SOS_Property_Advocacy_Case_Study.md` | Install SOP for SOS case study |
| `SOP_Paw4Paws_Case_Study.md` | Install SOP for Paw4Paws case study |
| `SOP_Financial_Education_Case_Study.md` | Install SOP for Financial Education case study |

---

## Questions?

Contact Tanya via the #reviewly Slack channel with any questions about this implementation.
