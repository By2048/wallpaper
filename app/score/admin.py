from django.contrib import admin
from app.user.models import UserProfile
from app.image.models import Image
from app.index import admin as index_admin

from .models import Source, UserRateing


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ('id', 'show_image', 'date_update')
    list_display_links = ('id', 'show_image', 'date_update')

    list_filter = ['date_update']

    search_fields = ['image__name']
    list_per_page = 10

    ordering = ['id']

    empty_value_display = '- null -'

    actions = [index_admin.export_as_json]


@admin.register(UserRateing)
class UserRatingAdmin(admin.ModelAdmin):

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ['id', 'show_user', 'show_image', 'date_evaluation']
    list_display_links = ['id', 'show_user', 'show_image', 'date_evaluation']

    # list_filter = ['tag__count', 'date_add']
    list_filter = ['point', 'date_evaluation']

    search_fields = ['user__name', 'image__name', 'image__url', 'date_evaluation']

    ordering = ['id']
    list_per_page = 10

    actions = [index_admin.export_as_json]

    empyt_value_dispaly = '- null -'
