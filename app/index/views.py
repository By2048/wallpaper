from django.shortcuts import render

import os


def index(request):
    all_img_path = ["https://images3.alphacoders.com/906/906816.jpg"]

    return render(request, 'index/index.html', context={'all_img_path': all_img_path})




