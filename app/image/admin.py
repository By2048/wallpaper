from django.contrib import admin
from .models import Image

from app.index import admin as index_admin


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # def show_tags(self, obj):
    #     return ' '.join([tag.name for tag in obj.tags.all()])
    # tags= Tag.objects.filter(image_id=obj.id)

    # show_tags.short_description = '显示所有标签'

    list_display = ['id', 'name', 'url', 'width', 'height', 'type']
    list_display_links = ['id', 'name', 'url', 'width', 'height', 'type']

    search_fields = ['name', 'width', 'height', 'type']

    list_filder = ['width', 'height', 'type']
    ordering = ['id']

    actions = [index_admin.export_as_json]

    list_per_page = 10
