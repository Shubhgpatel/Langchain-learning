from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatOllama(model="gemma2:2b", temperature=0.3)
# prompt 1
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template="write a 5 line summary on the following text.\n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic' : 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text' : result.content})

result2 = model.invoke(prompt2)

print(result2.content)