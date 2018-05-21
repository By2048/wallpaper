from django.urls import path

from user.views import \
    RegisterView, \
    UserinfoView, \
    rating_image, \
    add_favorite, \
    sign_in, \
    add_coin, \
    favorite, \
    Recharge, \
    ReleaseView, \
    ReleaseAdminView

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('info/', UserinfoView.as_view(), name='info'),
    path('rating_image/', rating_image, name='rating_image'),
    path('add_favorite/', add_favorite, name='add_favorite'),
    path('add_coin/', add_coin, name='add_coin'),
    path('sign_in/', sign_in, name='sign_in'),
    path('favorite/', favorite, name='favorite'),
    path('favorite/<int:category_id>/', favorite, name='favorite'),
    path('recharge/', Recharge.as_view(), name='recharge'),
    path('release/', ReleaseView.as_view(), name='release'),
    path('release_admin/', ReleaseAdminView.as_view(), name='release_admin'),
]
