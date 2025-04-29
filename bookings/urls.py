# bookings/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'menu', MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]