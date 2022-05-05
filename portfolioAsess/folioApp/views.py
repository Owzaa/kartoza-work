from collections import UserList
from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render

from account.models import UserProfile

  

# HomeView  function
def HomeView(request):
    return render(request,'home/index.html',{}) 
# Sign-up View Function
def SignUpView(request):
    return render(request,"sign-up/sign-up.html",context={}) 
# LoginView Function
def LoginView(request):
    return render(request,"login/login.html",{}) 

# MapViewDetails Page
def MapView(request):
    
    return render(request,"MapDetail/userMapDetails.html",context={}) 

# UserDetailView Function
def ProfileDetailsView(request):
    return render(request,"account/UserDetails/userDetails.html",context={}) 

# userEditDetailView Function
def ProfileEditDetailsView(request):
    return render(request,"UserEditDetails/userEditDetails.html",context={})

# Listing Our Accounts stored in the Database:
# AccountDetailsListingView ==> Subclassed->(ListView) 
''' class ListAccountDetails(ListView):
    model = UserProfile
 '''

# Listing all Accounts in our Database to our HTML TemplateView    
class ListAccounts(ListView):
    user = get_object_or_404(UserProfile)
    render(ListView,'List-Accounts.html',{'users':user})
    
