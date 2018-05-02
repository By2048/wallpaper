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


def hot(request, category_id=0):
    all_category = Category.objects.all()
    page_categorys = Paginator(all_category, 15, request=request)
    category_page = request.GET.get('category_page', 0)
    categorys = page_categorys.page(category_page)

    if category_id == 0:
        all_images = Image.objects.all().order_by('click')
    else:
        all_images = Image.objects.filter(categorys__id=category_id).order_by('click')
    page_images = Paginator(all_images, 20, request=request)
    image_page = request.GET.get('image_page', 1)
    images = page_images.page(image_page)

    return render(request, 'home/hot.html', context={
        'category_id':category_id,
        'image_page': image_page,
        'category_page': category_page,
        'categorys': categorys,
        'images': images
    })


def category(request, category_id=1):
    all_category = Category.objects.all()
    page_categorys = Paginator(all_category, 15, request=request)
    category_page = request.GET.get('category_page', 1)
    categorys = page_categorys.page(category_page)

    all_images = Image.objects.filter(categorys__id=category_id)
    page_images = Paginator(all_images, 20, request=request)
    image_page = request.GET.get('image_page', 1)
    images = page_images.page(image_page)

    return render(request, 'home/category.html', {
        'category_id':category_id,
        'image_page': image_page,
        'category_page': category_page,
        'categorys': categorys,
        'images': images
    })


def tag(request, tag_id=1):
    all_tag = Tag.objects.all()

    page_tags = Paginator(all_tag, 15, request=request)
    tag_page = request.GET.get('tag_page', 1)
    tags = page_tags.page(tag_page)

    all_images = Image.objects.filter(tags__id=tag_id)
    page_images = Paginator(all_images, 20, request=request)
    image_page = request.GET.get('image_page', 1)
    images = page_images.page(image_page)

    return render(request, 'home/tag.html', {
        'tag_page': tag_page,
        'image_page': image_page,
        'tags': tags,
        'images': images,
    })


def range(request):
    item = {
        'small': 'http://photopile-js.com/demo/images/thumbs/22.jpg',
        'big': 'http://photopile-js.com/demo/images/fullsize/08.jpg',
        'width': '84',
        'height': '60',
    }
    images = [item] * (168 - 35)
    return render(request, 'home/range.html', {'images': images})


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
