from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _




# Create your models here.
class User(AbstractUser):
    id = models.CharField(primary_key=True,max_length=20)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    phone_number = models.CharField(max_length=10)









