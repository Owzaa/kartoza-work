from django.shortcuts import get_object_or_404,render
from django.contrib.auth.models import User


#@login_required library


# filtering our user Database to list_view
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render (request,'account/List-Accounts.html',{'section':'people','users': users})

#User Authentication check when requeasting user_details
def user_detail(request,username):
    user= get_object_or_404 (Username=username,is_active=True)
    return render(request,'account/UserDetails/userDetails.html',{
        'section': 'people',
        'user': user})