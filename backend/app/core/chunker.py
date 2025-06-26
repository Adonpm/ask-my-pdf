from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

def chunk_documents_recursive(documents: List[Document], chunk_size:int =500, chunk_overlap:int =100) -> List[Document]:
    """
    Chunking using Recursive Character Text Splitter
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def chunk_documents_semantic(documents: List[Document], model_name:str ="hkunlp/instructor-xl") -> List[Document]:
    """
    Chunking using Semantic Chunker
    """
    embeddings=HuggingFaceEmbeddings(model_name=model_name)
    splitter=SemanticChunker(embeddings)
    return splitter.split_documents(documents)
