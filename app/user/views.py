# coding=utf-8
import json
import logging

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from user.forms import RegisterForm
from user.models import UserProfile
from user.models import Favorite
from user.models import Comment
from image.models import Image
from image.models import Rating


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


@csrf_exempt
class AddFavorite(LoginRequiredMixin, View):
    def post(self, request):
        image_id = request.POST.get('image_id', 0)
        if image_id == 0:
            dict_data = {
                'status': 'fail',
                'message': 'id error'
            }
            json_data = json.dumps(dict_data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            image = Image.objects.get(pk=image_id)
            favorite = Favorite.objects.get(user=request.user, image=image)
            if favorite:
                favorite.delete()
                dict_data = {
                    'status': 'success',
                    'message': '已取消收藏！'
                }
                json_data = json.dumps(dict_data)
                return HttpResponse(json_data, content_type='application/json')
            else:
                favorite = Favorite()
                favorite.image = image
                favorite.user = request.user
                favorite.add_time = timezone.now()
                favorite.save()
                dict_data = {
                    'status': 'success',
                    'message': '添加收藏成功！'
                }
                json_data = json.dumps(dict_data)
                return HttpResponse(json_data, content_type='application/json')


def RatingImage(request):
    """
    用户评分图片
    """
    if request.method == 'POST':
        image_id = request.POST.get('image_id', 0)
        star = request.POST.get('star', 0)
        if image_id == 0 or star == 0:
            data = {'status': 'fail', 'message': '图片ID/用户评分错误！'}
        else:
            image = Image.objects.get(pk=image_id)
            rating = Rating.objects.get(user=request.user, image=image)
            if rating:
                rating.star = star
                rating.date_add = timezone.now()
                rating.save()
                message = '重新评分成功！'
            else:
                rating = Rating()
                rating.star = star
                rating.user = request.user
                rating.image = image
                rating.date_add = timezone.now()
                rating.save()
                message = '评分成功！'
            data = {'status': 'success', 'message': message, }
        return JsonResponse(data)


# 发送邮箱验证码的view:


class SentMessage(LoginRequiredMixin, View):
    def post(self, request):
        from_user = request.POST.get('from_user_id', 0)
        to_user = request.POST.get('to_user_id', 0)


class AddComment(LoginRequiredMixin, View):
    def post(self, request):
        image_id = request.POST.get('image_id', 0)
        comment = Comment()
        comment.image = Image.objects.get(pk=image_id)
        comment.user = request.user
        comment.date_add = timezone.now()
        comment.save()
        data = {'status': 'success', 'message': '评论成功！'}
        return JsonResponse(data)


class UserinfoView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, 'user/info.html', {'user': user})


class Recharge(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, 'user/recharge.html', {'user': user})

    def post(self, request):
        user = request.user
        coin_num = request.POST.get('coin_num', 0)
        if coin_num > 0:
            if user.is_active == True:
                user.coin += coin_num
                user.save()
                message = '充值成功！'
            else:
                message = '用户未激活'
        else:
            message = '输入的硬币数量错误'
        return render(request, 'user/recharge.html', {'user': user, 'message': message})


class SignIn(LoginRequiredMixin, View):
    """
    用户签到模块
    """

    def get(self, request):
        user = request.user
        if user.is_active == False:
            data = {'status': 'fail', 'message': '用户未激活'}
        else:
            user.coin += 1
            user.save()
            data = {'status': 'success', 'message': '签到成功！'}
        return JsonResponse(data)
