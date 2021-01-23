from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers for authentication.
    """

    def create_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError(_("Users must have an email address"))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves a new super user"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return self.email.split("@")[0]
