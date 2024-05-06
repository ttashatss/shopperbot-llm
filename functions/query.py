from keys.keys import PINECONE_API_KEY, OPENAI_API_KEY

from pinecone import Pinecone, ServerlessSpec
from tqdm import tqdm
pc = Pinecone(api_key=PINECONE_API_KEY)

from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

MODEL = "text-embedding-ada-002"

def embed(data):
    
    response = client.embeddings.create(
        input=data,
        model=MODEL
    )
    
    vector = response.data[0].embedding
    
    #print(vector)
    
    return vector

def query(text:str, index_name, top_k=1):
    
    vector = embed(text)
    
    index = pc.Index(index_name)
    
    res = index.query(
        vector=vector,
        top_k=top_k,
        include_values=False
        )
    
    return res['matches']