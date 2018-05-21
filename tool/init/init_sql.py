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
from image.models import Tag

db_sqlite = conn = sqlite3.connect("image.db")
db_mysql = pymysql.connect("localhost", "root", "mysql_password", "wallpaper")


def create_default_user():
    try:
        user = UserProfile.objects.get(email='user_default@email.com')
    except Exception as e:
        user = UserProfile()
        user.username = 'user_default'
        user.email = 'user_default@email.com'
        user.password = make_password('qwer1234')
        user.save()


def create_super_user():
    try:
        user = UserProfile.objects.get(email='user_admin@email.com')
    except Exception as e:
        user = UserProfile()
        user.username = 'user_admin'
        user.email = 'user_admin@email.com'
        user.password = make_password('qwer1234')
        user.is_superuser = True
        user.is_staff = True
        user.save()


def init_category():
    user_default = UserProfile.objects.get(email='user_default@email.com')
    cur_sqlite = db_sqlite.cursor()
    cur_sqlite.execute("select name from category")
    for item in cur_sqlite.fetchall():
        category = Category()
        category.name = item[0]
        category.user = user_default
        category.save()
    category = Category()
    category.name = 'Other'
    category.user = user_default
    category.save()


def init_tag():
    user_default = UserProfile.objects.get(email='user_default@email.com')
    tag = Tag()
    tag.name = 'Other'
    tag.user = user_default
    tag.save()


def init_image():
    user_default = UserProfile.objects.get(email='user_default@email.com')
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

        image.user = user_default
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
                tags_info = tags_info.replace('\'', '\"')
                tags_info = tags_info.replace('\"s ', "\' s")
                try:
                    tags_info = json.loads(tags_info.replace('\'', '\"'))
                except:
                    pass
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
                logging.error(tags_info)
                logging.error(e)


def clear_all():
    Tag.objects.all().delete()
    Category.objects.all().delete()
    Image.objects.all().delete()
    UserProfile.objects.all().delete()

    cur_mysql = db_mysql.cursor()
    cur_mysql.execute("alter table `db_category` auto_increment=1")
    cur_mysql.execute("alter table `db_tag` auto_increment=1")
    cur_mysql.execute("alter table `db_image` auto_increment=1")
    cur_mysql.execute("alter table `db_user_profile` auto_increment=1")


if __name__ == '__main__':
    clear_all()
    create_super_user()
    create_default_user()
    init_category()
    init_tag()
    # init_image()
    pass
