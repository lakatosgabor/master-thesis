import json

input_file = '../../coco_dataset/train_dataset.json'
output_file_prefix = 'output_'
output_file_suffix = '.json'

with open(input_file, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        # elkészítjük az új JSON objektumot a sorból
        json_obj = json.loads(line)
        # készítünk egy új fájlnevet a sorszám alapján
        output_file_name = output_file_prefix + str(i) + output_file_suffix
        # írjuk ki a JSON objektumot az új fájlba
        with open(output_file_name, 'w', encoding='utf-8') as out_file:
            json.dump(json_obj, out_file, ensure_ascii=False)
