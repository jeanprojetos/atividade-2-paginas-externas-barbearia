# gerenciar_barbearia/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('barbearia/', views.barbearia_view, name='barbearia'),
    path('agendamento/', views.agendamento_view, name='agendamento'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
]