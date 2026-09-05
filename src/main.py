from pdf_processor import extract_text_from_pdf
from chunker import create_chunks
from embedding_model import generate_embeddings

def main():
    pdf_path = "data/papers/sample.pdf"

    pages = extract_text_from_pdf(pdf_path)

    chunks = create_chunks(pages)

    embeddings = generate_embeddings(chunks)

    print(f"Number of chunks: {len(chunks)}")
    print(f"Embedding shape: {embeddings.shape}")

    print("\nFirst embedding:")
    print(embeddings[0])


if __name__ == "__main__":
    main()