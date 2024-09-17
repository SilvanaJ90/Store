from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from langchain.schema import HumanMessage
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.chains import ConversationChain
from bs4 import BeautifulSoup
import requests
import google.generativeai as genai
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
import os
from langchain.chains.question_answering import load_qa_chain

# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

API_HUGGING = os.getenv('HUGGING_FACE')
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")




@csrf_exempt
def ask_question(request):
    pass