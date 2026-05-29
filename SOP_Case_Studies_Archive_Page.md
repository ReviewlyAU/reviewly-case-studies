# SOP: Case Studies Archive Page — Top 1% Technical SEO Implementation
**File:** `case-studies-archive.html`
**Target URL:** `https://reviewly.com.au/case-studies/`
**Assigned to:** Marvin (WordPress Developer)
**Brand Bible:** V6 (May 2026)
**Last updated:** 29 May 2026

---

## Purpose of This Document

This SOP defines every technical SEO requirement for implementing the case studies archive page at `reviewly.com.au/case-studies/` to Top 1% standard. It covers WordPress configuration, schema validation, image optimisation, internal linking, performance, and post-launch verification. Every step must be completed before the page is considered live.

---

## Pre-Implementation Checklist

Before touching WordPress, confirm the following are ready:

| Item | Status |
|---|---|
| HTML file downloaded from GitHub | [ ] |
| OG image (1200x630px JPEG) uploaded to WordPress Media Library | [ ] |
| Thumbnail images for all 4 case study cards uploaded to Media Library | [ ] |
| Reviewly logo file confirmed at correct Media Library path | [ ] |
| Google Search Console access confirmed | [ ] |
| Yoast SEO or Rank Math plugin active on the site | [ ] |

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

Character count: 63 characters. This is within the 50-60 character ideal range and fits within the 580px pixel width Google allows.

### 2.2 Meta Description

Set the meta description to exactly:

```
Real outcomes from Australian businesses that partnered with Reviewly. See how entity-driven visibility architecture delivers measurable results in AI search, Google, and local discovery.
```

Character count: 189 characters. This is within the 150-160 character recommended range for display.

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
| OG Image Alt | `Reviewly case studies — verified visibility architecture results for Australian businesses` |

### 2.5 Breadcrumb Configuration

If using Yoast SEO breadcrumbs, ensure the breadcrumb path for this page is:

```
Home > Case Studies
```

The BreadcrumbList schema is already embedded in the HTML file. Do not duplicate it via the plugin unless the plugin's output is identical. If the plugin generates a conflicting BreadcrumbList, disable the plugin's schema output for this page only.

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

- In **Yoast SEO**: Go to SEO > Search Appearance > Content Types > Pages and disable "Schema output" for this specific page using the page-level Yoast settings panel.
- In **Rank Math**: Go to the page's Rank Math settings > Schema tab and set Schema Type to "None" to prevent Rank Math from injecting its own schema.

The schema in the HTML file is the authoritative version. Plugin-generated schema must not conflict with it.

---

## Step 4: Image Optimisation

### 4.1 OG / Social Share Image

Upload a 1200x630px JPEG to the WordPress Media Library at the following path:

```
wp-content/uploads/2026/05/reviewly-case-studies-og.jpg
```

This image is referenced in the HTML file's Open Graph tags. If the upload path differs, update the `og:image` meta tag in the HTML accordingly.

