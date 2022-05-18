from collections import UserList
from re import template
from webbrowser import get
from django.forms import fields_for_model
from django.shortcuts import get_object_or_404,render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserProfile


#   filtering our user Database to list_view
''' def user_list(request):
    model = UserProfile
        
    usersList = UserProfile.objects.get()
    return render (request,'account/List-Accounts.html',{'users':UserList}) '''

#   User Authentication check when a user is requeasting user_details
def user_detall(request):
    user= get_object_or_404 ()
    return render(request,'account/UserDetails/userDetails.html',{'user': user})

#user Edit Details form_validation()
class OwnerEditView(object):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OwnerEditView, self).form_valid(form)

#Edit class for user-details
class UserEditView(OwnerEditView):
    model = UserProfile 
    fields = fields_for_model
    success_url = reverse_lazy('user_detail')
    template_name = 'account/UserEditDetails/userEditDetails.html'