from django.contrib.auth.forms import UserCreationForm
from . import models


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email')

class LoginForm():
    pass

class ChangePasswordForm():
    pass

class ResetPasswordForm():
    pass

