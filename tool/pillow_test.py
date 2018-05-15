# coding=utf-8
import os
from PIL import Image

img1 = Image.open('test_upload_1.jpg')

file_size = os.path.getsize('test_upload_1.jpg')

print(img1)
print(img1.size)


img1.thumbnail((300,300))

img1.save('test_upload_1_new.jpg')

print(img1.size)

img1.thumbnail((200,200))

img1.save('test_upload_1_new_1.jpg')