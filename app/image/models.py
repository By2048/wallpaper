from django.db import models
from datetime import datetime
# from app.category.models import Category

# from app.tag.models import Tag


# class Image(models.Model):
#     _type = (
#         ('0', 'jpg'),
#         ('1', 'png'),
#         ('2', 'gif'),
#         ('3', 'bmp'),
#         ('4', 'svg'),
#     )
#     id = models.AutoField(primary_key=True, verbose_name='图片ID')
#     name = models.CharField(max_length=50, verbose_name='图片名')
#     info = models.TextField(verbose_name='图片描述')
#     url = models.URLField(max_length=500, verbose_name='图片链接')
#     url_thumb = models.URLField(max_length=500, verbose_name='缩略图片链接')
#     category = models.OneToOneField(Category, verbose_name='图片分类',on_delete='CASCADE')
#     tags = models.ManyToManyField(Tag, verbose_name='图片标签')
#     width = models.IntegerField(verbose_name='图片宽度')
#     height = models.IntegerField(verbose_name='图片高度')
#     type = models.CharField(max_length=10, choices=_type, verbose_name='图片格式')
#
#     class Meta:
#         db_table = 'db_image'
#         verbose_name = '图片'
#         verbose_name_plural = verbose_name
