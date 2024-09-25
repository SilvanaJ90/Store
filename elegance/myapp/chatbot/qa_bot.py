import json
from django.http import JsonResponse
from myapp.chatbot.memory import memory
from myapp.chatbot.chain import generate_response_from_llm, docsearch


def parse_response(response):
    """Parsea la respuesta generada."""
    response_lines = response.split("\n")
    formatted_response = ""

    for line in response_lines:
        if line.strip():
            formatted_response += f"<p>{line.strip()}</p>"

    return formatted_response


def ask_question(request):
    """
    Endpoint para preguntas y respuestas (QA)
    """
    if request.method == 'POST':
        try:
            # Get the question from the request
            data = json.loads(request.body)
            question = data.get('question', '')

            if not question:
                return JsonResponse(
                    {'answer': 'Por favor, proporciona una pregunta.'},
                    status=400)

            # Retrieving relevant documents with FAISS
            docs = docsearch.similarity_search(question)

            if not docs:
                return JsonResponse(
                    {'answer': 'No se encontraron documentos relevantes.'},
                    status=404)

            # Load conversation history from memory
            context = memory.load_memory_variables({})["chat_history"]

            # Generate the final response using the custom LLM
            llm_response = generate_response_from_llm(question, context, docs)

            # Parse and format the LLM response
            parsed_response = parse_response(llm_response)

            # Save updated history to memory
            memory.save_context(
                {"human_input": question}, {"AI_response": parsed_response})

            # Return the processed response
            return JsonResponse({'answer': parsed_response})

        except Exception as e:
            # Error handling
            return JsonResponse(
                {'error': f"Ha ocurrido un error: {str(e)}"}, status=500)