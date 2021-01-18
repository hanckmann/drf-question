# from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# class UserManager(BaseUserManager):
#     use_in_migrations = True


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        error_messages={"unique": "A user with this email address already exists."},
    )
    name = models.CharField(
        verbose_name="name of user",
        blank=True,
        max_length=255,
        help_text="User provided name.",
    )

    # overwritten to remove the useless `first_name` and `last_name` fields from database
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    REQUIRED_FIELDS = ['email']

    # objects: UserManager = UserManager()  # type: ignore

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-date_joined"]
