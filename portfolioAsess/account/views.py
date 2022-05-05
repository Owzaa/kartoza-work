from django.shortcuts import get_object_or_404,render
from django.contrib.auth.models import User
from django import login_required


@login_required
# filtering our user Database to list_view
def user_list(request):
    class Meta:
        model = User.
    users = User.objects.filter(is_active=True)
    return render (request,'account/List-Accounts.html',{'users':users})

#User Authentication check when a user is requeasting user_details
@login_required
def user_detail(request,username):
    user= get_object_or_404 (Username=username,is_active=True)
    return render(request,'account/UserDetails/userDetails.html',{
        'section': 'people',
        'user': user})