# SOP: Financial Education Firm Case Study — WordPress Implementation
**Prepared by:** Reviewly CMO  
**Date:** May 2026  
**For:** Marvin (Web Developer)  
**Priority:** HIGH — Publish after Paw4Paws is live and indexed

---

## Overview

This SOP covers the installation of the anonymised Financial Education Firm case study on reviewly.com.au. This case study demonstrates Reviewly's ability to defend market leadership against global competitors (Coursera, IG) using Entity-first SEO and the HEAT framework. The client is not named — this is intentional and explained within the page content.

---

## Step 1: Confirm the Case Studies Custom Post Type Is Active

This step only needs to be done once. If you already completed it for the Paw4Paws case study, skip to Step 2.

- Ensure the **Custom Post Type UI** plugin is installed and active
- The CPT must be named `case-studies` with the slug `case-studies`
- The archive URL must be: `reviewly.com.au/case-studies/`
- If already done, confirm the archive is live before proceeding

---

## Step 2: Create a New Case Study Post

1. In the WordPress dashboard, go to **Case Studies > Add New**
2. Set the **post title** to:
   ```
   How Reviewly Defended 83% Share of Voice Against Global Competitors
   ```
3. Set the **post slug** (permalink) to:
   ```
   financial-education-share-of-voice
   ```
   Final URL will be: `reviewly.com.au/case-studies/financial-education-share-of-voice/`

---

## Step 3: Paste the HTML Content

1. In the WordPress block editor, click the **three-dot menu** (top right) and select **Code Editor** (or press `Ctrl+Shift+Alt+M`)
2. Delete any default content in the editor
3. Open the file `case-study-financial-education-firm.html` from the GitHub repository
4. Copy the **entire content between `<body>` and `</body>`** — do not copy the `<head>` section, as WordPress handles that separately
5. Paste it into the WordPress code editor
6. Switch back to **Visual Editor** to confirm the layout looks correct
7. Do not make any edits to the content — it is final and approved

---

## Step 4: Upload the Evidence Image

This case study does not have client-provided screenshots (it is anonymised). The page uses text-based evidence and data tables only. No images need to be uploaded for this case study.

---

## Step 5: Configure SEO Fields (Yoast or Rank Math)

In the Yoast or Rank Math panel at the bottom of the post editor, enter the following:

**SEO Title (under 60 characters):**
```
83% Share of Voice: Financial Education Case Study | Reviewly
```

**Meta Description (under 160 characters):**
```
How Reviewly helped an Australian financial education firm defend 83% Share of Voice against Coursera and IG using Entity-first SEO and the HEAT framework.
```

**Focus Keyword:**
```
financial education SEO case study
```

---

## Step 6: Add the Schema Markup

The HTML file already contains Article and FAQPage schema in the `<head>`. However, WordPress may strip this when pasting body content only. To ensure the schema is present:

1. In Yoast SEO, go to the **Schema** tab and set:
   - Page type: **Article**
   - Article type: **Article**
2. If using Rank Math, enable **Article Schema** in the schema settings for this post

Alternatively, if you have access to a plugin like **Schema Pro** or **WP Schema**, you can paste the full JSON-LD block from the HTML file's `<head>` section directly.

---

## Step 7: Set the Featured Image

Upload a featured image for this post. Recommended: use the Reviewly logo or a branded graphic. This image will be used as the Open Graph image when the URL is shared on LinkedIn or Slack.

- Upload to: **Media Library**
- Set as: **Featured Image** for this post
- Alt text: `Reviewly case study — financial education firm share of voice`

---

## Step 8: Publish and Verify

1. Set the post **status to Published**
2. Confirm the live URL is: `reviewly.com.au/case-studies/financial-education-share-of-voice/`
3. Open the URL in a browser and check:
   - [ ] Page loads correctly with the Reviewly navigation
   - [ ] Hero section shows the headline and stats strip
   - [ ] All data tables render correctly
   - [ ] FAQ section is visible at the bottom
   - [ ] CTA button links to `reviewly.com.au/contact/`
   - [ ] Footer shows ABN and contact details

---

## Step 9: Submit to Google Search Console

**This step is mandatory for indexing.**

1. Go to **Google Search Console** for reviewly.com.au
2. Use the **URL Inspection Tool**
3. Enter: `https://reviewly.com.au/case-studies/financial-education-share-of-voice/`
4. Click **Request Indexing**
5. Screenshot the confirmation and send it to Tanya via Slack to confirm completion

---

## Step 10: Internal Linking

Once the page is live, add an internal link to it from:

1. **The Case Studies archive page** (`reviewly.com.au/case-studies/`) — it should appear automatically if the CPT archive is configured correctly
2. **The Services page** — add a text link in the relevant section: *"See how we defended 83% Share of Voice for an Australian financial education firm [link]"*
3. **The Homepage** — if there is a case studies section or social proof section, add this case study alongside SOS and Paw4Paws

---

## Important Note: Why This Case Study Is Anonymised

This case study does not name the client. This is intentional — the engagement was delivered through a third-party partnership arrangement. The anonymisation is explained within the page content itself (in the FAQ section). Do not add the client name anywhere on the page.

---

## File Reference

| File | Location |
|---|---|
| HTML page | `case-study-financial-education-firm.html` in GitHub repo `ReviewlyAU/reviewly-case-studies` |
| This SOP | `SOP_Financial_Education_Case_Study.md` in same repo |

**GitHub repo:** https://github.com/ReviewlyAU/reviewly-case-studies

---

## Completion Checklist

- [ ] Custom Post Type `case-studies` confirmed active
- [ ] New post created with correct slug `financial-education-share-of-voice`
- [ ] HTML content pasted into Code Editor
- [ ] SEO title and meta description entered in Yoast/Rank Math
- [ ] Featured image uploaded and set
- [ ] Page published and live URL confirmed
- [ ] URL submitted to Google Search Console for indexing
- [ ] Tanya notified via Slack with confirmation screenshot
- [ ] Internal links added from Services page and Homepage

---

*Prepared by Reviewly CMO. All content is final and approved. Do not modify the page copy without written approval from Tanya Somerton.*
