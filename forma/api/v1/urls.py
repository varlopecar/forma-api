from django.urls import path, include
from rest_framework.routers import DefaultRouter
from forma.api.v1.views import ItemViewSet, test_endpoint

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', test_endpoint, name='test-endpoint'),
]
