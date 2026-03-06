"""
Batch Image Resizer
created and published by atrx07 
Usage: python image_resizer.py /path/to/folder width height
Example: python image_resizer.py ./images 1920 1080
Requires: pillow (pip install pillow)
"""
from PIL import Image
import os, sys

def resize_all(folder, w, h):
    files = [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in (".jpg",".jpeg",".png",".webp",".bmp")]
    out = os.path.join(folder, "resized")
    os.makedirs(out, exist_ok=True)
    for f in files:
        p = os.path.join(folder, f)
        img = Image.open(p)
        img = img.resize((int(w), int(h)))
        img.save(os.path.join(out, f))
    print(f"Resized {len(files)} images and saved to {out}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python image_resizer.py /path/to/folder width height")
    else:
        resize_all(sys.argv[1], sys.argv[2], sys.argv[3])
