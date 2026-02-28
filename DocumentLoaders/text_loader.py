from langchain_community.document_loaders import TextLoader,PyPDFLoader,CSVLoader,WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.3,
)

prompt = PromptTemplate(
    template = "Provide answer to the question: {question} from the following text: {text}",
    input_variables=["question","text"],
)

url = "https://www.espn.in/cricket/series/8604/game/1512750/ireland-vs-zimbabwe-32nd-match-group-b-icc-mens-t20-world-cup-2025-26"
loader = WebBaseLoader(url)
docs = loader.load()
# print(docs)

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"question": "give me some info about IRE Vs ZIM cricket match", "text": docs})
print(result) 