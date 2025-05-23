from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from forma.models import Item
from forma.api.v1.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    Version 1 exposes only basic fields.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(['GET'])
def test_endpoint(request):
    """
    A simple test endpoint that returns a greeting message.
    """
    return Response({
        'message': 'Hello from the test endpoint!',
        'status': 'success',
        'version': 'v1'
    })
