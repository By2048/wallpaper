from django.shortcuts import render
from django.http import HttpResponse

from wallpaper import settings

# Create your views here.


def index(request):
    # E:\MyGit\Wallpaper_Website\wallpaper
    return HttpResponse(settings.BASE_DIR)