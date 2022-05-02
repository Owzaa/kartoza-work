from msilib.schema import ListView
from django.shortcuts import render
from account.models import UserProfile




# HomeView  function
def HomeView(request):
    Template = "portfolioAsess/templates/home/"
    return render(request,template_name=Template,context_type={}) 
# Sign-up View Function
def SignUpView(request):
    Template = "portfolioAsess/templates/sign-up/"
    return render(request,template_name=Template,context={}) 
# LoginView Function
def Loginiew(request):
    Template = "portfolioAsess/templates/login/"
    return render(request,template_name=Template,context={}) 

# MapViewDetails Page
def MapView(request):
    Template = "portfolioAsess/templates/MapDetail/"
    return render(request,template_name=Template,context={}) 

# UserDetailView Function
def UserDetailsView(request):
    Template = "portfolioAsess/templates/accopunt/UserDetails/"
    return render(request,template_name=Template,context={}) 

# userEditDetailView Function
def UserEditDetailsView(request):
    Template = "portfolioAsess/templates/accopunt/UserEditDetails/"
    return render(request,template_name=Template,context={})

# Listing Our Accounts stored in the Database:
# AccountDetailsListingView ==> Subclassed->(ListView) 
class ListAccountDetails(ListView):
    model = UserProfile
