from backend.app.services.pdf_utils import extract_data_from_pdf
from backend.app.services.vector_store import get_vector_store, add_documents, get_retriever
from backend.app.core.chunker import chunk_documents_semantic, chunk_documents_recursive
from backend.app.services.rag_chain import rag_chain

async def rag_pipeline(file_path:str, user_input:str, use_semantic:bool = False) -> str:
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

    print(f"[STEP 3] Setting up vector store and retrievel pipeline...")
    vector_store = get_vector_store()
    add_documents(vector_store, chunks)
    retriever = get_retriever(vector_store)

    print(f"[STEP 4] Setting up RAG Chain...")
    chain = rag_chain(retriever)

    print(f"[STEP 5] Querying user input...")
    result = await chain.ainvoke(user_input)
    return result
    