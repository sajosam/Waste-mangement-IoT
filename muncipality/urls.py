
from turtle import home
from django.urls import path
from . import views


urlpatterns = [
    path('bin', views.bin, name='bin'),
    path('createbin', views.createbin, name='createbin'),
    # path('single', views.single, name='single'),
    path('create', views.createbin, name='create'),


]
