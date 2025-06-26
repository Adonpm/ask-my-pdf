from backend.app.services.pdf_utils import extract_data_from_pdf
from backend.app.core.chunker import chunk_documents_semantic, chunk_documents_recursive

def rag_pipeline(file_path:str, use_semantic:bool = False):
    print("[STEP 1] Extracting document pages...")
    docs = extract_data_from_pdf(file_path)
    print(f"[INFO] Total pages extracted: {len(docs)}")

    print(f"[STEP 2] {'Semantic' if use_semantic else 'Recursive'} chunking...")
    if use_semantic:
        chunks = chunk_documents_semantic(docs)
    else:
        chunks = chunk_documents_recursive(docs)

    print(f"[INFO] Total chunks created: {len(chunks)}")
    print(f"[PREVIEW] First chunk:\n{chunks[0].page_content[:300]}...\n")

    return chunks

if __name__ == "__main__":
    rag_pipeline(r"D:\PERSONAL\Agentic-AI-Masterclass\2. Langchain Basics\data\llama2.pdf", use_semantic=False)