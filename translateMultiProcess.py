from concurrent.futures import ThreadPoolExecutor
import json
from googletrans import Translator
from timeit import default_timer as timer

def translateData(i):
    fileCounter = str(i)
    fileName = "output_" + fileCounter + ".json"
    translator = Translator()
    with open(fileName, "r+", encoding='utf-8') as json_file:
        lines = json_file.readlines()
        for i in range(len(lines)):
            data = json.loads(lines[i])
            translated_captions = []
            for caption in data['captions']:
                translated_captions.append(translator.translate(caption, src='EN', dest='HU').text)
            data['captions'] = translated_captions
            lines[i] = json.dumps(data, ensure_ascii=False) + '\n'
            json_file.seek(0)
            json_file.writelines(lines)
            json_file.truncate()

    print('#' + fileName)
    print("")


start = timer()
with ThreadPoolExecutor(max_workers=90) as medence:
    for i in range(60000, 74783):
        medence.submit(translateData, i)

print("CPU:", timer() - start)
