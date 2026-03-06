"""
Auto File Renamer
created and published by atrx07 
Usage: python auto_renamer.py /path/to/folder prefix
Example: python auto_renamer.py ./downloads file_
"""
import os, sys

def auto_rename(folder, prefix="file_"):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder,f))]
    files.sort()
    for i, fname in enumerate(files, start=1):
        ext = os.path.splitext(fname)[1]
        new = f"{prefix}{i}{ext}"
        os.rename(os.path.join(folder, fname), os.path.join(folder, new))
    print(f"Renamed {len(files)} files in {folder}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python auto_renamer.py /path/to/folder [prefix]")
    else:
        folder = sys.argv[1]
        prefix = sys.argv[2] if len(sys.argv) > 2 else "file_"
        auto_rename(folder, prefix)
