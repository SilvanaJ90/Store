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

# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

# Function to create the connection and the agent
def get_sql_agent():
    # Create the database
    DATABASE_URL = f'postgresql://{settings.DATABASES["default"]["USER"]}:{settings.DATABASES["default"]["PASSWORD"]}@{settings.DATABASES["default"]["HOST"]}/{settings.DATABASES["default"]["NAME"]}'

   # Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

 # Create the database instance
    db = SQLDatabase(engine)

   # Instantiate the Google Generative AI LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=API_KEY)

    # Create the SQL agent
    return create_sql_agent(llm, db=db, verbose=True)

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        try:
            # Get the question from the request
            data = json.loads(request.body)
            question = data.get('question', '')

            if not question:
                return JsonResponse({'answer': 'Por favor, ingresa una pregunta.'}, status=400)

            # Get SQL Agent
            agent = get_sql_agent()

            # Create the user message
            human_message = HumanMessage(content=question)

            # Invoke the agent with the message
            result = agent.invoke([human_message])

            # Extract the answer from the result
            response = result.get('output', 'Lo siento, no pude encontrar la respuesta.')
            return JsonResponse({'answer': response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
