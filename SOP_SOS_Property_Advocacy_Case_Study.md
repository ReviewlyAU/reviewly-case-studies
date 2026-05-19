# SOP: Publishing the SOS Property Advocacy Case Study on reviewly.com.au

**Prepared by:** Tanya Somerton, Reviewly  
**For:** Marvin (WordPress Developer)  
**Date:** May 2026  
**Page URL when live:** `https://reviewly.com.au/case-studies/sos-property-advocacy/`

---

## What You Are Publishing

A case study page for SOS Property Advocacy, a Melbourne-based property buyers agency. This is one of four case studies going live on the Reviewly website. Each case study is being published separately, so this SOP covers only this one page.

The HTML file included in this ZIP is a complete, styled page. You do not need to design anything. Your job is to create the page in WordPress, paste the content in, upload the images, and fill in the SEO fields.

**Time required:** Approximately 45 to 60 minutes.

---

## Files in This ZIP

| File | What It Is |
|---|---|
| `case-study-sos-property-advocacy.html` | The complete page content and layout |
| `sos_ranking_ai_overview.png` | Evidence screenshot 1 (AI ranking overview) |
| `sos_gsc_performance.png` | Evidence screenshot 2 (Google Search Console data) |
| `SOP_SOS_Property_Advocacy_Case_Study.md` | This document |

---

## Step 1: Set Up the Custom Post Type (Do This Once Only)

If you have not already created a "Case Studies" Custom Post Type on the Reviewly WordPress site, do this first. If it already exists, skip to Step 2.

1. Install the plugin **Custom Post Type UI** (free on WordPress.org) if it is not already installed.
2. Go to **CPT UI > Add/Edit Post Types**.
3. Create a new post type with these settings:
   - **Post Type Slug:** `case-studies`
   - **Plural Label:** Case Studies
   - **Singular Label:** Case Study
   - **Has Archive:** Yes
   - **Rewrite Slug:** `case-studies`
4. Save the post type.
5. Go to **Settings > Permalinks** and click Save Changes (this flushes the rewrite rules so the new URLs work).

The archive page will now live at `reviewly.com.au/case-studies/`.

---

## Step 2: Create the Page

1. In the WordPress admin, go to **Case Studies > Add New**.
2. Set the **Title** to: `How SOS Property Advocacy Ranked #1 in 5 Days`
3. Set the **Slug** (permalink) to: `sos-property-advocacy`
   - The full URL will be: `reviewly.com.au/case-studies/sos-property-advocacy/`
   - You can edit the slug by clicking on the URL shown below the title field.

---

## Step 3: Paste the HTML Content

1. In the WordPress block editor, click the **three-dot menu** (top right corner of the editor) and select **Code Editor**. Alternatively, add a new block and choose **Custom HTML**.
2. Open the file `case-study-sos-property-advocacy.html` in a text editor (Notepad, TextEdit, VS Code, or any plain text editor).
3. Select all the content between the `<body>` and `</body>` tags (do not include the `<html>`, `<head>`, or `<body>` tags themselves, and do not include the `<style>` block in the `<head>` — just the visible page content).
4. Paste it into the WordPress Code Editor or Custom HTML block.

> **Note:** If the page already has a Reviewly header and footer from the WordPress theme, you may want to remove the `<nav>` and `<footer>` sections from the pasted HTML to avoid duplication. Ask Tanya if you are unsure.

---

## Step 4: Upload the Images

The HTML file currently references images hosted on a temporary Manus URL. You need to replace these with images hosted on the Reviewly WordPress Media Library.

1. Go to **Media > Add New** and upload both image files:
   - `sos_ranking_ai_overview.png`
   - `sos_gsc_performance.png`
2. After uploading, click on each image to get its **File URL** from the Attachment Details panel on the right.
3. In the HTML content you pasted, find the two `<img>` tags that reference these images. They will look like:
   ```
   src="https://sosstudy-rw7yvx7d.manus.space/manus-storage/sos_ranking_ai_overview..."
   src="https://sosstudy-rw7yvx7d.manus.space/manus-storage/sos_gsc_performance..."
   ```
4. Replace each `src` value with the WordPress Media Library URL for the corresponding image.

**Alt text to use for each image:**

| Image File | Alt Text |
|---|---|
| `sos_ranking_ai_overview.png` | SOS Property Advocacy ranking in Google AI Overview for property buyers agent Melbourne search query, showing Reviewly visibility architecture results |
| `sos_gsc_performance.png` | Google Search Console performance data for SOS Property Advocacy showing click and impression growth after Reviewly REVIEW Method implementation |

---

## Step 5: Fill in the SEO Fields

Use Yoast SEO or Rank Math (whichever is installed on the site). Fill in these fields exactly as written:

**SEO Title:**
```
How SOS Property Advocacy Ranked #1 in 5 Days | Reviewly Case Study
```

**Meta Description:**
```
SOS Property Advocacy went from invisible to #1 in Google AI Overview within 5 days of launching. See how Reviewly's visibility architecture built trust signals that Google and AI systems could read.
```

**Focus Keyword (Yoast) or Primary Keyword (Rank Math):**
```
property buyers agent Melbourne
```

---

## Step 6: Set the Featured Image

Upload the file `sos_ranking_ai_overview.png` as the Featured Image for this post. This is the image that will appear when the page is shared on social media or shown in the case studies archive.

---

## Step 7: Publish Settings

Before clicking Publish, confirm these settings:

- [ ] Post type is **Case Study** (not Page or Post)
- [ ] Slug is `sos-property-advocacy`
- [ ] Status is **Published** (not Draft)
- [ ] SEO title and meta description are filled in
- [ ] Featured image is set
- [ ] Both evidence images are uploaded and the src URLs in the HTML are updated

---

## Step 8: After Publishing

1. Visit the live URL: `https://reviewly.com.au/case-studies/sos-property-advocacy/`
2. Check that the page loads correctly and both images display.
3. Check that the page appears in the case studies archive at `https://reviewly.com.au/case-studies/`.
4. Send Tanya the live URL to confirm.

---

## Internal Linking (Tanya Will Handle This)

Once the page is live, Tanya will add internal links from the Reviewly homepage and services page pointing to this case study. You do not need to do this.

---

## Questions?

Contact Tanya Somerton at support@reviewly.com.au or via Slack before making any changes that are not covered in this SOP.
