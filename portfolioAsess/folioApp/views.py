from collections import UserList
from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from account.models import UserProfile


  

# HomeView  function
def HomeView(request):
    return render(request,template_name='kartoza-work/portfolioAsess/folioApp/templates/home/index.html',context={}) 
# Sign-up View Function
def SignUpView(request):
    Template = "/templates/sign-up/sign-up.html"
    return render(request,template_name=Template,context={}) 
# LoginView Function
def LoginView(request):
    Template = "/templates/login/login.html"
    return render(request,template_name=Template,context={}) 

# MapViewDetails Page
def MapView(request):
    Template = "/templates/MapDetail/userMapDetails.html"
    return render(request,template_name=Template,context={}) 

# UserDetailView Function
def User_DetailsView(request):
    Template = "/templates/accopunt/UserDetails/userDetails.html"
    return render(request,template_name=Template,context={}) 

# userEditDetailView Function
def User_EditDetailsView(request):
    Template = "/templates/accopunt/UserEditDetails/userEditDetails.html"
    return render(request,template_name=Template,context={})

# Listing Our Accounts stored in the Database:
# AccountDetailsListingView ==> Subclassed->(ListView) 
''' class ListAccountDetails(ListView):
    model = UserProfile
 '''

# Listing all Accounts in our TemplateView    
def ListAccounts(request):
    user = get_object_or_404(UserProfile)
    return render(request,template_name="/templates/account/List-Accounts.html",
            content_type={user})
    
