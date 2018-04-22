# coding=utf-8

from django.contrib import admin
from django.contrib import admin

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse

admin.site.site_title = 'Wallpaper 后台管理系统'
admin.site.site_header = 'Wallpaper'
admin.site.index_title = '数据管理'


def export_as_json(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

export_as_json.short_description = '将所选项导出为 JSON'
