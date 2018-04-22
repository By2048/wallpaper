# coding=utf-8
from django.urls import path
from image.views import DetailView

app_name = 'image'

urlpatterns = [
    path('detail/<int:id>', DetailView.as_view(), name='image_detail'),
]
