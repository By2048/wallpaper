# Generated by Django 2.0.3 on 2018-03-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_tagimage_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tagimage',
            old_name='tag',
            new_name='tags',
        ),
    ]