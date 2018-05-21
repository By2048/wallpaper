# coding=utf-8
import requests

# 上传文件到Nginx服务器

nginx_server = 'http://101.132.185.153:2200/upload/'

nginx_show = 'http://101.132.185.153:2199/'

"""
runserver
/home/venv/nginx_upload/bin/python /home/python/nginx_upload/manage.py runserver 0.0.0.0:2200

html upload
http://101.132.185.153:2200/upload/

html delete 
http://101.132.185.153:2200/delete/
"""


def upload_file():
    files = {
        "image_file": open("test_upload.jpg", "rb")
    }
    response = requests.post(nginx_server, files=files)
    print(response)


def upload_multiple_files():
    multiple_files = [
        ("image_file", open("test_upload_1.jpg", "rb")),
        ("image_file", open("test_upload_2.jpg", "rb")),
    ]
    response = requests.post(nginx_server, files=multiple_files)
    print(response)


if __name__ == '__main__':
    upload_multiple_files()


