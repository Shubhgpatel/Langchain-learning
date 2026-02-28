from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
from dotenv import load_dotenv
from ollama import chat
load_dotenv()

model = ChatOllama(model="gemma2:2b")

chat_history = [SystemMessage(content = "You're an Helpful AI Assistant")]
while True:
    user_input = input('You :')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI :",result.content)

print("Memory :", chat_history)