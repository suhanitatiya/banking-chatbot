from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot_model import Chatbot
from fastapi.middleware.cors import CORSMiddleware

# Initialize the app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load chatbot
chatbot = Chatbot("data/dataset.csv")  # Ensure dataset.csv exists

# Define request schema
class Query(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Welcome to the Banking Chatbot API!"}

@app.post("/chat/")
def chat(query: Query):
    user_message = query.message
    response = chatbot.get_response(user_message)
    if response:
        return {"response": response}
    else:
        raise HTTPException(status_code=400, detail="Unable to process the request")
