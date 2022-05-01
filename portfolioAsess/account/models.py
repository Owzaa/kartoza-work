from django.db import models
from django.contrib.auth.models import User

# User Account Model:
class User(models.Model):
        username = models.OneToOneField(User, on_delete=models.CASCADE)
        homeAddress = models.TextField()
        phoneNumber = models.CharField(max_length=10)
        location = models.CharField()
        
def __str__(self):
    return self.name
    (args)
        