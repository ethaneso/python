from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime 
import yfinance_ez as yf
from datetime import datetime

tickerName = "sample"
stock = yf.Ticker(tickerName)
financialsDataFrame = stock.quarterly_financials

arra1 = []
arra1.append(tickerName)
arra2 = []

for yr, info in y.items():
    finYr = datetime.fromtimestamp(int(yr)/1000)
    date = finYr.strftime('%Y-%m-%d')
    arra1.append(date)

arra2.append(arra1)

financialsWithoutYr = financialsDataFrame.reset_index().to_numpy().tolist()

for ele in financialsWithoutYr:
  arra3 = arra2
  arra3.append(ele)

financials = arra3

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id = 'sample_sheet_id'
dataRange = 'sample_sheet_range'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

# get from spreadsheet
# result = sheet.values().get(spreadsheetId=spreadsheet_id,
#                            range=dataRange).execute()
# values = result.get('values', [])
# print(result);

# write to spreadsheet
request = sheet.values().append(spreadsheetId=spreadsheet_id,
                                range="Sheet6!G1:L24",
                                valueInputOption="USER_ENTERED",
                                body={"values":financials}).execute()
