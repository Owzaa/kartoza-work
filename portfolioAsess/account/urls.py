from django import urls, views

#Url link for our Views Model data model
urlpatterns = [
    
    # User views
    urls(r'^$', views.user_list,name="user_list"),
    urls(r'^$',views.user_detail,name='user-detail'),
    urls('^account/users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$',
         ['user-detail']),

]