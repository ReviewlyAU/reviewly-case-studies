# SOP: Jones Plumbing Plus Case Study Page
## Reviewly Case Studies | Deployment and Technical SEO SOP
**File:** `case-study-jones-plumbing-plus.html`
**Target URL:** `https://reviewly.com.au/case-studies/jones-plumbing-plus/`
**Canonical slug:** `jones-plumbing-plus`
**Parent page:** `case-studies`
**Date:** June 2026
**Prepared by:** Reviewly CMO

---

## Pre-Deployment Checklist (Complete Before Publishing)

- [ ] WordPress page created at correct slug
- [ ] HTML pasted in Code Editor view
- [ ] Full Width template applied
- [ ] SEO plugin configured
- [ ] All four schema blocks validated in Rich Results Test
- [ ] Internal links added from four source pages
- [ ] Page published
- [ ] URL submitted to Google Search Console
- [ ] Post-publication checklist completed

---

## Step 1: WordPress Page Setup

1. Log into WordPress admin
2. Go to Pages > Add New
3. Set the page title to: `How a Plumbing Plus Member Outranked Reece in Local Search | Jones Plumbing Plus`
4. Set the slug to: `jones-plumbing-plus`
5. Set the parent page to: `case-studies`
6. The full URL must resolve to: `https://reviewly.com.au/case-studies/jones-plumbing-plus/`
7. Set the page template to **Full Width** (or the equivalent in the active theme that removes the sidebar and header/footer padding)
8. Switch the editor to **Code Editor** view (not Visual/Gutenberg)
9. Paste the entire contents of `case-study-jones-plumbing-plus.html` into the code editor
10. Do not publish yet - complete Steps 2 and 3 first

---

## Step 2: SEO Plugin Configuration (Yoast or Rank Math)

### If using Yoast SEO:

**SEO Title:**
```
How a Plumbing Plus Member Outranked Reece in Local Search | Jones Plumbing Plus | Reviewly
```

**Meta Description:**
```
Jones Plumbing Plus, a Plumbing Plus member in Albury-Corowa, outranked Reece with a visibility score of 60 vs 28. 583 GBP calls, $19,200 equivalent ad spend saved in 31 days. A Reviewly case study.
```

**Focus Keyword:** `Plumbing Plus member local search`

**Canonical URL:** `https://reviewly.com.au/case-studies/jones-plumbing-plus/`

**Robots:** Index, Follow (default - do not set to noindex)

**Open Graph Title:** `How a Plumbing Plus Member Outranked Reece in Local Search`

**Open Graph Description:** `Jones Plumbing Plus in Albury-Corowa outranked Reece (visibility 60 vs 28), generated 583 GBP calls, and saved $19,200 in equivalent ad spend in 31 days.`

**Open Graph Image:** Upload a 1200x630px JPEG with dark charcoal background, Reviewly wordmark, and the headline text. File name: `jones-plumbing-plus-og.jpg`

### If using Rank Math:

Apply the same title, description, canonical, and OG settings in the Rank Math meta box below the editor.

---

## Step 3: Schema Validation (Before Publishing)

The HTML file contains four schema blocks. All four must pass validation before the page is published.

**Tool:** https://search.google.com/test/rich-results

**How to validate:**
1. Save the page as a draft (do not publish yet)
2. Use the "URL" option in Rich Results Test if the draft is accessible, OR use the "Code" option and paste the schema blocks individually

**Schema Block 1: Article**
- Type: `Article`
- Expected: Author (Tanya Somerton), Publisher (Reviewly), datePublished, about (LocalBusiness - Jones Plumbing Plus)
- Must show: No errors, no warnings on required fields

**Schema Block 2: BreadcrumbList**
- Type: `BreadcrumbList`
- Expected: Three items - Home > Case Studies > Jones Plumbing Plus
- Must show: Breadcrumb eligible in rich results

**Schema Block 3: Organization**
- Type: `Organization`
- Expected: Reviewly name, URL, logo, sameAs (Wikidata)
- Must show: No errors

**Schema Block 4: FAQPage**
- Type: `FAQPage`
- Expected: Five question/answer pairs
- Must show: FAQ rich result eligible

If any schema block shows errors, do not publish. Fix the error and re-validate before proceeding.

---

## Step 4: Image Verification

All four images in the HTML file are served from the Reviewly CDN (`/manus-storage/` paths). These are pre-built and do not require uploading.

Verify each image loads correctly by previewing the draft page in a browser:

| Image | Alt Text | CDN Path |
|---|---|---|
| Ranking grid (before/after) | Local ranking grid showing position improvement across Albury-Wodonga | `/manus-storage/ranking-grid_64889446.webp` |
| Keyword distribution chart | 90 tracked keywords positions distribution May-June 2026 | `/manus-storage/keyword-distribution_736f8138.png` |
| Savings dashboard | $19,200 savings dashboard May-June 2026 | `/manus-storage/savings-dashboard_236de713.webp` |
| Competitor metrics | Visibility score 60 vs Reece 28 and SP Plus 15 | `/manus-storage/competitor-metrics_95b2320b.png` |

If any image does not load, check that the CDN paths are intact in the HTML. Do not replace with local uploads - use the CDN paths as written.

---

## Step 5: Internal Linking (Critical - Do Not Skip)

The case study page needs inbound internal links from four source pages. Without these links, the page is an orphan and will not receive link equity from the rest of the site.

