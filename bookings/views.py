from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
