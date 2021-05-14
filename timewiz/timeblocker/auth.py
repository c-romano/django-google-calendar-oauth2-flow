from django.contrib.auth.backends import BaseBackend
from .models import GoogleUser
from django.contrib.auth.models import User
from .managers import GoogleUserOAuth2Manager

class GoogleAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> GoogleUser:
        find_user = GoogleUser.objects.filter(id=user['sub'])
        if len(find_user) == 0:
            print('user not found. Saving...')
            print('\n ID is:'+user['sub']+'\n')
            new_user = GoogleUser.objects.create_new_google_user(user)
            print(new_user)
            return new_user
        return list(find_user).pop()

    def get_user(self, user_id):
        try:
            return GoogleUser.objects.get(pk=user_id)
        except GoogleUser.DoesNotExist:
            return None
