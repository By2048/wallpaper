# coding=utf-8
import imagehash
from PIL import Image

image_1 = r'test_原始.jpg'
image_2 = r'test_干扰.jpg'
image_3 = r'test_缩略图.jpg'
image_4 = r'test_不同图片.jpg'

hash_1 = imagehash.dhash(Image.open(image_1), hash_size=8)
hash_2 = imagehash.dhash(Image.open(image_2), hash_size=8)
hash_3 = imagehash.dhash(Image.open(image_3), hash_size=8)
hash_4 = imagehash.dhash(Image.open(image_4), hash_size=8)

print(hash_1)
print(hash_2)
print(hash_3)
print(hash_4)


print(1 - (hash_1 - hash_2) / len(hash_1.hash) ** 2)
print(1 - (hash_1 - hash_3) / len(hash_1.hash) ** 2)
print(1 - (hash_1 - hash_4) / len(hash_1.hash) ** 2)

