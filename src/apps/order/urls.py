from django.urls import path
from apps.order import views

urlpatterns = [
    path("all-order/", views.OrderListView.as_view(), name="order"),
    path("order-create/", views.OrderAddView.as_view(), name="order_add"),
    path("order-delete/<int:pk>/", views.OrderDeleteView.as_view(), name="order_delete"),
]
