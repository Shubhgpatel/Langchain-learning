from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatOllama(model="gemma2:2b", temperature=0.3)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Write a name , age and the city of any fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)


chain = template | model | parser
result = chain.invoke({})
print(result)
