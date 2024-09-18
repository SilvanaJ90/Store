import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .config import embeddings, llm  # Import configuration
from .scraper import scrape_webpage  # Import the scraping logic
from .text_splitter import split_text_into_chunks  # Import text splitter
from .vector_db import initialize_faiss  # Import FAISS logic
from .qa_chain import load_chain, parse_response  # Import QA chain logic

# Define the URL
url = 'https://lunamar.co/blogs/news/tendencias-en-accesorios-2024?srsltid=AfmBOoom1AHGRDfcJy2ZQeaePPqNpG87yGEwyw-cBNIFVfqyNF2G038k'

# Use the scrape_webpage function from the scraper module
raw_text = scrape_webpage(url)

# Use the split_text_into_chunks function from the text_splitter module
texts = split_text_into_chunks(raw_text)

# Create FAISS vector store
docsearch = initialize_faiss(texts, embeddings)

# Load QA chain with model
chain = load_chain(llm)

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
