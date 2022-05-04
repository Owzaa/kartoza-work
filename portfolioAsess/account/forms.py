from django.forms import ModelForm
from .models import UserProfile

# user_Profile form Class for Sign-up & Sign-in page....
class userProfileForm(ModelForm):
    class Meta:
        model = UserProfile 
        fields = ['username','home_address',' phone_number','   location']

# Creating a form for sign-up
form= userProfileForm()


# Creating a Form to change userDetails on existing Database..
UserProfile = UserProfile.objects.get(pk=1)

# form instance
form = userProfileForm(instance=UserProfile)