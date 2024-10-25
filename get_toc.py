from pypdf import PdfReader, PdfWriter
import pdf2image
import os

def create_res():
    if not os.path.exists("./res/"):
        print("Creating ./res/ folder...")
        os.mkdir(os.path.join("./", "res/"))

def to_png(output: str):
    pages = pdf2image.convert_from_path(f"{output}.pdf", 700)
    pages[0].save(f"{output}.png", "PNG")
    os.remove(f"{output}.pdf")

def get_toc(path: str = "./out/q3_theo_inf.pdf"):
    create_res()
    reader = PdfReader(path)
    writer = PdfWriter()
    
    text = ""
    output = "./res/toc"
    for page in reader.pages:
        text = page.extract_text() + "\n"
        text = text.lower()
        if "inhaltsverzeichnis" in text:
            writer.add_page(page)
        
    writer.write(f"{output}.pdf")
    to_png(output)

get_toc()