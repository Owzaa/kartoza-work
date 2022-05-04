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
    return render(request,"/login/login.html",{}) 

# MapViewDetails Page
def MapView(request):
    Template = "MapDetail/userMapDetails.html"
    return render(request,template_name=Template,context={}) 

# UserDetailView Function
def User_DetailsView(request):
    Template = "accopunt/UserDetails/userDetails.html"
    return render(request,template_name=Template,context={}) 

# userEditDetailView Function
def User_EditDetailsView(request):
    Template = "accopunt/UserEditDetails/userEditDetails.html"
    return render(request,template_name=Template,context={})

# Listing Our Accounts stored in the Database:
# AccountDetailsListingView ==> Subclassed->(ListView) 
''' class ListAccountDetails(ListView):
    model = UserProfile
 '''

# Listing all Accounts in our TemplateView    
def ListAccounts(request):
    user = get_object_or_404()
    return render(request,'account/List-Accounts.html',{})
    
