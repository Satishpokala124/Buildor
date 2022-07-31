import re
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return True if re.fullmatch(regex, email) else False


class MyUserManager(UserManager):
    """
    1. This class is our custom UserManager. 
    2. It inherits all the functionalities of django's default UserManager class.
    3. It is responsible for email, password validation and custom ID creation.
    """

    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        1. Validate email, password and generate a new ID.
        2. Create, save and return the user.
        """
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
        """
        1. Check for the max ID and increments it by 1 to generate a new ID
        2. If the DB is empty then the new ID will start from 1
        3. return new ID as a string
        """
        prefix = f'{self.model._meta.app_label[0]}{self.model._meta.object_name[0]}'
        # Filter all the users with their id's starting with the same prefixand get the highest id of these users
        id_max = self.filter(
            id__startswith=prefix
        ).aggregate(
            id_max=Max('id')
        )['id_max']
        # If there are no users then the new id starts from 1
        if not id_max:
            return f'{prefix}{"1".rjust(10, "0")}'
        id_max = int(str(id_max).strip(prefix))
        id_max = str(id_max+1).rjust(10, '0')
        new_id = f'{prefix}{id_max}'
        return new_id


class User(AbstractUser):
    """
    This is our custom User model which acts as the default auth user class for the whole project.
    """
    id = models.CharField(
        primary_key=True, max_length=20, null=False, blank=False, editable=False
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    phone_number = models.CharField(max_length=10)
    """
    1. Connect the custom UserManager class (MyUserManager) to our User class.
    2. This is necessary to use our custom UserManager class and its functionalities.
    """
    objects = MyUserManager()
