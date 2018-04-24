# coding=utf-8
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallpaper.settings")
django.setup()

from image.models import HotImage
from image.models import Image

import pymysql


def update_hot_image(num=12):
    HotImage.objects.all().delete()

    db_mysql = pymysql.connect("localhost", "root", "mysql_password", "wallpaper")
    cur_mysql = db_mysql.cursor()
    cur_mysql.execute("alter table `db_hot_image` auto_increment=1")
    cur_mysql.close()

    hot_imgs = Image.objects.all().order_by('-click')[:num]
    for img in hot_imgs:
        hot_image = HotImage()
        hot_image.image = img
        hot_image.save()

        print(img.get_image_name().ljust(15), end='')
        category = ''
        for item in img.categorys.all():
            category += item.get_category_name() + ' '
        print(category.ljust(20), end='')
        print(img.get_image_url())


if __name__ == '__main__':
    update_hot_image()
