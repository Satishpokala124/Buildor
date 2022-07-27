from django.db import models
from Accounts.models import User
# Create your models here.

class Builder(models.Model):
    id = models.CharField(max_length=15)
    userId  = models.OneToOneField(User,on_delete=models.CASCADE)
    man_force_id  = models.CharField(max_length=15)
    experence   = models.DecimalField(max_digits=2,decimal_places=2)
    property_type  = models.CharField(max_length=15)
    status  = models.CharField(max_length=15)
    wage  = models.CharField(max_length=15)
    photo_folder  = models.CharField(max_length=15)
    Location  = models.CharField(max_length=15)
    