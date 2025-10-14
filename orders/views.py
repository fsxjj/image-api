from rest_framework import generics
from .models import WallPaintingOrder
from .serializers import WallPaintingOrderSerializer

class WallPaintingOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = WallPaintingOrder.objects.all()
    serializer_class = WallPaintingOrderSerializer


class WallPaintingOrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WallPaintingOrder.objects.all()
    serializer_class = WallPaintingOrderSerializer
