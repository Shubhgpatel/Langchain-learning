from typing import Any


from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Virat Kohli is one of India's greatest batsmen, known for his aggressive batting style and exceptional consistency in both Test and ODI formats.",
    "Rohit Sharma is the Indian cricket team captain, famous for his elegant stroke play and holding the record for most double centuries in ODI cricket.",
    "Jasprit Bumrah is India's premier fast bowler, renowned for his unique bowling action and deadly yorkers that trouble the best batsmen in the world."
]

query = "Tell me about virat kohli"
query_embedding = embedding.embed_query(query)
vectors = embedding.embed_documents(docs)

similarity = cosine_similarity([query_embedding],vectors)[0]
index , score = (sorted(list(enumerate(similarity)),key=lambda x:x[1])[-1])

print(index)
print("similarity score is :",score)
