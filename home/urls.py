from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
        path('', views.Questions.as_view(), name='homepage'),
        path('<slug:slug>/', views.QuestionDetail.as_view(), name='question_detail'),
    ]
