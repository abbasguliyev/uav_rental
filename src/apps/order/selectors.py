from django.db.models.query import QuerySet
from apps.order.models import Order

def order_list() -> QuerySet[Order]:
    qs = Order.objects.select_related('user', 'uav').all()
    return qs
