import os
import json
from jinja2 import Environment, FileSystemLoader

TEMPLATE_FILE = "syllabus.jinja2.html"

# mapping nhiều folder
FOLDER_MAPPINGS = [
    ("json_Champion", "Champion"),
    ("json_Diamond", "Diamond"),
    ("json_Gladiator", "Gladiator"),
    ("json_Gold", "Gold"),
    ("json_Knight", "Knight"),
    ("json_Platinum", "Platinum"),
    ("json_Scout", "Scout"),
    ("json_Silver", "Silver"),
]

# Setup Jinja2 (chỉ init 1 lần)
env = Environment(loader=FileSystemLoader("."))
template = env.get_template(TEMPLATE_FILE)


def process_folder(json_dir, output_dir):
    print(f"\n📂 Processing folder: {json_dir} -> {output_dir}")

    # tạo folder output nếu chưa có
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(json_dir):
        if not file_name.endswith(".json"):
            continue

        json_path = os.path.join(json_dir, file_name)
        print(f"🔄 Processing {json_path} ...")

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # nếu JSON là list thì lấy phần tử đầu
                if isinstance(data, list):
                    data = data[0]

            html_output = template.render(**data)

            output_name = os.path.splitext(file_name)[0] + ".html"
            output_path = os.path.join(output_dir, output_name)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_output)

            print(f"✅ Done -> {output_path}")

        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")


# chạy cho tất cả folder mapping
for json_dir, output_dir in FOLDER_MAPPINGS:
    process_folder(json_dir, output_dir)

print("\n🎉 All folders processed successfully!")