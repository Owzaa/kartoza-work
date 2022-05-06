"""
Author: Olwethu Theo Nyondo
Project: Portfolio Application (Views.py)
Date: 06/05/2022
Published: https://github.com/Owzaa/repositry/

Book Refferenced(ISBN): Django Documentation
Version Release: 3.2.12.dev 
 
"""

from collections import UserList
from msilib.schema import ListView
from types import MemberDescriptorType
from django.http import HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required,permission_required
from account.models import UserProfile

  
  
"""
                         LIBRARY IMPORTS(DECORATORS)
                         
Imported 2 Decorators from our Library contrib.auth.decorators as per Requirement
from the ASSIGNMENT DOCUMENTATION
----------------------------------------------------------------------------------
                         AUTHORISATION DECORATORS:

@permission_required: This will check if user is permitted to ViewPage()
@login_required: This Checks if user logged in  to view or acess the Page()

"""


# HomeView  function
def HomeView(request):
    return render(request,'home/index.html',{}) 
# Sign-up View Function
def SignUpView(request):
    return render(request,"sign-up/sign-up.html",context={}) 
# LoginView Function
def LoginView(request):
    return render(request,"login/login.html",{}) 

""" 

                    MAP_PAGE()
           
@login_required decorator redirect user to login_url page if not Redirects
 to login page
 
@user.permission.View: only Auth_Admin can Assess this Page
"""

@login_required(login_url="/LoginView/")
def MapView(request):
    return render(request,"MapDetail/MapAccounts.html",context={}) 

# UserDetailView Function
@login_required(login_url="/LoginView/")
def ProfileDetailsView(request):
    return render(request,"account/UserDetails/userDetails.html",context={}) 

# userEditDetailView Function
@login_required(login_url="/LoginView/")
def ProfileEditDetailsView(request):
    return render(request,"account/UserEditDetails/userEditDetails.html",context={})

    
    

@login_required(login_url= 'LoginView')
@permission_required(perm='folioApp.view_choice', login_url='LoginView')
def ListAccounts(request):
    return render(request,'account/List-Accounts.html',{})
 


  
""" 
LOGIN / LOGOUT FUNCTIONS  

loginView - Log in User to our site
logout - log off User out of our site
-------------------------------------------------
LEGENDS: 

Assigned  m => 'Member' or USER object
--------------------------------------------------
LOGIN() FUNCTION

GET: username & password PARAMETERS_OBJECTS Then 
        use Request(param)
POST: Verify our User_logging details 
--------------------------------------------------
USER ACTIVITY 

request.Session : Activity Log
--------------------------------------------------
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
        del request.session['user_id']
    except KeyError:
        pass
    return render(request,'login/login.html')