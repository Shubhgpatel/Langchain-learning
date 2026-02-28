from itertools import chain
from re import template
from pandas.io.formats import style
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
load_dotenv()

st.header('Research Tool')
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

paper_input = st.selectbox("Select Research Paper", [
    "Attention Is All You Need (Transformer Architecture)",
    "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
])

style_input = st.selectbox("Select Explanation Style", [
    "Math-Oriented (with equations and proofs)",
    "Code-Based (with Python examples)",
    "Beginner Friendly (simple analogies, no jargon)"
])

template = load_prompt('template.json')

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input
})
    st.write(result.content)