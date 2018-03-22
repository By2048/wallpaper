from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone


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
        (1, '男'),
        (0, '女'),
        (-1, '中'),
    )
    _type = (
        (1, '普通用户'),
        (2, '会员'),
        (3, '作者')
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
    nickname = models.CharField(max_length=50, default='普通用户',verbose_name='昵称', help_text='实际展示给他人的名称，可随时更改')
    image = models.ImageField(upload_to='resource/user_image', default='/resource/user_image/default.png',
                              null=True, blank=True, verbose_name='头像',help_text='可不设置！')
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
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')
    expired_time = models.DateTimeField(default=datetime.now, verbose_name='过期时间')
    is_active = models.CharField(choices=_actives, max_length=10, default='0', verbose_name='激活链接是否点击')

    class Meta:
        db_table = 'db_user_authentication'
        verbose_name = '用户验证'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, null=True, verbose_name='用户', on_delete=models.DO_NOTHING)
    image = models.ForeignKey('image.Image', null=True, verbose_name='图片', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    def __str__(self):
        return "{0}    {1}".format(self.user.username, self.image.url)

    class Meta:
        db_table = 'db_user_favorite'
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
