from operator import rshift
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

model = ChatOllama(model='llama3.1:8b',temperature=0.5,)

result = model.invoke("give me a poem ")
print(result.content)