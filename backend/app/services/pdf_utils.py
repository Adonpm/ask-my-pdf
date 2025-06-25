from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List

def extract_data_from_pdf(file_path:str) -> List[Document]:
    """
    Tries to extract structured data from a PDF using UnstructuredPDFLoader.
    Falls back to PyPDFLoader if there's a failure (e.g., Poppler/Model issues).
    Returns a list[Document]
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
        
    return documents
