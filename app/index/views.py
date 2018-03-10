from django.shortcuts import render

import os


# Create your views here.

def index(request):
    all_img_path = ["http://www.runoob.com/wp-content/uploads/2014/07/slide1.png",
                    "http://www.runoob.com/wp-content/uploads/2014/07/slide2.png",
                    "http://www.runoob.com/wp-content/uploads/2014/07/slide3.png"]

    return render(request, 'index/index.html', context={'all_img_path': all_img_path})
