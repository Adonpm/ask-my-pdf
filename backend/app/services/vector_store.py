from langchain_huggingface import HuggingFaceEmbeddings
from langchain_milvus import Milvus
from langchain_core.documents import Document
from typing import List
import os
from dotenv import load_dotenv
from pymilvus import utility

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["MILVUS_API_KEY"] = os.getenv("MILVUS_API_KEY")

# Vector embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def get_vector_store(index_type:str='FLAT', metric_type:str='L2', collection_name='ask_my_pdf_collection'):
    '''
    Setting up vector store using Milvus.
    '''
    URI = os.getenv("MILVUS_URI")
    TOKEN = os.getenv("MILVUS_TOKEN")

    if not URI or not TOKEN:
        raise ValueError("Missing MILVUS_URI or MILVUS_TOKEN in environment variables")

    vector_store = Milvus(
        embedding_function=embeddings,
        connection_args={"uri": URI, "token": TOKEN, "secure": True},
        collection_name=collection_name,
        index_params={"index_type": index_type, "metric_type": metric_type}
    )
    return vector_store

def clean_metadata_keys(metadata: dict) -> dict:
    return {
        key.replace(".", "_").replace("-", "_"): value
        for key, value in metadata.items()
    }

def add_documents(vector_store:Milvus, docs:List[Document]):
    '''
    Inserting chunks to the vector store.
    '''
    # Sanitize metadata
    cleaned_docs = [
        Document(page_content=doc.page_content, metadata=clean_metadata_keys(doc.metadata))
        for doc in docs
    ]

    vector_store.add_documents(cleaned_docs)
    print(f"[INFO] Inserted {len(docs)} docs into {vector_store}")

def get_retriever(vector_store:Milvus, k:int=3):
    '''
    Setting up retriever
    '''
    print(f"[INFO] Retrieving is going on...")
    return vector_store.as_retriever(search_kwargs={"k": k})
    