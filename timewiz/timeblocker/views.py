import datetime
import json
from django.http.request import HttpRequest
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from google.auth import credentials

import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow

from googleapiclient.discovery import build

# Create your views here.


scopes = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/userinfo.profile']

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(r"C:\Users\c-o-n\Coding\Projects\time-wiz\client_secret.json", scopes=scopes)

flow.redirect_uri = 'http://localhost:8000/timeblocker/googlepermission/redirect'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'

)

def index(request):
    return HttpResponse("Hello there good buddy.")
    
def googlepermission(request):
    return redirect(authorization_url)

def googleredirect(request: HttpRequest):
    authorization_response = request.get_full_path()
    code = request.GET.get('code')
    token = flow.fetch_token(authorization_response=authorization_response)
    print("the code is:" + code)
    print("the access token is:" + str(token))
    
    credentials = flow.credentials

    print("credentials are: " + str(credentials))

    calendar = build('calendar', 'v3', credentials=credentials)

    print("was able to get to this point without causing mayhem.")

    now = datetime.datetime.utcnow().isoformat() + 'Z'

    print("Got to this point without any issues!\n")

    test3events = calendar.events().list(calendarId='primary', timeMin=now,
    maxResults=3, singleEvents=True, orderBy='startTime').execute()
    
    next3events = test3events.get('items', [])

    print("\n the next 3 events are:\n")

    for event in next3events:
        print(event)
        print("\n")

    calendar.close()

    return JsonResponse({"dude":"wheres my car"})