**OG image requirements:**
- Dimensions: exactly 1200x630px
- Format: JPEG
- File size: under 300KB (compress with TinyJPG or Squoosh)
- Content: Reviewly logo on brand blue background (#004AAD), with headline text "Client Results | Visibility Architecture Case Studies"

### 4.2 Case Study Card Thumbnail Images

Each case study card references a featured image. Upload the following four images to the WordPress Media Library:

| Image File | Alt Text | Used In |
|---|---|---|
| `sos-property-advocacy-case-study.jpg` | `SOS Property Advocacy case study — ranked #1 for property advocacy Melbourne in 5 days` | Featured card |
| `paw4paws-dog-grooming-case-study.jpg` | `Paw4Paws Dog Grooming — AI recommended in ChatGPT and Google AI Mode` | Card 1 |
| `bela-beauty-college-case-study.jpg` | `Bela Beauty College — 142% increase in Google Search impressions` | Card 2 |
| `financial-education-share-of-voice-case-study.jpg` | `Financial education firm — 83% Share of Voice defended against Coursera and IG` | Card 3 |

**Image requirements for all card thumbnails:**
- Dimensions: 800x500px minimum (16:10 ratio)
- Format: JPEG or WebP
- File size: under 150KB each
- Alt text: as specified in the table above (already set in the HTML file)

### 4.3 Image Compression

All images must be compressed before upload. Use one of the following:
- https://tinyjpg.com (free, drag and drop)
- https://squoosh.app (free, browser-based)
- ShortPixel WordPress plugin (bulk compression after upload)

Target file sizes: OG image under 300KB, card thumbnails under 150KB each.

### 4.4 WebP Conversion (Recommended)

If the WordPress theme or a plugin (e.g., ShortPixel, Imagify) supports automatic WebP conversion, enable it. WebP images are 25-35% smaller than JPEG at equivalent quality, which improves Core Web Vitals scores. The HTML file uses `loading="lazy"` on all images below the fold, which is already implemented.

---

## Step 5: Internal Linking

Internal links are the connective tissue that distributes authority from the archive page to each individual case study. The following internal links must be active and correct before the page goes live.

### 5.1 Links Already in the HTML File

The HTML file contains the following internal links. Verify each resolves correctly after the individual case study pages are installed:

| Link Text | Target URL | Status |
|---|---|---|
| "Read the Full Case Study" (SOS featured card) | `/case-studies/sos-property-advocacy/` | Verify after SOS URL fix |
| Paw4Paws card | `/case-studies/paw4paws-dog-grooming/` | Verify after Paw4Paws install |
| Bela Beauty College card | `/case-studies/bela-beauty-college/` | Verify after Bela install |
| Financial Education Firm card | `/case-studies/financial-education-share-of-voice/` | Verify after Financial Edu install |
| "Request a Visibility Audit" CTA | `/contact/` | Verify this URL is correct |

### 5.2 Links TO This Page (From Other Pages)

After the archive page is live, add links to it from the following existing pages on reviewly.com.au:

| Source Page | Anchor Text | Notes |
|---|---|---|
| Homepage | "See client results" or "View case studies" | Add to the social proof / results section |
| About page | "our client results" | Natural contextual link |
| Services / Visibility Architecture page | "documented client outcomes" | Contextual link in body copy |
| Navigation menu | "Results" or "Case Studies" | Add to main nav if not already present |
| Individual case study pages | "View all case studies" | Footer or "Next" navigation on each case study |

These inbound internal links are critical. Without them, the archive page is an orphan and will not receive link equity from the rest of the site.

---

## Step 6: Core Web Vitals and Performance

### 6.1 Current Performance Baseline

The HTML file is optimised for performance with the following already implemented:
- All images use `loading="lazy"` (except above-the-fold hero, which loads immediately)
- No external font requests (Arial/system-ui only, per Brand Bible V6)
- No JavaScript dependencies
- All CSS is inline (no render-blocking external stylesheets)
- No jQuery or WordPress script dependencies required

### 6.2 Caching

Ensure the following caching rules apply to this page:
- Page caching: enabled (WP Rocket, W3 Total Cache, or equivalent)
- Browser caching: enabled for static assets (images, CSS)
- CDN: if Cloudflare is active on reviewly.com.au, ensure the page is cached at the edge

### 6.3 Target Core Web Vitals Scores

| Metric | Target | Tool to Verify |
|---|---|---|
| LCP (Largest Contentful Paint) | Under 2.5 seconds | PageSpeed Insights |
| CLS (Cumulative Layout Shift) | Under 0.1 | PageSpeed Insights |
| FID / INP (Interaction to Next Paint) | Under 200ms | PageSpeed Insights |
| Mobile PageSpeed Score | 85+ | https://pagespeed.web.dev |
| Desktop PageSpeed Score | 95+ | https://pagespeed.web.dev |

Run PageSpeed Insights after the page goes live: https://pagespeed.web.dev/?url=https://reviewly.com.au/case-studies/

---

## Step 7: Heading Structure Audit

The heading hierarchy on the page must follow a strict H1 > H2 > H3 > H4 structure. No heading levels should be skipped. The current structure in the HTML file is:

| Heading | Text | Level |
|---|---|---|
| H1 | "When AI Knows Your Business, Customers Choose You" | H1 (hero) |
| H2 | "The Fastest Path to #1" | H2 (featured section) |
| H2 | "How a Brand New Business Ranked #1 for Its Top Keyword in 5 Days" | H2 (featured card) |
| H2 | "Verified Outcomes Across Four Sectors" | H2 (grid section) |
| H3 | "How Paw4Paws Turned Local Trust Into Search Demand" | H3 (card) |
| H3 | "How Bela Beauty College Increased Search Impressions by 142% in Six Months" | H3 (card) |
| H3 | "How an Australian Firm Defended 83% Share of Voice Against Global Competitors" | H3 (card) |
| H2 | "What We Measure and Why It Matters" | H2 (methodology) |
| H4 | "Google Search Console" | H4 (pillar) |
| H4 | "AI Recommendation Evidence" | H4 (pillar) |
| H4 | "Google Business Profile" | H4 (pillar) |
| H4 | "Keyword Position Tracking" | H4 (pillar) |
| H2 | "Find Out Where Your Business Stands in AI Search" | H2 (CTA) |

This structure is correct. Do not modify heading levels when pasting into WordPress.

---

## Step 8: FAQ Section Visibility

The FAQPage schema is embedded in the HTML file's `<head>` but the FAQ questions are not rendered as visible content on the page. To maximise the chance of Google displaying FAQ rich results, the questions and answers should also appear as visible text on the page.

Add the following FAQ section to the HTML file immediately before the CTA section. This is the visible version of the FAQPage schema:

```html
<!-- FAQ SECTION — visible content matching FAQPage schema -->
<div style="max-width:1140px; margin:0 auto; padding:64px 24px;">
  <div style="margin-bottom:40px;">
    <div style="font-size:11px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:#2C75E4; margin-bottom:10px;">Common Questions</div>
    <h2 style="font-size:clamp(1.6rem,3vw,2.2rem); font-weight:800; color:#ffffff; letter-spacing:-0.02em; line-height:1.2;">Frequently Asked <span style="color:#2C75E4;">Questions</span></h2>
  </div>
  <div style="display:flex; flex-direction:column; gap:16px;">
    <details style="background:#0d1526; border:1px solid rgba(44,117,228,0.18); border-radius:10px; padding:20px 24px;">
      <summary style="font-size:1rem; font-weight:700; color:#ffffff; cursor:pointer; list-style:none;">What is a Visibility Architecture Partner?</summary>
      <p style="margin-top:12px; font-size:0.9rem; color:#c8d4e8; line-height:1.7;">A Visibility Architecture Partner builds the entity structure, trust signals, and AI-readable content that makes a business the obvious answer in both traditional search and AI-generated recommendations. Reviewly is Australia's leading Visibility Architecture Partner, helping service businesses appear in Google, ChatGPT, Perplexity, and Google AI Mode.</p>
    </details>
    <details style="background:#0d1526; border:1px solid rgba(44,117,228,0.18); border-radius:10px; padding:20px 24px;">
      <summary style="font-size:1rem; font-weight:700; color:#ffffff; cursor:pointer; list-style:none;">How long does it take to see results from visibility architecture?</summary>
      <p style="margin-top:12px; font-size:0.9rem; color:#c8d4e8; line-height:1.7;">Results vary by business and market. SOS Property Advocacy ranked number one for its primary keyword within five days of launch. Paw4Paws Dog Grooming saw a 138% increase in Google Search Console clicks within the first reporting period. Most clients see measurable movement in Google Search Console within 30 to 90 days.</p>
    </details>
    <details style="background:#0d1526; border:1px solid rgba(44,117,228,0.18); border-radius:10px; padding:20px 24px;">
      <summary style="font-size:1rem; font-weight:700; color:#ffffff; cursor:pointer; list-style:none;">Does Reviewly work with businesses outside Australia?</summary>
      <p style="margin-top:12px; font-size:0.9rem; color:#c8d4e8; line-height:1.7;">Reviewly is an Australian-owned business focused on the Australian market. All case studies documented on this page are Australian businesses. Enquiries from international businesses are assessed on a case-by-case basis.</p>
    </details>
    <details style="background:#0d1526; border:1px solid rgba(44,117,228,0.18); border-radius:10px; padding:20px 24px;">
      <summary style="font-size:1rem; font-weight:700; color:#ffffff; cursor:pointer; list-style:none;">What evidence do you provide with each case study?</summary>
      <p style="margin-top:12px; font-size:0.9rem; color:#c8d4e8; line-height:1.7;">Every Reviewly case study is documented with four types of verified evidence: Google Search Console data (clicks, impressions, average position), AI recommendation screenshots from ChatGPT, Perplexity, Claude, and Google AI Mode, Google Business Profile Insights data, and before-and-after keyword position tracking against named competitors.</p>
    </details>
    <details style="background:#0d1526; border:1px solid rgba(44,117,228,0.18); border-radius:10px; padding:20px 24px;">
      <summary style="font-size:1rem; font-weight:700; color:#ffffff; cursor:pointer; list-style:none;">How is Reviewly different from an SEO agency?</summary>
      <p style="margin-top:12px; font-size:0.9rem; color:#c8d4e8; line-height:1.7;">Traditional SEO agencies optimise for Google's ranking algorithm. Reviewly builds entity architecture that makes businesses visible and trustworthy to both search engines and AI systems. This includes structured data, trust signal networks, AI-readable content, and entity disambiguation — work that most SEO agencies do not perform.</p>
    </details>
  </div>
</div>
```

Paste this block into the HTML file immediately before the `<!-- CTA -->` comment block.

---

## Step 9: Post-Publication Verification Checklist

Complete every item on this checklist after publishing the page. Do not mark the task as done until all items are ticked.

### Technical Checks

| Check | Tool | Expected Result |
|---|---|---|
| Page loads at correct URL | Browser | `https://reviewly.com.au/case-studies/` returns 200 |
| Canonical tag is correct | View Source or Screaming Frog | `<link rel="canonical" href="https://reviewly.com.au/case-studies/" />` |
| Meta title is correct | View Source | `Client Results \| Visibility Architecture Case Studies \| Reviewly` |
| Meta description is correct | View Source | 189-character description as specified |
| Robots meta is correct | View Source | `index, follow, max-snippet:-1, max-image-preview:large` |
| All 4 schema blocks validate | Rich Results Test | No errors on CollectionPage, BreadcrumbList, Organization, FAQPage |
| OG image loads correctly | Facebook Debugger | 1200x630px image displays in preview |
| Twitter Card renders | Twitter Card Validator | Summary large image with correct title and description |
| All internal links resolve | Click each card link | No 404 errors |
| Images load with correct alt text | View Source | All `<img>` tags have descriptive alt attributes |
| No render-blocking resources | PageSpeed Insights | No external CSS or JS blocking first paint |
| Mobile layout correct | Chrome DevTools mobile view | Cards stack to single column, text readable |

### SEO Submission

| Action | Tool | Notes |
|---|---|---|
| Submit URL for indexing | Google Search Console > URL Inspection > Request Indexing | Do this immediately after publishing |
| Fetch and render | Google Search Console | Confirm Googlebot can render the page |
| Check for crawl errors | Google Search Console > Coverage | No 4xx or 5xx errors |
| Verify in Bing Webmaster Tools | Bing Webmaster Tools > URL Submission | Submit `https://reviewly.com.au/case-studies/` |

### Social Sharing Test

| Platform | Tool | Expected Result |
|---|---|---|
| Facebook / LinkedIn | https://developers.facebook.com/tools/debug/ | OG image, title, and description display correctly |
| Twitter / X | https://cards-dev.twitter.com/validator | Summary large image card displays correctly |

---

## Step 10: Ongoing Maintenance

### When a New Case Study is Published

Each time a new case study goes live, update the archive page as follows:

1. Add a new card to the `cs-grid` section in the HTML file following the same structure as the existing cards.
2. Update the `ItemList` in the `CollectionPage` schema to include the new case study as a `ListItem` with the correct position number.
3. Update the `numberOfItems` value in the schema.
4. Update the aggregate stats in the hero section if the new case study adds new data points (e.g., a new AI platform, a new record metric).
5. Re-validate all schema after updating.
6. Submit the updated archive URL to Google Search Console for re-indexing.

### Quarterly Review

Every quarter, review the archive page for the following:

- Are all case study card links still resolving correctly?
- Have any case study URLs changed? (If so, update the archive page and schema.)
- Are the aggregate stats in the hero section still accurate?
- Has the OG image become outdated? (Update if Reviewly branding changes.)
- Are there new case studies to add?

---

## Technical SEO Audit Summary

The following table summarises every technical SEO element on this page and its implementation status at time of delivery.

| Element | Implemented in HTML | Marvin Action Required |
|---|---|---|
| `<title>` tag | Yes | Set in SEO plugin to match |
| Meta description | Yes | Set in SEO plugin to match |
| Canonical URL | Yes | Set in SEO plugin to match |
| Robots meta | Yes | None |
| Open Graph tags (title, desc, url, image, type, locale, site_name) | Yes | Upload OG image to Media Library |
| og:image dimensions (width, height, type) | Yes | None |
| Twitter Card meta | Yes | None |
| CollectionPage + ItemList schema | Yes | Validate in Rich Results Test |
| BreadcrumbList schema | Yes | Validate in Rich Results Test |
| Organization schema | Yes | Validate in schema.org validator |
| FAQPage schema | Yes | Add visible FAQ section (see Step 8) |
| H1 tag | Yes | Do not modify |
| H2-H4 hierarchy | Yes | Do not modify |
| Image alt text (all images) | Yes | None |
| `loading="lazy"` on below-fold images | Yes | None |
| Internal links to case study pages | Yes | Verify all resolve after installs |
| Internal links FROM other pages TO archive | No | Add links from homepage, about, services, nav |
| OG image file | No | Create and upload (1200x630px JPEG) |
| Card thumbnail images (4 images) | No | Upload to Media Library |
| Image compression | No | Compress all images before upload |
| WebP conversion | No | Enable via ShortPixel or Imagify |
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
| `case-studies-archive.html` | The complete archive page HTML — paste into WordPress |
| `SOP_Case_Studies_Archive_Page.md` | This document |
| `SOP_Paw4Paws_Case_Study.md` | Install SOP for Paw4Paws case study |
| `SOP_Financial_Education_Case_Study.md` | Install SOP for Financial Education case study |
| `SOP_SOS_Property_Advocacy_Case_Study.md` | Install SOP for SOS case study |

---

## Questions?

Contact Tanya via the #reviewly Slack channel with any questions about this implementation.
