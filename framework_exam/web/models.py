from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator

from framework_exam.web.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Photo(models.Model):
    photo = models.FileField(
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg'])])

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

# class Profile(models.Model):
#     FIRST_NAME_MAX_LENGTH = 30
#     LAST_NAME_MAX_LENGTH = 30
#
#     first_name = models.CharField(
#         max_length=FIRST_NAME_MAX_LENGTH,
#     )
#
#     last_name = models.CharField(
#         max_length=LAST_NAME_MAX_LENGTH,
#     )
#
#     user = models.OneToOneField(
#         AppUser,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
