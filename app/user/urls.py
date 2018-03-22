from django.urls import path
from user.views import RegisterView

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
