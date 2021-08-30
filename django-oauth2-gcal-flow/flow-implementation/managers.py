from django.contrib.auth import models
from django.db.models.fields import DecimalField
import google.oauth2.credentials

class GoogleUserOAuth2Manager(models.UserManager):
    def create_new_google_user(self, user):
        new_user = self.create(
            id=user['sub'],
            email=user['email'],
            name=user['name'],
            given_name=user['given_name'],
            family_name=user['family_name'],
            locale=user['locale']
        )
        return new_user

    def update_google_creds(self, requested_id, creds: google.oauth2.credentials.Credentials):
        
        # this function is very delicate, should eventually be improved
        self.filter(pk=requested_id).update(
            token = creds.token,
            refresh_token=creds.refresh_token,
            id_token=creds.id_token,
            token_uri=creds.token_uri,
            client_id=creds.client_id,
            client_secret=creds.client_secret,
            default_scopes=creds.default_scopes
        )