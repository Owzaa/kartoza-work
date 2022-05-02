from collections import UserList
from gc import get_objects
from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from account.models import UserProfile


  

# HomeView  function
def HomeView(request):
    Template = "folioApp/templates/home/index.html"
    return render(request,template_name=Template,context={}) 
# Sign-up View Function
def SignUpView(request):
    Template = "folioApp/templates/sign-up/sign-up.html"
    return render(request,template_name=Template,context={}) 
# LoginView Function
def LoginView(request):
    Template = "folioApp/templates/login/login.html"
    return render(request,template_name=Template,context={}) 

# MapViewDetails Page
def MapView(request):
    Template = "folioApp/templates/MapDetail/userMapDetails.html"
    return render(request,template_name=Template,context={}) 

# UserDetailView Function
def User_DetailsView(request):
    Template = "folioApp/templates/accopunt/UserDetails/userDetails.html"
    return render(request,template_name=Template,context={}) 

# userEditDetailView Function
def User_EditDetailsView(request):
    Template = "folioApp/templates/accopunt/UserEditDetails/userEditDetails.html"
    return render(request,template_name=Template,context={})

# Listing Our Accounts stored in the Database:
# AccountDetailsListingView ==> Subclassed->(ListView) 
''' class ListAccountDetails(ListView):
    model = UserProfile
 '''

# Listing all Accounts in our TemplateView    
def ListAccounts(request):
    user = get_object_or_404(UserProfile)
    return render(request,template_name="folioApp/templates/account/List-Accounts.html",
            content_type={user})
    
