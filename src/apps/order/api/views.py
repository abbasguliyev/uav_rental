from rest_framework.views import Response
from rest_framework import status, viewsets
from apps.order.selectors import order_list
from apps.order.api.serializers import OrderSerializer
from apps.order.filters import OrderFilter
from apps.order.api.services import create_order, update_order

class OrderViewSet(viewsets.ModelViewSet):
    queryset = order_list()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_order(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_order(instance=instance, **serializer.validated_data)
        return Response(serializer.data)