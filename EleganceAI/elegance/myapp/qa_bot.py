# Standard Python Libraries
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import custom modules
from .scraper import scrape_webpage
from .text_splitter import split_text_into_chunks

# LangChain and Google Generative AI Libraries
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

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

# Define the URL
url = 'https://lunamar.co/blogs/news/tendencias-en-accesorios-2024?srsltid=AfmBOoom1AHGRDfcJy2ZQeaePPqNpG87yGEwyw-cBNIFVfqyNF2G038k'

# Use the scrape_webpage function from the scraper module
raw_text = scrape_webpage(url)

# Use the split_text_into_chunks function from the text_splitter module
texts = split_text_into_chunks(raw_text)

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
