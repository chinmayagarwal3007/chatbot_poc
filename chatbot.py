from langchain.llms.bedrock import Bedrock
from aws_config import get_bedrock_runtime_client

# Initialize the chatbot model
def get_chatbot():
    client = get_bedrock_runtime_client()
    
    # Replace with the actual model ID if different
    llm = Bedrock(
        client=client,
        model_id="meta.llama3-70b-instruct-v1:0",  # Check Bedrock console for exact ID
        model_kwargs={
            "temperature": 0.7,
            "top_p": 0.9
        }
    )
    return llm

# Function to send a prompt and get the response
def ask_bot(question: str) -> str:
    llm = get_chatbot()
    return llm(question)
