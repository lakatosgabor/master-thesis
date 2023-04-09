import os
import json

json_file_path = "coco_dataset/train_dataset.json"
test_folder_path = "coco_dataset/train2014"

with open(json_file_path, "r") as f:
    data = f.readlines()

for i, line in enumerate(data):
    try:
        item = json.loads(line)
        image_path = item.get("image_path")
        if image_path:
            full_path = os.path.join(test_folder_path, image_path)
            if not os.path.exists(full_path):
                print(f"Image path {image_path} not found in test folder. Removing item from JSON.")
                data.pop(i)
    except json.decoder.JSONDecodeError:
        print(f"Line {i + 1} is not a valid JSON object. Removing from JSON.")
        data.pop(i)

# Rewrite the JSON file with the updated data
with open(json_file_path, "w") as f:
    f.writelines(data)
