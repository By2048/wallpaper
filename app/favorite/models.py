from django.db import models

from datetime import datetime

# from app.user.models import User
# from app.image.models import Image


# class Favorite(models.Model):
#     id = models.AutoField(primary_key=True)
#     uer = models.ForeignKey(User, null=True, verbose_name='用户', on_delete=models.CASCADE)
#     image = models.ForeignKey(Image, null=True, verbose_name='图片', on_delete=models.CASCADE)
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         db_table = 'db_favorite'
#         verbose_name = '用户收藏'
#         verbose_name_plural = verbose_name
