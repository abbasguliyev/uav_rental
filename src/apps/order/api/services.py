from apps.order.selectors import order_list
from apps.order.models import Order

def create_order(user, uav) -> Order:
    obj = Order.objects.create(user = user, uav = uav)
    return obj

def update_order(instance, **data) -> Order:
    obj = order_list().filter(pk=instance.pk).update(**data)
    return obj
