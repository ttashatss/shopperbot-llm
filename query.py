# #%%Imports
# import sys
# sys.path.append('/Users/tashatanarugsachock/Desktop/shopperbot-llm')
# from keys.keys import DRIVE_KEY_PATH, DRIVE_FOLDER_ID
# from keys.keys import OPENAI_API_KEY
# from keys.keys import PINECONE_API_KEY, INDEX_NAME

# import json
# from openai import OpenAI
# from pinecone import Pinecone

# #%%Setup
# with open(DRIVE_KEY_PATH) as config_file:
#     config = json.load(config_file)

# credentials = service_account.Credentials.from_service_account_info(
#     {"client_email": config["client_email"],
#      "private_key": config["private_key"],
#      "token_uri": config["token_uri"]},
#     scopes=["https://www.googleapis.com/auth/drive", 
#             "https://www.googleapis.com/auth/spreadsheets", 
#             "https://www.googleapis.com/auth/documents"])

# drive_service = build("drive", "v3", credentials=credentials)
# sheets_service = build('sheets', 'v4', credentials=credentials)
# docs_service = build("docs", "v1", credentials=credentials)


# client = OpenAI(api_key=OPENAI_API_KEY)
# model = 'text-embedding-ada-002'

# pc = Pinecone(api_key=PINECONE_API_KEY)
# index = pc.Index(INDEX_NAME)

# #%%Functions
# def query_index(prompt:str):
    
#     xq = client.embeddings.create(input=prompt, model=model).data[0].embedding
    
#     res = index.query(vector=[xq], top_k=1, include_metadata=True)
    
#     z=res['matches']
    
#     result = []
    
#     for match in res['matches']:
#         result.append(match['id'])
#         #print(f"{match['score']:.2f}: {match['id']}")

#     return result

# def read_docs(file_ids:list):
    
#     contents = []
    
#     for fid in file_ids:
#         request = drive_service.files().export_media(fileId=fid, mimeType='text/plain')
#         content = request.execute()

#         # Decode the content from bytes to string
#         content_str = content.decode('utf-8')
        
#         contents.append(content_str)

#     return contents

# def generate_answer(prompt:str, contents:list):
    
#     endpoint = "https://api.openai.com/v1/chat/completions"
    
#     info = ''
#     for i in range(len(contents)):
#         info += f'Information{i+1}: {contents[i]}\n\n'
#     prompt = info + f'Question: {prompt}'
        
#     response = client.completions.create(
#       model="gpt-3.5-turbo-instruct",
#       prompt=prompt,
#       #temperature=0.7,
#       max_tokens=100
#     )
    
#     ans = response.dict()['choices'][0]['text']
#     return ans


# #%%Main
# def query(prompt:str):
    
#     var_fn = {}
    
#     index_result = query_index(prompt)
#     var_fn.update({'index_result': index_result})
    
#     file_ids = []
#     for res in index_result:
#         file_id = res.split(': ')[1]
#         file_ids.append(file_id)
        
#     contents = read_docs(file_ids)
    
#     response = generate_answer(prompt, contents)
#     var_fn.update({'response': response})
    
#     return var_fn

# if __name__ == "__main__":
#     prompt = 'Siam Paragon Car park'
#     print(query(prompt))