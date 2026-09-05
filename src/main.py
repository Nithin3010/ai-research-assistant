from pdf_processor import extract_text_from_pdf


def main():
    pdf_path = "data/papers/sample.pdf"

    pages = extract_text_from_pdf(pdf_path)

    for page in pages:
        print(f"\n--- Page {page['page']} ---")
        print(page["text"])


if __name__ == "__main__":
    main()