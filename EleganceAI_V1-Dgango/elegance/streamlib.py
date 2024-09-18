import streamlit as st
import json
from yourmodule.config import embeddings, llm  # Importa la configuración del LLM y embeddings
from yourmodule.scraper import scrape_webpage  # Importa la lógica de scraping
from yourmodule.text_splitter import split_text_into_chunks  # Importa el splitter de texto
from yourmodule.vector_db import initialize_faiss  # Importa FAISS para búsqueda de vectores
from yourmodule.qa_chain import load_chain, parse_response  # Importa la lógica de QA

# Define la URL de scraping
URL = 'https://lunamar.co/blogs/news/tendencias-en-accesorios-2024?srsltid=AfmBOoom1AHGRDfcJy2ZQeaePPqNpG87yGEwyw-cBNIFVfqyNF2G038k'

# Scraping y procesamiento de datos
@st.cache_data(show_spinner=False)
def initialize_chatbot():
    raw_text = scrape_webpage(URL)
    texts = split_text_into_chunks(raw_text)
    docsearch = initialize_faiss(texts, embeddings)
    chain = load_chain(llm)
    return docsearch, chain

# Inicializar FAISS y el modelo
docsearch, chain = initialize_chatbot()

# Función para procesar la pregunta
def process_question(question):
    # Buscar documentos relevantes en FAISS
    docs = docsearch.similarity_search(question)
    
    if not docs:
        return 'No se encontraron documentos relevantes.'
    
    # Ejecutar la cadena de QA con el modelo
    result = chain.run(input_documents=docs, question=question)
    parsed_response = parse_response(result)
    
    return parsed_response

# Configuración de la interfaz de Streamlit
st.title('EleganceAI Chatbot')
st.write("Pregúntale a EleganceAI sobre las últimas tendencias en accesorios.")

# Crear una caja de texto para ingresar preguntas
question = st.text_input("Escribe tu pregunta aquí:")

if st.button("Enviar"):
    if question.strip() == '':
        st.warning("Por favor, ingresa una pregunta válida.")
    else:
        st.write(f"**Usuario:** {question}")
        with st.spinner('Procesando...'):
            answer = process_question(question)
        st.write(f"**Elegance:** {answer}")
