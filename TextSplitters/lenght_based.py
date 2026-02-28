from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """
Cricket is a bat-and-ball sport played between two teams of eleven players on a field with a 22-yard pitch at its center. Known for its strategic depth and rich traditions, cricket is particularly popular in countries like India, England, Australia, Pakistan, South Africa, the West Indies, New Zealand, Sri Lanka, and Bangladesh.

Cricket originated in England during the 16th century and became the national sport by the 18th century. The first international match was played between the United States and Canada in 1844. The sport spread globally through the British Empire, and the first Test match was played between Australia and England in 1877. The International Cricket Council (ICC), founded in 1909, now governs the sport worldwide.
"""

splitter = CharacterTextSplitter(
    chunk_size= 100, 
    chunk_overlap=0,
    separator = ''
)

chunks = splitter.split_text(text)
print(chunks[0])