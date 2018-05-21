# coding=utf-8

from tool import init_sql
from tool import init_hot_image
from tool import init_carousel_image

if __name__ == '__main__':
    init_sql.clear_all()
    init_sql.create_super_user()
    init_sql.create_default_user()
    init_sql.init_category()
    init_sql.init_tag()

    init_hot_image.update_hot_image()
    init_carousel_image.update_carousel_image()
