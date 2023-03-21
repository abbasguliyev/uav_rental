from rest_framework import serializers
from apps.uav.models import Uav, Category, Brand

class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uav
        fields = [
            'id', 'name', 'description', 'category', 'brand',
            'weight', 'endurance', 'flight_range', 'max_speed',
            'image', 'price'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name']