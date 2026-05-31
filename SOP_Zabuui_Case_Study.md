# SOP: Zabuui Hairdesigners Case Study Page
## Deployment Standard Operating Procedure for Marvin
**Version:** 1.0
**Date:** 31 May 2026
**Prepared by:** Reviewly CMO
**File:** `case-study-zabuui.html`
**Target URL:** `https://reviewly.com.au/case-studies/zabuui-hairdesigners-local-seo-wodonga/`

---

## Pre-Deployment Checklist (Read Before Starting)

All technical SEO work has been completed in the HTML file. Do not modify the `<head>` section, schema blocks, or CSS colour variables. Your job is to install the page correctly in WordPress, not to redesign it.

**Brand Bible V6 compliance has been verified:**
- Font: Arial, system-ui (no Google Fonts)
- Colours: #004AAD (Primary Blue), #2C75E4 (Accent Blue), #1B1B1F (Dark Charcoal), #FFFFFF (White)
- Zero em dashes
- Zero teal or purple values
- Zero off-brand colours

---

## What Is Already Done (No Action Required from Marvin)

| Element | Status |
|---|---|
| Meta title and description | Complete |
| Canonical tag | Complete - points to /case-studies/zabuui-hairdesigners-local-seo-wodonga/ |
| Robots meta tag | Complete - index, follow, max-snippet:-1 |
| Open Graph tags (og:title, og:description, og:image, og:url) | Complete |
| Twitter Card tags | Complete |
| OG image (1200x630px) | Pre-built and embedded via CDN URL |
| Article schema (JSON-LD) | Complete |
| BreadcrumbList schema (JSON-LD) | Complete |
| FAQPage schema (JSON-LD) | Complete |
| Heading hierarchy (H1, H2, H3, H4) | Complete |
| All image alt text | Complete |
| DAN tracking pixel | Complete |
| Brand Bible V6 colours throughout | Complete |
| Arial/system-ui font (no Google Fonts) | Complete |
| Internal breadcrumb navigation | Complete |

---

## Step 1: WordPress Page Setup

1. Log in to the Reviewly WordPress admin at `reviewly.com.au/wp-admin`
2. Go to **Pages > Add New**
3. Set the page title to: `Case Study: Zabuui Hairdesigners`
4. Set the page slug to exactly: `zabuui-hairdesigners-local-seo-wodonga`
5. Set the parent page to: `case-studies` (this creates the URL /case-studies/zabuui-hairdesigners-local-seo-wodonga/)
6. Set the page template to: **Full Width** or **Elementor Full Width** (no sidebar, no header/footer from the theme - the HTML file includes its own navigation)
7. Switch to **Code Editor** view (not the visual editor)
8. Paste the entire contents of `case-study-zabuui.html` into the editor
9. Do not click Publish yet - complete Steps 2 and 3 first

---

## Step 2: SEO Plugin Configuration (Yoast or Rank Math)

Configure the SEO plugin to match the HTML exactly. Do not let the plugin override the canonical or meta description.

**If using Yoast SEO:**
- SEO Title: `Local SEO Case Study: From Position 38 to Number One | Zabuui Hairdesigners | Reviewly`
- Meta Description: `Zabuui Hairdesigners moved from position 38 to number one in local search within six months. A Reviewly REVIEW Method strategy supported a 9x business sale outcome within three years. See how visibility architecture builds a business worth selling.`
- Canonical URL: `https://reviewly.com.au/case-studies/zabuui-hairdesigners-local-seo-wodonga/`
- Social image: Upload the Zabuui card image (provided separately or use the CDN URL already in the HTML)
- Disable Yoast from outputting its own schema if the plugin allows it - the HTML already contains the correct schema

**If using Rank Math:**
- Title: same as above
- Description: same as above
- Canonical: same as above
- Schema: set to Article, but note the HTML already contains the correct Article + BreadcrumbList + FAQPage schema blocks

---

## Step 3: Schema Validation (Required Before Publishing)

Validate all three schema blocks before the page goes live. A page with broken schema is worse than a page with no schema.

1. Open Google's Rich Results Test: `https://search.google.com/test/rich-results`
2. Enter the page URL once it is saved as a draft (use the preview URL)
3. Confirm the following schema types are detected with no errors:
   - Article
   - BreadcrumbList (Home > Case Studies > Zabuui Hairdesigners)
   - FAQPage (3 questions visible)
4. If any errors appear, do not publish. Contact the CMO before proceeding.

---

## Step 4: Internal Linking (Critical for SEO)

The page needs inbound internal links from the rest of the site to receive link equity. Without these, the page is an orphan and will rank poorly.

**Required links to add:**

