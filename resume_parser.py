import PyPDF2

def extract_text_from_pdf(file):
    # file is the Werkzeug FileStorage object from Flask; it supports .stream
    reader = PyPDF2.PdfReader(file.stream)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text
