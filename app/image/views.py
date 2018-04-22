# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from image.models import Image


def detail_view(request, image_id):
    if image_id == 0:
        data = {'message': '此图片不存在!'}
    else:
        image = Image.objects.get(pd=image_id)
        data = {'image': image}
    return render(request, 'image/detail.html', data)
