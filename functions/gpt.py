from keys.keys import OPENAI_API_KEY

from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)


def gpt(prompt:str):
    
    endpoint = "https://api.openai.com/v1/chat/completions"
        
    response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt,
      #temperature=0.7,
      max_tokens=100
    )
    
    ans = response.dict()['choices'][0]['text']
    
    return ans