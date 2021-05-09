from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
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
