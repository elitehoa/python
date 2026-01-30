import os
import json
import re
from docx import Document

INPUT_DIR = "LP Primary 1"
OUTPUT_DIR = "output_json"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== CONTROL CHAR CLEANER =====
CONTROL_CHARS = re.compile(
    r"[\x00-\x08\x0B\x0C\x0E-\x1F]"
)

def clean_control_chars(text: str) -> str:
    return CONTROL_CHARS.sub("", text)

total_files = 0
success_files = 0
empty_files = 0
json_error_files = 0

for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".docx"):
        continue

    total_files += 1
    doc_path = os.path.join(INPUT_DIR, filename)
    doc = Document(doc_path)

    # ===== GOM TOÀN BỘ TEXT TRONG DOCX =====
    raw_text = "\n".join(
        p.text for p in doc.paragraphs if p.text.strip()
    ).strip()

    if not raw_text:
        empty_files += 1
        print(f"⚠️ EMPTY: {filename}")
        continue

    # ===== CLEAN CONTROL CHARS =====
    cleaned_text = clean_control_chars(raw_text)

    # ===== PARSE JSON =====
    try:
        data = json.loads(cleaned_text)
    except json.JSONDecodeError as e:
        json_error_files += 1
        print(f"❌ JSON ERROR: {filename}")
        print(f"    ↳ {e}")
        continue

    # ===== GHI RA FILE JSON =====
    out_name = filename.replace(".docx", ".json")
    out_path = os.path.join(OUTPUT_DIR, out_name)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    success_files += 1
    print(f"✅ OK: {out_name}")

# ===== SUMMARY =====
print("\n========== SUMMARY ==========")
print(f"📂 Total .docx files : {total_files}")
print(f"✅ Converted         : {success_files}")
print(f"⚠️ Empty             : {empty_files}")
print(f"❌ JSON error        : {json_error_files}")
print("🎉 DONE")