| Source Page | Where to Add the Link | Anchor Text |
|---|---|---|
| /case-studies/ (archive page) | Add a new card for Zabuui to the archive grid | "Zabuui Hairdesigners - Position 38 to #1" |
| Homepage | In the case studies or results section | "See how Zabuui sold for 9x" |
| /about/ | In the results or track record section | "local SEO case study" |
| /services/ | In the local SEO or visibility architecture section | "local visibility case study" |

**How to add the Zabuui card to the archive page:**
The archive page (`case-studies-archive.html`) already has a three-column grid. Add a fourth card following the same HTML structure as the existing Paw4Paws, Bela, or Financial Education cards. Use the Zabuui card image CDN URL:
`https://d2xsxph8kpxj0f.cloudfront.net/310519663277344756/Rw7yvX7d6MJiwMBUzbGRZf/reviewly-zabuui-card-eQBm4EZCUE2vAN8bwp9WTX.webp`

---

## Step 5: Publish and Submit to Google Search Console

1. Click **Publish** in WordPress
2. Verify the page loads correctly at: `https://reviewly.com.au/case-studies/zabuui-hairdesigners-local-seo-wodonga/`
3. Log in to Google Search Console for reviewly.com.au
4. Go to **URL Inspection**
5. Enter the full URL and click **Request Indexing**
6. Also submit the updated /case-studies/ archive URL for re-indexing (it now has a new card)

---

## Step 6: Post-Publication Verification Checklist

Complete every item on this checklist before marking the task as done.

**Technical checks:**
- [ ] Page loads at the correct URL with no 404 or redirect errors
- [ ] Canonical tag in the page source matches the target URL exactly
- [ ] Robots meta tag is present: `index, follow`
- [ ] All four schema blocks visible in Rich Results Test with no errors
- [ ] OG image displays correctly when the URL is pasted into LinkedIn's Post Inspector (`https://www.linkedin.com/post-inspector/`)
- [ ] Page is mobile-responsive (test on a phone or use Chrome DevTools)
- [ ] No broken image links (right-click > Inspect on each image)
- [ ] DAN tracking pixel is present before `</body>` in page source

**Content checks:**
- [ ] H1 reads: "From Position 38 to Number One. Then Sold for 9x."
- [ ] Breadcrumb shows: Home > Case Studies > Zabuui Hairdesigners
- [ ] Proof stats bar shows: 38 to #1, 9x sale multiple, six months, 755 monthly searches
- [ ] FAQ section is visible and expanded (3 questions)
- [ ] CTA section links to the Visibility Audit page
- [ ] No em dashes visible anywhere on the page
- [ ] No teal or purple colours visible anywhere on the page

**GSC and indexing:**
- [ ] URL submitted to Google Search Console for indexing
- [ ] Archive page re-submitted for indexing
- [ ] Notify CMO via Slack once the page is live and indexed

---

## Step 7: Notify CMO

Once the page is live and all checklist items are complete, send the following message in Slack:

> Zabuui case study is live at reviewly.com.au/case-studies/zabuui-hairdesigners-local-seo-wodonga/ - all schema validated, GSC submitted, internal links added. Archive page updated with new card.

---

## Key Facts Reference (for Internal Linking Copy)

Use these verified facts when writing anchor text or surrounding copy for internal links. Do not invent new claims.

| Claim | Source |
|---|---|
| Position 38 to #1 in local search | Documented in case study, GSC-verified |
| Six months to achieve #1 | Documented in case study |
| 9x business sale multiple within three years | Documented in case study |
| Keyword: "hairdresser Wodonga" - 755 monthly searches | Documented in case study |
| Business: Zabuui Hairdesigners, Wodonga VIC | Documented in case study |
| Strategy: REVIEW Method by Reviewly | Documented in case study |

---

## Backlog Task: WordPress Custom Post Type

When the site is ready for a larger infrastructure build, the case studies section should be migrated to a WordPress custom post type. This will allow the archive page to auto-count published case studies and auto-calculate average results without manual updates. This is a separate project - do not attempt it as part of this deployment. Raise it with the CMO when the timing is right.

---

## File Reference

| File | Purpose |
|---|---|
| `case-study-zabuui.html` | The complete case study page - paste into WordPress Code Editor |
| `SOP_Zabuui_Case_Study.md` | This document |
| Zabuui card image CDN URL | `https://d2xsxph8kpxj0f.cloudfront.net/310519663277344756/Rw7yvX7d6MJiwMBUzbGRZf/reviewly-zabuui-card-eQBm4EZCUE2vAN8bwp9WTX.webp` |

All files are in the GitHub repository: `https://github.com/ReviewlyAU/reviewly-case-studies`
