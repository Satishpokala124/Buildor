from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _


class MyUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email or not len(email.strip()):
            raise TypeError(f"'email' can't be None")
        if not password or not len(password.strip()):
            raise TypeError(f"'password' can't be None")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    phone_number = models.CharField(max_length=10)
