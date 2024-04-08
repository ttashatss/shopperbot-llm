from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

from keys.keys import DRIVE_KEY_PATH

with open(DRIVE_KEY_PATH) as config_file:
    config = json.load(config_file)

credentials = service_account.Credentials.from_service_account_info(
{"client_email": config["client_email"],
    "private_key": config["private_key"],
    "token_uri": config["token_uri"]},
scopes=["https://www.googleapis.com/auth/drive", 
        "https://www.googleapis.com/auth/spreadsheets", 
        "https://www.googleapis.com/auth/documents"])

def read_docs(file_ids:list):

    drive_service = build("drive", "v3", credentials=credentials)
    sheets_service = build('sheets', 'v4', credentials=credentials)
    docs_service = build("docs", "v1", credentials=credentials)
        
    contents = []
    
    for fid in file_ids:
        request = drive_service.files().export_media(fileId=fid, mimeType='text/plain')
        content = request.execute()

        # Decode the content from bytes to string
        content_str = content.decode('utf-8')
        
        contents.append(content_str)

    return contents
