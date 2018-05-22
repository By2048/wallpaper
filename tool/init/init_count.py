# coding=utf-8
import os
import random

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallpaper.settings")
django.setup()

from image.models import Category, Image


def init_category_count():
    for image in Image.objects.all():
        categorys = image.categorys.all()
        for category in categorys:
            category.count += 1
            category.save()


def init_tag_count():
    for image in Image.objects.all():
        tags = image.tags.all()
        for tag in tags:
            tag.count += 1
            tag.save()


def init_pid():
    for image in Image.objects.all():
        pid = int(os.path.split(image.url)[-1].split('.')[0])
        print(pid)
        image.pid = pid
        image.save()


if __name__ == '__main__':
    # init_category_count()
    # init_tag_count()
    init_pid()
