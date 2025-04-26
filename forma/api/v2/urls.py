from django.urls import path, include
from rest_framework.routers import DefaultRouter
from forma.api.v2.views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]