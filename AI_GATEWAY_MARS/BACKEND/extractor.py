import pdfplumber
from docx import Document

def extract_text(file):

    filename = file.filename.lower()

    if filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    if filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join([p.text for p in doc.paragraphs])

    raise Exception("Format non supporté")
