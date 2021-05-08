from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(r"C:\Users\c-o-n\Coding\Projects\time-wiz\client_secret.json", scopes=scopes)

flow.run_console()

