from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order, TechCard, InventoryItem
from .serializers import OrderSerializer, TechCardSerializer, InventoryItemSerializer

# ViewSet для заказов
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Настройка фильтров и поиска
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']  # Поля для фильтрации
    search_fields = ['name']  # Поля для поиска

# ViewSet для техкарт
class TechCardViewSet(viewsets.ModelViewSet):
    queryset = TechCard.objects.all()
    serializer_class = TechCardSerializer

# ViewSet для складских объектов
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
