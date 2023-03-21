from django.db.models.query import QuerySet
from apps.uav.models import Uav, Category, Brand

def category_list() -> QuerySet[Category]:
    qs = Category.objects.all()
    return qs

def brand_list() -> QuerySet[Brand]:
    qs = Brand.objects.all()
    return qs

def uav_list() -> QuerySet[Uav]:
    qs = Uav.objects.select_related('category', 'brand').all()
    return qs
