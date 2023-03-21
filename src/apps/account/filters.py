import django_filters
from django.contrib.auth import get_user_model

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = get_user_model()
        fields = {
            "first_name": ["exact", "icontains"],
            "last_name": ["exact", "icontains"],
            "email": ["exact", "icontains"],
            "phone": ["exact", "icontains"],
            "company": ["exact", "icontains"],
        }