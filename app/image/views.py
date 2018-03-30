from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

from image.models import Image


class ImageView(View):
    def get(self, request):
        image_id = request.GET.get('image_id', 0)
        if image_id == 0:
            return render(request, 'image/not_exist.html', context={})
        else:
            image = Image.objects.filter(pd=image_id)
            return render(request, 'image/detail.html', context={'image': image})



