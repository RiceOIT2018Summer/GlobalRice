"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
# SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SPREADSHEET_ID = '14rWedcwXlFQdqjHw2MnAZL6qNxZYwDvZO4VF4BdrAf0'
RANGE_NAME = 'Faculty!A2:G'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    htmlstr = open("cellTemplate.html").read()
    for row in values:
        htmlstrout = htmlstr.replace("[NAME]", row[0])
        htmlstrout = htmlstrout.replace("[DEPARTMENT]", row[3])
        htmlstrout = htmlstrout.replace("[WEBSITE]", row[4])
        htmlstrout = htmlstrout.replace("[PHOTO_SOURCE]", row[5])
        print(htmlstrout)
