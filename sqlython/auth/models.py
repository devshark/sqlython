from django.db import models

# Create your models here.
class Login(models.Model):
	username = models.CharField(max_length=20)
	password = models.TextField()
	email = models.CharField(max_length=200)