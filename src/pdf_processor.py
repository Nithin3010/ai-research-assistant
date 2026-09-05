import fitz


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        page_data = {
            "page": page_number,
            "text": page.get_text()
        }

        pages.append(page_data)

    document.close()

    return pages