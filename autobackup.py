"""
Auto Backup Script
created and published by atrx07 
Usage: python auto_backup.py /path/to/source /path/to/destination
This mirrors the source folder into destination (overwrite if exists).
"""
import os, sys, shutil

def mirror(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"Backed up {src} to {dst}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python auto_backup.py /path/to/source /path/to/destination")
    else:
        mirror(sys.argv[1], sys.argv[2])
