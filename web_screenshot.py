"""
Website Screenshot Tool
created and published by atrx07 
Usage: python web_screenshot.py https://example.com output.png
Optional: requires imgkit and wkhtmltoimage if you want full HTML render.
If not installed, the script will fetch simple page title as a fallback.
"""
import sys
try:
    import imgkit
    IMGKIT = True
except:
    IMGKIT = False
import requests
from bs4 import BeautifulSoup

def screenshot(url, out):
    if IMGKIT:
        imgkit.from_url(url, out)
        print(f"Saved screenshot to {out} (using imgkit).")
        return
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string if soup.title else url
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (1200, 600), color=(25,25,40))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("DejaVuSans.ttf", 28)
    except:
        f = ImageFont.load_default()
    d.text((50,50), f"Snapshot: {title}", font=f, fill=(255,255,255))
    img.save(out)
    print(f"Saved fallback image to {out} with page title. To use full screenshots, install imgkit + wkhtmltoimage.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python web_screenshot.py <url> output.png")
    else:
        screenshot(sys.argv[1], sys.argv[2])
