import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd


def database(resource,city,bg="None"):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("ICBOT2021").sheet1  # Open the spreadhseet

    data = sheet.get_all_records()  # Get a list of all records



    df = pd.DataFrame(data)

    df = df.sort_values(by="last_verified")
    df = df.drop_duplicates(subset=['region', 'name', 'contact_number'],keep="last")
    update = df[(df['resource'] == resource) & (df['region'] == city) & (df['blood_group'] == bg) & (df['upload_status'])==1]
    update1=update.head(10)


    return update1


