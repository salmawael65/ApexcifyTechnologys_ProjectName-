
# Task 3 - Internship Project (ApexcifyTechnologys)

import os
import shutil

print("   Welcome to Smart File Organizer by Salma 🌸✨\n")

#  User should write the path

folder = input(" Write the path of the folder you want to organize 📂: ").strip()

mode = input("Do you want to copy or move files? [m/c]: ").lower()

# Makan El folder El geded

organized = os.path.join(folder, "Important Files")
os.makedirs(organized, exist_ok=True)

file_groups = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Excel": [".xlsx", ".xls"],
    "Videos": [".mp4", ".avi", ".mov"]
}

# Ne5azen num of files Elly etnaalet

counter = 0

# Yebda2 ta5zeen

for item in os.listdir(folder):
    path = os.path.join(folder, item)

    if os.path.isfile(path):
        moved = False
        for group, exts in file_groups.items():
            if item.lower().endswith(tuple(exts)):
                target = os.path.join(organized, group)
                os.makedirs(target, exist_ok=True)

                new_path = os.path.join(target, item)
                if mode == "c":
                    shutil.copy2(path, new_path)
                    action = "Copied"
                else:
                    shutil.move(path, new_path)
                    action = "Moved"

                print(f"✔ {item} → {group} ({action})")
                counter += 1
                moved = True
                break

        if not moved:
            other = os.path.join(organized, "Others")
            os.makedirs(other, exist_ok=True)
            new_path = os.path.join(other, item)

            if mode == "c":
                shutil.copy2(path, new_path)
                action = "Copied"
            else:
                shutil.move(path, new_path)
                action = "Moved"

            print(f"📂 {item} → Others ({action})")
            counter += 1

print(f"\n Done! {counter} files have been organized successfully. 🎉")
