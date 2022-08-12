from turtle import home
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bin', views.bin, name='bin'),
    path('single', views.single, name='single'),
    path('create', views.create, name='create'),

]

