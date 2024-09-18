import os
import google.generativeai as genai
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

# Configure Hugging Face Embeddings
API_HUGGING = os.getenv('HUGGING_FACE')
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Instantiate the Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=API_KEY,
    temperature=0
)
