from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser

class MyUserCreationForm(UserCreationForm):

        class Meta(UserCreationForm):
                model = CustomUser
                fields = ('username', )

class MyUserChangeForm(UserChangeForm):

        class Meta(UserChangeForm):
                model = CustomUser
                fields = ('username',)

class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'picture', 'website', 'github', 'about', ]
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.TextInput(attrs={'readonly': 'readonly'})
        }
