"""
Screenshot Sorter
created and published by atrx07 
Usage: python screenshot_sorter.py /path/to/folder
Moves files with "screenshot" (case-insensitive) in the name into Screenshots/ folder.
"""
import os, sys, shutil

def sort_screenshots(folder):
    dest = os.path.join(folder, "Screenshots")
    os.makedirs(dest, exist_ok=True)
    moved = 0
    for fname in os.listdir(folder):
        if "screenshot" in fname.lower():
            shutil.move(os.path.join(folder, fname), os.path.join(dest, fname))
            moved += 1
    print(f"Moved {moved} screenshots to {dest}")

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("Usage: python screenshot_sorter.py /path/to/folder")
    else:
        sort_screenshots(sys.argv[1])
