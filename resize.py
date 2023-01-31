from PIL import Image
import os

directory = "myData/0"

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(os.path.join(directory, filename))
        image = image.resize((200, 200))
        image.save(os.path.join(directory, filename))
