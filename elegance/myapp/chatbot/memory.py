from langchain.chains import LLMChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from myapp.chatbot.config import llm

prompt_template = """
Eres una Inteligencia artificial llamada EleganceAI,
brinda servicos de accesorios en un tienda online
debes ser amable
"""

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=prompt_template
        ),  # The persistent system prompt
        MessagesPlaceholder(
            variable_name="chat_history"
        ),  # Where the memory will be stored.
        HumanMessagePromptTemplate.from_template(
            "{human_input}"
        ),  # Where the human input will be injected
    ]
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
    )


chat_llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=False,
    memory=memory,
    )
