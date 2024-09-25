from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from myapp.chatbot.text_splitter import text_splitter
from myapp.chatbot.config import embeddings

# Load the texts
# loader = TextLoader('myapp/chatbot/doc/processed_data/accesorios_tendencia_procesado.txt')
# documents = loader.load()

# Load the texts
loader = PyPDFLoader('myapp/chatbot/doc/raw_data/Documento-7.pdf')
documents = loader.load()

# Call the function and get the texts
texts = text_splitter(documents)


def initialize_faiss(texts, embeddings):
    """Function to initialize FAISS with the embeddings"""
    # Extract only text content from Document objects
    text_contents = [doc.page_content for doc in texts]
    # Create FAISS vector store from texts and embeddings
    return FAISS.from_texts(text_contents, embeddings)
    #return FAISS.from_texts(texts, embeddings)
