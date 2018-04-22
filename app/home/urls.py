# coding=utf-8
from django.urls import path

from home.views import IndexView, TagView, BlackHouseView
from home.views import test_ajax

app_name = 'home'

urlpatterns = [
    path('tag/', TagView.as_view(), name='tag'),
    path('blackhouse/', BlackHouseView.as_view(), name='blackhouse'),
    path('test_ajax/', test_ajax, name='test_ajax'),
]
