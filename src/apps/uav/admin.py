from django.contrib import admin
from apps.uav.models import Category, Brand, Uav

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug')
    list_display_links = ('id', 'category_name')
    prepopulated_fields = {"slug": ["category_name"]}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name')
    list_display_links = ('id', 'brand_name')
    prepopulated_fields = {"slug": ["brand_name"]}

@admin.register(Uav)
class UavAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category', 'brand', 'weight', 'endurance', 'flight_range', 'max_speed')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ["name"]}
