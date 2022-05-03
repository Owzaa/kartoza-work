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
from django.urls import path
from folioApp.views import HomeView,SignUpView,LoginView,MapView,User_DetailsView,User_EditDetailsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='HomeView'),
    path('sign-up/', SignUpView, name='sign-up'),
    path('login/', LoginView, name='login'),
    path('user-Details/', User_DetailsView, name='user-details'),
    path('user-Edit-Details/', User_EditDetailsView, name='user-edit-details'),
    path('MapDetails/', MapView, name='map-details')


]
