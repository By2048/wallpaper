from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from captcha.fields import CaptchaField
from django import forms

class RegisterForm(UserCreationForm):
    captcha = CaptchaField()
    captcha.label='验证码'
    captcha.help_text='请输入验证码'
    captcha.error_messages = '验证码输入错误'
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ['username', 'nickname', 'email', 'password1', 'password2','captcha', 'sex',
                  'birthday', 'address', 'information']
