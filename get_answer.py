from functions.query import query
from functions.read_docs import read_docs
from functions.gpt import gpt

def get_answer(prompt:str):
    
    if prompt[-1] != '?':
        prompt += '?'
    
    store = query(prompt, index_name='stores')
    score = store[0]['score']
    
    if score > 0.83:
        index = 'stores-db'
    else:
        index = 'paragon-db'
        
    match = query(prompt, index_name=index)
    match_id = match[0]['id']
    
    info = read_docs(file_id=match_id)
    prompt = info + f'Question: {prompt}'
    
    ans = gpt(prompt)
    ans = ans.strip()
    
    return ans