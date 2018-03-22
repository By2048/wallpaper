from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ['username', 'nickname', 'email', 'password1', 'password2', 'sex',
                  'image', 'birthday', 'address', 'information']
