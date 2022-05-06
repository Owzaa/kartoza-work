from ast import arg
from msilib.schema import ListView
from types import MemberDescriptorType
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from account.models import UserProfile
from account.forms import ProfileForm
from account.forms import userProfileForm
  

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
    
    return render(request,"MapDetail/MapDetails.html",context={}) 

# UserDetailView Function
def ProfileDetailsView(request):
    return render(request,"account/UserDetails/userDetails.html",context={}) 

# userEditDetailView Function
def ProfileEditDetailsView(request):
    return render(request,"UserEditDetails/userEditDetails.html",context={})

# Listing Our Accounts stored in the Database:
# AccountDetailsListingView ==> Subclassed->(ListView) 
# class ListAccountDetails(ListView):
#     model = UserProfile
# Listing all Accounts in our Database to our HTML TemplateView    
def ListAccounts(request):
     return   render(request,'account/List-Accounts.html',{})
    
""" 
This View logs in a Mmeber of the SIte
LEGEND: 
m => Member


Login / logout Views()  Session=> activity 
by showing who and when on the admin page
"""
def login(request):
    m = MemberDescriptorType.objects.get(username=request.POST['username'])
    
    if m.password == request.POST['password']:
        #Session Activity Log Request for Our Admin Log HISTORY
        request.session['member_id'] = m.id
        return HttpResponse('Welcome You are Logged in!') 
    # If ERROR    
    else:
        return HttpResponse("Your Username and Password didn't match.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out")