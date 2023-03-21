from django.urls import path, include
from rest_framework import routers
from apps.uav.api.views import UavViewSet, CategoryViewSet, BrandViewSet

router = routers.DefaultRouter()
router.register(r'category/', CategoryViewSet, basename="category")
router.register(r'brand/', BrandViewSet, basename="brand")
router.register(r'', UavViewSet, basename="uav")

urlpatterns = [
    path('', include(router.urls)),
]
