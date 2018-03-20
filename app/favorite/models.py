from django.db import models

from django.utils import timezone

from app.user.models import UserProfile
from app.image.models import Image


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, null=True, verbose_name='用户', on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Image, null=True, verbose_name='图片', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    def __str__(self):
        return "{0}    {1}".format(self.user.username, self.image.url)

    class Meta:
        db_table = 'db_favorite'
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
