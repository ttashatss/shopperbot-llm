from keys.keys import DRIVE_KEY_PATH

import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

with open(DRIVE_KEY_PATH) as config_file:
    config = json.load(config_file)

credentials = service_account.Credentials.from_service_account_info(
    {"client_email": config["client_email"],
     "private_key": config["private_key"],
     "token_uri": config["token_uri"]},
    scopes=["https://www.googleapis.com/auth/drive", 
            "https://www.googleapis.com/auth/spreadsheets", 
            "https://www.googleapis.com/auth/documents"])

drive_service = build("drive", "v3", credentials=credentials)
sheets_service = build('sheets', 'v4', credentials=credentials)
docs_service = build("docs", "v1", credentials=credentials)


def read_docs(file_id):
    
    request = drive_service.files().export_media(fileId=file_id, mimeType='text/plain')
    content = request.execute()

    # Decode the content from bytes to string
    content = content.decode('utf-8')
        
    return content
    
