from django.db import models

# Create your models here.

class GoogleUser(models.Model):
    
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)
    last_login = models.DateTimeField()
