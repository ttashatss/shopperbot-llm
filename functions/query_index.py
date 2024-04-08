def query_index(client, model, index,prompt:str):
    
    xq = client.embeddings.create(input=prompt, model=model).data[0].embedding
    
    res = index.query(vector=[xq], top_k=1, include_metadata=True)
    z=res['matches']
    
    result = []
    
    for match in res['matches']:
        result.append(match['id'])
        #print(f"{match['score']:.2f}: {match['id']}")

    return result