from django.db import models

# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

