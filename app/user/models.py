from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=False)
    register_date = models.DateTimeField()
    last_login = models.DateTimeField()
    integral = models.IntegerField()

    class Meta():
        pass
