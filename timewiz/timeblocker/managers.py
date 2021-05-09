from django.contrib.auth import models
from django.db.models.fields import DecimalField

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