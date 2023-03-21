import django_filters
from django import forms
from django.forms.widgets import NumberInput

from apps.uav.models import Uav
from apps.uav.selectors import category_list, brand_list

class UavFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Name",
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    category = django_filters.ModelChoiceFilter(
        queryset = category_list(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    brand = django_filters.ModelChoiceFilter(
        queryset = brand_list(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    weight = django_filters.NumberFilter(
        label='Weight',
        widget=NumberInput(
            attrs={'class': 'form-control'}
            ))
    endurance = django_filters.NumberFilter(
        label='Endurance',
        widget=NumberInput(
            attrs={'class': 'form-control'}
            ))
    flight_range = django_filters.NumberFilter(
        label='Flight',
        widget=NumberInput(
            attrs={'class': 'form-control'}
            ))
    max_speed = django_filters.NumberFilter(
        label='Speed',
        widget=NumberInput(
            attrs={'class': 'form-control'}
            ))
    price = django_filters.NumberFilter(
        label='Price',
        widget=NumberInput(
            attrs={'class': 'form-control'}
            ))
    class Meta:
        model = Uav
        fields = ('name', 'category', 'brand', 'weight', 'endurance', 'flight_range', 'max_speed', 'price')