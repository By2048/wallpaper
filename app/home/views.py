from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

import os

from image.models import ImageCategory, ImageTag


@method_decorator(login_required)
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        all_img_path = ["http://101.132.185.153:2199/1.jpg",
                        "http://101.132.185.153:2199/2.jpg",
                        "http://101.132.185.153:2199/3.jpg",
                        "http://101.132.185.153:2199/4.jpg",
                        "http://101.132.185.153:2199/5.jpg",
                        "http://101.132.185.153:2199/6.jpg",
                        "http://101.132.185.153:2199/7.jpg",
                        "http://101.132.185.153:2199/8.jpg",
                        "http://101.132.185.153:2199/9.jpg"]

        return render(request, 'home/index.html', context={'all_img_path': all_img_path})


class TagView(View):
    def get(self, request):
        all_tag = ImageTag.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_tag, 10, request=request)

        tags = p.page(page)
        return render(request, 'home/tag.html', context={'tags': tags})

#
# from django.shortcuts import render_to_response
#
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
#
# # 尝试获取页数参数
# try:
#     page = request.GET.get('page', 1)
# except PageNotAnInteger:
#     page = 1
# # objects是取到的数据
# objects = ['john', 'edward', 'josh', 'frank']
#
# # Provide Paginator with the request object for complete querystring generation
# # 对于取到的数据进行分页处理。
# p = Paginator(objects, request=request)
# # 此时前台显示的就应该是我们此时获取的第几页的数据
# people = p.page(page)
#
# return render_to_response('index.html', {
#     'people': people,
# }
