from django.db import models

from Builders.models import Builder
from Employees.models import Employee


class ManForceManager(models.Manager):
    """
    Manager class for ManForce model
    TODO:
    1. create() function for object creation
    """
    pass


class ManForce(models.Model):
    """
    ManForce class
    TODO:
    1. Refactor all the field types.
    2. remove null=True for all fields
    """
    id = models.CharField(
        primary_key=True, max_length=20, null=False, blank=False, editable=False
    )
    no_of_carpenters = models.IntegerField(null=True)
    no_of_builders = models.IntegerField(null=True)
    no_of_electricians = models.IntegerField(null=True)
    no_of_plumbers = models.IntegerField(null=True)
    no_of_painters = models.IntegerField(null=True)
    no_of_blacksmiths = models.IntegerField(null=True)
    """
    Connect the custom Manager class (ManForceManager) to our ManForce class.
    """
    manforce = ManForceManager()
