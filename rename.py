import os

# A mappa elérési útja, ahol a fájlok találhatók
folder_path = "MyData/0"

# Az előtag, amit hozzá szeretnénk adni a fájlnevekhez
prefix = "algopirin-"

name = 1
# Az összes fájl lekérdezése a mappából
for filename in os.listdir(folder_path):
    # Az elérési út összeállítása a fájlhoz
    file_path = os.path.join(folder_path, filename)

    # Ha a fájl egy fájl, és nem egy mappa
    if os.path.isfile(file_path):
        # Az új fájlnév összeállítása az előtaggal
        new_file_path = os.path.join(folder_path, prefix + str(name) + '.jpg')

        # A fájl átnevezése
        os.rename(file_path, new_file_path)
    name += 1

print("Az összes fájl sikeresen át lett nevezve!")
