from django.db import models
from datetime import datetime


# from app.category.models import Category
# from app.tag.models import Tag


class Image(models.Model):
    _type = (
        ('0', 'jpg'),
        ('1', 'png'),
        ('2', 'gif'),
        ('3', 'bmp'),
        ('4', 'svg'),
    )
    name = models.CharField(max_length=50, verbose_name='图片名')
    description = models.TextField(verbose_name='图片描述')
    url = models.URLField(max_length=500, verbose_name='图片链接')
    url_thumb = models.URLField(max_length=500, verbose_name='缩略图片链接')
    # category = models.ForeignKey(Category, verbose_name='图片分类', on_delete='DO_NOTHING')
    # tags = models.ManyToManyField(Tag, verbose_name='图片标签', on_delete=models.CASCADE)
    width = models.IntegerField(verbose_name='图片宽度')
    height = models.IntegerField(verbose_name='图片高度')
    type = models.CharField(max_length=10, choices=_type, verbose_name='图片格式')

    def __str__(self):
        return self.name + '.' + self.type

    def get_image_url(self):
        return self.url

    def get_image_name(self):
        return self.name

    class Meta:
        db_table = 'db_image'
        verbose_name = '图片'
        verbose_name_plural = verbose_name
