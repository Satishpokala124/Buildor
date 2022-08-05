from django.db import models

from Accounts.models import User
from BluePrints.models import BluePrint


class BookingManager(models.Manager):
    """
    Manager class for Booking model
    TODO:
    1. create() function for object creation
    """
    pass


class Booking(models.Model):
    """
    Booking class
    TODO:
    1. Refactor all the field types.
    2. Discuss the max_lengths for all CharFields
    3. remove null=True for all fields
    """
    id = models.CharField(
        primary_key=True, max_length=20, null=False, blank=False, editable=False
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    blueprint = models.ForeignKey(to=BluePrint, on_delete=models.CASCADE)
    location = models.CharField(max_length=500, null=True)
    price_quoted = models.CharField(max_length=10, null=True)
    plan = models.CharField(max_length=10, null=True)
    """
    Connect the custom Manager class (BluePrintManager) to our BluePrint class.
    """
    bookings = BookingManager()
