from langchain_community.vectorstores import FAISS

def initialize_faiss(texts, embeddings):
    # Create FAISS vector store
    return FAISS.from_texts(texts, embeddings)
