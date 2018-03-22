"""wallpaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from index.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('_tmp/', include('app._tmp.urls')),
    # path('category/', include('app.category.urls')),
    path('user/', include('app.user.urls')),
    path('', view=IndexView.as_view(), name='index'),
    # 使用 Django 默认的登陆模板
    path('user/', include('django.contrib.auth.urls')),
]
