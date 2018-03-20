from django.contrib import admin
from .models import Favorite
from app.user.models import UserProfile
from app.image.models import Image

from app.index import admin as index_admin


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):

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
