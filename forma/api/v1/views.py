from rest_framework import viewsets
from forma.models import Item
from forma.api.v1.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    Version 1 exposes only basic fields.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer