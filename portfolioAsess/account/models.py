from pickletools import long1
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse_lazy

# UserProfile Model:
class UserProfile(models.Model):
        username = models.OneToOneField(User, on_delete=models.CASCADE)
        homeAddress = models.TextField()
        phoneNumber = models.CharField(max_length=12)
        location = models.CharField(max_length=200) 
# return userProfile name as string    
      

# @receiver Send/Receive Signals for our object 
# Instances when save button is clicked               

@receiver (post_save,sender=User)
def create_user(self,sender,instance,created, **kwargs):
    if created:
       create_user_profile(instance=User)


#@receiver saving our userProfile instance object     
@receiver (post_save,sender=User)
def create_user_profile(instance,self, **kwargs):
        instance.self.save() 


def __str__(self):
        return self.username