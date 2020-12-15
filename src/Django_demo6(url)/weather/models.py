from django.db import models


# Create your models here.
class User(models.Model):
    userID = models.CharField(max_length=8)
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
