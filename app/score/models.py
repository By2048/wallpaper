from django.db import models
from app.user.models import UserProfile
from app.image.models import Image

from django.utils import timezone


class Source(models.Model):
    image = models.OneToOneField(Image, verbose_name='图片', on_delete=models.DO_NOTHING)
    date_update = models.DateTimeField(default=timezone.now, verbose_name='更新时间')

    class Meta():
        db_table = 'db_source'
        verbose_name = '图片得分'
        verbose_name_plural = verbose_name


class UserRateing(models.Model):
    _point = (
        (1, '1 星'),
        (2, '2 星'),
        (3, '3 星'),
        (4, '4 星'),
        (5, '5 星'),
    )
    user = models.ForeignKey(UserProfile, verbose_name='评价的用户', on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Image, verbose_name='评价的图片', on_delete=models.DO_NOTHING)
    point = models.IntegerField(choices=_point, verbose_name='得分')
    date_evaluation = models.DateTimeField(default=timezone.now, verbose_name='评分时间')

    class Meta():
        db_table = 'db_source_rateing'
        verbose_name = '用户评分'
        verbose_name_plural = verbose_name
