"""
Downloads Cleaner
created and published by atrx07 
Usage: python downloads_cleaner.py /path/to/folder days_threshold
Moves files older than days_threshold to Trash folder inside the folder.
"""
import os, sys, time, shutil

def clean(folder, days=30):
    cutoff = time.time() - (int(days) * 86400)
    trash = os.path.join(folder, "Trash")
    os.makedirs(trash, exist_ok=True)
    moved = 0
    for fname in os.listdir(folder):
        full = os.path.join(folder, fname)
        if not os.path.isfile(full): continue
        if os.path.getmtime(full) < cutoff:
            shutil.move(full, os.path.join(trash, fname))
            moved += 1
    print(f"Moved {moved} files older than {days} days to {trash}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python downloads_cleaner.py /path/to/folder [days]")
    else:
        folder = sys.argv[1]
        days = sys.argv[2] if len(sys.argv)>2 else 30
        clean(folder, days)
