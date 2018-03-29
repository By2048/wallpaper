from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
from django.db.models import F

from .models import UserProfile, UserFavorite
from home import admin as index_admin


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'sex', 'type', 'coin']
    list_display_links = ['username', 'email', 'sex', 'type', 'coin']

    list_filter = ['sex', 'type', 'date_joined', 'last_login']
    search_fields = ['username', 'nickname', 'email']
    list_per_page = 10

    ordering = ['id']
    empty_value_display = '- null -'

    actions = ['add_100_coin', index_admin.export_as_json]

    def add_100_coin(self, request, quertset):
        user_ids = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        # Entry.objects.all().update(n_pingbacks=F('n_pingbacks') + 1)
        for user_id in user_ids:
            user = UserProfile.objects.get(pk=user_id)
            # user.objects.update(coin=F('coin') + 100)
            current_coin = user.coin
            user.coin = current_coin + 100
            user.save()
        self.message_user(request, "%s 个用户成功更新" % len(user_ids))

    add_100_coin.short_description = '增加 100 硬币'


@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户名'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ['id', 'show_user', 'show_image', 'add_time']

    list_display_links = ['id', 'show_user', 'show_image', 'add_time']

    search_fields = ['show_user']

    list_filter = ['add_time']

    ordering = ['id']

    list_per_page = 10

    actions = [index_admin.export_as_json]
