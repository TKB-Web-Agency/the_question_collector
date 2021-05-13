from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
        path('', views.Questions.as_view(), name='homepage'),
        path('<slug:slug>/', views.QuestionDetail.as_view(), name='question_detail'),
        path('add-new-question', views.add_new_question, name='add_new_question'),
    ]
