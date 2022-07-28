from django.urls import path
from Accounts import views

urlpatterns = [
    path('login/', views.login, name='user_login'),
    path('register/', views.register, name='user_register'),
    path('logout/', views.logout, name='user_logout')
]