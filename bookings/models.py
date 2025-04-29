from django.db import models

# Create your models here.

# bookings/models.py
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    table = models.IntegerField()

    def __str__(self):
        return f"Booking {self.id} for {self.user.username} at {self.date} {self.time}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

