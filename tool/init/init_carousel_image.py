# coding=utf-8
# coding=utf-8
import os
import random

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallpaper.settings")
django.setup()

from image.models import Carousel
from image.models import Image

import pymysql


def update_carousel_image(num=12):
    Carousel.objects.all().delete()

    db_mysql = pymysql.connect("localhost", "root", "mysql_password", "wallpaper")
    cur_mysql = db_mysql.cursor()
    cur_mysql.execute("alter table `db_carousel_image` auto_increment=1")
    cur_mysql.close()

    carousel_imgs = Image.objects.all().order_by('?')[:num]
    for img in carousel_imgs:
        carousel_image = Carousel()
        carousel_image.image = img
        carousel_image.index = random.randint(1, 10000)
        carousel_image.save()

        print(img.get_image_name().ljust(15), end='')
        category = ''
        for item in img.categorys.all():
            category += item.get_category_name() + ' '
        print(category.ljust(20), end='')
        print(img.get_image_url())


if __name__ == '__main__':
    update_carousel_image()
