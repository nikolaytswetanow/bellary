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

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
