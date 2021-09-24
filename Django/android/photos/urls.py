from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:image_name>', views.getPhoto, name='')
]