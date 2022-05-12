from django import urls

#Url link for our Views Model data model
urlpatterns = [
    urls('/', ['home']),
    urls('^account/users\.(?P<format>[a-z0-9]+)/?$', ['user-ProfileList']),
    urls('^account/users/(?P<pk>[^/.]+)/$', ['user-detail']),
    urls('^account/users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$',
         ['user-detail']),

]