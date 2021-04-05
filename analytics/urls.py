from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'analytics'

urlpatterns = [
    # path('resultats/', TemplateView.as_view(template_name="analytics/index.html"), name='analytics_homepage'),
    path('staff_checking/', views.staff_checking, name='staff_checking'),
    path('school_analytics/', views.school_analytics, name='school_analytics'),
    path('counseling_analytics/', views.counseling_analytics, name='counseling_analytics'),
    path('subject_analytics/', views.subject_analytics, name='subject_analytics'),
    path('adm_analytics/', views.adm_analytics, name='adm_analytics'),
    path('inf_analytics/', views.inf_analytics, name='inf_analytics'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('unidentified_staff/', views.unidentified_staff, name='unidentified_staff'),
    path('not_authorized<str:user_email>/', views.not_authorized, name='not_authorized'),
]

