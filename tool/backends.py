from . import models

#
# class EmailBackend(object):
#     def authenticate(self, request, **credentials):
#         email = credentials.get('email', credentials.get('username'))
#         try:
#             user = models.User.objects.get(email=email)
#         except models.User.DoesNotExist:
#             pass
#         else:
#             if user.check_password(credentials['password']):
#                 return user
#
#     def get_user(self, user_id):
#         try:
#             return models.User.objects.get(pk=user_id)
#         except models.User.DoesNotExist:
#             return None
