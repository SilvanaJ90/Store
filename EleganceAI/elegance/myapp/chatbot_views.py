from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sqlalchemy import create_engine
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.schema import HumanMessage
from django.conf import settings
import google.generativeai as genai
import os

# Configurar Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

# Función para crear la conexión y el agente
def get_sql_agent():
    # Crear la conexión con la base de datos usando settings.py
    DATABASE_URL = f'postgresql://{settings.DATABASES["default"]["USER"]}:{settings.DATABASES["default"]["PASSWORD"]}@{settings.DATABASES["default"]["HOST"]}/{settings.DATABASES["default"]["NAME"]}'
    
    # Crear el motor de SQLAlchemy
    engine = create_engine(DATABASE_URL)
    
    # Crear la instancia de la base de datos
    db = SQLDatabase(engine)
    
    # Instanciar el LLM de Google Generative AI
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=API_KEY)
    
    # Crear el agente SQL
    return create_sql_agent(llm, db=db, verbose=True)

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        try:
            # Obtener la pregunta desde el request
            data = json.loads(request.body)
            question = data.get('question', '')

            if not question:
                return JsonResponse({'answer': 'Por favor, ingresa una pregunta.'}, status=400)

            # Obtener el agente SQL
            agent = get_sql_agent()

            # Crear el mensaje de usuario
            human_message = HumanMessage(content=question)

            # Invocar el agente con el mensaje
            result = agent.invoke([human_message])

            # Extraer la respuesta del resultado
            response = result.get('output', 'Lo siento, no pude encontrar la respuesta.')
            return JsonResponse({'answer': response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

