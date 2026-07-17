from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

page = Path(__file__).with_name("trades-and-construction.html")
text = page.read_text(encoding="utf-8")
errors = []
warnings = []

final_url = "https://reviewly.com.au/who-reviewly-is-for/trades-and-construction/"
required_links = {
    "/who-reviewly-is-for/",
    "/who-reviewly-is-for/trade-suppliers/",
    "/who-reviewly-is-for/multi-location/",
}

if "—" in text:
    errors.append("Em dash found")
if re.search(r"\[[^\]]*(drop|insert|placeholder|link)[^\]]*\]", text, re.I):
    errors.append("Unresolved placeholder found")

for retired in ("#2C75E4", "#22d3ee", "#0e7490"):
    if retired.lower() in text.lower():
        errors.append(f"Retired or template colour found: {retired}")

red_patterns = {
    "SaaS": r"\bSaaS\b",
    "review software": r"\breview software\b",
    "review platform": r"\breview platform\b",
    "SEO agency": r"\bSEO agenc(?:y|ies)\b",
    "guaranteed leads": r"\bguaranteed leads\b",
    "free trial": r"\bfree trial\b",
}
for label, pattern in red_patterns.items():
    if re.search(pattern, text, re.I):
        errors.append(f"Red List language found: {label}")

# Metadata in the implementation comment.
title_match = re.search(r"<title>(.*?)</title>", text, re.S)
desc_match = re.search(r'<meta name="description" content="(.*?)">', text, re.S)
if not title_match:
    errors.append("Title tag missing from implementation notes")
else:
    title = title_match.group(1).strip()
    if len(title) > 60:
        errors.append(f"Title exceeds 60 characters: {len(title)}")
if not desc_match:
    errors.append("Meta description missing from implementation notes")
else:
    description = desc_match.group(1).strip()
    if len(description) > 160:
        errors.append(f"Meta description exceeds 160 characters: {len(description)}")

if f'rel="canonical" href="{final_url}"' not in text:
    errors.append("Final nested self-referencing canonical missing")

prohibited_texts = (
    "Jones Plumbing Plus",
    "Reece",
    "SP Plus",
    "Visibility Score",
    "66.9%",
    "25.5",
    "18.1",
    "/trades-and-construction/",
    "/services/trades-construction/",
    "/best-geo-agencies-australia/",
)
for prohibited_text in prohibited_texts:
    # Allow the final URL, which contains the old slug as its final path segment.
    searchable = text.replace(final_url, "") if prohibited_text == "/trades-and-construction/" else text
    if prohibited_text.lower() in searchable.lower():
        errors.append(f"V2 prohibition found: {prohibited_text}")

if "<h2>How we'd approach a multi-site trades business</h2>" not in text:
    errors.append("Approved multi-site approach heading missing")

for link in required_links:
    if f'href="{link}"' not in text:
        errors.append(f"Required hub-and-spoke link missing: {link}")

# Validate commented JSON-LD blocks.
script_payloads = re.findall(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', text, re.S)
if len(script_payloads) < 2:
    errors.append("Expected Article and FAQPage JSON-LD blocks")
json_objects = []
for index, payload in enumerate(script_payloads, start=1):
    try:
        json_objects.append(json.loads(payload))
    except json.JSONDecodeError as exc:
        errors.append(f"JSON-LD block {index} invalid: {exc}")

schema_types = {item.get("@type") for item in json_objects}
for required in ("Article", "FAQPage"):
    if required not in schema_types:
        errors.append(f"Required schema missing: {required}")

article_schema = next((item for item in json_objects if item.get("@type") == "Article"), None)
if article_schema:
    schema_page_url = article_schema.get("mainEntityOfPage", {}).get("@id")
    if schema_page_url != final_url:
        errors.append(f"Article mainEntityOfPage mismatch: {schema_page_url}")

soup = BeautifulSoup(text, "html.parser")
if soup.find("nav") or soup.find("footer"):
    errors.append("Hand-coded navigation or footer found")
if not soup.select_one(".page-content-block"):
    errors.append("WordPress content-block wrapper missing")
if not soup.find("h1"):
    errors.append("H1 missing")

visible_faqs = [q.get_text(" ", strip=True) for q in soup.select(".geo-faq q")]
faq_schema = next((item for item in json_objects if item.get("@type") == "FAQPage"), None)
schema_faqs = [item.get("name", "").strip() for item in faq_schema.get("mainEntity", [])] if faq_schema else []
if visible_faqs != schema_faqs:
    errors.append(f"FAQ schema/body mismatch: visible={visible_faqs}; schema={schema_faqs}")
if len(visible_faqs) != 4:
    errors.append(f"Expected 4 visible FAQs, found {len(visible_faqs)}")

# No client result percentages may appear in visible copy.
for removable in soup.find_all(["style", "script"]):
    removable.decompose()
visible_text = soup.get_text(" ", strip=True)
found_percentages = set(re.findall(r"\b\d+(?:\.\d+)?%", visible_text))
if found_percentages:
    errors.append("Client or research percentage claims found: " + ", ".join(sorted(found_percentages)))

print(f"File: {page}")
print(f"Title length: {len(title_match.group(1).strip()) if title_match else 'missing'}")
print(f"Meta description length: {len(desc_match.group(1).strip()) if desc_match else 'missing'}")
print(f"Visible FAQs: {len(visible_faqs)}")
print(f"Schema types: {', '.join(sorted(str(t) for t in schema_types))}")
print(f"Percentages found: {', '.join(sorted(found_percentages)) or 'none'}")
if warnings:
    print("Warnings:")
    for warning in warnings:
        print(f"- {warning}")
if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print("PASS")
