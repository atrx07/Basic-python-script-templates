"""
PDF Merger
created and published by atrx07 
Usage: python pdf_merger.py /path/to/output.pdf input1.pdf input2.pdf ...
Requires: PyPDF2 (pip install PyPDF2)
"""
import sys
from PyPDF2 import PdfMerger

def merge(output, inputs):
    merger = PdfMerger()
    for pdf in inputs:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"Merged {len(inputs)} PDFs into {output}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python pdf_merger.py output.pdf input1.pdf input2.pdf ...")
    else:
        merge(sys.argv[1], sys.argv[2:])
