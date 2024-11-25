from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, TechCardViewSet, InventoryItemViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'techcards', TechCardViewSet)
router.register(r'inventory', InventoryItemViewSet)

urlpatterns = router.urls
