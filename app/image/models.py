from django.utils import timezone

from django.db import models

from user.models import UserProfile


class Image(models.Model):
    _type = (
        ('0', 'jpg'),
        ('1', 'png'),
        ('2', 'gif'),
        ('3', 'bmp'),
        ('4', 'svg'),
    )
    name = models.CharField(max_length=50, verbose_name='图片名')
    description = models.TextField(verbose_name='图片描述', null=True, blank=True)
    url = models.URLField(max_length=500, verbose_name='图片链接')
    url_thumb = models.URLField(max_length=500, verbose_name='缩略图片链接')
    # category = models.ForeignKey(Category, verbose_name='图片分类', on_delete='DO_NOTHING')
    # tags = models.ManyToManyField(Tag, verbose_name='图片标签', on_delete=models.CASCADE)
    width = models.IntegerField(verbose_name='图片宽度')
    height = models.IntegerField(verbose_name='图片高度')
    type = models.CharField(max_length=10, choices=_type, verbose_name='图片格式')
    click = models.IntegerField(verbose_name='点击次数', default=0)

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


class HotImage(models.Model):
    image = models.ForeignKey(Image, verbose_name='图片', on_delete=models.CASCADE)
    index = models.IntegerField(verbose_name='图片展示顺序', unique=True)
    date_add = models.DateTimeField(default=timezone.now, verbose_name='更新时间')

    def __str__(self):
        return "{0}   {1}   {2}".format(self.index, self.image.name, self.image.url_thumb)

    class Meta:
        db_table = 'db_hot_image'
        verbose_name = '热门图片'
        verbose_name_plural = verbose_name


class ImageTag(models.Model):
    name = models.CharField(max_length=10, default='')
    count = models.IntegerField(default=0)

    class Meta():
        db_table = 'db_image_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def get_tag_name(self):
        return self.name

    def __str__(self):
        return self.name


class TagImage(models.Model):
    tags = models.ManyToManyField(ImageTag, verbose_name='标签')
    image = models.ForeignKey(Image, verbose_name='图片', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    date_add = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta():
        db_table = 'db_tag_image'
        verbose_name = '用户添加的图片标签'
        verbose_name_plural = verbose_name


class ImageScore(models.Model):
    image = models.OneToOneField(Image, verbose_name='图片', on_delete=models.DO_NOTHING)
    average_stars = models.FloatField(verbose_name='图片的平均得分')
    date_update = models.DateTimeField(default=timezone.now, verbose_name='更新时间')

    class Meta():
        db_table = 'db_image_score'
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
    start = models.IntegerField(choices=_point, verbose_name='得分')
    date_evaluation = models.DateTimeField(default=timezone.now, verbose_name='评分时间')

    class Meta():
        db_table = 'db_user_rateing'
        verbose_name = '用户评分'
        verbose_name_plural = verbose_name


class ImageCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='分类名')
    count = models.IntegerField(default=0, verbose_name='分类数量')

    class Meta:
        db_table = 'db_image_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_category_name(self):
        return self.name


class CategoryImage(models.Model):
    category = models.ForeignKey(ImageCategory, verbose_name='分类', on_delete=models.CASCADE)
    image = models.ForeignKey('image.Image', verbose_name='图片', on_delete=models.CASCADE)
    user = models.ForeignKey('user.UserProfile', verbose_name='用户', on_delete=models.DO_NOTHING)
    date_add = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    def __str__(self):
        return "{0} {1}".format(self.category.name, self.image.name)

    class Meta():
        db_table = 'db_category_image'
        verbose_name = '图片分类'
        verbose_name_plural = verbose_name