**Add a link to this page from each of the following:**

### 5a. Case Studies Archive Page (`/case-studies/`)
Add a new card to the archive page grid for Jones Plumbing Plus. The card should include:
- Headline: "How a Plumbing Plus Member Outranked Reece in Local Search"
- Sector tag: PLUMBING SUPPLIES | Albury-Corowa NSW
- Result callout: Visibility Score 60 vs Reece 28
- Badge: Plumbing Plus Member
- Link: `/case-studies/jones-plumbing-plus/`

### 5b. Homepage (`/`)
Add a reference to the Jones Plumbing Plus result in the results or social proof section. Suggested text: "Jones Plumbing Plus, a Plumbing Plus member in Albury-Corowa, achieved a visibility score of 60 against Reece at 28." Link the business name to `/case-studies/jones-plumbing-plus/`.

### 5c. Services or How It Works page
Add a sentence referencing the Jones Plumbing Plus result as an example of the REVIEW Method in action. Link to `/case-studies/jones-plumbing-plus/`.

### 5d. About page or Tanya Somerton author page
Add the Jones Plumbing Plus result to the evidence of outcomes section. Link to `/case-studies/jones-plumbing-plus/`.

---

## Step 6: Publish and Submit to Google Search Console

1. Publish the page
2. Confirm the live URL resolves correctly: `https://reviewly.com.au/case-studies/jones-plumbing-plus/`
3. Open Google Search Console
4. Go to URL Inspection
5. Enter the full URL
6. Click "Request Indexing"
7. Note the date of submission

---

## Step 7: Post-Publication Checklist

Complete within 24 hours of publishing:

**Technical:**
- [ ] Live URL loads correctly in browser
- [ ] Canonical tag in page source matches `https://reviewly.com.au/case-studies/jones-plumbing-plus/`
- [ ] All four images load without broken image icons
- [ ] Breadcrumb displays correctly in page header
- [ ] FAQ accordion opens and closes correctly on click
- [ ] Page renders correctly on mobile (test at 375px width)
- [ ] No console errors in browser developer tools

**SEO:**
- [ ] Rich Results Test passes on live URL for FAQPage and BreadcrumbList
- [ ] GSC URL Inspection shows page is indexed or indexing requested
- [ ] Page appears in site search (`site:reviewly.com.au/case-studies/jones-plumbing-plus/`)
- [ ] Internal links from archive, homepage, services, and about pages are live

**Social:**
- [ ] Share the URL on LinkedIn to generate the first social signal
- [ ] Verify the OG image and title display correctly when the URL is pasted into LinkedIn
- [ ] Share in the Reviewly Facebook page with a short caption referencing the Plumbing Plus member angle

**Notify:**
- [ ] Slack message to Tanya confirming page is live and indexed

---

## Step 8: Strategic Distribution (Tanya to Action)

This case study has a specific distribution opportunity beyond standard SEO. The Plumbing Plus member angle makes it directly relevant to the 320+ independent Plumbing Plus members across Australia.

**Recommended actions:**

1. **Share directly with the Plumbing Plus national office.** Ask if they would be willing to distribute the case study to their member network via their newsletter or member portal. This is a peer-to-peer proof point, not a sales pitch.

2. **LinkedIn post in Tanya's voice.** Publish a post referencing the result with the angle: "An independent Plumbing Plus member in regional NSW outranked Reece in local search. Here is how." Tag Jones Plumbing Plus and Plumbing Plus in the post.

3. **Email to Jones Plumbing Plus.** Send the live URL to the client and ask them to share it with their own network and on their social channels.

4. **Add to the Jones Plumbing Plus PDF.** Update the PDF case study to include the live URL so recipients can visit the full case study online.

---

## Page Positioning Summary

| Element | Value |
|---|---|
| Primary keyword | Plumbing Plus member local search |
| Secondary keywords | independent plumbing supplier SEO, beat Reece local search, plumbing showroom visibility, Albury plumbing supplier |
| Target audience | Plumbing Plus members, independent plumbing suppliers, trade showroom operators |
| Strategic angle | Peer-to-peer proof that an independent member can outrank a national chain |
| Schema stack | Article, BreadcrumbList, Organization, FAQPage |
| Canonical URL | https://reviewly.com.au/case-studies/jones-plumbing-plus/ |
| Word count | Approximately 2,800 words |
| Images | 4 (all CDN-hosted, no upload required) |
| DAN pixel | Present before </body> |

---

## What Marvin Does NOT Need to Do

- Create or upload any images (all four are CDN-hosted and embedded)
- Write any copy (all content is in the HTML file)
- Configure any schema (all four blocks are in the HTML head)
- Design anything (full CSS is in the HTML file)
- Add the DAN tracking pixel (already in the HTML)

---

## Backlog Task: WordPress Custom Post Type

When the case studies section reaches 8+ pages, Marvin should build a WordPress custom post type for case studies. This will allow the archive page to auto-count published case studies, auto-calculate average metrics from custom fields, and create a structured taxonomy for filtering by industry and location. This is a 3-4 hour build. Add to Marvin's backlog with a trigger: "When case studies reach 8 published pages."

---

*SOP prepared by Reviewly CMO. All claims in the HTML file are sourced from Google Search Console, Google Business Profile performance reports, and rank tracking tool screenshots supplied by the client. Do not alter any statistics without written approval from Tanya Somerton.*
