from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

Prompt_template = "Eres una IA llamada EleganceAI especializada en responder preguntas sobre accesorios en la tienda Elegance. Pregunta: {question}"
