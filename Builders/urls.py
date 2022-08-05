from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('builders', views.Builders.as_view())
]
