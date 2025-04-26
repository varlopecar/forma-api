from rest_framework import viewsets
from forma.models import Item
from forma.api.v2.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    Version 2 exposes all fields including timestamps.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer