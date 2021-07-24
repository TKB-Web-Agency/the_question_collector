from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
        path('', views.Questions.as_view(), name='homepage'),
        path('filter/<slug:slug>/', views.filter, name='filter_by'),
        path('question/<slug:slug>/', views.question_detail, name='question_detail'),
        path('add-new-question', views.add_new_question, name='add_new_question'),
        path('add-new-category', views.add_new_category, name='add_new_category'),
    ]
