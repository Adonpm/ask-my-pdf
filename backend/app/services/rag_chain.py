from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain import hub
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_milvus import Milvus
import re

def rag_chain(retriever: Milvus):
    print(f"[INFO] RAG Pipeline is going on...")
    # retriever
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # prompt
    #prompt = hub.pull("rlm/rag-prompt")
    prompt = PromptTemplate(
        template=
        """You are an assistant answering questions only from the provided context.
        If the answer cannot be found in the context, respond with "I don't know".
        Context: {context}
        Question: {question}""",
        input_variables=["context", "question"]
    )

    # llm
    llm = ChatGroq(model="deepseek-r1-distill-llama-70b")

    # output_parser
    output_parser = StrOutputParser()

    # Removing think section
    def remove_think_section(text):
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

    # chain = retriver_pipeline | prompt | llm | output_parser
    rag_chain = (
        {"context": retriever | format_docs, "question":RunnablePassthrough()}
        | prompt
        | llm
        | output_parser 
        | RunnableLambda(remove_think_section)
    )
    return rag_chain
