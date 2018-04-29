# coding=utf-8
import logging

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from image.models import Category, Tag, Image, Carousel
from user.models import BlackHouse, UserProfile


class IndexView(View):
    def get(self, request):
        hot_images = Image.objects.all().order_by('click')[:16]

        if request.user.is_authenticated:
            recommend_images = []  # 推荐给用户的图片
        else:
            recommend_images = []

        carousel = Carousel.objects.all().order_by('index')
        carousel_images = []
        for item in carousel:
            carousel_images.append(item.image.url_thumb)

        item = {
            'id': 1234,
            'url': 'http://img.zcool.cn/community/0142135541fe180000019ae9b8cf86.jpg',
            'name': 'qwe.jpg',
            'width': 1024,
            'height': 768,
        }
        carousel_images = [item] * 3
        hot_images = [item] * 16
        recommend_images = [item] * 8

        return render(request, 'home/index.html', {
            'hot_images': hot_images,
            'carousel_images': carousel_images,
            'recommend_images': recommend_images,
        })


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


class BlackHouseView(View):
    def get(self, request):
        black_houses = BlackHouse.objects.all()
        return render(request, 'home/blackhouse.html', {'black_houses': black_houses})

    def post(self, request):
        name = request.POST.get('name', '')
        black_houses = []
        data = None
        if name != '':
            user_username = UserProfile.objects.filter(username__contains=name)
            user_nickname = UserProfile.objects.filter(nickname__contains=name)
            for user in user_nickname + user_username:
                _item = BlackHouse.objects.get(user=user)
                if _item not in black_houses:
                    black_houses.append(_item)
            data = {'black_houses': black_houses}
        else:
            data = {'message': '请输入查询信息!'}
        return render(request, 'home/blackhouse.html', data)


# @csrf_exempt
def test_ajax(request):
    """
    用户评分图片
    """
    if request.method == 'GET':
        return render(request, 'home/test_ajax.html')

    if request.method == 'POST':
        # id = request.POST.get('id', 0)
        user = request.user

        logging.error(user)
        pp = user.sex1
        logging.error(pp)
        logging.error('stop')
        return JsonResponse({"success": "23sdr123====7879789"})


@csrf_exempt
def serarch_image(request):
    images = []
    if request.method == 'POST':
        img_info = request.POST.get('img_info')
        try:
            img_id = int(img_info)
            images = Image.objects.get(pk=img_id)
        except ValueError:
            pass
