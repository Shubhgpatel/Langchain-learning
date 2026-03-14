from typing import TypedDict,Annotated,Literal
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from dotenv import load_dotenv
load_dotenv()

model = ChatOllama(model="gemma2:2b",temperature=0.3)


# class Review(TypedDict):
#     summary : Annotated[str,"A concise summary of the review"]
#     sentiment : Annotated[str,"The sentiment of the review, either positive or negative or neutral or mixed"]

class Review(BaseModel):
    summary : str = Field(description="A concise summary of the review")
    sentiment : str = Field(description="The sentiment of the review, either positive or negative or neutral or mixed")


prompt = PromptTemplate(
    input_variables=["review"],
    template=(
        "Extract the summary and sentiment of the following review:\n\n"
        "{review}\n\n"
        "The summary should be concise and to the point, no more than 2 sentences."
    )
)

structured_model = model.with_structured_output(Review)

chain = prompt | structured_model

result = chain.invoke({"review":"""I recently purchased the Yamaha YFL-222 Student Flute after weeks of research, and my experience has been a rollercoaster of emotions. 

On the positive side, the build quality is absolutely phenomenal for its price range - the silver-plated finish is smooth, scratch-resistant, and gives it a premium look that rivals flutes costing twice as much. The tone quality surprised me immensely; it produces a warm, rich sound that my music teacher described as 'unexpectedly professional.' The keys are responsive and well-padded, making transitions between notes seamless even for a beginner like me. The case that comes with it is sturdy, well-lined, and has enough compartments for accessories.

However, my experience wasn't without frustrations. The assembly instructions were poorly written and nearly incomprehensible for a first-time buyer. I spent almost 45 minutes trying to figure out the correct way to join the three sections without damaging them. Additionally, after about three weeks of regular practice, I noticed one of the key pads was slightly misaligned, causing an occasional airy sound on the lower D note. Customer service was responsive but asked me to ship the flute back at my own expense, which felt unreasonable for a manufacturing defect.

The intonation is mostly accurate across all registers, though the upper octave can feel slightly sharp in humid weather conditions - a quirk I've seen mentioned in other reviews as well. For a student instrument priced at $300, I expected the cleaning rod and polishing cloth included in the box to be of better quality; they feel cheap and almost disposable.

Overall, despite the hiccups, I would cautiously recommend this flute to beginner-to-intermediate players who are serious about learning. It's not perfect, but with proper maintenance and maybe a professional setup from a local music shop, it punches well above its weight class. Just be prepared for a bit of a learning curve and potentially some minor quality control issues out of the box."""})

output = (dict(result))
print(output)