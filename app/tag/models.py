from django.db import models


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, default='')
    count = models.IntegerField(default=0)

    class Meta():
        db_table = 'db_tag'
        verbose_name = '图片标签'
        verbose_name_plural = verbose_name


# class ImageTag(models.Model):
#     id = models.AutoField(primary_key=True)
#     # image
