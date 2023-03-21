from django import forms
from apps.uav.models import Uav, Category, Brand
from apps.uav.selectors import category_list, brand_list

class UavForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'5',
        'class': 'form-control',
        'placeholder': 'Description'
    }))
    category = forms.ModelChoiceField(queryset = category_list(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Category'
    }))
    brand = forms.ModelChoiceField(queryset = brand_list(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Brand'
    }))
    weight = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Weight'
    }))
    endurance = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Endurance'
    }))
    flight_range = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Flight Range'
    }))
    max_speed = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Max Speed'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-file',
        'placeholder': 'Image'
    }))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Price'
    }))


    class Meta:
        model = Uav
        fields = [
            'name', 
            'description', 
            'category', 
            'brand',
            'weight',
            'endurance',
            'flight_range',
            'max_speed',
            'image',
            'price',
            ]
        

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))

    class Meta:
        model = Category
        fields = ['category_name',]

class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))

    class Meta:
        model = Brand
        fields = ['brand_name',]