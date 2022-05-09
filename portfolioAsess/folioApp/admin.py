from django.contrib import admin
from account.models import UserProfile
from django.contrib.auth.models import User

#list display on adminProfile
# class UserProfile(admin.ModelAdmin):
#     list_display = ()




# Registering User Model from Accounts App
# to our Admin.site models here.
admin.site.register(UserProfile)
