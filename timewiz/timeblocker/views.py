import datetime
import json
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from google.auth import credentials

import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow

from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from googleapiclient.discovery import build

from oauth2client.contrib.django_util.storage import DjangoORMStorage

from .models import GoogleUser

# Create your views here.


scopes = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(r"C:\Users\c-o-n\Coding\Projects\time-wiz\client_secret.json", scopes=scopes)

flow.redirect_uri = 'http://localhost:8000/timeblocker/googlepermission/redirect'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'

)

def index(request):
    """ THIS IS BROKEN RN:
    storage = DjangoORMStorage(GoogleUser, 'id', request.user, 'credentials')
    credential = storage.get()
    print(credential) """
    return HttpResponse("Hello there good buddy.")

@login_required(login_url="/timeblocker/googlepermission")
def get_authenticated_user(request: HttpRequest):
    print(request.user)
    user = request.user
    return JsonResponse({
        "id": user.id,
        "name": user.name,
        "email": user.email
     })

def googlepermission(request):
    return redirect(authorization_url)

def googleredirect(request: HttpRequest):
    print("\n")
    print(request.get_full_path())
    print("\n")
    authorization_response = request.get_full_path()
    # code = request.GET.get('code')
    token = flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials

    print("\ncredentials are: ")
    for item in credentials:
        print(item)
    print("\n")

    # calendar = build('calendar', 'v3', credentials=credentials)

    # this line decrypts the user id from google
    userid = id_token.verify_oauth2_token(credentials.id_token, requests.Request(), credentials.client_id)

    google_user = authenticate(request, user=userid)
    
    google_user = list(google_user).pop()

    # this was a test to see what the googleuser object looked like
    # print("\n google_user: ")
    # print(google_user)

    login(request, google_user)

    # this was a test to see what the userid contained
    # print("\nuserid contents:")
    # for item in userid:
    #   print(item + str(userid[item]))

    # This tested getting items from the calendar service object. It will probably not be here.
    # now = datetime.datetime.utcnow().isoformat() + 'Z'
    # test3events = calendar.events().list(calendarId='primary', timeMin=now,
    # maxResults=3, singleEvents=True, orderBy='startTime').execute()
    # next3events = test3events.get('items', [])

    calendar.close()

    return redirect('/timeblocker/auth/user')