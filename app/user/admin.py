from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'sex', 'type', 'integral']
    list_display_links = ['username', 'email', 'sex', 'type', 'integral']
    list_filter = ['sex', 'type', 'integral']

    empty_value_display='- null -'
