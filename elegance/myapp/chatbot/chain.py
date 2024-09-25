from langchain.chains import LLMChain
from langchain.chains import RetrievalQA

from myapp.chatbot.config import llm, embeddings
from myapp.chatbot.memory import prompt, memory
from myapp.chatbot.vector_db import initialize_faiss, documents

# initialize faiss vectordb
docsearch = initialize_faiss(documents, embeddings)

# LLM string to generate responses using the custom prompt
chat_llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=False,
    memory=memory
)

# Create the QA Chain with FAISS and use the response from the custom LLM
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=docsearch.as_retriever(),
    chain_type="stuff",
    memory=memory
)


# Function to process the response of the custom LLM
def generate_response_from_llm(question, context, documents):
    """Use the custom LLM to generate a response."""
    # Match the question and the content of the retrieved documents
    combined_input = f"Pregunta: {question}\n\nDocumentos:\n"
    for doc in documents:
        combined_input += f"- {doc.page_content}\n"
    # Execute the LLM chain with the prompt and context
    result = chat_llm_chain.run({
        "human_input": combined_input,
        "chat_history": context,
    })

    return result
