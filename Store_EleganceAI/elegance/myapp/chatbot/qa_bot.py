import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from myapp.chatbot.config import embeddings
from myapp.chatbot.vector_db import initialize_faiss, texts
from myapp.chatbot.memory import memory, chat_llm_chain

# initialize faiss vectordb
docsearch = initialize_faiss(texts, embeddings)


def parse_response(response):
    """ parse the responses """
    response_lines = response.split("\n")
    formatted_response = ""

    for line in response_lines:
        if line.strip():
            formatted_response += f"<p>{line.strip()}</p>"

    return formatted_response


@csrf_exempt
def ask_question(request):
    """
    Questions and Answers
    """
    if request.method == 'POST':
        try:
            # Get the question from the request
            data = json.loads(request.body)
            question = data.get('question', '')

            if not question:
                return JsonResponse(
                    {'answer': 'Por favor,proporciona una pregunta.'},
                    status=400)

            # Search relevant documents in FAISS based on the question
            docs = docsearch.similarity_search(question)

            if not docs:
                return JsonResponse(
                    {'answer': 'No se encontraron documentos relevantes.'},
                    status=404)

            # Get context from conversation history
            context = memory.load_memory_variables({})["chat_history"]

            # Run the LLM chain to get the response
            result = chat_llm_chain.run(
                {"human_input": question, "chat_history": context})

            # Process the model response
            parsed_response = parse_response(result)

            # Return the processed response
            return JsonResponse({'answer': parsed_response})

        except Exception as e:
            # Error 500
            return JsonResponse({'error': str(e)}, status=500)
