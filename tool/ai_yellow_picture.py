# coding=utf-8
from aip import AipImageCensor

''' 图片审核 '''

APP_ID = '11198069'
API_KEY = 'dpZA2BIUPqLr0fE0Lf4r1hRy'
SECRET_KEY = '4tx1NWwcFZnlOo3OCqXGsdP6WGMkUFR3'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 色情识别
# result = client.imageCensorUserDefined('http://www.example.com/image.jpg')
# result = client.imageCensorUserDefined(get_file_content('yellow_1.jpg'))
# print(result)
# {'conclusion': '不合规', 'log_id': 152567525151028,
# 'data': [{'msg': '存在色情内容', 'probability': 0.993896, 'type': 1},
#  {'msg': '存在恶心内容', 'probability': 0.9356292, 'type': 4}]}

# 暴恐识别
# result = client.imageCensorUserDefined(get_file_content('xjp.jpg'))
# print(result)
# {'conclusion': '不合规', 'log_id': 152567546413054,
#  'data': [{'msg': '存在水印码内容', 'probability': 0.51623607, 'type': 5},
#  {'msg': '存在政治敏感内容', 'stars': [{'probability': 0.83760697, 'name': '习近平'}], 'type': 8}]}

# GIF色情识别
# result = client.antiPornGif(get_file_content('antiporn.gif'))

# 头像审核
# result = client.faceAudit(get_file_content('img.jpg'))

# 组合审核
'''
1、ocr：通用文字识别
2、public：公众人物识别
3、politician：政治人物识别1
4、antiporn：色情识别 
5、terror：暴恐识别。
6、webimage：网图OCR识别
7、disgust:恶心图
8、watermark:水印、二维码
'''
# result = client.imageCensorComb(get_file_content('img.jpg'), ['ocr', 'antiporn', ])



''' 图片识别 '''
# https://ai.baidu.com/docs#/ImageClassify-API/c8911f08

"""
ewrrwer
"""





