from django.urls import path, include
from rest_framework import routers
from apps.order.api.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet, basename="order")

urlpatterns = [
    path('', include(router.urls)),
]
