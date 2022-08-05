from Accounts.models import MyUserManager, User
from django.db import models


class EmployeeManager(MyUserManager):
    """
    1. Manager class for Employee model
    2. Inherits from MyUserManager class.
    TODO:
    1. create() function for object creation
    """
    pass


class Employee(User):
    """
    TODO: 
        1. Need to check the max_length values
        2. Remove 'null=True' from necessary fields. It is set to 'True' for testing purposes.
    """
    salary = models.CharField(max_length=15, null=True)
    role = models.CharField(max_length=5, null=True)
    """
    Connect the custom Manager class (EmployeeManager) to our Employee class.
    """
    employees = EmployeeManager()
