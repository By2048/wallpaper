# Generated by Django 2.0.3 on 2018-03-25 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20180325_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_add',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='图片添加时间'),
        ),
    ]
