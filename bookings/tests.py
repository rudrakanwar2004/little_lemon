# bookings/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Booking, MenuItem
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class BookingAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # Create a JWT token for the user
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  # Pass the token in the header

        self.booking = Booking.objects.create(user=self.user, date="2025-04-29", time="18:00:00", table=1)
        self.menu_item = MenuItem.objects.create(name="Pizza", description="Delicious cheese pizza", price=9.99)

    def test_booking_creation(self):
        # Make sure the user is authenticated, and then create a booking
        response = self.client.post('/api/bookings/', {'user': self.user.id, 'date': '2025-05-01', 'time': '20:00:00', 'table': 2}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_menu_item_creation(self):
        # Test for menu item creation
        response = self.client.post('/api/menu/', {'name': 'Burger', 'description': 'Juicy beef burger', 'price': 7.99}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
