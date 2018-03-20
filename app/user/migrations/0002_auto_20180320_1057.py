# Generated by Django 2.0.3 on 2018-03-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(blank=True, choices=[('1', '普通用户 '), ('2', '会员'), ('3', '作者')], default='0', max_length=50, null=True, verbose_name='用户类型'),
        ),
    ]