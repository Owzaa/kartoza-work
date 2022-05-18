from django import forms
from django.forms import ModelForm
from account.models import UserProfile
from account.views import user_detail
from account.views import user_list

# user_Profile form Class for Sign-up & Sign-in page....
class userProfileForm(ModelForm):
    class Meta:
        model = UserProfile 
        fields = ['firstName','lastName','username','homeAddress','phoneNumber','location']

# Creating a form for sign-up
form= userProfileForm()


# Creating a Form to change userDetails on existing Database..
# form instance
form = userProfileForm(instance=UserProfile)

# ProfileForm for UserProfile Registration
class ProfileForm(forms.Form):
    class Meta:
        model=UserProfile
        
    firstName = forms.ChoiceField(max_length=30)
    lastName=forms.CharField(max_length=100)   
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    home_address = forms.CharField(widget=forms.Textarea())
    phone_number = forms.CharField(max_length=10)
    location = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())

