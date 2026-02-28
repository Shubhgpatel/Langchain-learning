from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("SHUBH_RESUME_UPDATED.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 100, 
    chunk_overlap=10,
    separators = ["\n\n", "\n", "."]
)

chunks = splitter.split_documents(docs)
print(chunks[0].page_content)