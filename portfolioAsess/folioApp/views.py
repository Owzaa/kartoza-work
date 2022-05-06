from ast import arg
from msilib.schema import ListView
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
    
    return render(request,"MapDetail/userMapDetails.html",context={}) 

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
        user = get_object_or_404()
        render(request,'List-Accounts.html',{'users':user})
    
""" 
Accessing all the data that has been
passed to the POST by our Form()

"""
def login(request):
    username = "Not yet logged in"
    
    if request.method == "POST":
    #GET: ourForm (request.POST): the posted form data
        LoginForm =ProfileForm(request.POST) 
    if LoginForm.is_valid():
        username =LoginForm.cleaned_data['username']
        
    else:
        LoginForm =userProfileForm()
    return render(request,"account/UserDetails/userDetails.html",{'username': username}) 
