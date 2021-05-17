from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db import models

import google.oauth2.credentials

from .managers import GoogleUserOAuth2Manager


# Create your models here.

class GoogleUser(models.Model):
    objects = GoogleUserOAuth2Manager()

    id = models.DecimalField(primary_key=True, max_digits=30, decimal_places=0)
    email = models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True)
    token = models.CharField(max_length=200, null=True)
    refresh_token = models.CharField(max_length=200, null=True)
    id_token = models.CharField(max_length=1500, null=True)
    token_uri = models.CharField(max_length=100, null=True)
    client_id = models.CharField(max_length=100, null=True)
    client_secret = models.CharField(max_length=100, null=True)
    default_scopes = models.CharField(max_length=100, null=True)

    def is_authenticated(self, request):
        return True

    """ WAS PLAYING WITH THIS BUT NOT SURE IF NEEDED
    def add_credentials(self, creds: google.oauth2.credentials.Credentials):
        self.token = creds.token,
        self.refresh_token=creds.refresh_token,
        self.id_token=creds.id_token,
        self.token_uri=creds.token_uri,
        self.client_id=creds.client_id,
        self.client_secret=creds.client_secret,
        self.default_scopes=creds.default_scopes
    """