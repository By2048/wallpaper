# coding=utf-8

from tool.init import init_sql
from tool.init import init_hot_image
from tool.init import init_carousel_image

if __name__ == '__main__':
    init_hot_image.update_hot_image()
    init_carousel_image.update_carousel_image()
