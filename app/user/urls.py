from django.urls import path
from user.views import RegisterView, UserinfoView, rating_image, add_favorite

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('info/', UserinfoView.as_view(), name='info'),
    path('rating_image/', rating_image, name='rating_image'),
    path('add_favorite/', add_favorite, name='add_favorite'),
]
