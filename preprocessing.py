import nltk
from nltk.tokenize import sent_tokenize
from PyPDF2 import PdfReader

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    text = '\n'.join(paragraphs)
    return text

def chunk_text(text, chunk_size=5):
    sentences = sent_tokenize(text)
    return [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]
