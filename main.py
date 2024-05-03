from openai import OpenAI
from pinecone import Pinecone
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

from keys.keys import OPENAI_API_KEY, PINECONE_API_KEY, INDEX_NAME
from functions.query import query


client = OpenAI(api_key=OPENAI_API_KEY)
model = 'text-embedding-ada-002'

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

class Input(BaseModel):
    userId: str
    userInfo: Optional[str] = None
    prompt: str
    location: Optional[str] = None

app = FastAPI()

@app.post("/")
async def api_post(input: Input):
    print(input)
    answer = query(client, model, index, input.prompt)
    answer = answer.replace('\r', '').replace('\n', '')
    answer = answer.replace('Answer: ', '')
    return answer
    

# if __name__ == "__main__":
#     prompt = 'From this question, what is the correct choice - you can answer with only one letter A, B, C, or D? Question: What is the capital of France? Choice: A. Paris B. London C. Berlin D. Madrid'
#     print(query(client, model, index, prompt)) 

#Hi   