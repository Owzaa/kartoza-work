from django.shortcuts import get_object_or_404,render
from django.contrib.auth.models import User
from django import ajax_required,login_required

#@login_required library
@ajax_required
@login_required
# filtering our user Database to list_view
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render (request,'account/List-Accounts.html',{'section':'people','users': users})

#User Authentication check when requeasting user_details
@login_required
def user_detail(request,username):
    user= get_object_or_404 (Username=username,is_active=True)
    return render(request,'account/UserDetails/userDetails.html',{
        'section': 'people',
        'user': user})