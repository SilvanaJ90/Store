import os
from dotenv import load_dotenv
from django.conf import settings

import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain.schema import HumanMessage

from langchain.prompts import (
    ChatPromptTemplate, PromptTemplate,
    SystemMessagePromptTemplate, AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import (
    AIMessage, HumanMessage, SystemMessage
)

from langchain.output_parsers import CommaSeparatedListOutputParser


# Load environment variables from .env file
load_dotenv("./../.env")

# Configure Django with environment variables for the database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Initialize Django if necessary
if not settings.configured:
    settings.configure(DATABASES=DATABASES)

# Create the connection URL for SQLAlchemy
DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST", "127.0.0.1")}/{os.getenv("POSTGRES_DB")}'

# Create the SQLAlchemy engine using the connection URL
engine = create_engine(DATABASE_URL)

# Create the SQLDatabase object using the engine
db = SQLDatabase(engine)

# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=API_KEY)

# Create the SQL agent
agent = create_sql_agent(
    llm,
    db=db,
    verbose=True
)

# system template
system_template = "Eres una IA especializada en la administración de una tienda de accesorios. Generas respuestas rápidas y claras para consultas relacionadas con la base de datos de la tienda."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# human template
human_template = """
Consulta: {consulta_tipo}
Detalles: {detalles_consulta}
"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Crear un chat prompt con los mensajes del sistema y humano
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# Completar la solicitud con parámetros específicos
solicitud_completa = chat_prompt.format_prompt(
    detalles_consulta="Quiero saber cuántos usuarios hay en el sistema. (Nota: Considera solo usuarios con is_user=True)"
)

# Obtener el resultado de la respuesta formateada
result = llm.invoke(solicitud_completa)

print(result.content)

# parser

Ouput_parser = CommaSeparatedListOutputParser()

format_instructions = Ouput_parser.get_format_instructions() #Nos devuelve las instrucciones que a pasar  al LLM en funcion de 

# respuesta imaginaria
respuesta = "aretes, pulsera, cartera "
Ouput_parser.parse(respuesta)

# Creamos la plantilla de usuario con la concatenacion de la variable "request" y la variable forma 
# las instrucciones adicionales que le pasaremos al LLM


human_template = '{request}\n{format_instructions}'
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

#creamos el prompt y le damos forma a las variables
chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])
chat_prompt.format_prompt(request="dime cuantos usuaris hay en el sistema",
                          format_instructions = Ouput_parser.get_format_instructions())


#Transforma el objeto prompt a una lista de mensajes y lo guarda en solicitud completa

solicitud_completa = chat_prompt.format_prompt(request="dime cuantos usuaris hay en el sistema",
                          format_instructions = Ouput_parser.get_format_instructions())

result = llm.invoke(solicitud_completa)

----
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

            # Crear el mensaje del sistema
            system_template = "Eres una IA especializada en la administración de una tienda de accesorios. Generas respuestas claras para consultas sobre productos, categorías y usuarios en la base de datos."
            system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

            # Crear el mensaje del usuario con el prompt adecuado
            human_template = """
            Genera una consulta SQL que responda a la siguiente pregunta sobre la base de datos de la tienda:
            Consulta: {consulta_tipo}
            Detalles: {detalles_consulta}
            """
            human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

            # Completar el prompt para el agente
            chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
            solicitud_completa = chat_prompt.format_prompt(consulta_tipo="Consulta SQL", detalles_consulta=question)

            # Invocar el agente con el mensaje
            result = agent.invoke([HumanMessage(content=solicitud_completa.content)])

            # Extraer y verificar la consulta generada
            response = result.get('output', 'Lo siento, no pude encontrar la respuesta.')
            
            # Si no hay respuesta válida, loguear la consulta y los detalles
            if 'output' not in result:
                return JsonResponse({'answer': 'No se pudo generar una consulta SQL válida. Verifica la estructura de la pregunta.'})

            return JsonResponse({'answer': response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        ----

        #guardar una plantilla de PromptTemplate
        plantilla = "pregunta: {pregunta_usuario}\nRespuesta: Vamos a verlo paso a paso"
        prompt = PromptTemplate(template=plantilla)
        prompt.save("prompt.json")

        # Cargar prompt

        from langchain.prompts import load_prompt

        prompt_cargado = load_prompt("prompt.json")
        