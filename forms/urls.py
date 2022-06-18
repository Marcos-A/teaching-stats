from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'forms'
urlpatterns = [
    path('user_checking/', views.user_checking, name='user_checking'),
    path('school_form/', views.school_evaluation, name='school_evaluation'),
    path('counselor_form/', views.counseling_evaluation, name='counseling_evaluation'),
    path('subject_form/', views.subject_evaluation, name='subject_evaluation'),
    path('recorded_response/', views.recorded_response, name='recorded_response'),
    path('unidentified_user/', views.unidentified_user, name='unidentified_user'),
    path('empty_survey/', views.empty_survey, name='empty_survey'),
    path('wrong_email<str:user_email>/', views.wrong_email, name='wrong_email'),
    path('not_enrolled<str:user_email>/', views.not_enrolled, name='not_enrolled'),
    path('duplicated_answer<str:user_email>/', views.duplicated_answer, name='duplicated_answer'),
]
