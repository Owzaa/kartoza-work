from django.db import models
from django.contrib.auth.models import User

# User Account Model:
class UserProfile(models.Model):
        username = models.OneToOneField(User, on_delete=models.CASCADE)
        homeAddress = models.TextField()
        phoneNumber = models.CharField(max_length=12)
        location = models.CharField(max_length=200) 
              
        def __str__(self):
            return self.name

        