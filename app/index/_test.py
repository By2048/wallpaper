import os

img_path = '..\\..\\static\\_tmp\\_img'
print(os.path.abspath(img_path))

print(os.listdir(img_path))


print([os.path.abspath(path) for path in os.listdir(img_path)])