from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .qa_admin import agent, HumanMessage
from django.shortcuts import render


def qa_admin(request):
    return render(request, 'qa_admin.html')


@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question', '')

            if not question:
                return JsonResponse({'answer': 'Por favor, ingresa una pregunta.'}, status=400)

            human_message = HumanMessage(content=question)
            result = agent.invoke([human_message])
            
            # Extraer la respuesta del resultado
            response = result.get('output', 'Lo siento, no pude encontrar la respuesta.')
            return JsonResponse({'answer': response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)