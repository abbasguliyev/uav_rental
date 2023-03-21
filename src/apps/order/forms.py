from django import forms
from apps.order.models import Order
from apps.uav.selectors import uav_list
from apps.account.selectors import user_list

class OrderForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset = user_list(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'User'
    }))
    uav = forms.ModelChoiceField(queryset = uav_list(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Uav'
    }))

    class Meta:
        model = Order
        fields = ['user', 'uav']
        
