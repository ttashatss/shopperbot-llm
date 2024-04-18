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
    answer = query(client, model, index, input.prompt)
    return answer
    

# if __name__ == "__main__":
#     # prompt = 'Siam Paragon Car park'
#     # print(query(client, model, index, prompt)) 

#Hi   