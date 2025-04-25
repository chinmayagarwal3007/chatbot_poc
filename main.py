from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ask_bot

app = FastAPI(debug=True)

# Pydantic model for request body
class Message(BaseModel):
    question: str

@app.get("/")
def fn():
    print('first fnc')
    return {"message": "first fnc"}
    
# Route to handle chat input
@app.post("/chat")
async def chat(message: Message):
    try:
        response = ask_bot(message.question)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
