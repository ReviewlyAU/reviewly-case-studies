from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

page = Path(__file__).with_name("trades-and-construction.html")
text = page.read_text(encoding="utf-8")
errors = []
warnings = []

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

if 'rel="canonical" href="https://reviewly.com.au/trades-and-construction/"' not in text:
    errors.append("Self-referencing canonical missing")

for prohibited_text in (
    "compared with 28 for Reece and 15 for SP Plus",
    "/services/trades-construction/",
    "/best-geo-agencies-australia/",
):
    if prohibited_text.lower() in text.lower():
        errors.append(f"Approved change-note prohibition found: {prohibited_text}")

if "<h2>The result in the field</h2>" not in text:
    errors.append("Approved field-result heading missing")

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

soup = BeautifulSoup(text, "html.parser")
if soup.find("nav") or soup.find("footer"):
    errors.append("Hand-coded navigation or footer found")
if not soup.select_one(".page-content-block"):
    errors.append("WordPress content-block wrapper missing")
if not soup.find("h1"):
    errors.append("H1 missing")

visible_faqs = soup.select(".geo-faq q")
faq_schema = next((item for item in json_objects if item.get("@type") == "FAQPage"), None)
if faq_schema and len(faq_schema.get("mainEntity", [])) != len(visible_faqs):
    errors.append(
        f"FAQ schema/body mismatch: {len(faq_schema.get('mainEntity', []))} schema vs {len(visible_faqs)} visible"
    )

# Verify percentage claims in visible copy against the approved evidence register.
for removable in soup.find_all(["style", "script"]):
    removable.decompose()
visible_text = soup.get_text(" ", strip=True)
allowed_percentages = {"66.9%"}
found_percentages = set(re.findall(r"\b\d+(?:\.\d+)?%", visible_text))
unapproved = found_percentages - allowed_percentages
if unapproved:
    errors.append("Unapproved percentage claims found: " + ", ".join(sorted(unapproved)))

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
