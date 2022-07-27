import re
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return True if re.fullmatch(regex, email) else False


class MyUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email or not len(email.strip()):
            raise AttributeError("email can't be None or empty")
        if not password or not len(password.strip()):
            raise AttributeError("password can't be None or empty")
        if not validate_email(email):
            raise AttributeError('invalid email')
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("id", self.custom_id_generator())
        return self._create_user(username, email, password, **extra_fields)

    def custom_id_generator(self):
        prefix = f'{self.model._meta.app_label[0]}{self.model._meta.object_name[0]}'
        id_max = int(self.aggregate(id_max=Max('id'))['id_max'].strip(prefix))
        id_max = str(id_max+1).rjust(15, '0')
        new_id = f'{prefix}{id_max}'
        return new_id


class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=20, null=False, blank=False, editable=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    phone_number = models.CharField(max_length=10)
    objects = MyUserManager()
