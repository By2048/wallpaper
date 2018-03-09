from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

app_name='_tmp'
urlpatterns = [
    path('index/', views.index, name='index'),
]