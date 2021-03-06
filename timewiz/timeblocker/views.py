import datetime
import json
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from google.auth import credentials
from pyasn1.type.univ import Null

import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow

from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from googleapiclient.discovery import build

from .models import GoogleUser
from .managers import GoogleUserOAuth2Manager

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
    user_validated = False
    
    user = request.user
    
    print("refresh token is:")
    print(user.refresh_token)

    if user.refresh_token != None:
        print("The user is validated!")
        user_validated = True
    else:
        print("User isn't validated!")
        return redirect('/timeblocker/googlepermission')
    
    user_credentials = google.oauth2.credentials.Credentials(
        token=user.token,
        refresh_token=user.refresh_token,
        id_token=user.id_token,
        token_uri=user.token_uri,
        client_id=user.client_id,
        client_secret=user.client_secret,
        default_scopes=user.default_scopes
    )

    if not user_credentials.valid:
        if user_validated:
            user_credentials.refresh(user)

    calendar = build('calendar', 'v3', credentials=user_credentials)

    now = datetime.datetime.utcnow()

    nowFormatted = now.isoformat() + 'Z'

    today = now.date()

    todayGoogle = datetime.datetime.combine(today, datetime.datetime.min.time()).isoformat() + 'Z'

    print(todayGoogle)

    today_single_events = calendar.events().list(calendarId='primary', timeMin=todayGoogle, singleEvents=True, orderBy='startTime').execute()

    
    """
    test3events = calendar.events().list(calendarId='primary', timeMin=now,
    maxResults=3, singleEvents=True, orderBy='startTime').execute()
    
    next3events = test3events.get('items', [])

    calendar.close()

    # This tested getting items from the calendar service object. It will probably not be here.
    
    TESTS TO SEE THE NEXT ITEMS IN THE CALENDAR

    for item in next3events:
        print("\n")
        print(item)
    
    calendar.close()
    """

    return HttpResponse("Hello there.")

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
    

    calendar = build('calendar', 'v3', credentials=credentials)

    # this line decrypts the user id from google
    userid = id_token.verify_oauth2_token(credentials.id_token, requests.Request(), credentials.client_id)

    google_user = authenticate(request, user=userid)
    
    # commented out as this is now taken care of in authenticate fxn
    # google_user = list(google_user).pop()


    # this was a test to see what the googleuser object looked like
    # print("\n google_user: ")
    # print(google_user)

    login(request, google_user)

    user = request.user
    
    # this references managers.py to update the credentials in the DB
    GoogleUser.objects.update_google_creds(user.id, credentials)

    """ THIS PRINTS ALL THE ITEMS IN CREDENTIALS OBJECT
    print(
        "\nCredentials are: \n",
        credentials.token, "\n",
        credentials.refresh_token, "\n",
        credentials.id_token, "\n",
        credentials.token_uri, "\n",
        credentials.client_id, "\n",
        credentials.client_secret, "\n",
        credentials.default_scopes, "\n"
        )
    """

    # this was a test to see what the userid contained
    # print("\nuserid contents:")
    # for item in userid:
    #   print(item + str(userid[item]))

    return redirect('/timeblocker/auth/user')