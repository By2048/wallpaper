from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

import json

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
        return render(request, 'user/register.html', context={'register_form': register_form, 'next': next})

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
            return render(request, 'user/register.html', context={'register_form': register_form})


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


class RatingImage(LoginRequiredMixin, View):
    def post(self, request):
        image_id = request.POST.get('image_id', 0)
        star = request.POST.get('star', 0)
        if image_id == 0 or star == 0:
            dict_data = {
                'status': 'fail',
                'message': 'image_id star empty'
            }
            json_data = json.dumps(dict_data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            image = Image.objects.get(pk=image_id)
            rating = Rating.objects.filter(user=request.user, image=image)
            if rating:
                rating.star = star
                rating.date_add = timezone.now()
                rating.save()
                dict_data = {
                    'status': 'success',
                    'message': '重新评分成功！'
                }
                json_data = json.dumps(dict_data)
                return HttpResponse(json_data, content_type='application/json')
            else:
                rating = Rating()
                rating.star = star
                rating.user = request.user
                rating.image = image
                rating.date_add = timezone.now()
                rating.save()
                dict_data = {
                    'status': 'success',
                    'message': '评分成功！'
                }
                json_data = json.dumps(dict_data)
                return HttpResponse(json_data, content_type='application/json')

        # # 发送邮箱验证码的view:


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
        dict_data = {
            'status': 'success',
            'message': '评论成功！'
        }
        json_data = json.dumps(dict_data)
        return HttpResponse(json_data, content_type='application/json')


class UserinfoView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile = UserProfile.objects.get(pk=request.user.id)
        user_info = {
            'email': user_profile.email,
            'date_joined': user_profile.date_joined,
            'username': user_profile.username,
            'nickname': user_profile.nickname,
            'image': user_profile.image,
            'sex': user_profile.get_sex_display(),
            'birthday': user_profile.birthday,
            'address': user_profile.address,
            'phone': user_profile.phone,
            'information': user_profile.information,
            'last_login': user_profile.last_login,
            'type': user_profile.type,
            'coin': user_profile.coin
        }
        return render(request, 'user/info.html', {'user_info': user_info})
