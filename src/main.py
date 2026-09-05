from pdf_processor import extract_text_from_pdf
from chunker import create_chunks


def main():
    pdf_path = "data/papers/sample.pdf"

    pages = extract_text_from_pdf(pdf_path)

    chunks = create_chunks(pages)

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:3], start=1):
        print(f"\n--- Chunk {i} ---")
        print(f"Page: {chunk['page']}")
        print(chunk["text"])


if __name__ == "__main__":
    main()