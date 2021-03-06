from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import CustomUser

class MyUserAdmin(UserAdmin):
        add_form = MyUserCreationForm
        form = MyUserChangeForm
        model = CustomUser
        list_display = ['username', 'website']
        fieldsets = UserAdmin.fieldsets + (
                (None, {'fields': ('website', 'picture', 'about', 'uuid' )}),
                ) #this will allow to change these fields in admin module


admin.site.register(CustomUser, MyUserAdmin)
