from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
        path('signup/', views.SignUpView.as_view(), name='signup'),
        path('profile/<str:author>', views.profile, name='profile'),
        path('edit-profile/<str:author>', views.edit_profile, name='edit_profile'),
        ]
