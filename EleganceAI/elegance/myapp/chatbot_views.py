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
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.chains import ConversationChain
import os


# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

# Template for the prompt
SYSTEM_PROMPT = """
Eres una AI llamada EleganceAI, generas consultas a una base
de datos SQL de una tienda de accesorios.
El administrador consulta acerca de productos, cantidad de productos,
stock en la tienda, categorías, usuarios.
Estas son las tablas en la base de datos: {tables_info}.
Por ejemplo, si el usuario pregunta cuántos usuarios hay en la base de datos,
debes consultar la tabla `myapp_user`y verificar el campo `is_user`
para diferenciar usuarios registrados de administradores.
Responde de manera clara y directa.
"""

TABLES_INFO = """
public  | myapp_category | tabla | elegance_dev
public  | myapp_comments | tabla | elegance_dev
public  | myapp_orders   | tabla | elegance_dev
public  | myapp_product  | tabla | elegance_dev
public  | myapp_user     | tabla | elegance_dev
"""


# Function to create the connection and the agent
def get_sql_agent():
    DATABASE_URL = (
        f'postgresql://{settings.DATABASES["default"]["USER"]}:'
        f'{settings.DATABASES["default"]["PASSWORD"]}@'
        f'{settings.DATABASES["default"]["HOST"]}/'
        f'{settings.DATABASES["default"]["NAME"]}'
    )

    # Crear el motor SQLAlchemy
    engine = create_engine(DATABASE_URL)

    # Instanciar la base de datos
    db = SQLDatabase(engine)

    # Instantiate the Google Generative AI model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", google_api_key=API_KEY)

    memory = ConversationBufferMemory()

    # Create the SQL agent
    return create_sql_agent(llm, db=db, memory=memory, verbose=True)


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
                return JsonResponse(
                    {'answer': 'Por favor, ingresa una pregunta.'}, status=400)

            # Get SQL Agent
            agent = get_sql_agent()

            # Create the user message
            human_message = HumanMessage(content=SYSTEM_PROMPT.format(
                tables_info=TABLES_INFO) + "\n\n" + question)

            # Invoke the agent with the message
            result = agent.invoke([human_message])

            # Parse the response
            response = result.get(
                'output', 'Lo siento, no pude encontrar la respuesta.')
            parsed_response = parse_response(response)
            return JsonResponse({'answer': parsed_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
