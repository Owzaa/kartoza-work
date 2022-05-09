from django.shortcuts import get_object_or_404,render
from django.contrib.auth.models import User
from .models import UserProfile


#   filtering our user Database to list_view
def user_list(request):
    class Meta:
        model = UserProfile
    users = UserProfile.objects.filter(is_active=True)
    return render (request,'account/List-Accounts.html',{'users':users})

#   User Authentication check when a user is requeasting user_details
def user_detail(request):
    user= get_object_or_404 (is_active=True)
    return render(request,'account/UserDetails/userDetails.html',{})



