from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

import os

from image.models import Category, Tag, Image, Carousel


class IndexView(View):
    def get(self, request):
        hot_images = Image.objects.all().order_by('click')[:10]

        if request.user.is_authenticated:
            recommend_images = []  # 推荐给用户的图片
        else:
            recommend_images = []

        carousel = Carousel.objects.all().order_by('index')
        carousel_images = []
        for item in carousel:
            carousel_images.append(item.image.url_thumb)

        return render(request, 'home/index.html', context={
            'hot_images': hot_images,
            'recommend_images': recommend_images,
            'carousel_images': carousel_images
        })


# class IndexView(LoginRequiredMixin, View):
#     login_url = '/user/login/'
#     redirect_field_name = 'next'
#     pass

class CategoryView(View):
    """分类视图
    根据分类的ID来显示分类下的图片
    """

    def get(self, request):
        all_category = Category.objects.all()
        category_id = request.GET.get('category_id', 1)
        category_images = Image.objects.filter(category__id=category_id)[:20]
        return render(request, 'home/category.html', context={
            'all_category': all_category,
            'category_image': category_images
        })


class TagView(View):
    def get(self, request):
        all_tag = Tag.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_tag, 10, request=request)

        tags = p.page(page)
        return render(request, 'home/tag.html', context={
            'tags': tags
        })


class HotView(View):
    def get(self, request):
        hot_images = Image.objects.all().order_by('click')[:30]
        return render(request, 'home/hot.html', context={
            'hot_images': hot_images
        })
