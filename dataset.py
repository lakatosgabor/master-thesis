import json
import collections

images_dir = "coco_dataset/train2014"
annotation_file = "coco_dataset/annotations/captions_train2014.json"
with open(annotation_file, "r") as f:
    annotations = json.load(f)["annotations"]

image_path_to_caption = collections.defaultdict(list)
for element in annotations:
    caption = f"{element['caption'].lower().rstrip('.')}"
    image_path = images_dir + "/COCO_train2014_" + "%012d.jpg" % (element["image_id"])
    image_path_to_caption[image_path].append(caption)

lines = []
for image_path, captions in image_path_to_caption.items():
    lines.append(json.dumps({"image_path": image_path, "captions": captions}))

train_lines = lines[:-8000]
valid_line = lines[-8000:]
with open("coco_dataset/train_dataset.json", "w") as f:
    f.write("\n".join(train_lines))

with open("coco_dataset/valid_dataset.json", "w") as f:
    f.write("\n".join(valid_line))
