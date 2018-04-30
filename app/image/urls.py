# coding=utf-8
from django.urls import path
from image.views import DetailView, add_tag, add_category

app_name = 'image'

urlpatterns = [
    path('detail/<int:image_id>/', DetailView.as_view(), name='detail'),
    path('add_tag/', add_tag, name='add_tag'),
    path('add_category/', add_category, name='add_category'),
]
