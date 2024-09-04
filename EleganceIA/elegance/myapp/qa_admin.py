import os
from dotenv import load_dotenv
from django.conf import settings

import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain.schema import HumanMessage


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


