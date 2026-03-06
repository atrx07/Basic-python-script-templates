"""
Image to Text OCR
created and published by atrx07 
Usage: python ocr_image.py /path/to/image.jpg
Optional: install pytesseract and tesseract engine for best results.
If pytesseract is not installed, the script prints a helpful message.
Requires (optional): pytesseract, pillow
"""
import sys
try:
    from PIL import Image
    import pytesseract
except Exception as e:
    print("Optional dependency missing. For OCR install: pip install pillow pytesseract and system tesseract engine.")
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ocr_image.py /path/to/image")
    else:
        img = Image.open(sys.argv[1])
        text = pytesseract.image_to_string(img)
        print("---- OCR OUTPUT ----")
        print(text)
