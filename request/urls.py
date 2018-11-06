from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assigned_requests/', views.assigned_request, name='assigned_requests'),
    path('main_donation_screen/<str:user_name>', views.main_donation, name='main_donation'),
    path('login/', views.login, name='login'),
    path('new_user/', views.new_user, name='/new_user/'),
    path('status/', views.status, name='/status/'),
    path('settings/', views.settings, name='/settings/'),
    path('new_donation/', views.new_donation, name='/new_donation/')
    ]

