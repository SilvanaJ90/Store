import os
from dotenv import load_dotenv
from django.conf import settings
import langchain
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_google_alloydb_pg import AlloyDBEngine, AlloyDBVectorStore
from langchain.sql_database import SQLDatabase

# Configure Django settings manually (if not running in manage.py shell)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elegance.settings')  # Replace 'myapp' with your app name
settings.configure()
db_url = settings.DATABASES['default']['URL']
db = SQLDatabase.from_uri(db_url)
genai.configure(api_key=settings.API_KEY)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Create a AlloyDBEngine instance
alloydb_engine = AlloyDBEngine(db)

# Create an AlloyDBVectorStore instance
alloydb_vector_store = AlloyDBVectorStore(alloydb_engine)
# Example usage:
query = "Los comentarios del producto 1 son positivos o negativos"
response = llm(query)
print(response)

# Example usage with vector store:
document = "Los comentarios del producto 1 son positivos con un score de "
alloydb_vector_store.add_documents([document])

search_results = alloydb_vector_store.similarity_search(query)
print(search_results)

