from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('rest/login', views.user_login, name='user_login')
]