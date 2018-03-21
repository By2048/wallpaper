from django.db import models
from django.utils import timezone
from app.user.models import UserProfile
from app.image.models import Image


class Tag(models.Model):
    name = models.CharField(max_length=10, default='')
    count = models.IntegerField(default=0)

    class Meta():
        db_table = 'db_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def get_tag_name(self):
        return self.name

    def __str__(self):
        return self.name


class TagImage(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    image = models.ForeignKey(Image, verbose_name='图片', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    date_add = models.DateTimeField(default=timezone.now, verbose_name='添加时间')


    class Meta():
        db_table = 'db_tag_image'
        verbose_name = '用户添加的图片标签'
        verbose_name_plural = verbose_name
