from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 intresting facts about {topic}',
    input_variables=['topic']
)

model = ChatOllama(model="gemma2:2b")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic" : "cricket"})

print(result)

chain.get_graph().print_ascii()