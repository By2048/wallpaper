# coding=utf-8
import requests

# 上传文件到Nginx服务器

server = 'http://101.132.185.153:2200/'


def upload_file():
    files = {
        "image_file": open("test_upload.jpg", "rb")
    }
    response = requests.post(server, files=files)
    print(response)


def upload_multiple_files():
    multiple_files = [
        ("image_file", open("test_upload_1.jpg", "rb")),
        ("image_file", open("test_upload_2.jpg", "rb")),
    ]
    response = requests.post(server, files=multiple_files)
    print(response)
