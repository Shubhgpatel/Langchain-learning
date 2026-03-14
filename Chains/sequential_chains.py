from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate 5 pointer summary from the following {text}',
    input_variables=['text']
)

model = ChatOllama(model="gemma2:2b")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic" : "Education's negative Impact on Students"})

print(result)

chain.get_graph().print_ascii()