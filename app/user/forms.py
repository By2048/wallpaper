from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from captcha.fields import CaptchaField

from django import forms


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()
    captcha.label = '验证码'
    captcha.help_text = '请输入验证码'
    captcha.error_messages = '验证码输入错误'

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ['username', 'nickname', 'email', 'password1', 'password2', 'captcha', 'sex', 'birthday', 'address',
                  'information']


class ActiveForm(forms.Form):
    # 激活时验证码实现
    # 激活时不对邮箱密码做验证
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 忘记密码实现
class ForgetForm(forms.Form):
    # 此处email与前端name需保持一致。
    email = forms.EmailField(required=True)
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class UploadImageForm(forms.ModelForm):
    # 用于文件上传，修改头像
    class Meta:
        model = UserProfile
        fields = ['picture']


# 用于个人中心修改个人信息
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'sex', 'birthday', 'address', 'phone', 'information']
