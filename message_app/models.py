# Importing django modules
from django.db import models
from django.contrib.auth.models import User

# Importing custom utils
from message_app.utiles import store_username_and_delete

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
class Message(models.Model):
    LEVEL_CHOICES = [
        ("#DC3545",'Danger'),
        ("#FFC107",'Warning'),
        ("#17A2B8",'Inform')
    ]
    body = models.TextField()
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default="#17A2B8")
    user = models.ForeignKey(User, null=False, blank=True, on_delete=models.SET(store_username_and_delete))
    company = models.ForeignKey(Company, null=False, blank=True, on_delete=models.CASCADE)
