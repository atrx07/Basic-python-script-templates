"""
Auto Folder Organizer
created and published by atrx07 
Usage: python folder_organizer.py /path/to/folder
Moves files into Images, Videos, Documents, Audio, Others based on extension.
"""
import os, sys, shutil

EXT_MAP = {
    "Images": [".jpg",".jpeg",".png",".gif",".bmp",".webp"],
    "Videos": [".mp4",".mkv",".mov",".avi"],
    "Documents": [".pdf",".docx",".doc",".txt",".xlsx",".pptx"],
    "Audio": [".mp3",".wav",".aac",".ogg"]
}

def organize(folder):
    for fname in os.listdir(folder):
        full = os.path.join(folder, fname)
        if not os.path.isfile(full):
            continue
        ext = os.path.splitext(fname)[1].lower()
        placed = False
        for k, exts in EXT_MAP.items():
            if ext in exts:
                dest = os.path.join(folder, k)
                os.makedirs(dest, exist_ok=True)
                shutil.move(full, os.path.join(dest, fname))
                placed = True
                break
        if not placed:
            dest = os.path.join(folder, "Others")
            os.makedirs(dest, exist_ok=True)
            shutil.move(full, os.path.join(dest, fname))
    print("Organization complete. Check subfolders.")
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python folder_organizer.py /path/to/folder")
    else:
        organize(sys.argv[1])
