from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ask_bot

app = FastAPI()

# Pydantic model for request body
class Message(BaseModel):
    question: str

# Route to handle chat input
@app.post("/chat")
async def chat(message: Message):
    try:
        response = ask_bot(message.question)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
