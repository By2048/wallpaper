# coding=utf-8
from django.urls import path

from home.views import BlackHouseView, category, tag, range, hot

from home.views import test_ajax

app_name = 'home'

urlpatterns = [
    path('blackhouse/', BlackHouseView.as_view(), name='blackhouse'),
    path('test_ajax/', test_ajax, name='test_ajax'),
    path('category/', category, name='category'),
    path('category/<int:category_id>/', category, name='category'),
    path('tag/', tag, name='tag'),
    path('tag/<int:tag_id>/', tag, name='tag'),
    path('range/', range, name='range'),

    path('hot/', hot, name='hot'),
    path('hot/<int:category_id>/', hot, name='hot'),
]
