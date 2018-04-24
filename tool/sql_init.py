# coding=utf-8
import os

import django
from django.contrib.auth.hashers import make_password
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallpaper.settings")
django.setup()

import random
import pymysql
import logging
import sqlite3

from image.models import Category
from image.models import Image
from user.models import UserProfile
from image.models import Tag, TagImage

db_sqlite = conn = sqlite3.connect("image.db")
db_mysql = pymysql.connect("localhost", "root", "mysql_password", "wallpaper")


def init_category():
    cur_sqlite = db_sqlite.cursor()
    cur_sqlite.execute("select name from category")
    for item in cur_sqlite.fetchall():
        category = Category(name=item[0], count=0)
        category.save()


def init_user():
    try:
        user = UserProfile.objects.get(email='default_user@email.com')
    except Exception as e:
        logging.error(e)
        user = UserProfile()
        user.username = 'default_user'
        user.email = 'default_user@email.com'
        user.password = make_password('qwer1234')
        user.save()


def init_image():
    upload_user = UserProfile.objects.get(email='default_user@email.com')
    cur_sqlite = db_sqlite.cursor()
    cur_sqlite.execute("select name,url_image,url_thumb,width,height,file_type,category_id,tags from image")

    for item in cur_sqlite.fetchall():
        image = Image()
        image.name = item[0]
        image.url = item[1]
        image.url_thumb = item[2]
        image.width = item[3]
        image.height = item[4]
        image.type = item[5].replace('.', '')

        image.user = upload_user
        image.save()

        category_id = item[6]
        if category_id != '':
            category = Category.objects.get(pk=int(item[6]))
            image.categorys.add(category)

        tags_info = item[7]
        if tags_info != '':
            tags_info = "{'tags':" + tags_info + "}"
            try:
                tags_info = json.loads(tags_info.replace('\'', '\"'))
            except Exception as e:
                logging.error(e)
            try:
                for item in tags_info['tags']:
                    try:
                        tag = Tag.objects.get(name=item['name'])
                        image.tags.add(tag)
                    except Exception as e:
                        tag = Tag()
                        tag.name = item['name']
                        tag.save()
                        image.tags.add(tag)
            except Exception as e:
                logging.error(str(tags_info))
                logging.error(e)


def clear_all():
    Category.objects.all().delete()

    cur_mysql = db_mysql.cursor()
    cur_mysql.execute("alter table `db_category` auto_increment=1")

    Image.objects.all().delete()


if __name__ == '__main__':
    clear_all()
    # init_useraxa()
    init_category()
    init_image()
