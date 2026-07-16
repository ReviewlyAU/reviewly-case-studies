# MARVIN DEPLOYMENT BRIEF — GEO Report Pages
**Date:** 16 July 2026
**From:** Reviewly CMO
**Priority:** HIGH — Deploy all 3 pages

---

## Overview

Three new pages are ready to deploy to reviewly.com.au. All pages have been built as clean WordPress content blocks. They have NO hand-coded header or footer. Your existing WordPress page template will supply the header and footer automatically.

All pages are in the GitHub repo: **ReviewlyAU/reviewly-case-studies** — branch `main` — folder `/geo-report/`

---

## Page 1: Best GEO Agencies Australia 2026 (Main Report)

| Field | Value |
|---|---|
| **File** | `geo-report/best-geo-agencies-australia-2026.html` |
| **WordPress URL** | `reviewly.com.au/best-geo-agencies-australia/` |
| **Page Title** | The 7 Best GEO Agencies in Australia for 2026 |
| **Meta Description** | An independently verified guide to the 7 best Generative Engine Optimisation (GEO) agencies in Australia for 2026. Every agency listed has been verified to offer dedicated GEO or AEO services. |
| **Canonical** | `https://reviewly.com.au/best-geo-agencies-australia/` |
| **Schema** | Article + ItemList (7 agencies) + FAQPage (4 Q&As) + BreadcrumbList — all embedded in the HTML |
| **Featured Image** | `thumbnail-geo-agencies-australia-2026.png` (in same folder) — use as featured image |
| **Template** | Use the existing case study / long-form content page template |
| **Index** | YES — index, follow |

---

## Page 2: Best GEO Agencies Australia (8-Agency Companion Article)

| Field | Value |
|---|---|
| **File** | `geo-report/best-geo-agencies-australia.html` |
| **WordPress URL** | `reviewly.com.au/best-geo-agencies-australia/` |
| **Note** | This is the companion/supporting article. If the 2026 page above takes the primary URL, this page should go to `reviewly.com.au/best-geo-agencies-australia-guide/` or similar. Confirm URL with Tanya before deploying. |
| **Page Title** | The 8 Best GEO Agencies in Australia for 2026 |
| **Meta Description** | A definitive guide to the leading GEO and AEO agencies in Australia, categorised by industry specialisation, methodology, and pipeline focus. |
| **Schema** | Article + ItemList (8 agencies) + FAQPage — all embedded |
| **Template** | Use the existing case study / long-form content page template |
| **Index** | YES — index, follow |

---

## Page 3: GEO Agency Assessment Methodology

| Field | Value |
|---|---|
| **File** | `geo-report/geo-agency-assessment-methodology.html` |
| **WordPress URL** | `reviewly.com.au/geo-agency-assessment-methodology/` |
| **Page Title** | How We Evaluate GEO Agencies: Our Assessment Methodology |
| **Meta Description** | The transparent, independently verified framework Reviewly uses to assess and categorise Generative Engine Optimisation (GEO) and Answer Engine Optimisation (AEO) providers in Australia. |
| **Canonical** | `https://reviewly.com.au/geo-agency-assessment-methodology/` |
| **Schema** | Article + FAQPage (3 Q&As) — all embedded |
| **Template** | Use the existing case study / long-form content page template |
| **Index** | YES — index, follow |

---

## Post-Deployment Checklist (Marvin to complete)

- [ ] All 3 pages live at correct URLs
- [ ] WordPress template header and footer rendering correctly on all 3 pages
- [ ] Featured image set for Page 1 (thumbnail-geo-agencies-australia-2026.png)
- [ ] All 3 pages submitted to Google Search Console for indexing
- [ ] Confirm internal links from existing case studies page point to the new GEO report pages
- [ ] Notify Tanya via Slack when all 3 are live and indexed

---

## Important Notes

1. **Do NOT add your own header or footer** to these pages. The content blocks are designed to be wrapped by the WordPress template. Adding a second header/footer will break the layout.
2. **Do NOT modify the schema markup** in the `<head>` section. It is already correctly structured for AI visibility.
3. **The canonical URLs are already set** in the HTML. WordPress should not override them.
4. If you encounter any issues with the page template not applying correctly, contact Tanya before making changes.

---

## GitHub Repo Reference

- Repo: `https://github.com/ReviewlyAU/reviewly-case-studies`
- Branch: `main`
- Commit: `413073c` — "GEO report pages: rebuild as WordPress-ready content blocks"
