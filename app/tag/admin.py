from django.contrib import admin
from .models import Tag, TagImage
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from app.index import admin as index_admin


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class CountFilter(admin.SimpleListFilter):
        title = '标签数量'
        parameter_name = 'count'

        def lookups(self, request, model_admin):
            return (
                ('0', '小于 100'),
                ('1', '大于 100'),
            )

        def queryset(self, request, queryset):
            if self.value() == '0':
                return queryset.filter(count__lte='100')
            if self.value() == '1':
                return queryset.filter(count__gte='100')

    list_display = ('id', 'name', 'count')
    list_display_links = ('id', 'name', 'count')

    list_filter = (CountFilter,)

    search_fields = ['id', 'name']
    list_per_page = 10

    ordering = ['id']

    empty_value_display = '- null -'

    actions = [index_admin.export_as_json]


@admin.register(TagImage)
class TagImageAdmin(admin.ModelAdmin):

    def show_tag(self, obj):
        return obj.tag.get_tag_name()

    show_tag.short_description = '分类名'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户'

    list_display = ['id', 'show_tag', 'show_image', 'show_user', 'date_add']
    list_display_links = ['id', 'show_tag', 'show_image', 'show_user', 'date_add']

    # list_filter = ['tag__count', 'date_add']
    list_filter = ['date_add']

    search_fields = ['tag__name', 'date_add']

    ordering = ['id']
    list_per_page = 10

    actions = [index_admin.export_as_json]

    empyt_value_dispaly = '- null -'
