from django.db import models
# from app.user.models import User
# from app.image.models import Image

from datetime import datetime

from datetime import datetime


# class Source(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name='')
#     image = models.OneToOneField(Image, verbose_name='图片', on_delete='CASCADE')
#     update_time = models.DateTimeField(default=datetime.now, verbose_name='')
#
#     class Meta():
#         db_table = 'db_source'
#         verbose_name = '图片评分'
#         verbose_name_plural = verbose_name
#
#
# class UserRateing(models.Model):
#     _point = (
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#     )
#     id = models.AutoField(primary_key=True, verbose_name='')
#     users = models.ManyToManyField(User, verbose_name='评价的用户')
#     images = models.ForeignKey(Image, verbose_name='评价的图片', on_delete='CASCADE')
#     point = models.IntegerField(choices=_point, verbose_name='得分')
#     evaluation_time = models.DateTimeField(default=datetime.now, verbose_name='评分时间')
#
#     class Meta():
#         db_table = 'db_source_rateing'
#         verbose_name = '用户评分'
#         verbose_name_plural = verbose_name
