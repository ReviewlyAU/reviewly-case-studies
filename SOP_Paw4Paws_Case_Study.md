# SOP: Publishing the Paw4Paws Dog Grooming Case Study on reviewly.com.au

**Prepared by:** Tanya Somerton, Reviewly  
**For:** Marvin (WordPress Developer)  
**Date:** May 2026  
**Page URL when live:** `https://reviewly.com.au/case-studies/paw4paws-dog-grooming/`

---

## What You Are Publishing

A case study page for Paw4Paws Dog Grooming, a comfort-first dog grooming business in Wodonga, Victoria. This is one of four case studies going live on the Reviewly website. Each case study is being published separately, so this SOP covers only this one page.

The HTML file included in this ZIP is a complete, styled page. You do not need to design anything. Your job is to create the page in WordPress, paste the content in, upload the images, and fill in the SEO fields.

**Time required:** Approximately 45 to 60 minutes.

---

## Files in This ZIP

| File | What It Is |
|---|---|
| `case-study-paw4paws-dog-grooming.html` | The complete page content and layout |
| `paw4paws_chatgpt_evidence.webp` | Evidence screenshot 1 (ChatGPT recommendation) |
| `paw4paws_google_ai_evidence.png` | Evidence screenshot 2 (Google AI Mode recommendation) |
| `SOP_Paw4Paws_Case_Study.md` | This document |

---

## Step 1: Set Up the Custom Post Type (Do This Once Only)

If you have not already created a "Case Studies" Custom Post Type on the Reviewly WordPress site, do this first. If it already exists from a previous case study, skip to Step 2.

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
2. Set the **Title** to: `How Paw4Paws Turned Local Trust Into Search Demand`
3. Set the **Slug** (permalink) to: `paw4paws-dog-grooming`
   - The full URL will be: `reviewly.com.au/case-studies/paw4paws-dog-grooming/`
   - You can edit the slug by clicking on the URL shown below the title field.

---

## Step 3: Paste the HTML Content

1. In the WordPress block editor, click the **three-dot menu** (top right corner of the editor) and select **Code Editor**. Alternatively, add a new block and choose **Custom HTML**.
2. Open the file `case-study-paw4paws-dog-grooming.html` in a text editor (Notepad, TextEdit, VS Code, or any plain text editor).
3. Select all the content between the `<body>` and `</body>` tags (do not include the `<html>`, `<head>`, or `<body>` tags themselves, and do not include the `<style>` block in the `<head>` -- just the visible page content).
4. Paste it into the WordPress Code Editor or Custom HTML block.

> **Note:** If the page already has a Reviewly header and footer from the WordPress theme, you may want to remove the `<nav>` and `<footer>` sections from the pasted HTML to avoid duplication. Ask Tanya if you are unsure.

---

## Step 4: Upload the Images

The HTML file currently references images hosted on a Manus CDN URL. You need to replace these with images hosted on the Reviewly WordPress Media Library.

1. Go to **Media > Add New** and upload both image files:
   - `paw4paws_chatgpt_evidence.webp`
   - `paw4paws_google_ai_evidence.png`
2. After uploading, click on each image to get its **File URL** from the Attachment Details panel on the right.
3. In the HTML content you pasted, find the two `<img>` tags that reference these images. They will look like:
   ```
   src="/manus-storage/paw4paws_chatgpt_evidence_05933ada.webp"
   src="/manus-storage/paw4paws_google_ai_evidence_d14e35fb.png"
   ```
4. Replace each `src` value with the WordPress Media Library URL for the corresponding image.

**Alt text to use for each image:**

| Image File | Alt Text |
|---|---|
| `paw4paws_chatgpt_evidence.webp` | ChatGPT recommending Paw4Paws Dog Grooming as the first result for the query dog groomer in Wodonga, showing the business address and phone number |
| `paw4paws_google_ai_evidence.png` | Google AI Mode listing Paw4Paws Dog Grooming as the first local grooming salon for dog groomers in Wodonga, showing 4.8 stars with 92 reviews and describing the business as highly regarded for stress-free cage-free grooming |

---

## Step 5: Fill in the SEO Fields

Use Yoast SEO or Rank Math (whichever is installed on the site). Fill in these fields exactly as written:

**SEO Title:**
```
How Paw4Paws Turned Local Trust Into Search Demand | Reviewly Case Study
```

**Meta Description:**
```
Paw4Paws Dog Grooming grew Google Search clicks by 138%, doubled its review base from 45 to 92, and became the #1 recommended dog groomer in Wodonga on ChatGPT and Google AI. See how Reviewly built the visibility architecture.
```

**Focus Keyword (Yoast) or Primary Keyword (Rank Math):**
```
dog groomer Wodonga
```

---

## Step 6: Set the Featured Image

Upload the file `paw4paws_google_ai_evidence.png` as the Featured Image for this post. This is the image that will appear when the page is shared on social media or shown in the case studies archive. The Google AI Mode screenshot is the most visually compelling evidence image for this case study.

---

## Step 7: Publish Settings

Before clicking Publish, confirm these settings:

- [ ] Post type is **Case Study** (not Page or Post)
- [ ] Slug is `paw4paws-dog-grooming`
- [ ] Status is **Published** (not Draft)
- [ ] SEO title and meta description are filled in
- [ ] Featured image is set
- [ ] Both evidence images are uploaded and the src URLs in the HTML are updated

---

## Step 8: After Publishing

1. Visit the live URL: `https://reviewly.com.au/case-studies/paw4paws-dog-grooming/`
2. Check that the page loads correctly and both images display.
3. Check that the page appears in the case studies archive at `https://reviewly.com.au/case-studies/`.
4. Send Tanya the live URL to confirm.

---

## Internal Linking (Tanya Will Handle This)

Once the page is live, Tanya will add internal links from the Reviewly homepage and services page pointing to this case study. You do not need to do this.

---

## Questions?

Contact Tanya Somerton at support@reviewly.com.au or via Slack before making any changes that are not covered in this SOP.
