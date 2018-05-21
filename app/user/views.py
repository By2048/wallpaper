# coding=utf-8
import os
import json
import logging
import datetime
import hashlib

import wallpaper.settings as settings

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from pure_pagination import Paginator

from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from PIL import Image as PImage

from user.forms import RegisterForm
from user.models import UserProfile, Favorite, SignIn, Coin
from image.models import Image, Rating, Tag, Category


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        next = request.GET.get('next', '')
        return render(request, 'user/register.html', {'register_form': register_form, 'next': next})

    def post(self, request):
        next = request.POST.get('next', '')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Subject here',
                'Here is the message.',
                'user_admin@email.com',
                [form.email],
                fail_silently=False,
            )
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            register_form = RegisterForm()
            return render(request, 'user/register.html', {'register_form': register_form, 'next': next})


def add_favorite(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id', 0)
        image_id = int(image_id)
        if image_id == 0:
            status = 'fail'
            message = '图片ID错误！'
        else:
            image = Image.objects.get(pk=image_id)
            favorite = Favorite.objects.filter(user=request.user, image=image)
            if favorite:
                favorite.delete()
                status = 'success',
                message = '已取消收藏！'
            else:
                favorite = Favorite()
                favorite.image = image
                favorite.user = request.user
                favorite.save()
                status = 'success',
                message = '添加收藏成功！'
        return JsonResponse({"status": status, "message": message})


def add_coin(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id', 0)
        if image_id == 0:
            status = 'fail'
            message = '图片ID错误！'
        else:
            image = Image.objects.get(pk=image_id)
            user = request.user
            coin = Coin.objects.filter(user=request.user, image=image)

            if coin:
                coin.delete()
                user.coin += 1
                user.save()
                status = 'success',
                message = '已取消投币！'
            else:
                if user.coin < 1:
                    status = 'fail',
                    message = '硬币不足！'
                else:
                    user.coin -= 1
                    user.save()
                    coin = Coin()
                    coin.image = image
                    coin.user = request.user
                    coin.save()
                    status = 'success',
                    message = '投币成功！'
        return JsonResponse({"status": status, "message": message})


def rating_image(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id', 0)
        star = request.POST.get('star', 0)
        star = float(star)
        if image_id == 0 or star == 0:
            status = 'fail'
            message = '传输数据失败'
        elif star == float(-1):
            status = 'success'
            user = request.user
            image = Image.objects.get(pk=image_id)
            rating = Rating.objects.filter(user=user, image=image)
            if rating:
                rating.delete()
                message = '取消评分成功！'
            else:
                message = '尚未评分！'
        else:
            user = request.user
            image = Image.objects.get(pk=image_id)
            rating = Rating.objects.filter(user=user, image=image)
            if rating:
                rating.update(star=star)
                status = 'success'
                message = '重新评分成功！'
            else:
                rating = Rating()
                rating.user = request.user
                rating.image = Image.objects.get(pk=image_id)
                rating.star = star
                rating.save()
                status = 'success'
                message = '添加评分成功！'
        return JsonResponse({"status": status, "message": message})


class SentMessage(LoginRequiredMixin, View):
    def post(self, request):
        from_user = request.POST.get('from_user_id', 0)
        to_user = request.POST.get('to_user_id', 0)


class UserinfoView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, 'user/info.html', {'user': user})

    def post(self, request):
        user = request.user
        nickname = request.POST.get('nickname', '')
        picture = request.FILES.get('picture', '')
        email = request.POST.get('email', '')
        sex = request.POST.get('sex', '')
        birthday = request.POST.get('birthday', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('address', '')
        information = request.POST.get('information', '')

        if nickname != '':
            user.nickname = nickname
        if picture:
            upload_path = os.path.join(settings.MEDIA_ROOT, 'user_pic')
            md5 = hashlib.md5()
            for chrunk in picture.chunks():
                md5.update(chrunk)

            type = os.path.splitext(picture.name)[-1]
            md5_name = md5.hexdigest()

            img_path = os.path.join(upload_path, md5_name) + type

            img = open(img_path, 'wb')
            for chrunk in picture.chunks():
                img.write(chrunk)
            img.close()

            url = os.path.join(settings.MEDIA_URL, 'user_pic', md5_name) + type

            user.picture = url

        if email != '':
            user.email = email
        if sex != '':
            user.sex = sex
        if birthday != '':
            user.birthday = birthday
        if address != '':
            user.address = address
        if phone != '':
            user.phone = phone
        if information != '':
            user.information = information

        user.save()

        return render(request, 'user/info.html', {'user': user})


class Recharge(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, 'user/recharge.html', {'user': user})

    def post(self, request):
        user = request.user
        coin_num = request.POST.get('coin_num', '')
        if coin_num == '':
            status = 'fail'
            message = '未输入内容！'
        else:
            coin_num = int(coin_num)
            if coin_num > 0:
                if user.is_active == True:
                    user.coin += coin_num
                    user.save()
                    status = 'success'
                    message = '充值成功！'
                else:
                    status = 'fail'
                    message = '用户未激活'
            else:
                message = '输入的硬币数量错误'
        return render(request, 'user/recharge.html', {'user': user, 'status': status, 'message': message})


def sign_in(request):
    """用户签到"""

    if request.method == 'POST':
        user = request.user
        now_date = datetime.datetime.now().date()
        sign_in = SignIn.objects.filter(user=user, date_add__gte=now_date)

        if user.is_active == False:
            status = 'fail'
            message = '用户未激活'
        elif sign_in:
            status = 'fail'
            message = '已经签到 签到时间为  ' + sign_in[0].date_add.strftime('%I:%M:%S %p')
        else:
            user.coin += 1
            user.sign_in_times += 1
            user.save()
            sign_in = SignIn()
            sign_in.user = user
            sign_in.save()
            status = 'success'
            message = '签到成功 签到时间为  ' + datetime.datetime.now().strftime('%I:%M:%S %p')
        return JsonResponse({'status': status, 'message': message})


@login_required
def favorite(request, category_id=0):
    # todo 查询优化
    user = request.user

    all_category = []
    all_image = []

    all_favorite = Favorite.objects.filter(user=user).order_by('-date_add')

    if len(all_favorite) == 0:
        return render(request, 'user/favorite.html', {
            'message': '暂无收藏!'
        })

    for favorite in all_favorite:
        image = Image.objects.get(pk=favorite.image.id)
        all_image.append(image)

    for image in all_image:
        for item in image.categorys.all():
            if item not in all_category:
                all_category.append(item)

    for category in all_category:
        cnt = 0
        for item in all_image:
            if category in item.categorys.all():
                cnt += 1
        category.count = cnt

    page_categorys = Paginator(all_category, 15, request=request)
    category_page = request.GET.get('category_page', 1)
    categorys = page_categorys.page(category_page)

    if category_id == 0:
        category = all_category[0]
    else:
        category = Category.objects.get(pk=category_id)

    _all_image = []
    for item in all_image:
        if category in item.categorys.all():
            _all_image.append(item)

    page_images = Paginator(_all_image, 20, request=request)
    image_page = request.GET.get('image_page', 1)
    images = page_images.page(image_page)

    return render(request, 'user/favorite.html', {
        'category_id': category_id,
        'image_page': image_page,
        'category_page': category_page,
        'categorys': categorys,
        'images': images
    })


# 作者发布图片
class ReleaseView(LoginRequiredMixin, View):
    def get(self, request):
        all_category = Category.objects.all()

        return render(request, 'user/release.html', {
            'all_category': all_category,
        })

    def post(self, request):
        all_category = Category.objects.all()
        images = request.FILES.getlist("image_file")
        categorys = request.POST.getlist("image_category")
        description = request.POST.get("image_description")
        tags = request.POST.get('image_tag', '')
        if tags != '' and tags.find('|'):
            tags = tags.split('|')

        all_file_url = []
        upload_path = os.path.join(settings.MEDIA_ROOT, 'release')
        upload_path_thumb = os.path.join(settings.MEDIA_ROOT, 'release_thumb')
        if images:
            for image in images:
                md5 = hashlib.md5()
                for chrunk in image.chunks():
                    md5.update(chrunk)
                name = image.name
                size = image.size
                type = os.path.splitext(name)[-1]
                md5_name = md5.hexdigest()

                img_path = os.path.join(upload_path, md5_name) + type
                img_path_thumb = os.path.join(upload_path_thumb, md5_name) + type

                url = os.path.join(settings.MEDIA_URL, 'release', md5_name) + type
                url_thumb = os.path.join(settings.MEDIA_URL, 'release_thumb', md5_name) + type

                all_file_url.append(url_thumb)

                img = open(img_path, 'wb')
                for chrunk in image.chunks():
                    img.write(chrunk)
                img.close()

                pimg = PImage.open(img_path)

                _img = Image()
                _img.user = request.user
                _img.name = name
                _img.description = description
                _img.url = url
                _img.url_thumb = url_thumb
                _img.size = size
                _img.width, _img.height = pimg.size
                _img.type = type.strip('.')
                _img.save()

                pimg.thumbnail((300, 300))
                pimg.save(img_path_thumb)

                if len(categorys) == 0:
                    category = Category.objects.get(name='Other')
                    category.count += 1
                    category.save()
                    _img.categorys.add(category)
                else:
                    for category_id in categorys:
                        category = Category.objects.get(pk=category_id)
                        category.count += 1
                        category.save()
                        _img.categorys.add(category)

                if len(tags) == 0:
                    tag = Tag.objects.get(name='Other')
                    tag.count += 1
                    tag.save()
                    _img.tags.add(tag)

                else:
                    for tag_name in tags:
                        tag = None
                        try:
                            tag = Tag.objects.get(name=tag_name)
                        except:
                            pass
                        if tag:
                            tag.count += 1
                            tag.save()
                            _img.tags.add(tag)
                        else:
                            tag = Tag()
                            tag.name = tag_name
                            tag.user = request.user
                            tag.count += 1
                            tag.save()
                            _img.tags.add(tag)
                _img.save()

            return render(request, 'user/release.html', {
                'message': '文件上传成功！',
                'all_file_url': all_file_url,
                'all_category': all_category,
            })
        else:
            return render(request, 'user/release.html', {
                'message': '请先选择需要上传的文件！',
                'all_category': all_category,
            })


class ReleaseAdminView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        images = Image.objects.filter(user=user).order_by('-date_add')
        return render(request, 'user/release_admin.html', {'images': images})

    def post(self, request):
        # todo 目前一次只处理一条数据,后续改为批量删除
        user = request.user
        image_id = request.POST.get('image_id')
        image = Image.objects.get(pk=image_id)
        status = 'fail'
        message = '删除失败！'
        if image.user == user:
            for category in image.categorys.all():
                category.count -= 1
                category.save()
            try:
                for tag in image.tags:
                    tag.count -= 1
                    tag.save()
            except:
                pass
            image.delete()
            status = 'success'
            message = '删除成功！'
        return JsonResponse({'status': status, 'message': message})
