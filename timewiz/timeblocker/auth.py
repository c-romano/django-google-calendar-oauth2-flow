from django.contrib.auth.backends import BaseBackend
from .models import GoogleUser

class GoogleAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user):
        find_user = GoogleUser.objects.filter(id=user['id'])
        if len(find_user) == 0:
            print('user not found. Saving...')