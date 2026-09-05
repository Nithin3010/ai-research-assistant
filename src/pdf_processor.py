import fitz

from text_cleaner import clean_text


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        raw_text = page.get_text()
        cleaned_text = clean_text(raw_text)

        page_data = {
            "page": page_number,
            "text": cleaned_text
        }

        pages.append(page_data)

    document.close()

    return pages