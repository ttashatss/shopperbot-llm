from openai import OpenAI
from pinecone import Pinecone

from keys.keys import OPENAI_API_KEY, PINECONE_API_KEY, INDEX_NAME
from functions.query import query

client = OpenAI(api_key=OPENAI_API_KEY)
model = 'text-embedding-ada-002'

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

if __name__ == "__main__":
    prompt = 'Siam Paragon Car park'
    print(query(client, model, index, prompt))