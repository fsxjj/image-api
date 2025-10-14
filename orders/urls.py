from django.urls import path
from .views import WallPaintingOrderListCreateAPIView, WallPaintingOrderDetailAPIView

urlpatterns = [
    path('wall-paintings/', WallPaintingOrderListCreateAPIView.as_view(), name='wallpainting-list-create'),
    path('wall-paintings/<int:pk>/', WallPaintingOrderDetailAPIView.as_view(), name='wallpainting-detail'),
]
