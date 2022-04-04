# Used: https://towardsdatascience.com/how-to-import-google-sheets-data-into-a-pandas-dataframe-using-googles-api-v4-2020-f50e84ea4530

from googleapiclient.discovery import build
from google.oauth2 import service_account

# Fill in credentials by:
# (1) Go to https://console.cloud.google.com/apis
# (2) Use this guide: https://towardsdatascience.com/how-to-import-google-sheets-data-into-a-pandas-dataframe-using-googles-api-v4-2020-f50e84ea4530 
# but it is easier just to go credentials > service accounts > create key and then paste the json in place below.
# (3) spreadsheet or document ID can be found in the url after the '/d/' up until the next '/'
# (4) DATA_TO_PULL is a cell reference (i.e. 'Name of sheet!F1:F100'). This can be just a sheet name or cells specifically.

# INSERT your credentials here, in the folowing form:

# credentials = {
#   "type": "",
#   "project_id": "",
#   "private_key_id": "",
#   "private_key": "",
#   "client_email": "",
#   "client_id": "",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": ""
# }

def pull_sheet_data_values(SPREADSHEET_ID,DATA_TO_PULL,credentials):
    creds = service_account.Credentials.from_service_account_info(credentials, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=DATA_TO_PULL).execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                  range=DATA_TO_PULL).execute()
        data = rows.get('values')
        print("COMPLETE: Data copied")
    return data

def pull_doc_values(DOCUMENT_ID,credentials):
    creds = service_account.Credentials.from_service_account_info(credentials, scopes=['https://www.googleapis.com/auth/documents.readonly'])
    service = build('docs', 'v1', credentials=creds)
    result = service.documents().get(documentId=DOCUMENT_ID).execute()
    return result