from django import forms
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

# ProfileForm for UserProfile Registration
class ProfileForm(forms.Form):
    class Meta:
        model=userProfileForm
        
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    home_address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=10)
    location = forms.CharField()
    
def __init__(self):
    return self.username