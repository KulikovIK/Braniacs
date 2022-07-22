from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from mainapp.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(verbose_name=_('email'), blank=True, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name=_('age'), **NULLABLE)
    avatar = models.ImageField(
        verbose_name=_('avatar'), upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return f'{self.pk} | {self.username}'
