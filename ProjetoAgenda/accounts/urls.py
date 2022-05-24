from django.urls import path
from . import views

"""
URLs do app accounts.
Exemplo:
 >> accounts/ 
 >> accounts/login/ 
 >> accounts/TelaInicial/ 
 >> accounts/register/ 
 >> accounts/dashboard/ 
"""
urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('TelaInicial/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]