# Standard Python Libraries
import os
import json
import requests

# Django Libraries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Scraping Libraries
from bs4 import BeautifulSoup

# LangChain and Google Generative AI Libraries
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import HumanMessage


# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

API_HUGGING = os.getenv('HUGGING_FACE')
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

template = """{question}"""

prompt_template = PromptTemplate(
    template=template,
    input_variables=['question']
)

# Instantiate the Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=API_KEY,
    temperature=0
)

# Scrape content from a web page
url = 'https://lunamar.co/blogs/news/tendencias-en-accesorios-2024?srsltid=AfmBOoom1AHGRDfcJy2ZQeaePPqNpG87yGEwyw-cBNIFVfqyNF2G038k' 
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract text (this may vary depending on the page structure)
raw_text = ""
for paragraph in soup.find_all('p'):  # Extract all the text from the paragraphs
    raw_text += paragraph.get_text()

# Split text into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
texts = text_splitter.split_text(raw_text)

# Create FAISS vector store
docsearch = FAISS.from_texts(texts, embeddings)

# Load QA chain with model
chain = load_qa_chain(llm, chain_type="stuff")

# Function to format the output
def parse_response(response):
    return response.strip()


@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        try:
            # Get the question from the request
            data = json.loads(request.body)
            question = data.get('question', '')

            if not question:
                return JsonResponse({'answer': 'Please provide a question.'}, status=400)

            # Search for relevant documents in FAISS
            docs = docsearch.similarity_search(question)

            if not docs:
                return JsonResponse({'answer': 'No relevant documents found.'}, status=404)

            # Query the Google Generative AI model
            result = chain.run(input_documents=docs, question=question)

            # Return the processed answer
            parsed_response = parse_response(result)
            return JsonResponse({'answer': parsed_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
