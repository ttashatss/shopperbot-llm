from functions.query_index import query_index
from functions.read_docs import read_docs
from functions.generate_answer import generate_answer

def query(client, model, index, prompt:str):
    
    var_fn = {}
    
    index_result = query_index(client=client, model=model, index=index, prompt=prompt)
    var_fn.update({'index_result': index_result})
    
    file_ids = []
    for res in index_result:
        file_id = res.split(': ')[1]
        file_ids.append(file_id)
        
    contents = read_docs(file_ids=file_ids)
    
    response = generate_answer(client=client, prompt=prompt, contents=contents)
    var_fn.update({'response': response})
    answer = var_fn.get('response', '')
    
    return answer