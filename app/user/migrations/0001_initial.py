# Generated by Django 2.0.3 on 2018-03-22 22:14

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': '此用户名已被占用！'}, help_text='必填！50个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号，不能与他人重复，不可修改。', max_length=50, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='用户名')),
                ('nickname', models.CharField(default='普通用户', help_text='实际展示给他人的名称，可随时更改', max_length=50, verbose_name='昵称')),
                ('image', models.ImageField(default='/resource/user_image/default.png', help_text='可不设置！', upload_to='image/%Y/%m', verbose_name='头像')),
                ('sex', models.IntegerField(blank=True, choices=[(1, '男'), (0, '女'), (-1, '中')], default=-1, help_text='可不填 默认为中性！', null=True, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, help_text='可不填！', max_length=10, null=True, verbose_name='生日')),
                ('address', models.CharField(blank=True, help_text='可不填！', max_length=100, null=True, verbose_name='地址')),
                ('phone', models.CharField(blank=True, help_text='可不填！', max_length=11, null=True, verbose_name='手机号')),
                ('information', models.TextField(blank=True, help_text='可不填！', null=True, verbose_name='信息')),
                ('last_login', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='最后登录时间')),
                ('type', models.IntegerField(blank=True, choices=[(1, '普通用户'), (2, '会员'), (3, '作者')], default=1, null=True, verbose_name='用户类型')),
                ('coin', models.IntegerField(default=100, verbose_name='用户积分')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'db_user_profile',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAuthentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_code', models.CharField(max_length=50, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('1', '注册'), ('2', '找回密码')], max_length=10, verbose_name='验证类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
                ('expired_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='过期时间')),
                ('is_active', models.CharField(choices=[('0', '未激活'), ('1', '已激活')], default='0', max_length=10, verbose_name='激活链接是否点击')),
            ],
            options={
                'verbose_name': '用户验证',
                'verbose_name_plural': '用户验证',
                'db_table': 'db_user_authentication',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='image.Image', verbose_name='图片')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
                'db_table': 'db_user_favorite',
            },
        ),
    ]
