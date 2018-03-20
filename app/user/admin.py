from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers

from .models import *


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'sex', 'type', 'coin']
    list_display_links = ['username', 'email', 'sex', 'type', 'coin']

    list_filter = ['sex', 'type', 'date_joined', 'last_login']
    search_fields = ['username', 'nickname', 'email']
    list_per_page = 10

    ordering = ['id']
    empty_value_display = '- null -'

    actions = ['add_100_coin','export_as_json']

    def add_100_coin(self, request, quertset):
        user_ids = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        for user_id in user_ids:
            user = UserProfile.objects.get(pk=user_id)
            current_coin = user.coin
            user.coin = current_coin + 100
            user.save()
        self.message_user(request, "%s 个用户成功更新" % len(user_ids))

    add_100_coin.short_description = '增加 100 硬币'

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type='application/json')
        serializers.serialize('json', queryset, stream=response)
        return response

    export_as_json.short_description = '将所选项导出为 JSON'
