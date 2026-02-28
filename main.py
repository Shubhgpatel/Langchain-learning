from re import template
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    base_url="https://api.groq.com/openai/v1"
)

# response = llm.invoke("Who is the Prime Minister of India?")
# print(response.content)

prompt = PromptTemplate(
    input_variables=["topic"],
    template = "explain the topic {topic} in simple words for a beginner"
)

# formatted_prompt = prompt.format(topic = "Natural Language Processing")
# print(formatted_prompt)

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"topic": "Natural Language Processing"})
print(result)

