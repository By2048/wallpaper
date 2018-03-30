from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone

from django.core.files.storage import FileSystemStorage
from captcha.fields import CaptchaField
from tool import ImageTool


# class ImageStorage(FileSystemStorage):
#     from django.conf import settings
#     def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
#         super(ImageStorage, self).__init__(location, base_url)
#
#     def _save(self, name, content):
#         import os, time, random
#         ext = os.path.splitext(name)[1]
#         # 文件目录
#         d = os.path.dirname(name)
#         # 定义文件名，年月日时分秒随机数
#         fn = time.strftime('%Y%m%d%H%M%S')
#         fn = fn + '_%d' % random.randint(0, 100)
#         # 重写合成文件名
#         name = os.path.join(d, fn + ext)
#         return super(ImageStorage, self)._save(name, content)
#         # 调用父类方法


class UserProfile(AbstractUser):
    """在Django中默认的Usr进行拓展
    db_user_profile
    id
    password
    is_superuser
    username
    first_name
    last_name
    email
    is_staff
    is_active
    date_joined
    nickname
    sex
    birthday
    address
    phone
    information
    last_login
    type
    coin
    image
    """
    _sex = (
        ('male', '男'),
        ('female', '女'),
        ('neutral', '中'),
    )
    _type = (
        ('user', '普通用户'),
        ('vip', '会员'),
        ('author', '作者')
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='用户名',
        help_text=('必填！50个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号，不能与他人重复，不可修改。'),
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': ("此用户名已被占用！"),
        },
    )
    nickname = models.CharField(max_length=50, default='用户默认昵称', verbose_name='昵称', help_text='实际展示给他人的名称，可随时更改')
    image = models.ImageField(upload_to='image/%Y/%m',
                              # storage=ImageStorage(),
                              default='resource/user_image/default.png',
                              verbose_name='头像', help_text='用户显示的头像！')
    sex = models.IntegerField(choices=_sex, default=-1, null=True, blank=True, verbose_name='性别',
                              help_text='可不填 默认为中性！')
    birthday = models.DateField(max_length=10, null=True, blank=True, verbose_name='生日', help_text='可不填！')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='地址', help_text='可不填！')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号', help_text='可不填！')
    information = models.TextField(null=True, blank=True, verbose_name='信息', help_text='可不填！')
    last_login = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='最后登录时间')
    type = models.IntegerField(choices=_type, default=1, verbose_name='用户类型', blank=True, null=True)
    coin = models.IntegerField(default=100, verbose_name='用户积分')

    def __str__(self):
        return self.username

    def get_user_nickname(self):
        return self.nickname

    def get_user_username(self):
        return self.username

    class Meta(AbstractUser.Meta):
        db_table = 'db_user_profile'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


# 用户验证
class UserAuthentication(models.Model):
    _types = (
        ('1', '注册'),
        ('2', '找回密码'),
    )
    _actives = (
        ('0', '未激活'),
        ('1', '已激活'),
    )
    verification_code = models.CharField(max_length=50, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=_types, max_length=10, verbose_name='验证类型')
    date_send = models.DateTimeField(default=datetime.now, verbose_name='发送时间')
    date_expired = models.DateTimeField(default=datetime.now, verbose_name='过期时间')
    is_active = models.CharField(choices=_actives, max_length=10, default='0', verbose_name='激活链接是否点击')

    class Meta:
        db_table = 'db_user_authentication'
        verbose_name = '用户验证'
        verbose_name_plural = verbose_name


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, null=True, verbose_name='用户', on_delete=models.CASCADE)
    image = models.ForeignKey('image.Image', null=True, verbose_name='图片', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    def __str__(self):
        return "{0}    {1}".format(self.user.username, self.image.url)

    class Meta:
        db_table = 'db_favorite'
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class Message(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='from_user', verbose_name='发送的用户', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserProfile, related_name='to_user', verbose_name='接受的用户', on_delete=models.CASCADE)
    message = models.CharField(max_length=1000, verbose_name='消息内容')
    is_read = models.BooleanField(default=False, verbose_name='时候读取')
    date_send = models.DateTimeField(default=timezone.now, verbose_name='消息发送时间')

    class Meta:
        db_table = 'db_message'
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    image = models.ForeignKey('image.Image', null=True, verbose_name='图片', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000, verbose_name='评论内容')
    date_add = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        db_table = 'db_comment'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name
