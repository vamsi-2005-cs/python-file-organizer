import os
import shutil

folder = input("Enter folder path to organize: ")

file_types = {

    "Images": [
        ".jpg", ".jpeg", ".png",
        ".gif", ".bmp", ".webp"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov", ".flv"
    ],

    "Documents": [
        ".pdf", ".docx", ".doc",
        ".txt", ".pptx", ".xlsx"
    ],

    "Music": [
        ".mp3", ".wav", ".aac"
    ],

    "Archives": [
        ".zip", ".rar", ".tar",
        ".gz"
    ]
}

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isdir(path):
        continue

    extention = os.path.splitext(file)[1].lower()
    moved = False

    for category, extentions in file_types.items():
        if extention in extentions:
            target = os.path.join(folder, category)
            os.makedirs(target, exist_ok=True)
            shutil.move(path, os.path.join(target, file))
            print(f"{file} -> {category}")
            moved = True
            break

    if not moved:
        others = os.path.join(folder, "Others")
        os.makedirs(others, exist_ok=True)
        shutil.move(path, os.path.join(others, file))
        print(f"{file} -> Others")

print("Done!")