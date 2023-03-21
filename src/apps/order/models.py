from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="orders")
    uav = models.ForeignKey("uav.Uav", on_delete=models.CASCADE, related_name="orders")

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
