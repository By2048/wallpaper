from django.urls import path
from .views import IndexView, TagView

app_name = 'home'

urlpatterns = [
    path('tag/', TagView.as_view(), name='tag')
]
