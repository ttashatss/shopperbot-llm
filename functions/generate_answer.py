def generate_answer(client, prompt:str, contents:list):
    
    endpoint = "https://api.openai.com/v1/chat/completions"
    
    info = ''
    for i in range(len(contents)):
        info += f'Information{i+1}: {contents[i]}\n\n'
    prompt = info + f'Question: {prompt}'
        
    response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt,
      temperature=0.7,
      max_tokens=100
    )
    
    ans = response.dict()['choices'][0]['text']
    return ans
