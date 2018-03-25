from django.shortcuts import render
from django.views.generic.base import View

import os


class IndexView(View):
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

    def post(self, request):
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
