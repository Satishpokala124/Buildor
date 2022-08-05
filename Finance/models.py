from django.db import models

from BluePrints.models import BluePrint


class FinanceManager(models.Manager):
    """
    Manager class for Finance model
    TODO:
    1. create() function for object creation
    """
    pass


class Finance(models.Model):
    """
    Finance class
    TODO:
    1. Refactor all the field types.
    2. Discuss the max_lengths for all CharFields
    3. remove null=True for all fields
    """
    id = models.CharField(
        primary_key=True, max_length=20, null=False, blank=False, editable=False
    )
    blueprint = models.ForeignKey(to=BluePrint, on_delete=models.DO_NOTHING)
    material_cost = models.CharField(max_length=10, null=True)
    labor_cost = models.CharField(max_length=10, null=True)
    """
    Connect the custom Manager class (FinanceManager) to our Finance class.
    """
    finances = FinanceManager()
