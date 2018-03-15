from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(models.Model):
    _sex = (
        ('1', '男'),
        ('0', '女'),
        ('-1', '中'),
    )
    _type = (
        ('0', 'default'),
        ('1', 'vip'),
    )
    id = models.AutoField(primary_key=True, verbose_name='用户ID')
    username = models.CharField(max_length=50, default='', verbose_name='用户名')
    password = models.CharField(max_length=50, verbose_name='密码')
    image = models.ImageField(upload_to='resource/user_image', default='/static/resource/user_image/default.png',
                              null=True, blank=True, verbose_name='头像')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    is_active = models.BooleanField(default=False, verbose_name='用户是否可以使用')
    sex = models.CharField(max_length=10, choices=_sex, default='中', null=True, blank=True, verbose_name='性别')
    birthday = models.DateField(max_length=10, null=True, blank=True, verbose_name='生日')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='地址')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    information = models.TextField(null=True, blank=True, verbose_name='信息')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    last_login = models.DateTimeField(default=datetime.now, verbose_name='最后登录时间')
    type = models.CharField(max_length=50, choices=_type, default='0', verbose_name='用户类型')
    integral = models.IntegerField(default=100, verbose_name='用户积分')

    class Meta():
        db_table = 'db_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # 自定义显示的信息
    def __str__(self):
        return '{0}({1})'.format(self.username, self.email)


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
    id = models.AutoField(primary_key=True, verbose_name='ID')
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
