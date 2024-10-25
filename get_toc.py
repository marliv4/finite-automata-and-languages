from pypdf import PdfReader, PdfWriter
import pdf2image
import os

def create_res():
    if not os.path.exists("./res/"):
        print("Creating ./res/ folder...")
        os.mkdir(os.path.join("./", "res/"))

def get_toc(path: str = "./out/q3_theo_inf.pdf"):
    create_res()
    reader = PdfReader(path)
    writer = PdfWriter()
    
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
        if "Inhaltsverzeichnis" in text:
            writer.add_page(page)
            writer.write("./res/toc.png")
            break

get_toc()