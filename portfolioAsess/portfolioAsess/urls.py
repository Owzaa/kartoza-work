"""portfolioAsess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from folioApp.views import HomeView,logout, ListAccounts,SignUpView,LoginView,MapView,ProfileEditDetailsView,ProfileDetailsView

"""url patterns Views functions
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^account/', include('account.urls', app_name='account')),
    path('', HomeView, name='HomeView'),
    path('sign-up/', SignUpView, name='SignUpView'),
    path('login/', LoginView, name='LoginView'),
    path('logout/', logout, name='logout'),
    path('Profile-Details/', ProfileDetailsView, name='ProfileDetailsView'),
    path('Edit-Profile-Details/', ProfileEditDetailsView, name='ProfileEditDetailsView'),
    path('MapDetails/', MapView, name='MapDetails'),
    path('All-Accounts/', ListAccounts, name='ListAccounts')
]
