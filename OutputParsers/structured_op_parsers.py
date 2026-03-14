from os import name
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import ResponseSchema,StructuredOutputParser
load_dotenv()

model = ChatOllama(model="gemma2:2b", temperature=0.3)

schema = [
    ResponseSchema(name = 'fact_1', description ='Fact 1 about the topic'),
    ResponseSchema(name = 'fact_2', description ='Fact 2 about the topic'),
    ResponseSchema(name = 'fact_3', description ='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template=f'Give me three facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
)