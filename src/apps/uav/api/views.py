from rest_framework.views import Response
from rest_framework import status, viewsets
from apps.uav.selectors import uav_list, category_list, brand_list
from apps.uav.api.serializers import UavSerializer, CategorySerializer, BrandSerializer
from apps.uav.filters import UavFilter
from apps.uav.api.services import create_uav, update_uav, create_category, update_category, create_brand, update_brand

class UavViewSet(viewsets.ModelViewSet):
    queryset = uav_list()
    serializer_class = UavSerializer
    filterset_class = UavFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_uav(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_uav(instance=instance, **serializer.validated_data)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category_list()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_category(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_category(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = brand_list()
    serializer_class = BrandSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_brand(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_brand(instance=instance, **serializer.validated_data)
        return Response(serializer.data)