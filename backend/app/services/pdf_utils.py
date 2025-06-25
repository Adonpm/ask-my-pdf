from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyPDFLoader

def extract_data_from_pdf(file_path):
    """
    Tries to extract structured data from a PDF using UnstructuredPDFLoader.
    Falls back to PyPDFLoader if there's a failure (e.g., Poppler/Model issues).
    Returns text which is obtained by joining list of documents.
    """
    try:
        print("[INFO] Trying UnstructuredPDFLoader...")
        loader = UnstructuredPDFLoader(file_path)
        documents = loader.load()
        print("[INFO] Successfully loaded with UnstructuredPDFLoader.")
    except Exception as e:
        print(f"[WARNING] UnstructuredPDFLoader failed: {e}")
        loader = PyPDFLoader(file_path)
        documents=loader.load()
        print("[INFO] Successfully loaded with PyPDFLoader.")
    
    full_text = "\n\n".join(doc.page_content for doc in documents)
    return full_text
