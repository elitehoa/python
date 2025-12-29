import os
import json

# Thư mục xuất file
output_dir = "json_lesson_plan"
os.makedirs(output_dir, exist_ok=True)

units = range(1, 2)  # U1 → U8
# lessons = ["L1", "L2", "L3", "L4", "L5a", "L5b", "L7"]  # không có L6
lessons = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9"]  # không có L6


for u in units:
    for l in lessons:
        filename = f"KG2_U{u}_{l}_LP.json"
        filepath = os.path.join(output_dir, filename)

        data = {
            "id": filename.replace(".json", ""),
            "title": "",
            "description": ""
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Created: {filename}")

print("🎉 All JSON files generated successfully!")
