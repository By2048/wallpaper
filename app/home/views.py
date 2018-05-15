# coding=utf-8
import logging
import random

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from image.models import Category, Tag, Image, Carousel
from user.models import BlackHouse, UserProfile


class IndexView(View):
    def get(self, request):

        image_num = 16

        all_image = Image.objects.all()

        hot_images = all_image.order_by('click')[:image_num]

        if request.user.is_authenticated:
            recommend_images = all_image.order_by('?')[:image_num]
        else:
            recommend_images = all_image.order_by('?')[:image_num]

        all_carousel = Carousel.objects.all().order_by('index')
        carousel_images = []
        for item in all_carousel:
            carousel_images.append(item.image)

        return render(request, 'home/index.html', {
            'hot_images': hot_images,
            'carousel_images': carousel_images,
            'recommend_images': recommend_images,
        })


def hot(request, category_id=0):
    all_category = Category.objects.all()
    page_categorys = Paginator(all_category, 15, request=request)
    category_page = request.GET.get('category_page', 1)
    categorys = page_categorys.page(category_page)

    if category_id == 0:
        all_images = Image.objects.all().order_by('click')
    else:
        all_images = Image.objects.filter(categorys__id=category_id).order_by('click')
    page_images = Paginator(all_images, 20, request=request)
    image_page = request.GET.get('image_page', 1)
    images = page_images.page(image_page)

    return render(request, 'home/hot.html', context={
        'category_id': category_id,
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
        'category_id': category_id,
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
    range_images = Image.objects.all().order_by('?')[:133]
    images = []
    max_width = 140
    for item in range_images:
        if item.width > max_width:
            width = max_width
            height = int(item.height * max_width / item.width)
        else:
            width = item.width
            height = item.height

        _item = {
            'url_thumb': item.url_thumb,
            'url': item.url,
            'width': width,
            'height': height,
        }
        images.append(_item)
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
def search(request):
    keyword = request.GET.get('keyword', '')

    if keyword == '':
        message = '请输入查询内容！'
        return render(request, 'home/search.html', {
            'message': message
        })

    # 以图片id进行搜索
    img_id = ''
    try:
        img_id = int(keyword)
    except ValueError:
        pass
    finally:
        if isinstance(img_id, int):
            if len(str(img_id)) >= 5:
                search_images = Image.objects.filter(id=img_id)
                if search_images:
                    return render(request, 'home/search.html', {
                        'images': search_images,
                        'keyword': keyword,
                        'message': '无查询内容！'
                    })

    all_cateory = Category.objects.all()
    for category in all_cateory:
        if category.name.lower() == keyword.lower():
            search_images = Image.objects.filter(categorys__id=category.id)
            page_images = Paginator(search_images, 25, request=request)
            image_page = request.GET.get('image_page', 1)
            images = page_images.page(image_page)

            return render(request, 'home/search.html', {
                'images': images,
                'image_page': image_page,
                'keyword': keyword
            })

    all_tag = Tag.objects.all()
    for tag in all_tag:
        if tag.name.lower() == keyword.lower():
            search_images = Image.objects.filter(tags=tag)
            page_images = Paginator(search_images, 25, request=request)
            image_page = request.GET.get('image_page', 1)
            images = page_images.page(image_page)

            return render(request, 'home/search.html', {
                'images': images,
                'image_page': image_page,
                'keyword': keyword
            })

    message = '没有搜索到内容,随机展示50张图片！'
    search_images = Image.objects.order_by('?')[:50]
    page_images = Paginator(search_images, 25, request=request)
    image_page = request.GET.get('image_page', 1)
    images = page_images.page(image_page)

    return render(request, 'home/search.html', {
        'message': message,
        'images': images,
        'keyword': keyword
    })
