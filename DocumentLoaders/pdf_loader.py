from langchain_community.document_loaders import TextLoader,PyPDFLoader,CSVLoader,WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.3,
)

# prompt = PromptTemplate(
#     template = "Write a summary of the following text: {text}",
#     input_variables=["text"],
# )

# pdf loader
# loader = PyPDFLoader("SHUBH_RESUME_UPDATED.pdf")
# docs = loader.load()
# print(docs)

# web base loader
url = "https://www.espn.com/"
loader = WebBaseLoader(url)
docs = loader.load()
print(docs[0].page_content) 


# chain = prompt | llm | StrOutputParser()
# result = chain.invoke({"text": docs})
# print(result) 


