# coding=utf-8
from django.urls import path

from tmp.views import upload_files

app_name = 'tmp'

urlpatterns = [
    path('upload_files/', upload_files, name='upload_files'),
]
