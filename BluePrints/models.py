from django.db import models

from Builders.models import Builder
from Employees.models import Employee


class BluePrintManager(models.Manager):
    """
    Manager class for BluePrint model
    TODO:
    1. create() function for object creation
    """
    pass


class BluePrint(models.Model):
    """
    BluePrint class
    TODO:
    1. Refactor all the field types.
    2. Discuss the max_lengths for all CharFields
    3. remove null=True for all fields
    """
    id = models.CharField(
        primary_key=True, max_length=20, null=False, blank=False, editable=False
    )
    employee = models.ForeignKey(to=Employee, on_delete=models.DO_NOTHING)
    builder = models.ForeignKey(to=Builder, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=10, null=True)
    progress = models.FloatField(null=True)
    estimate = models.CharField(max_length=10, null=True)
    plan = models.CharField(max_length=10, null=True)
    delivery_time = models.IntegerField(null=True)
    """
    Connect the custom Manager class (BluePrintManager) to our BluePrint class.
    """
    blueprints = BluePrintManager()
