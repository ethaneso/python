from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime 
import json
import yfinance_ez as yf

from datetime import datetime

ticker = "sample"

quarterly = stock.quarterly_financials
yearly = stock.financials

stock = yf.Ticker(ticker)
financialsDataFrame = yearly

financialsObject = financialsDataFrame.to_json()
y = json.loads(financialsObject)

arra1 = []
arra1.append(ticker)
arra4 = []

for yr, info in y.items():
# print(yr)
    finYr = datetime.fromtimestamp(int(yr)/1000)
    date = finYr.strftime('%Y-%m-%d')
    arra1.append(date)

arra4.append(arra1)

financialsWithoutYr = financialsDataFrame.reset_index().to_numpy().tolist()
print(financialsWithoutYr)
for ele in financialsWithoutYr:
  arra5 = arra4
  arra5.append(ele)
  print(arra5)
financials = arra5
print(financials)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id = 'sample_sheet_id'
dataRange = 'Sheet6!A:E'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=spreadsheet_id,
#                            range=dataRange).execute()
# values = result.get('values', [])
# print(result);

request = sheet.values().append(spreadsheetId=spreadsheet_id,
                                range=dataRange,
                                valueInputOption="USER_ENTERED",
                                body={"values":financials}).execute()

print(request)
