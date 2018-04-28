# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from image.models import Image, Tag, Category
from user.models import Favorite


class DetailView(View):
    def get(self, request, image_id):
        if image_id == 0:
            data = {'message': '此图片不存在!'}
        else:
            image = Image.objects.get(pk=image_id)
            favorite = Favorite.objects.filter(user=request.user, image=image)
            if favorite:
                is_favorite = 'True'
            else:
                is_favorite = 'False'
            data = {
                'image_id': image_id,
                'name': image.name if image.name else image.id,
                'width': image.width,
                'height': image.height,
                'click': image.click,
                'show_width': image.width if image.width < 1300 else 1300,
                'show_height': image.height if image.width < 1300 else int(1300 * image.height / image.width),
                'description': image.description,
                'url': image.url,
                'tags': image.tags.all(),
                'all_categorys': Category.objects.all(),
                'categorys': image.categorys.all(),
                'is_favorite': is_favorite,
            }
        return render(request, 'image/detail.html', data)


def add_tag(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name', '')
        image_id = request.POST.get('image_id', 0)
        if tag_name == '' or image_id == 0:
            status = 'fail'
            message = '输入错误'
        else:
            tag = Tag.objects.filter(name=tag_name)
            image = Image.objects.get(pk=image_id)
            if tag:
                image.tags.remove(tag[0])
                status = 'fail'
                message = '此标签已经删除！'
            else:
                tag = Tag()
                tag.name = tag_name
                tag.user = request.user
                tag.save()
                image.tags.add(tag)
                status = 'success'
                message = '添加标签成功！'
        return JsonResponse({"status": status, "message": message})


def add_category(request):
    if request.method == 'POST':
        category_ids = request.POST.get('category_ids', '')
        category_ids = category_ids.strip(',')
        image_id = request.POST.get('image_id', 0)
        if category_ids == '' or image_id == 0:
            status = 'fail'
            message = '请先选择内容！'
        else:
            category_ids = category_ids.split(',')
            image = Image.objects.get(pk=image_id)
            image_categorts = image.categorys.all()
            status = 'success'
            message = ''
            for category_id in category_ids:
                category = Category.objects.get(pk=category_id)
                if category in image_categorts:
                    status = 'fail'
                    image.categorys.remove(category)
                    message += '此 ' + category.name + ' 已删除\n'
                else:
                    image.categorys.add(category)
                    status = 'success'
                    message = '添加 ' + category.name + ' 成功\n'
            message = message.rstrip('\n')

        return JsonResponse({"status": status, "message": message})


def test_view(request):
    images = ['']
    data = {'images': images}
    return render(request, 'image/test.html', data)
