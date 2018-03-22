from user.models import UserProfile
import django.contrib.auth.backends


class EmailBackend(object):
    def authenticate(self, request, **credentials):
        email = credentials.get('email', credentials.get('username'))
        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            pass
        else:
            if user.check_password(credentials['password']):
                return user

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None
