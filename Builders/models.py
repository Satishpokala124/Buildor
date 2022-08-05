from Accounts.models import MyUserManager, User
from django.db import models


class BuilderManager(MyUserManager):
    """
    1. Manager class for Builder model.
    2. Inherits from MyUserManager class.
    TODO:
    1. create() function for object creation
    """
    pass


class Builder(User):
    """
    TODO: 
        1. Need to map foreign key in ManForce model
        2. Remove 'null=True' from necessary fields. It is set to 'True' for testing purposes.
    """
    man_force_id = models.CharField(max_length=15, null=True)
    experience = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    property_type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=15, null=True)
    wage = models.CharField(max_length=15, null=True)
    photo_folder = models.CharField(max_length=15, null=True)
    Location = models.CharField(max_length=15, null=True)

    builders = BuilderManager()
