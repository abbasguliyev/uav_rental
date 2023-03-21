from django.contrib import admin
from apps.order.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id',)
    list_filter = ('id', 'user')
    search_fields = ('id', 'user')
