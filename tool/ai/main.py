# coding=utf-8
import os
import requests
import base64
import logging

logging.basicConfig(level=logging.INFO)

from PIL import Image as PImage

APP_ID = '11198069'
API_KEY = 'dpZA2BIUPqLr0fE0Lf4r1hRy'
SECRET_KEY = '4tx1NWwcFZnlOo3OCqXGsdP6WGMkUFR3'
ACCESS_TOKEN = "24.caabce7c65930e3ba4ea5656dd3cd3b2.2592000.1529409154.282335-11198069"

""" 读取图片 """


def get_image_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_image_base64(image_path):
    with open(image_path, 'rb') as file:
        image_base64 = base64.b64encode(file.read())
    return image_base64


def get_thumb_image(image_path):
    _type = os.path.splitext(image_path)[-1]
    tmp_image_path = '_tmp' + _type
    pimg = PImage.open(image_path)
    pimg.thumbnail((1024, 1024))
    pimg.save(tmp_image_path)
    return tmp_image_path


# https://ai.baidu.com/docs#/ImageClassify-API/c8911f08


def get_token():
    # access_token的有效期为30天，需要每30天进行定期更换；
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={AK}&client_secret={SK}' \
        .format(AK=API_KEY, SK=SECRET_KEY)
    response = requests.get(host)
    return response.text
    """
    {
        "access_token": "24.caabce7c65930e3ba4ea5656dd3cd3b2.2592000.1529409154.282335-11198069",
        "session_key": "9mzdWBGc4OOHa8t\/9x4BU3cZXCTjmD0Hi92Do7sE\/rqAyfAdxYAN3rtwjplAFO4pUrZBE0QdpHvBca+cY1z+Bkxyb7MQMw==",
        "scope": "public vis-classify_dishes vis-antiporn_antiporn_v2 vis-classify_watermark vis-classify_car brain_gif_antiporn vis-classify_terror brain_all_scope solution_face brain_antiporn brain_antiterror vis-classify_\u6076\u5fc3\u56fe\u8bc6\u522b\u670d\u52a1 vis-classify_animal brain_politician brain_imgquality_general vis-classify_plant brain_watermark brain_object_detect brain_realtime_logo brain_dish_detect brain_car_detect brain_animal_classify brain_plant_classify brain_disgust brain_antispam_spam brain_advanced_general_classify wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base",
        "refresh_token": "25.4471713f771e8a3e39ce6f8f6a690ad8.315360000.1842177154.282335-11198069",
        "session_secret": "e73aa254a3784304d0e5cc2d04e9b638",
        "expires_in": 2592000
    }
   """


def get_image_info(image_path, type=1):
    """
    Base64编码字符串，以图片文件形式请求时必填。(支持图片格式：jpg，bmp，png，jpeg)，图片大小不超过4M。最短边至少15px，最长边最大4096px
    """
    image_path = get_thumb_image(image_path)
    image_base64 = get_image_base64(image_path)
    access_token = '?access_token=' + ACCESS_TOKEN
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {'image': image_base64}
    if type == 6:
        body = {'images': image_base64}
    urls = {
        # 自定义图像审核接口
        0: 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/user_defined',
        # 通用图像分析——通用物体和场景识别
        1: 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general',
        # 细粒度图像识别——菜品识别
        2: 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish',
        # 细粒度图像识别—车型识别
        3: 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car',
        # 细粒度图像识别—动物识别
        4: 'https://aip.baidubce.com/rest/2.0/image-classify/v1/animal',
        # 细粒度图像识别—植物识别
        5: 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant',
        # 用户头像审核
        6: 'https://aip.baidubce.com/rest/2.0/solution/v1/face_audit',
    }
    response = requests.post(url=urls[type] + access_token, headers=header, data=body)
    return response.text


if __name__ == '__main__':
    img_1 = '政治人物.jpg'
    img_2 = '菜品.jpg'
    img_3 = '车.jpg'
    img_4 = '动物.jpg'
    img_5 = '植物.jpg'
    img_6 = '黄色图片1.jpg'
    img_7 = '黄色图片2.jpg'

    image_content = get_image_info(img_6, 0)
    print(image_content)

