from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'forms'
urlpatterns = [
    path('form/', views.school_evaluation, name='school_evaluation'),
    path('recorded_response/', views.recorded_response, name='recorded_response'),
    path('wrong_email/', views.wrong_email, name='wrong_email'),
    path('not_enrolled/', views.not_enrolled, name='not_enrolled'),
    path('duplicated_answer', views.duplicated_answer, name='duplicated_answer'),
    path('user_checking/', views.user_checking, name='user_checking'),
]