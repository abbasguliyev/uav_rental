from django.contrib import admin
from django.contrib.auth import get_user_model

@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone', 'address')
    list_display_links = ('id', 'email')
    list_filter = ('id', 'email', 'first_name', 'last_name', 'phone')
    search_fields = ('id', 'email')
