from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rest/addshape', views.addshape, name='addshape'),
    path('rest/getshapes', views.getshapes, name='getshapes'),
    path('rest/getshapelist', views.getshapelist, name='getshapelist'),
    path('rest/getallshape', views.getallshape, name='getallshape'),
    path('rest/getoneshape', views.getoneshape)
]