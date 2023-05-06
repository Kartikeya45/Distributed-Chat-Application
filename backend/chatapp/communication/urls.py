from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('contacts/', views.contacts, name="contacts"),
]