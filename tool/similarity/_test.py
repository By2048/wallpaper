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

sim_2 = 1 - (hash_1 - hash_2) / len(hash_1.hash) ** 2
sim_3 = 1 - (hash_1 - hash_3) / len(hash_1.hash) ** 2
sim_4 = 1 - (hash_1 - hash_4) / len(hash_1.hash) ** 2

if __name__ == '__main__':
    print(hash_1)
    print(hash_2, '\t', sim_2, '\t', image_2)
    print(hash_3, '\t', sim_3, '\t\t', image_3)
    print(hash_4, '\t', sim_4, '\t', image_4)
