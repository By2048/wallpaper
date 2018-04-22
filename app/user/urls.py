from django.urls import path
from user.views import RegisterView, UserinfoView

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('info/', UserinfoView.as_view(), name='info'),
]
