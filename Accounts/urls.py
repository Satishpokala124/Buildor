from django.urls import path

from Accounts import views

urlpatterns = [
    path('login/', views.login,),
    path('register/', views.register),
    path('logout/', views.logout)
]