from rest_framework.routers import DefaultRouter
from app.views import TestModelViewSet

router = DefaultRouter()
router.register(r'items', TestModelViewSet, base_name='item')

urlpatterns = router.urls
