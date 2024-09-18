from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

template = """{question}"""
prompt_template = PromptTemplate(
    template=template,
    input_variables=['question']
)

def load_chain(llm):
    return load_qa_chain(llm, chain_type="stuff")

def parse_response(response):
    return response.strip()
